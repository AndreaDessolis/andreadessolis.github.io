"""I loghi dei programmi HDX per il sito (PNG 256x256), dagli script delle icone
dei progetti (cosi' sono sempre uguali a quelli dei programmi).
Uso: python loghi.py  (scrive in _sorgenti\immagini)"""
import importlib.util
import os

from PIL import Image

QUI = os.path.dirname(os.path.abspath(__file__))
SVILUPPO = r'D:\Software Portable\Sviluppo Software'


def carica(progetto):
    percorso = os.path.join(SVILUPPO, progetto, 'risorse', 'icone', 'genera_icone.py')
    spec = importlib.util.spec_from_file_location('icone_' + progetto.replace(' ', '_'), percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


if __name__ == '__main__':
    carica('HDX VM').logo().resize((256, 256), Image.LANCZOS).save(os.path.join(QUI, 'immagini', 'hdx-vm.png'))
    carica('HDX Recorder').logo('registrazione').resize((256, 256), Image.LANCZOS).save(
        os.path.join(QUI, 'immagini', 'hdx-recorder.png'))
    # PCloud Access: il suo script disegna l'icona con disegna() (non logo()).
    carica('PCloud Access').disegna().resize((256, 256), Image.LANCZOS).save(
        os.path.join(QUI, 'immagini', 'pcloud-access.png'))
    print('Fatto')
