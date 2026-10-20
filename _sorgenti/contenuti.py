"""I contenuti del sito, in italiano (it) e inglese (en).

Per aggiungere un programma: una voce in PROGRAMMI (nell'ordine in cui
compare), il suo logo in immagini\\ e, se ha guida e novita', i percorsi.
Versione e data di ogni programma stanno in versioni.json: le scrive lo
script pubblica.py quando si pubblica una versione nuova.
"""

import json as _json
import os as _os

PAYPAL = 'https://paypal.me/AndreaDessolis'
EMAIL = 'dessolisandrea@gmail.com'
GITHUB = 'https://github.com/AndreaDessolis'

PROGRAMMI = [
    {
        'id': 'gram-access',
        'pagina': 'gramaccess.html',  # l'indirizzo di sempre, per non rompere i link
        'nome': 'Gram Access',
        'logo': 'gram-access.png',
        'alt': {
            'it': 'Logo di Gram Access: un fumetto bianco con la lettera G in Braille e tre onde sonore, su un cerchio verde acqua',
            'en': 'Gram Access logo: a white speech bubble with the letter G in Braille and three sound waves, on a teal circle',
        },
        'stato': 'disponibile',
        'repository': 'Gram-Access',
        'setup': 'GramAccess-Setup.exe',
        'guida': r'D:\Software Portable\Sviluppo Software\Gram Access\Release\GramAccess\Guida.html',
        'novita': ('gram-access-txt', r'D:\Software Portable\Sviluppo Software\Gram Access\Release\changelog.txt'),
        'community': 'https://t.me/+t7KuNQH-xQczMDVk',
        'frase': {
            'it': 'Un client non ufficiale per Telegram, per Windows, pensato e costruito fin dal primo giorno per chi usa uno screen reader.',
            'en': 'An unofficial Telegram client for Windows, designed and built from day one for people who use a screen reader.',
        },
        'breve': {
            'it': 'Telegram accessibile: chat, gruppi, canali, chiamate e messaggi vocali.',
            'en': 'Accessible Telegram: chats, groups, channels, calls and voice messages.',
        },
        'introduzione': {
            'it': [
                'Gram Access è un client non ufficiale: usa l\'API di Telegram e fa parte dell\'ecosistema Telegram, ma non è sviluppato né approvato da Telegram.',
                'Non è una versione "adattata" di un altro programma: ogni funzione nasce già pensando a come deve suonare con NVDA o JAWS, non solo a come deve apparire sullo schermo. L\'obiettivo è offrire un\'esperienza Telegram completa, non ridotta, a chi non può o non vuole affidarsi alla vista.',
            ],
            'en': [
                'Gram Access is an unofficial client: it uses the Telegram API and is part of the Telegram ecosystem, but it is not developed or endorsed by Telegram.',
                'It is not an "adapted" version of another program: every feature is designed from the start for how it sounds with NVDA or JAWS, not only for how it looks on screen. The goal is a complete Telegram experience, not a reduced one, for people who cannot or do not want to rely on sight.',
            ],
        },
        'requisiti': {
            'it': ['Windows 10 o 11.', 'Un account Telegram.'],
            'en': ['Windows 10 or 11.', 'A Telegram account.'],
        },
        'funzioni': {
            'it': [
                'Messaggi, chat, gruppi e canali gestiti in modo completo e accessibile, dalla lista chat fino alle impostazioni di amministrazione.',
                'Gruppi e canali come in Telegram: il ruolo di chi scrive, le etichette dei membri e i messaggi di benvenuto per chi entra.',
                'Una ricerca divisa in persone, gruppi, canali e bot, con le ricerche recenti e la ricerca dei messaggi in tutte le chat.',
                'Chiamate vocali e videochiamate, incluse quelle di gruppo e in conferenza, con la registrazione delle chiamate.',
                'Messaggi vocali con trascrizione automatica in testo e riproduzione in sequenza.',
                'Formattazione del testo letta chiaramente: grassetto, corsivo, citazioni e altro.',
                'Emoji, adesivi e GIF da esplorare con ricerca e frecce, non con una griglia visiva.',
                'Checklist, sondaggi, traduzione dei messaggi e riassunti dei testi più lunghi.',
                'Intelligenza artificiale: quella di Telegram per correggere e tradurre ciò che scrivi e, con una tua chiave Gemini, la descrizione di foto, video e documenti e le risposte alle tue domande sui messaggi.',
                'Lettura del testo nelle immagini con il riconoscimento di Windows, senza internet.',
                'Un aspetto curato anche per chi guarda lo schermo, con il supporto agli ingranditori.',
                'Aggiornamenti automatici, e in italiano, inglese e spagnolo.',
            ],
            'en': [
                'Messages, chats, groups and channels handled completely and accessibly, from the chat list to the administration settings.',
                'Groups and channels as in Telegram: the role of who is writing, member tags and welcome messages for people who join.',
                'Search split into people, groups, channels and bots, with recent searches and search of messages in all chats.',
                'Voice and video calls, including group and conference calls, with call recording.',
                'Voice messages with automatic transcription and playback in sequence.',
                'Text formatting read clearly: bold, italic, quotes and more.',
                'Emoji, stickers and GIFs explored with search and arrow keys, not with a visual grid.',
                'Checklists, polls, message translation and summaries of longer texts.',
                'Artificial intelligence: Telegram\'s own to correct and translate what you write and, with your own Gemini key, descriptions of photos, videos and documents and answers to your questions about messages.',
                'Reading text in images with Windows recognition, without internet.',
                'A careful look for sighted users too, with screen magnifier support.',
                'Automatic updates, in Italian, English and Spanish.',
            ],
        },
    },
    {
        'id': 'hdx-vm',
        'pagina': 'hdx-vm.html',
        'nome': 'HDX VM',
        'logo': 'hdx-vm.png',
        'alt': {
            'it': 'Logo di HDX VM: tre cursori di un mixer, turchese, lilla e magenta, sopra la scritta VM, su un quadrato blu notte e viola',
            'en': 'HDX VM logo: three mixer faders, turquoise, lilac and magenta, above the letters VM, on a midnight blue and purple square',
        },
        'stato': 'disponibile',
        'repository': 'HDX-VM',
        'setup': 'HDX-VM-Setup.exe',
        'guida': r'D:\Software Portable\Sviluppo Software\HDX VM\documenti\Guida.html',
        'novita': ('hdx-json', r'D:\Software Portable\Sviluppo Software\HDX VM\rilascio\changelog.json'),
        'frase': {
            'it': 'Voicemeeter, il mixer audio di Windows, comandato in modo completamente accessibile con lo screen reader.',
            'en': 'Voicemeeter, the Windows audio mixer, controlled in a fully accessible way with your screen reader.',
        },
        'breve': {
            'it': 'Voicemeeter accessibile: dove va l\'audio, i volumi e il mixer di ogni canale.',
            'en': 'Accessible Voicemeeter: where audio goes, volumes and the mixer of every channel.',
        },
        'introduzione': {
            'it': [
                'Voicemeeter è un mixer audio molto potente, ma la sua finestra non si può usare con lo screen reader. HDX VM lo comanda al posto suo: decidi da dove arriva l\'audio, dove va e a che volume, e passi da una situazione all\'altra con un tasto, anche mentre sei in un altro programma.',
                'Per esempio: far sentire a chi ti chiama su WhatsApp, Zoom o Telegram il tuo microfono e la tua sintesi vocale, mentre tu ascolti tutto in cuffia.',
            ],
            'en': [
                'Voicemeeter is a very powerful audio mixer, but its window cannot be used with a screen reader. HDX VM controls it for you: you decide where audio comes from, where it goes and how loud, and you switch from one setup to another with a key, even while you are in another program.',
                'For example: letting the people calling you on WhatsApp, Zoom or Telegram hear your microphone and your speech synthesizer, while you hear everything in your headphones.',
            ],
        },
        'requisiti': {
            'it': ['Windows 10 o 11 a 64 bit.',
                   'Voicemeeter (Standard, Banana o Potato), da installare a parte dal sito di VB-Audio: HDX VM lo trova da solo.'],
            'en': ['Windows 10 or 11, 64-bit.',
                   'Voicemeeter (Standard, Banana or Potato), installed separately from the VB-Audio website: HDX VM finds it by itself.'],
        },
        'funzioni': {
            'it': [
                'Fonti e destinazioni in due elenchi: dove va ogni suono si accende e si spegne con un tasto.',
                'I programmi mandati nelle fonti virtuali, ognuno col suo volume.',
                'Il mixer di ogni canale: volume, pulizia della voce, limitatore, equalizzatore, effetti e cambio di voce.',
                'Il livello di ogni canale a comando, e un avviso quando il suono distorce.',
                'Interruttori con scorciatoie valide in tutto Windows, anche con il volume in dissolvenza.',
                'Configurazioni da salvare e richiamare con un tasto.',
                'Le impostazioni audio di Voicemeeter: frequenza, buffer e collegamenti.',
                'Annunci a voce o con suoni, a scelta, e la finestra nell\'area di notifica.',
                'Aggiornamenti automatici, e in italiano, inglese e spagnolo.',
            ],
            'en': [
                'Sources and destinations in two lists: where each sound goes is turned on and off with a key.',
                'Programs sent to virtual sources, each with its own volume.',
                'The mixer of each channel: volume, voice cleanup, limiter, equalizer, effects and voice changer.',
                'The level of each channel on demand, and a warning when the sound distorts.',
                'Switches with shortcuts that work everywhere in Windows, with volume fades too.',
                'Configurations to save and recall with a key.',
                'Voicemeeter audio settings: sample rate, buffers and connections.',
                'Announcements by voice or with sounds, as you choose, and the window in the notification area.',
                'Automatic updates, in Italian, English and Spanish.',
            ],
        },
    },
    {
        'id': 'pcloud-access',
        'pagina': 'pcloud-access.html',
        'nome': 'PCloud Access',
        'logo': 'pcloud-access.png',
        'alt': {
            'it': 'Logo di PCloud Access: una nuvola azzurra con una freccia bianca verso l\'alto',
            'en': 'PCloud Access logo: a light blue cloud with a white upward arrow',
        },
        'stato': 'disponibile',
        'repository': 'PCloud-Access',
        'setup': 'PCloud-Access-Setup.exe',
        'guida': r'D:\Software Portable\Sviluppo Software\PCloud Access\documenti\Guida.html',
        'novita': ('hdx-json', r'D:\Software Portable\Sviluppo Software\PCloud Access\rilascio\changelog.json'),
        'frase': {
            'it': 'Il tuo spazio pCloud come una cartella di Windows, in modo completamente accessibile con lo screen reader.',
            'en': 'Your pCloud space like a Windows folder, fully accessible with your screen reader.',
        },
        'breve': {
            'it': 'pCloud accessibile: file, cartelle, trasferimenti, link e condivisioni.',
            'en': 'Accessible pCloud: files, folders, transfers, links and sharing.',
        },
        'introduzione': {
            'it': [
                'pCloud conserva i tuoi file su internet, ma i suoi programmi non sono comodi da usare con NVDA o JAWS. PCloud Access ti fa usare il tuo spazio pCloud come un elenco di file e cartelle di Esplora risorse, con i tasti di Windows che conosci già: carichi e scarichi sapendo sempre a che punto sei, apri i file, condividi link e cartelle.',
                'PCloud Access è un programma indipendente: usa l\'interfaccia pubblica di pCloud, ma non è un prodotto di pCloud AG né è sponsorizzato da pCloud. La tua password va solo a pCloud e non viene mai salvata.',
            ],
            'en': [
                'pCloud keeps your files on the internet, but its programs are not comfortable to use with NVDA or JAWS. PCloud Access lets you use your pCloud space as a list of files and folders like File Explorer, with the Windows keys you already know: you upload and download always knowing how far along you are, open files, share links and folders.',
                'PCloud Access is an independent program: it uses pCloud\'s public interface, but it is not a pCloud AG product and is not endorsed by pCloud. Your password goes only to pCloud and is never saved.',
            ],
        },
        'requisiti': {
            'it': ['Windows 10 o 11 a 64 bit.', 'Un account pCloud (dal programma si apre la pagina di pCloud per crearlo).'],
            'en': ['Windows 10 or 11, 64-bit.', 'A pCloud account (the program opens the pCloud page to create one).'],
        },
        'funzioni': {
            'it': [
                'L\'elenco dei file come in Esplora risorse: copia, taglia e incolla anche con Esplora risorse, rinomina, cestino, versioni precedenti e Annulla.',
                'Caricamenti e scaricamenti con una finestra dedicata che dice percentuale, velocità e tempo che manca; lo stato a voce anche mentre sei in un altro programma.',
                'Audio e video si ascoltano subito senza scaricarli; gli altri file si aprono con il loro programma e, se li salvi, tornano su pCloud da soli.',
                'Schede, Indietro e Avanti, Preferiti e Recenti, raggiungibili con un tasto.',
                'Link pubblici, link per farti mandare file, cartelle condivise e inviti, pCloud Transfer.',
                'Zip, raccolte musicali, ricerca in tutto il tuo pCloud e scaricamento da internet direttamente in pCloud.',
                'L\'elenco si aggiorna da solo quando qualcosa cambia da un altro dispositivo.',
                'Il tuo account: verifica per email, dispositivi collegati, password, email, inviti agli amici.',
                'Annunci a voce o con suoni, a scelta, e la finestra nell\'area di notifica.',
                'Aggiornamenti automatici, e in italiano, inglese e spagnolo.',
            ],
            'en': [
                'The file list like in File Explorer: copy, cut and paste also with File Explorer, rename, trash, previous versions and Undo.',
                'Uploads and downloads with their own window that tells you percentage, speed and time left; spoken status even while you are in another program.',
                'Audio and video play right away without downloading; other files open with their program and, if you save them, go back to pCloud by themselves.',
                'Tabs, Back and Forward, Favorites and Recent items, one key away.',
                'Public links, links to receive files, shared folders and invitations, pCloud Transfer.',
                'Zip, music collections, search across your whole pCloud and downloading from the internet straight into pCloud.',
                'The list updates by itself when something changes from another device.',
                'Your account: email verification, connected devices, password, email, inviting friends.',
                'Announcements by voice or with sounds, as you choose, and the window in the notification area.',
                'Automatic updates, in Italian, English and Spanish.',
            ],
        },
    },
    {
        'id': 'hdx-recorder',
        'pagina': 'hdx-recorder.html',
        'nome': 'HDX Recorder',
        'logo': 'hdx-recorder.png',
        'alt': {
            'it': 'Logo di HDX Recorder: un grande punto rosso di registrazione tra barrette di onda sonora dal turchese al magenta, su un quadrato blu notte e viola',
            'en': 'HDX Recorder logo: a large red recording dot between sound wave bars from turquoise to magenta, on a midnight blue and purple square',
        },
        'stato': 'in_arrivo',
        'frase': {
            'it': 'Un registratore audio e video pensato per chi usa uno screen reader.',
            'en': 'An audio and video recorder designed for people who use a screen reader.',
        },
        'breve': {
            'it': 'Registrare audio e video con lo screen reader: microfoni, computer, radio, schermo e webcam.',
            'en': 'Recording audio and video with a screen reader: microphones, computer audio, radio, screen and webcam.',
        },
        'introduzione': {
            'it': ['HDX Recorder è in arrivo: lo sto provando con alcuni amici prima di pubblicarlo. Qui sotto trovi cosa farà.'],
            'en': ['HDX Recorder is coming soon: I am testing it with some friends before publishing it. Below you find what it will do.'],
        },
        'funzioni': {
            'it': [
                'Registrazione da microfoni, dall\'audio del computer, da singoli programmi e dalle radio di Internet.',
                'Video dello schermo, di una finestra e della webcam.',
                'Registrazioni programmate, anche con il programma chiuso.',
                'Molti formati: WAV, MP3, FLAC, Opus, AAC e altri.',
                'Schede audio ASIO, mixer delle sorgenti e pad sonori.',
                'Intelligenza artificiale con una tua chiave Gemini.',
            ],
            'en': [
                'Recording from microphones, computer audio, single programs and Internet radio.',
                'Video of the screen, of a window and of the webcam.',
                'Scheduled recordings, even with the program closed.',
                'Many formats: WAV, MP3, FLAC, Opus, AAC and more.',
                'ASIO sound cards, source mixer and sound pads.',
                'Artificial intelligence with your own Gemini key.',
            ],
        },
    },
]

# I testi fissi delle pagine.
T = {
    'it': {
        'lingua_nome': 'Italiano', 'altra_lingua': 'English', 'salta': 'Vai al contenuto principale',
        'menu': 'Menu principale', 'home': 'Home', 'programmi': 'Programmi', 'chi_sono': 'Chi sono', 'contatti': 'Contatti',
        'scrivimi': 'scrivimi',
        'home_titolo': 'Ciao, sono Andrea',
        'home_lede': 'Musica, tecnologia e la voglia di rendere le cose un po\' più semplici da usare, per tutti.',
        'home_testo': 'Questo è il mio piccolo spazio online. Qui trovi i programmi che costruisco, tutti gratuiti e pensati fin dall\'inizio per chi usa uno screen reader, e se vuoi la mia storia nella pagina "Chi sono".',
        'i_miei_programmi': 'I miei programmi',
        'programmi_titolo': 'Programmi',
        'programmi_lede': 'Tutti gratuiti, per Windows, e pensati fin dal primo giorno per chi usa uno screen reader.',
        'programmi_testo': 'Ogni programma ha la sua pagina con il download, la guida da leggere online e le novità di ogni versione. Si aggiornano da soli quando esce una versione nuova.',
        'scopri': 'Scopri {0}', 'scarica': 'Scarica {0}', 'versione_del': 'Versione {0} del {1}',
        'in_arrivo': 'In arrivo',
        'gratuito': 'Gratuito, per Windows 10 e 11. Il link porta sempre all\'ultima versione.',
        'cosa_serve': 'Cosa serve', 'cosa_fa': 'Cosa fa',
        'guida_novita': 'Guida e novità',
        'leggi_guida': 'La guida di {0}, da leggere online',
        'leggi_novita': 'Le novità di ogni versione',
        'tutte_versioni': 'Tutte le versioni su GitHub',
        'sostieni_titolo': 'Sostieni il progetto',
        'sostieni_testo': 'I miei programmi sono gratuiti e li porto avanti da solo, nel tempo libero. Se ti sono utili, puoi aiutarmi con una donazione.',
        'sostieni': 'Sostieni con PayPal',
        'community': 'Unisciti alla community su Telegram',
        'community_testo': 'Nella community di Gram Access su Telegram puoi fare domande, confrontarti con altri utenti e dare suggerimenti.',
        'domande': 'Hai domande o suggerimenti? <a href="contatti.html">Scrivimi</a>.',
        'novita_titolo': 'Novità di {0}', 'novita_lede': 'Le versioni dalla più recente. Le stesse novità si leggono nel programma, in Aiuto.',
        'torna_a': 'Torna a {0}',
        'chi_sono_lede': 'Mi chiamo Andrea Dessolis, e se dovessi riassumermi in poche parole direi: musica, tecnologia, e la voglia di capire come le due cose possano aiutarsi a vicenda.',
        'chi_sono_testo': [
            'Suono la chitarra da anni, ed è una delle cose che mi rilassa e mi diverte di più. Ma la vera svolta della mia vita è arrivata quando, già adulto, ho perso la vista. Da quel momento la tecnologia non è più stata solo un hobby: è diventata uno strumento fondamentale, quasi vitale, per continuare a vivere le cose che amo e per scoprirne di nuove.',
            'Da lì è nata la mia passione per tutto ciò che riguarda l\'accessibilità: software, metodi, piccoli accorgimenti che possono fare una grande differenza per chi, come me, si affida ogni giorno a uno screen reader. Mi piace pensare che ogni programma, ogni sito, ogni strumento possa essere reso più semplice da usare per tutti: basta volerlo fare davvero.',
            'È da questa idea che sono nati i <a href="programmi.html">miei programmi</a>: prima Gram Access per Telegram, poi HDX VM per Voicemeeter e PCloud Access per pCloud, e presto HDX Recorder per registrare.',
        ],
        'contatti_lede': 'Che sia per uno dei miei programmi, per l\'accessibilità o solo per due chiacchiere: scrivimi pure.',
        'email_titolo': 'Email', 'email_testo': 'Il modo più semplice per raggiungermi è via email:',
        'contatti_programmi': 'Dai programmi puoi scrivermi anche con Aiuto, Contattami: prepara già il messaggio con la versione che usi.',
        'guida_inglese': '',
        'mesi': ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre'],
    },
    'en': {
        'lingua_nome': 'English', 'altra_lingua': 'Italiano', 'salta': 'Skip to main content',
        'menu': 'Main menu', 'home': 'Home', 'programmi': 'Programs', 'chi_sono': 'About me', 'contatti': 'Contact',
        'scrivimi': 'write to me',
        'home_titolo': 'Hi, I\'m Andrea',
        'home_lede': 'Music, technology and the wish to make things a little easier to use, for everyone.',
        'home_testo': 'This is my small place online. Here you find the programs I build, all free and designed from the start for people who use a screen reader, and if you like my story on the "About me" page.',
        'i_miei_programmi': 'My programs',
        'programmi_titolo': 'Programs',
        'programmi_lede': 'All free, for Windows, and designed from day one for people who use a screen reader.',
        'programmi_testo': 'Each program has its own page with the download, the guide to read online and what\'s new in every version. They update themselves when a new version comes out.',
        'scopri': 'Discover {0}', 'scarica': 'Download {0}', 'versione_del': 'Version {0}, {1}',
        'in_arrivo': 'Coming soon',
        'gratuito': 'Free, for Windows 10 and 11. The link always gets the latest version.',
        'cosa_serve': 'What you need', 'cosa_fa': 'What it does',
        'guida_novita': 'Guide and what\'s new',
        'leggi_guida': 'The {0} guide, to read online (in Italian)',
        'leggi_novita': 'What\'s new in every version',
        'tutte_versioni': 'All versions on GitHub',
        'sostieni_titolo': 'Support the project',
        'sostieni_testo': 'My programs are free and I develop them on my own, in my spare time. If you find them useful, you can help me with a donation.',
        'sostieni': 'Support via PayPal',
        'community': 'Join the community on Telegram',
        'community_testo': 'In the Gram Access community on Telegram you can ask questions, talk with other users and make suggestions.',
        'domande': 'Questions or suggestions? <a href="contatti.html">Write to me</a>.',
        'novita_titolo': 'What\'s new in {0}', 'novita_lede': 'Versions from the most recent. The same notes are in the program, in Help.',
        'torna_a': 'Back to {0}',
        'chi_sono_lede': 'My name is Andrea Dessolis, and if I had to sum myself up in a few words I would say: music, technology, and the wish to understand how the two can help each other.',
        'chi_sono_testo': [
            'I have been playing the guitar for years, and it is one of the things that relaxes and amuses me most. But the real turning point of my life came when, already an adult, I lost my sight. From that moment technology was no longer just a hobby: it became an essential tool, almost vital, to keep enjoying the things I love and to discover new ones.',
            'That is where my passion for everything about accessibility comes from: software, methods, small touches that can make a big difference for people who, like me, rely on a screen reader every day. I like to think that every program, every website, every tool can be made easier to use for everyone: you just have to really want it.',
            'This is the idea behind <a href="programmi.html">my programs</a>: first Gram Access for Telegram, then HDX VM for Voicemeeter and PCloud Access for pCloud, and soon HDX Recorder for recording.',
        ],
        'contatti_lede': 'Whether it is about one of my programs, accessibility or just a chat: feel free to write to me.',
        'email_titolo': 'Email', 'email_testo': 'The easiest way to reach me is by email:',
        'contatti_programmi': 'From the programs you can also write to me with Help, Contact me: it prepares the message with the version you use.',
        'guida_inglese': 'The guide is in Italian for now.',
        'mesi': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    },
}

# Versione e data dell'ultima pubblicazione di ogni programma (le scrive pubblica.py).
_VERSIONI = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'versioni.json'), encoding='utf-8'))
for _p in PROGRAMMI:
    _p.update(_VERSIONI.get(_p['id'], {}))
