"""Costruisce il sito andreadessolis.com dai contenuti (contenuti.py).

Uso: python _sorgenti\\genera.py [cartella di uscita]
     (senza cartella: la radice del repository, cioe' la cartella sopra _sorgenti)

Tutte le pagine nascono da un modello solo (intestazione, menu, fondo), in
italiano (alla radice) e in inglese (in en\\). Per ogni programma: la sua
pagina, le novita' e la guida online (la stessa del programma, in italiano).
GitHub Pages non pubblica le cartelle che iniziano con "_": i sorgenti
restano nel repository ma non finiscono sul sito.
"""
import datetime
import html
import json
import os
import re
import shutil
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
from contenuti import ADDON, EMAIL, GITHUB, GRUPPO_TELEGRAM, PAYPAL, PROGRAMMI, T  # noqa: E402
from privacy import PRIVACY  # noqa: E402

DOMINIO = 'https://andreadessolis.com/'
LINGUE = ('it', 'en')


def e(testo):
    return html.escape(testo, quote=True)


def data_leggibile(iso, lingua):
    d = datetime.date.fromisoformat(iso)
    mese = T[lingua]['mesi'][d.month - 1]
    return f'{d.day} {mese} {d.year}' if lingua == 'it' else f'{mese} {d.day}, {d.year}'


def link_download(p):
    return f'{GITHUB}/{p["repository"]}/releases/latest/download/{p["setup"]}'


# ---------------------------------------------------------------- il modello

ORIZZONTE = '''<svg class="horizon" viewBox="0 0 800 90" preserveAspectRatio="none" aria-hidden="true" focusable="false">
  <path class="l1" d="M0,70 Q200,20 400,55 T800,40" fill="none" stroke-width="3" opacity="0.55"/>
  <path class="l2" d="M0,80 Q200,45 400,70 T800,55" fill="none" stroke-width="3" opacity="0.45"/>
  <path class="l3" d="M0,88 Q200,65 400,82 T800,70" fill="none" stroke-width="3" opacity="0.4"/>
  <circle class="sun" cx="{sole}" cy="30" r="20" opacity="0.85"/>
</svg>'''


def pagina(lingua, nome_file, titolo, voce_menu, corpo, sole=700, descrizione=''):
    """Una pagina completa. nome_file: relativo alla cartella della lingua
    (anche in una sottocartella, per esempio novita/hdx-vm.html)."""
    t = T[lingua]
    profondita = nome_file.count('/')
    su = '../' * profondita                      # alla cartella della lingua
    radice = su + ('../' if lingua == 'en' else '')  # alla radice del sito
    altra = 'en' if lingua == 'it' else 'it'
    # La stessa pagina nell'altra lingua.
    if lingua == 'it':
        altra_href = su + 'en/' + nome_file
    else:
        altra_href = radice + nome_file
    voci = [('home', 'index.html'), ('programmi', 'programmi.html'), ('addon', 'addon-nvda.html'),
            ('chi_sono', 'chi-sono.html'), ('contatti', 'contatti.html')]
    menu = []
    for chiave, href in voci:
        corrente = ' aria-current="page"' if chiave == voce_menu else ''
        menu.append(f'        <li><a href="{su}{href}"{corrente}>{e(t[chiave])}</a></li>')
    # Il gruppo Telegram in ogni pagina, subito trovabile (31 ott 2026).
    menu.append(f'        <li><a href="{GRUPPO_TELEGRAM}">{e(t["gruppo_menu"])}</a></li>')
    menu.append(f'        <li class="lang"><a href="{altra_href}" lang="{altra}" hreflang="{altra}">{e(t["altra_lingua"])}</a></li>')
    titolo_completo = titolo if titolo == 'Andrea Dessolis' else f'{titolo} — Andrea Dessolis'
    url_it = DOMINIO + nome_file
    url_en = DOMINIO + 'en/' + nome_file
    meta_descrizione = f'<meta name="description" content="{e(descrizione)}">\n' if descrizione else ''
    return f'''<!doctype html>
<html lang="{lingua}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titolo_completo)}</title>
{meta_descrizione}<link rel="alternate" hreflang="it" href="{url_it}">
<link rel="alternate" hreflang="en" href="{url_en}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Karla:wght@400;500;700&display=swap">
<link rel="stylesheet" href="{radice}style.css">
</head>
<body>

<a class="skip-link" href="#contenuto">{e(t["salta"])}</a>

<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="{su}index.html">Andrea Dessolis</a>
    <nav aria-label="{e(t["menu"])}">
      <ul class="nav-list">
{chr(10).join(menu)}
      </ul>
    </nav>
  </div>
</header>

{ORIZZONTE.format(sole=sole)}

<main id="contenuto">
  <div class="wrap">
{corpo}
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <p>&copy; <span id="anno">2026</span> Andrea Dessolis — <a href="{su}contatti.html">{e(t["scrivimi"])}</a></p>
  </div>
</footer>
<script>
  try {{ document.getElementById('anno').textContent = new Date().getFullYear(); }} catch (e) {{}}
</script>
</body>
</html>
'''


# ---------------------------------------------------------------- i pezzi

def scheda(p, lingua, livello):
    """La scheda di un programma (Home e Programmi). livello: h2 o h3."""
    t = T[lingua]
    radice = '../' if lingua == 'en' else ''
    azioni = [f'<a class="btn btn-secondary btn-small" href="{p["pagina"]}">{e(t["scopri"].format(p["nome"]))}</a>']
    if p['stato'] == 'disponibile':
        stato = t['versione_del'].format(p['versione'], data_leggibile(p['data'], lingua))
        azioni.insert(0, f'<a class="btn btn-primary btn-small" href="{link_download(p)}">{e(t["scarica"].format(p["nome"]))}</a>')
    else:
        stato = t['in_arrivo']
    return f'''      <li class="program-card">
        <img class="program-logo" src="{radice}immagini/{p["logo"]}" width="72" height="72" alt="">
        <{livello}><a href="{p["pagina"]}">{e(p["nome"])}</a></{livello}>
        <span class="status">{e(stato)}</span>
        <p>{e(p["breve"][lingua])}</p>
        <div class="card-actions">
          {"".join(azioni)}
        </div>
      </li>'''


def griglia(lingua, livello):
    return '    <ul class="program-grid">\n' + '\n'.join(scheda(p, lingua, livello) for p in PROGRAMMI) + '\n    </ul>'


def gruppo(lingua):
    """L'angolo di HDX, il gruppo Telegram di tutti i programmi: in alto nella
    Home, nelle pagine dei programmi e in quella delle add-on."""
    t = T[lingua]
    return f'''    <h2>{e(t["gruppo_titolo"])}</h2>
    <p>{e(t["gruppo_testo"])}</p>
    <div class="cta-row">
      <a class="btn btn-secondary" href="{GRUPPO_TELEGRAM}">{e(t["gruppo_pulsante"])}</a>
    </div>'''


def sostieni(lingua):
    t = T[lingua]
    return f'''    <h2>{e(t["sostieni_titolo"])}</h2>
    <p>{e(t["sostieni_testo"])}</p>
    <div class="cta-row">
      <a class="btn btn-secondary" href="{PAYPAL}">{e(t["sostieni"])}</a>
    </div>'''


# ---------------------------------------------------------------- le pagine

def home(lingua):
    t = T[lingua]
    corpo = f'''    <h1>{e(t["home_titolo"])}</h1>
    <p class="lede">{e(t["home_lede"])}</p>
    <p>{e(t["home_testo"])}</p>

{gruppo(lingua)}

    <h2>{e(t["i_miei_programmi"])}</h2>
{griglia(lingua, "h3")}

{sostieni(lingua)}'''
    return pagina(lingua, 'index.html', 'Andrea Dessolis', 'home', corpo, descrizione=t['programmi_lede'])


def elenco_programmi(lingua):
    t = T[lingua]
    corpo = f'''    <h1>{e(t["programmi_titolo"])}</h1>
    <p class="lede">{e(t["programmi_lede"])}</p>
    <p>{e(t["programmi_testo"])}</p>
{griglia(lingua, "h2")}'''
    return pagina(lingua, 'programmi.html', t['programmi_titolo'], 'programmi', corpo, sole=400, descrizione=t['programmi_lede'])


def pagina_programma(p, lingua):
    t = T[lingua]
    radice = '../' if lingua == 'en' else ''
    parti = [f'''    <div class="program-head">
      <img class="program-logo" src="{radice}immagini/{p["logo"]}" width="96" height="96" alt="{e(p["alt"][lingua])}">
      <h1>{e(p["nome"])}</h1>
    </div>
    <p class="lede">{e(p["frase"][lingua])}</p>''']
    for paragrafo in p['introduzione'][lingua]:
        parti.append(f'    <p>{e(paragrafo)}</p>')
    if p['stato'] == 'disponibile':
        parti.append(f'''    <div class="download">
      <div class="cta-row">
        <a class="btn btn-primary" href="{link_download(p)}">{e(t["scarica"].format(p["nome"]))}</a>
      </div>
      <p class="version">{e(t["versione_del"].format(p["versione"], data_leggibile(p["data"], lingua)))}. {e(t["gratuito"])}</p>
    </div>''')
    else:
        parti.append(f'    <p class="note">{e(t["in_arrivo"])}.</p>')
    parti.append(gruppo(lingua))
    if p.get('requisiti'):
        voci = '\n'.join(f'      <li>{e(r)}</li>' for r in p['requisiti'][lingua])
        parti.append(f'    <h2>{e(t["cosa_serve"])}</h2>\n    <ul>\n{voci}\n    </ul>')
    voci = '\n'.join(f'      <li>{e(f)}</li>' for f in p['funzioni'][lingua])
    parti.append(f'    <h2>{e(t["cosa_fa"])}</h2>\n    <ul class="feature-list">\n{voci}\n    </ul>')
    if p['stato'] == 'disponibile':
        collegamenti = []
        if p.get('guida'):
            collegamenti.append(f'<li><a href="{radice}guide/{p["id"]}.html">{e(t["leggi_guida"].format(p["nome"]))}</a></li>')
        if p.get('novita'):
            collegamenti.append(f'<li><a href="novita/{p["id"]}.html">{e(t["leggi_novita"])}</a></li>')
        collegamenti.append(f'<li><a href="{GITHUB}/{p["repository"]}/releases">{e(t["tutte_versioni"])}</a></li>')
        if p['id'] in PRIVACY:
            collegamenti.append(f'<li><a href="privacy-{p["id"]}.html">{e(t["leggi_privacy"].format(p["nome"]))}</a></li>')
        parti.append(f'    <h2>{e(t["guida_novita"])}</h2>\n    <ul>\n      ' + '\n      '.join(collegamenti) + '\n    </ul>')
    parti.append(sostieni(lingua))
    parti.append(f'    <p>{t["domande"].replace("contatti.html", "contatti.html")}</p>')
    return pagina(lingua, p['pagina'], p['nome'], 'programmi', '\n\n'.join(parti), sole=680, descrizione=p['frase'][lingua])


def pagina_privacy(p, lingua):
    """La privacy di un programma (privacy.py): i testi possono contenere
    collegamenti HTML, quindi non si trasformano."""
    t = T[lingua]
    dati = PRIVACY[p['id']]
    testi = dati[lingua]
    parti = [f'    <h1>{e(testi["titolo"])}</h1>',
             f'    <p class="lede">{testi["lede"]}</p>',
             f'    <p class="note">{e(t["aggiornata_il"].format(data_leggibile(dati["aggiornata"], lingua)))}</p>']
    for titolo, elementi in testi['sezioni']:
        parti.append(f'    <h2>{e(titolo)}</h2>')
        for elemento in elementi:
            if isinstance(elemento, list):
                parti.append('    <ul>\n' + '\n'.join(f'      <li>{voce}</li>' for voce in elemento) + '\n    </ul>')
            else:
                parti.append(f'    <p>{elemento}</p>')
    parti.append(f'    <p><a href="{p["pagina"]}">{e(p["nome"])}</a></p>')
    return pagina(lingua, f'privacy-{p["id"]}.html', testi['titolo'], 'programmi', '\n'.join(parti), sole=560,
                  descrizione=testi['titolo'])


def sezione_addon(a, lingua):
    """Una add-on nella pagina delle add-on. L'attributo data-versione serve a
    pubblica.py per controllare che la pagina online dica la versione nuova."""
    t = T[lingua]
    nome = a['nome'][lingua]
    funzioni = '\n'.join(f'      <li>{e(f)}</li>' for f in a['funzioni'][lingua])
    parti = [f'''    <section id="{a["id"]}" class="addon" data-versione="{a["id"]} {e(a.get("versione", ""))}">
    <h2>{e(nome)}</h2>
    <p>{e(a["frase"][lingua])}</p>
    <ul class="feature-list">
{funzioni}
    </ul>''']
    if a.get('versione'):
        versione = t['versione_del'].format(a['versione'], data_leggibile(a['data'], lingua))
        parti.append(f'''    <div class="download">
      <div class="cta-row">
        <a class="btn btn-primary" href="{link_download(a)}">{e(t["scarica"].format(nome))}</a>
      </div>
      <p class="version">{e(versione)}. {e(t["addon_per_nvda"].format(a["nvda_minimo"]))}</p>
    </div>
    <ul>
      <li><a href="guide/{a["id"]}.html">{e(t["addon_guida"].format(nome))}</a></li>
      <li><a href="novita/{a["id"]}.html">{e(t["leggi_novita"])}</a></li>
      <li><a href="{GITHUB}/{a["repository"]}/releases">{e(t["tutte_versioni"])}</a></li>
    </ul>''')
    else:
        parti.append(f'    <p class="note">{e(t["in_arrivo"])}.</p>')
    parti.append('    </section>')
    return '\n'.join(parti)


def pagina_addon(lingua):
    t = T[lingua]
    passi = '\n'.join(f'      <li>{e(p)}</li>' for p in t['addon_installa'])
    corpo = f'''    <h1>{e(t["addon"])}</h1>
    <p class="lede">{e(t["addon_lede"])}</p>
    <p>{e(t["addon_testo"])}</p>

{gruppo(lingua)}

{chr(10).join(sezione_addon(a, lingua) for a in ADDON)}

    <h2>{e(t["addon_installa_titolo"])}</h2>
    <ol>
{passi}
    </ol>
    <p>{e(t["addon_aggiorna"])}</p>

{sostieni(lingua)}
    <p>{t["domande"]}</p>'''
    return pagina(lingua, 'addon-nvda.html', t['addon'], 'addon', corpo, sole=560, descrizione=t['addon_lede'])


def chi_sono(lingua):
    t = T[lingua]
    paragrafi = '\n'.join(f'    <p>{testo}</p>' for testo in t['chi_sono_testo'])
    corpo = f'''    <h1>{e(t["chi_sono"])}</h1>
    <p class="lede">{e(t["chi_sono_lede"])}</p>
{paragrafi}
    <div class="cta-row">
      <a class="btn btn-primary" href="programmi.html">{e(t["programmi"])}</a>
      <a class="btn btn-secondary" href="contatti.html">{e(t["contatti"])}</a>
    </div>'''
    return pagina(lingua, 'chi-sono.html', t['chi_sono'], 'chi_sono', corpo, sole=120)


def contatti(lingua):
    t = T[lingua]
    corpo = f'''    <h1>{e(t["contatti"])}</h1>
    <p class="lede">{e(t["contatti_lede"])}</p>
    <div class="panel">
      <h2>{e(t["email_titolo"])}</h2>
      <p>{e(t["email_testo"])}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>{e(t["contatti_programmi"])}</p>
    </div>'''
    return pagina(lingua, 'contatti.html', t['contatti'], 'contatti', corpo, sole=120)


# ---------------------------------------------------------------- le novita'

def versioni_da_json(percorso, lingua):
    """Il changelog dei programmi HDX: [(versione, data, [(titolo, [voci])])]."""
    dati = json.load(open(percorso, encoding='utf-8'))
    risultato = []
    for v in dati['versioni']:
        sezioni = [(s['titolo'], s['voci']) for s in v.get(lingua) or v.get('it') or []]
        risultato.append((v['versione'], v.get('data'), sezioni))
    return risultato


def versioni_da_testo(percorso, lingua):
    """Il changelog.txt di Gram Access: blocchi "Versione X", con [IT] [EN] [ES]."""
    testo = open(percorso, encoding='utf-8-sig').read()
    blocchi = re.split(r'^Versione (\d+\.\d+\.\d+)\s*$', testo, flags=re.M)
    risultato = []
    for i in range(1, len(blocchi), 2):
        versione, corpo = blocchi[i], blocchi[i + 1]
        parti = re.split(r'^\[(IT|EN|ES)\]\s*$', corpo, flags=re.M)
        per_lingua = {parti[j].lower(): parti[j + 1].strip() for j in range(1, len(parti), 2)}
        risultato.append((versione, None, per_lingua.get(lingua) or per_lingua.get('it', '')))
    return risultato


def html_da_testo(testo):
    """Il testo di una versione di Gram Access: titoli in maiuscolo, elenchi con "-"
    o numerati ("1. "), il resto paragrafi."""
    righe = [r.rstrip() for r in testo.splitlines()]
    uscita, elenco, tipo = [], None, 'ul'

    def chiudi():
        nonlocal elenco
        if elenco:
            uscita.append(f'<{tipo}>\n' + '\n'.join(f'<li>{e(x)}</li>' for x in elenco) + f'\n</{tipo}>')
        elenco = None

    for riga in righe:
        if not riga.strip():
            # Le voci numerate sono separate da righe vuote: l'elenco continua.
            if tipo != 'ol':
                chiudi()
            continue
        numerata = re.match(r'^\d+\.\s+(.*)$', riga.strip())
        if riga.startswith('- ') or numerata:
            nuovo_tipo = 'ol' if numerata else 'ul'
            if elenco and nuovo_tipo != tipo:
                chiudi()
            tipo = nuovo_tipo
            elenco = (elenco or []) + [numerata.group(1) if numerata else riga[2:].strip()]
            continue
        chiudi()
        lettere = re.sub(r'[^A-Za-zÀ-ÿ]', '', riga)
        if lettere and riga == riga.upper() and len(riga) < 60:
            uscita.append(f'<h3>{e(riga.strip())}</h3>')
        else:
            uscita.append(f'<p>{e(riga.strip())}</p>')
    chiudi()
    return '\n'.join(uscita)


def pagina_novita(p, lingua):
    t = T[lingua]
    voce_menu = 'programmi'
    if isinstance(p['nome'], dict):
        # Un'add-on: nome nella lingua della pagina, e le novita' si leggono in NVDA.
        p = dict(p, nome=p['nome'][lingua])
        t = dict(t, novita_lede=t['addon_novita_lede'])
        voce_menu = 'addon'
    tipo, percorso = p['novita']
    blocchi = []
    if tipo == 'hdx-json':
        for versione, data, sezioni in versioni_da_json(percorso, lingua):
            if data:
                titolo = t['versione_del'].format(versione, data_leggibile(data, lingua))
            else:
                titolo = ('Versione ' if lingua == 'it' else 'Version ') + versione
            corpo = []
            for titolo_sezione, voci in sezioni:
                corpo.append(f'<h3>{e(titolo_sezione)}</h3>\n<ol>\n' + '\n'.join(f'<li>{e(v)}</li>' for v in voci) + '\n</ol>')
            blocchi.append(f'<section class="release">\n<h2>{e(titolo)}</h2>\n' + '\n'.join(corpo) + '\n</section>')
    else:
        for versione, _, testo in versioni_da_testo(percorso, lingua):
            titolo = ('Versione ' if lingua == 'it' else 'Version ') + versione
            blocchi.append(f'<section class="release">\n<h2>{e(titolo)}</h2>\n{html_da_testo(testo)}\n</section>')
    corpo = f'''    <h1>{e(t["novita_titolo"].format(p["nome"]))}</h1>
    <p class="lede">{e(t["novita_lede"])}</p>
    <p><a href="../{p["pagina"]}">{e(t["torna_a"].format(p["nome"]))}</a></p>
{chr(10).join(blocchi)}'''
    return pagina(lingua, f'novita/{p["id"]}.html', t['novita_titolo'].format(p['nome']), voce_menu, corpo, sole=680)


# ---------------------------------------------------------------- le guide

def guida(p):
    """La guida del programma, cosi' com'e', con in cima il ritorno al sito."""
    testo = open(p['guida'], encoding='utf-8').read()
    barra = (f'<div style="padding:10px 16px;border-bottom:2px solid #F0DDB0;background:#FFEFD1;color:#2B241B;'
             f'font-family:Segoe UI,Arial,sans-serif"><a style="color:#0E6B63" href="../{p["pagina"]}">'
             f'Torna a {e(p["nome"])} su andreadessolis.com</a> · '
             f'<a style="color:#0E6B63" href="../en/{p["pagina"]}" lang="en" hreflang="en">Back to {e(p["nome"])} (English)</a></div>')
    return re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + barra, testo, count=1)


def guida_addon(a, lingua):
    """La guida dell'add-on nella sua lingua, con in cima il ritorno alla pagina
    delle add-on. Sta in guide\\ (italiano) o en\\guide\\ (inglese)."""
    testo = open(a['guide'][lingua], encoding='utf-8').read()
    torna = T[lingua]['torna_a'].format(a['nome'][lingua])
    barra = (f'<div style="padding:10px 16px;border-bottom:2px solid #F0DDB0;background:#FFEFD1;color:#2B241B;'
             f'font-family:Segoe UI,Arial,sans-serif"><a style="color:#0E6B63" href="../{a["pagina"]}">'
             f'{e(torna)} — andreadessolis.com</a></div>')
    return re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + barra, testo, count=1)


# ---------------------------------------------------------------- gli aggiornamenti

def aggiornamenti_addon():
    """Il file che le add-on leggono a ogni avvio di NVDA per sapere se c'e' una
    versione nuova: per ogni add-on (col suo nome interno, quello del manifest)
    versione, link fisso, impronta del pacchetto e novita' di quella versione.
    Un'add-on senza impronta non viene proposta: la scrive pubblica.py."""
    voci = {}
    for a in ADDON:
        if not (a.get('versione') and a.get('sha256')):
            continue
        novita = {}
        for lingua in LINGUE:
            versione = next((v for v in versioni_da_json(a['novita'][1], lingua) if v[0] == a['versione']), None)
            novita[lingua] = [voce for _titolo, elenco in (versione[2] if versione else []) for voce in elenco]
        voci[a['setup'].rsplit('.', 1)[0]] = {
            'nome': a['nome'],
            'versione': a['versione'],
            'url': link_download(a),
            'sha256': a['sha256'],
            'pagina': {'it': DOMINIO + a['pagina'], 'en': DOMINIO + 'en/' + a['pagina']},
            'novita': novita,
        }
    return json.dumps({'formato': 1, 'addon': voci}, ensure_ascii=False, indent=2) + '\n'


# ---------------------------------------------------------------- tutto

def scrivi(cartella, relativo, contenuto):
    percorso = os.path.join(cartella, *relativo.split('/'))
    os.makedirs(os.path.dirname(percorso), exist_ok=True)
    with open(percorso, 'w', encoding='utf-8', newline='\n') as f:
        f.write(contenuto)


def genera(uscita):
    for lingua in LINGUE:
        prefisso = '' if lingua == 'it' else 'en/'
        scrivi(uscita, prefisso + 'index.html', home(lingua))
        scrivi(uscita, prefisso + 'programmi.html', elenco_programmi(lingua))
        scrivi(uscita, prefisso + 'chi-sono.html', chi_sono(lingua))
        scrivi(uscita, prefisso + 'contatti.html', contatti(lingua))
        for p in PROGRAMMI:
            scrivi(uscita, prefisso + p['pagina'], pagina_programma(p, lingua))
            if p['stato'] == 'disponibile' and p.get('novita'):
                scrivi(uscita, prefisso + f'novita/{p["id"]}.html', pagina_novita(p, lingua))
            if p['id'] in PRIVACY:
                scrivi(uscita, prefisso + f'privacy-{p["id"]}.html', pagina_privacy(p, lingua))
        scrivi(uscita, prefisso + 'addon-nvda.html', pagina_addon(lingua))
        for a in ADDON:
            if a.get('versione'):
                scrivi(uscita, prefisso + f'novita/{a["id"]}.html', pagina_novita(a, lingua))
                scrivi(uscita, prefisso + f'guide/{a["id"]}.html', guida_addon(a, lingua))
    for p in PROGRAMMI:
        if p['stato'] == 'disponibile' and p.get('guida'):
            scrivi(uscita, f'guide/{p["id"]}.html', guida(p))
    scrivi(uscita, 'addon-nvda.json', aggiornamenti_addon())
    shutil.copyfile(os.path.join(QUI, 'style.css'), os.path.join(uscita, 'style.css'))
    os.makedirs(os.path.join(uscita, 'immagini'), exist_ok=True)
    for p in PROGRAMMI:
        shutil.copyfile(os.path.join(QUI, 'immagini', p['logo']), os.path.join(uscita, 'immagini', p['logo']))


if __name__ == '__main__':
    uscita = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(QUI)
    genera(uscita)
    print('Sito generato in', uscita)
