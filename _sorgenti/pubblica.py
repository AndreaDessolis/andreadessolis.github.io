"""Pubblica sul sito una versione di un programma, sempre allo stesso modo.

    python _sorgenti\\pubblica.py <programma> <setup> [--prova]
    python _sorgenti\\pubblica.py conteggi

<programma> e' l'id in contenuti.py (gram-access, hdx-vm, hdx-recorder);
<setup> il setup compilato di quella versione. Il numero di versione si legge
dal setup stesso. Si lancia SOLO quando l'autore dice "pubblica", e tocca
solo quel programma:

  1. legge versione e note (it, en) dalle novita' del programma: devono
     esserci gia', approvate;
  2. crea la release v<versione> nel repository del programma
     (AndreaDessolis/<repository>) con il setup col nome fisso e, per Gram
     Access, il pacchetto delle modifiche a tgcalls (licenza LGPL);
  3. scarica il setup dal link fisso del sito e controlla che sia identico;
  4. solo se tutto e' andato bene: somma in download.json i download delle
     versioni precedenti e le toglie (resta una sola versione);
  5. scrive versione e data in versioni.json, rigenera il sito, lo mette
     online e controlla che la pagina del programma dica la versione nuova.

--prova fa i controlli (setup, versione, note, pacchetto tgcalls, pagine)
senza toccare GitHub ne' il sito. "conteggi" dice i download di ogni programma.
"""
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
sys.path.insert(0, QUI)
import contenuti  # noqa: E402
import genera  # noqa: E402

PROPRIETARIO = 'AndreaDessolis'
TGCALLS = r'D:\TBuild\tgcalls'


def esegui(*comando, cartella=None, uscita=True):
    esito = subprocess.run(comando, cwd=cartella, capture_output=True)
    if esito.returncode != 0:
        raise SystemExit(f'Non riuscito: {" ".join(comando)}\n{esito.stderr.decode("utf-8", "replace")}')
    return esito.stdout.decode('utf-8', 'replace') if uscita else esito.stdout


def programma(id_programma):
    for p in contenuti.PROGRAMMI:
        if p['id'] == id_programma:
            return p
    raise SystemExit(f'Programma sconosciuto: {id_programma} (in contenuti.py: '
                     + ', '.join(p['id'] for p in contenuti.PROGRAMMI) + ')')


def versione_del_setup(setup):
    """La versione scritta nel setup (Inno Setup la copia dal programma)."""
    comando = f"(Get-Item -LiteralPath '{setup}').VersionInfo.ProductVersion"
    v = esegui('powershell', '-NoProfile', '-Command', comando).strip()
    # "1.0.0.0" -> "1.0.0"
    if v.count('.') == 3:
        v = v.rsplit('.', 1)[0]
    if not re.fullmatch(r'\d+\.\d+\.\d+', v):
        raise SystemExit(f'Non leggo la versione del setup ({v!r})')
    return v


def impronta(percorso):
    h = hashlib.sha256()
    with open(percorso, 'rb') as f:
        for blocco in iter(lambda: f.read(1 << 20), b''):
            h.update(blocco)
    return h.hexdigest()


# ---------------------------------------------------------------- le note

def note(p, versione):
    """Le note della release, in italiano e inglese, dalle novita' del programma."""
    tipo, percorso = p['novita']
    parti = [f'## {p["nome"]} {versione}\n']
    for lingua, nome_lingua in (('it', 'Italiano'), ('en', 'English')):
        if tipo == 'hdx-json':
            voce = next((v for v in genera.versioni_da_json(percorso, lingua) if v[0] == versione), None)
            if not voce:
                raise SystemExit(f'Nelle novita\' di {p["nome"]} manca la versione {versione}')
            testo = []
            for titolo, voci in voce[2]:
                testo.append(f'{titolo}:\n' + '\n'.join(f'{i}. {v}' for i, v in enumerate(voci, 1)))
            testo = '\n\n'.join(testo)
        else:
            voce = next((v for v in genera.versioni_da_testo(percorso, lingua) if v[0] == versione), None)
            if not voce or not voce[2]:
                raise SystemExit(f'Nelle novita\' di {p["nome"]} manca la versione {versione}')
            testo = voce[2]
        pagina = p['pagina'] if lingua == 'it' else 'en/' + p['pagina']
        parti.append(f'**{nome_lingua}**\n\n{testo}\n\n{genera.DOMINIO}{pagina}\n')
    if p['id'] == 'gram-access':
        parti.append('---\nGram Access usa tgcalls (licenza LGPL): il file gramaccess-tgcalls.patch contiene le sole '
                     'modifiche fatte a tgcalls. / Gram Access uses tgcalls (LGPL license): the file '
                     'gramaccess-tgcalls.patch contains only the changes made to tgcalls.\n')
    return '\n'.join(parti)


def pacchetto_tgcalls(cartella):
    """Le sole modifiche di Gram Access a tgcalls, in UTF-8 come escono da git."""
    diff = esegui('git', '-C', TGCALLS, 'diff', uscita=False)
    if not diff.strip():
        raise SystemExit('Il pacchetto tgcalls risulta vuoto: controllare ' + TGCALLS)
    if re.search(rb'[A-Za-z]:\\|Users\\|desso', diff):
        raise SystemExit('Il pacchetto tgcalls contiene un percorso personale: controllarlo a mano')
    percorso = os.path.join(cartella, 'gramaccess-tgcalls.patch')
    with open(percorso, 'wb') as f:
        f.write(diff)
    return percorso


# ---------------------------------------------------------------- i download

def release(repository):
    risposta = esegui('gh', 'api', f'repos/{PROPRIETARIO}/{repository}/releases', '--paginate')
    return json.loads(risposta) if risposta.strip() else []


def download_della_release(r):
    return sum(a['download_count'] for a in r.get('assets', []) if a['name'].lower().endswith('.exe'))


def conteggi():
    registro = json.load(open(os.path.join(QUI, 'download.json'), encoding='utf-8'))
    for p in contenuti.PROGRAMMI:
        voce = registro.get(p['id'], {})
        passati = voce.get('storico', 0) + sum(voce.get('versioni_tolte', {}).values())
        adesso = sum(download_della_release(r) for r in release(p['repository'])) if p.get('repository') else 0
        print(f'{p["nome"]}: {passati + adesso} download in tutto ({adesso} della versione di adesso)')


# ---------------------------------------------------------------- pubblica

def pubblica(id_programma, setup, prova):
    p = programma(id_programma)
    if p['stato'] != 'disponibile':
        raise SystemExit(f'{p["nome"]} risulta "in arrivo" in contenuti.py: prima va messo "disponibile"')
    if not os.path.isfile(setup):
        raise SystemExit('Manca il setup: ' + setup)
    versione = versione_del_setup(setup)
    testo_note = note(p, versione)
    oggi = datetime.date.today().isoformat()
    print(f'{p["nome"]} {versione}, setup {os.path.getsize(setup):,} byte')
    if any(r['tag_name'] == f'v{versione}' for r in release(p['repository'])):
        if not prova:
            raise SystemExit(f'La versione {versione} risulta gia\' pubblicata in {p["repository"]}')
        print(f'(Nota: la {versione} risulta gia\' pubblicata: sul serio non si ripubblicherebbe.)')

    lavoro = tempfile.mkdtemp(prefix='pubblica_')
    try:
        file_setup = os.path.join(lavoro, p['setup'])
        shutil.copyfile(setup, file_setup)
        allegati = [file_setup]
        if p['id'] == 'gram-access':
            allegati.append(pacchetto_tgcalls(lavoro))
        file_note = os.path.join(lavoro, 'note.md')
        open(file_note, 'w', encoding='utf-8').write(testo_note)
        print('\nLe note:\n' + testo_note)
        if prova:
            # Le pagine si generano in una cartella a parte: il sito non si tocca.
            vecchie = dict(contenuti._VERSIONI)
            p.update({'versione': versione, 'data': oggi})
            genera.genera(os.path.join(lavoro, 'sito'))
            print('PROVA riuscita: allegati', [os.path.basename(a) for a in allegati], '- niente pubblicato.')
            p.update(vecchie.get(p['id'], {}))
            return

        esegui('git', 'pull', '--quiet', cartella=RADICE)
        precedenti = release(p['repository'])
        repo = f'{PROPRIETARIO}/{p["repository"]}'
        esegui('gh', 'release', 'create', f'v{versione}', *allegati, '--repo', repo, '--title', f'{p["nome"]} {versione}',
               '--notes-file', file_note, '--latest')
        print('Release creata.')

        # Il link del sito deve dare proprio questo setup.
        scaricato = os.path.join(lavoro, 'scaricato.exe')
        for tentativo in range(6):
            try:
                urllib.request.urlretrieve(genera.link_download(p), scaricato)
                if impronta(scaricato) == impronta(setup):
                    break
            except OSError:
                pass
            time.sleep(10)
        else:
            raise SystemExit('Il link di download non da\' ancora il setup nuovo: la release c\'e\', le vecchie NON sono '
                             'state tolte e il sito NON e\' cambiato. Controllare e riprovare.')
        print('Link di download controllato: il setup scaricato e\' identico.')

        # Una sola versione: le precedenti si contano e si tolgono.
        registro_file = os.path.join(QUI, 'download.json')
        registro = json.load(open(registro_file, encoding='utf-8'))
        voce = registro.setdefault(p['id'], {'storico': 0, 'versioni_tolte': {}})
        for r in precedenti:
            voce['versioni_tolte'][r['tag_name']] = voce['versioni_tolte'].get(r['tag_name'], 0) + download_della_release(r)
            esegui('gh', 'release', 'delete', r['tag_name'], '--repo', repo, '--yes', '--cleanup-tag')
            print(f'Tolta la versione vecchia {r["tag_name"]} ({download_della_release(r)} download, segnati nel registro).')
        json.dump(registro, open(registro_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

        # Il sito: versione e data, le pagine, online.
        versioni_file = os.path.join(QUI, 'versioni.json')
        versioni = json.load(open(versioni_file, encoding='utf-8'))
        versioni[p['id']] = {'versione': versione, 'data': oggi}
        json.dump(versioni, open(versioni_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        p.update(versioni[p['id']])
        genera.genera(RADICE)
        esegui('git', 'add', '-A', cartella=RADICE)
        esegui('git', '-c', 'user.name=AndreaDessolis', '-c', f'user.email={contenuti.EMAIL}', 'commit', '-q', '-m',
               f'{p["nome"]} {versione}', cartella=RADICE)
        esegui('gh', 'auth', 'setup-git')
        esegui('git', 'push', '-q', cartella=RADICE)
        url = genera.DOMINIO + p['pagina']
        for tentativo in range(30):
            time.sleep(10)
            try:
                if f'Versione {versione} del' in urllib.request.urlopen(url).read().decode('utf-8'):
                    print(f'Sito aggiornato: {url} dice la versione {versione}.')
                    return
            except OSError:
                pass
        print(f'ATTENZIONE: dopo 5 minuti {url} non dice ancora {versione}: controllare GitHub Pages.')
    finally:
        shutil.rmtree(lavoro, ignore_errors=True)


if __name__ == '__main__':
    argomenti = [a for a in sys.argv[1:] if a != '--prova']
    if argomenti == ['conteggi']:
        conteggi()
    elif len(argomenti) == 2:
        pubblica(argomenti[0], argomenti[1], '--prova' in sys.argv)
    else:
        print(__doc__)
