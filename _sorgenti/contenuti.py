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
                'Il tuo account: accesso anche con la verifica in due passaggi (SMS, app pCloud, app di autenticazione, codici di riserva), dispositivi collegati, password, email, inviti agli amici.',
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
                'Your account: sign-in also with two-factor authentication (SMS, pCloud app, authenticator app, backup codes), connected devices, password, email, inviting friends.',
                'Announcements by voice or with sounds, as you choose, and the window in the notification area.',
                'Automatic updates, in Italian, English and Spanish.',
            ],
        },
    },
    {
        'id': 'tube-player',
        'pagina': 'tube-player.html',
        'nome': 'Tube Player',
        'logo': 'tube-player.png',
        'alt': {
            'it': 'Logo di Tube Player: un vecchio televisore bianco con le antenne, con un tasto Play corallo e tre onde sonore sullo schermo, su un quadrato blu petrolio',
            'en': 'Tube Player logo: an old white television with antennas, with a coral Play button and three sound waves on the screen, on a petrol blue square',
        },
        'stato': 'disponibile',
        'repository': 'Tube-Player',
        'setup': 'Tube-Player-Setup.exe',
        'guida': r'D:\Software Portable\Sviluppo Software\Tube Player\documenti\Guida.html',
        'novita': ('hdx-json', r'D:\Software Portable\Sviluppo Software\Tube Player\rilascio\changelog.json'),
        'frase': {
            'it': 'YouTube in modo semplice e accessibile: cerchi, ascolti, guardi e scarichi i video con lo screen reader.',
            'en': 'YouTube made simple and accessible: search, listen to, watch and download videos with your screen reader.',
        },
        'breve': {
            'it': 'YouTube accessibile: ricerca, canali, playlist, lettore, download e raccolte.',
            'en': 'Accessible YouTube: search, channels, playlists, player, downloads and collections.',
        },
        'introduzione': {
            'it': [
                'YouTube è pieno di musica, video e trasmissioni, ma la sua pagina web è lunga e faticosa da esplorare con NVDA o JAWS. Tube Player ti fa usare YouTube come un elenco semplice, con i tasti di Windows che conosci già: cerchi, scegli con le frecce e premi Invio. Il video parte in un lettore fatto di pulsanti veri, tutti raggiungibili con il Tab.',
                'Tube Player è un programma indipendente: non è un prodotto di YouTube né di Google. Per leggere YouTube usa yt-dlp e per riprodurre i video usa mpv, due programmi liberi che scarica e tiene aggiornati da solo. Non serve un account.',
            ],
            'en': [
                'YouTube is full of music, videos and shows, but its web page is long and tiring to explore with NVDA or JAWS. Tube Player lets you use YouTube as a simple list, with the Windows keys you already know: you search, choose with the arrow keys and press Enter. The video starts in a player made of real buttons, all reachable with Tab.',
                'Tube Player is an independent program: it is not a product of YouTube or Google. To read YouTube it uses yt-dlp and to play videos it uses mpv, two free programs that it downloads and keeps up to date by itself. No account is needed.',
            ],
        },
        'requisiti': {
            'it': ['Windows 10 o 11 a 64 bit.',
                   'Una connessione a internet: al primo avvio il programma scarica da solo i componenti che gli servono.'],
            'en': ['Windows 10 or 11, 64-bit.',
                   'An internet connection: the first time it starts, the program downloads by itself the components it needs.'],
        },
        'funzioni': {
            'it': [
                'Ricerca di video, canali e playlist, con risultati che dicono canale, durata e visualizzazioni, e un elenco che si allunga da solo.',
                'Canali e playlist come cartelle: Invio per entrare, Backspace per tornare indietro; dentro un canale i suoi video, le sue playlist e le sue dirette.',
                'Un lettore accessibile: posizione, pausa, avanti e indietro, volume, velocità, e le immagini da accendere solo quando servono.',
                'I tasti principali valgono ovunque, e i video partono in fretta perché si preparano in anticipo.',
                'Riproduzione continua di una playlist, di un canale o dei risultati, con video successivo e precedente.',
                'La scheda di ogni video, con la descrizione e i capitoli da cui farlo partire.',
                'Download di video e audio in tanti formati (MP3, M4A, Opus, FLAC, MP4, MKV e il formato originale), anche di playlist e canali interi.',
                'Le raccolte: i tuoi elenchi di video, canali e playlist, ognuno con il nome che vuoi.',
                'Annunci a voce o con suoni, a scelta, e scorciatoie tutte modificabili.',
                'Aggiornamenti automatici, e in italiano, inglese e spagnolo.',
            ],
            'en': [
                'Search for videos, channels and playlists, with results that tell you channel, length and views, and a list that grows by itself.',
                'Channels and playlists like folders: Enter to go inside, Backspace to go back; inside a channel its videos, its playlists and its live streams.',
                'An accessible player: position, pause, forward and back, volume, speed, and the picture to turn on only when you need it.',
                'The main keys work everywhere, and videos start quickly because they are prepared in advance.',
                'Continuous playback of a playlist, a channel or the results, with next and previous video.',
                'The details of every video, with the description and the chapters to start it from.',
                'Video and audio downloads in many formats (MP3, M4A, Opus, FLAC, MP4, MKV and the original format), whole playlists and channels too.',
                'Collections: your own lists of videos, channels and playlists, each with the name you want.',
                'Announcements by voice or with sounds, as you choose, and fully customizable shortcuts.',
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
        'stato': 'disponibile',
        'repository': 'HDX-Recorder',
        'setup': 'HDX-Recorder-Setup.exe',
        # La guida come la distribuisce il programma (senza le parti ASIO,
        # che restano fuori finche' non c'e' l'accordo di Steinberg).
        'guida': r'D:\Software Portable\Sviluppo Software\HDX Recorder\Programma\Documenti\Guida.html',
        'novita': ('hdx-json', r'D:\Software Portable\Sviluppo Software\HDX Recorder\rilascio\changelog.json'),
        'frase': {
            'it': 'Registrare audio e video e andare in diretta su una radio web, tutto con lo screen reader: per podcast, trasmissioni radio, lezioni e tutorial.',
            'en': 'Recording audio and video and going live on a web radio, all with your screen reader: for podcasts, radio shows, lessons and tutorials.',
        },
        'breve': {
            'it': 'Registrazioni audio e video, dirette radio con la regia, mixer, effetti e intelligenza artificiale.',
            'en': 'Audio and video recordings, radio broadcasts with a control room, mixer, effects and artificial intelligence.',
        },
        'introduzione': {
            'it': [
                'HDX Recorder registra insieme tutto quello che ti serve, ognuno al suo volume: i microfoni, l\'audio del computer o di un solo programma, una musica di sottofondo, una radio da Internet e, per il video, lo schermo, una finestra o la webcam. Si comanda tutto con la tastiera, e lo screen reader ti dice sempre cosa sta succedendo, anche mentre lavori in un altro programma.',
                'Quando vuoi andare in onda, HDX Recorder diventa la tua radio: trasmetti su una radio web con una regia completa, pensata per chi conduce senza guardare lo schermo, con la scaletta dei brani, le sigle, i pad sonori, la pausa in onda, il monitor in cuffia e l\'audio per gli ospiti collegati, per esempio su Zoom.',
            ],
            'en': [
                'HDX Recorder records together everything you need, each at its own volume: microphones, computer audio or the audio of a single program, background music, an Internet radio and, for video, the screen, a window or the webcam. Everything is controlled with the keyboard, and your screen reader always tells you what is happening, even while you work in another program.',
                'When you want to go on air, HDX Recorder becomes your radio station: you broadcast on a web radio with a complete control room, designed for people who host without looking at the screen, with the track list, jingles, sound pads, the on-air break, the headphone monitor and the audio for guests connected, for example, on Zoom.',
            ],
        },
        'requisiti': {
            'it': ['Windows 10 o 11 a 64 bit.',
                   'Uno screen reader: HDX Recorder parla con NVDA e con JAWS anche quando non è in primo piano.'],
            'en': ['Windows 10 or 11, 64-bit.',
                   'A screen reader: HDX Recorder talks with NVDA and JAWS even when it is not in the foreground.'],
        },
        'funzioni': {
            'it': [
                'Più sorgenti insieme: microfoni e ingressi, audio del computer, un solo programma, file di sottofondo, radio da Internet e pad sonori, ognuna con il suo volume.',
                'Molti formati: WAV, AIFF, FLAC, ALAC, MP3, Opus e AAC, con il mix e, se vuoi, una traccia separata per ogni sorgente.',
                'Il controllo prima del via, la prova dei livelli e l\'avviso di saturazione: sai sempre se si sente bene, prima e durante la registrazione.',
                'Il mixer, gli effetti per ogni sorgente (riduzione del rumore, compressore, equalizzatore, de-esser, riverbero e altri), il mix finale e le scene da richiamare con un tasto.',
                'Il video dello schermo, di una finestra o della webcam, con la composizione, lo sfondo, il testo, lo zoom che segue e le evidenze per i tutorial.',
                'Le dirette su radio web in MP3, AAC o Opus, anche su più radio insieme, con la regia: scaletta, conto alla rovescia e sigla, pausa in onda, preascolto, registro di messa in onda e la diretta di prova per allenarsi.',
                'Dirette su YouTube con il tuo account: la diretta si crea da sola sul canale, con titolo, descrizione, visibilità e miniatura, il titolo si cambia in onda, la chat si ascolta e si risponde, e le dirette si possono programmare (in arrivo con la prossima versione).',
                'Il monitor del conduttore in cuffia e i ritorni per gli ospiti collegati, con il volume regolabile anche in diretta.',
                'Registrazioni programmate, anche con il programma chiuso, e gli automatismi del silenzio.',
                'Intelligenza artificiale con una tua chiave Gemini o OpenAI: trascrizioni e sottotitoli, riassunti, controllo della qualità e descrizione del video.',
                'Annunci a voce o con suoni riconoscibili, e scorciatoie tutte modificabili, anche valide in tutto Windows.',
                'Aggiornamenti automatici, e in italiano, inglese e spagnolo.',
            ],
            'en': [
                'Many sources together: microphones and inputs, computer audio, a single program, background files, Internet radio and sound pads, each at its own volume.',
                'Many formats: WAV, AIFF, FLAC, ALAC, MP3, Opus and AAC, with the mix and, if you want, a separate track for each source.',
                'The pre-start check, the level test and the clipping warning: you always know if it sounds right, before and during the recording.',
                'The mixer, effects for each source (noise reduction, compressor, equalizer, de-esser, reverb and more), the final mix and scenes to recall with a key.',
                'Video of the screen, of a window or of the webcam, with composition, background, text, follow zoom and highlights for tutorials.',
                'Live broadcasts on web radio in MP3, AAC or Opus, on several radios at once too, with the control room: track list, countdown and jingle, on-air break, preview, on-air log and the test live to practise.',
                'YouTube live broadcasts with your account: the live is created on your channel automatically, with title, description, visibility and thumbnail, the title can be changed on air, you can listen to the chat and reply, and live broadcasts can be scheduled (coming with the next version).',
                'The presenter\'s headphone monitor and returns for connected guests, with their volume adjustable even on air.',
                'Scheduled recordings, even with the program closed, and silence automations.',
                'Artificial intelligence with your own Gemini or OpenAI key: transcriptions and subtitles, summaries, quality check and video description.',
                'Announcements by voice or with recognizable sounds, and fully customizable shortcuts, also working everywhere in Windows.',
                'Automatic updates, in Italian, English and Spanish.',
            ],
        },
    },
]

# Le add-on per NVDA: tutte nella pagina addon-nvda.html, una sezione ciascuna
# (l'ancora #id e' anche l'indirizzo scritto nel manifest delle add-on).
# Ognuna ha un repository di sole release con il pacchetto dal nome fisso;
# novita' e guide vengono dalla cartella dell'add-on.
_ADDON = r'D:\Software Portable\Sviluppo Software\NVDA Addons'
ADDON = [
    {
        'id': 'navigazione-web',
        'nome': {'it': 'Navigazione web', 'en': 'Web Navigation'},
        'repository': 'NVDA-Navigazione-Web',
        'setup': 'navigazioneWeb.nvda-addon',
        'cartella': _ADDON + r'\Navigazione web',
        'nvda_minimo': '2024.1',
        'frase': {
            'it': 'Le funzioni di JAWS per il web che NVDA non ha, ognuna da accendere o spegnere nelle impostazioni.',
            'en': 'The JAWS web features that NVDA does not have, each one to turn on or off in the settings.',
        },
        'funzioni': {
            'it': [
                'Intestazioni con un link, come i titoli dei video di YouTube: si legge la riga completa, con la durata, e il focus va sul link.',
                'Maiusc+Invio, Ctrl+Invio e il tasto Applicazioni aprono il link dove sei, non quello che aveva il focus.',
                'NVDA+A, con lo schema di tastiera desktop, dice l\'indirizzo della pagina; premuto due volte lo copia.',
                'Tasti di salto per schede, articoli e regione principale, che fanno scorrere la pagina per cercare altri elementi.',
                'La ricerca di NVDA ricorda la parola cercata per ogni pagina, anche dopo il riavvio.',
                'Elementi della pagina con NVDA+F6: pulsanti, caselle, tabelle, link e altro, con filtro.',
                'Segnaposti con J, per la pagina o per tutto il sito, e il segnaposto temporaneo.',
                'Punti smart con Y, come la Smart Glance di JAWS: il testo che si nota a vista.',
            ],
            'en': [
                'Headings with a link, like YouTube video titles: the full line is read, with the length, and the focus moves to the link.',
                'Shift+Enter, Control+Enter and the Applications key open the link where you are, not the one that had the focus.',
                'NVDA+A, with the desktop keyboard layout, reports the page address; pressed twice, it copies it.',
                'Quick navigation keys for tabs, articles and the main landmark, which scroll the page to look for more elements.',
                'NVDA\'s search remembers the searched word for each page, even after a restart.',
                'Page elements with NVDA+F6: buttons, fields, tables, links and more, with a filter.',
                'Placemarkers with J, for the page or for the whole site, and the temporary placemarker.',
                'Smart points with Y, like the Smart Glance of JAWS: the text that stands out to the eye.',
            ],
        },
    },
    {
        'id': 'shortcut-conflict-helper',
        'nome': {'it': 'Shortcut Conflict Helper', 'en': 'Shortcut Conflict Helper'},
        'repository': 'NVDA-Shortcut-Conflict-Helper',
        'setup': 'shortcut_conflict_helper.nvda-addon',
        'cartella': _ADDON + r'\Shortcut Conflict Helper',
        'nvda_minimo': '2024.1',
        'frase': {
            'it': 'Trova i tasti assegnati a più comandi nella finestra Gesti e comandi, e ti aiuta a sistemarli.',
            'en': 'Finds the keys assigned to more than one command in the Input gestures window, and helps you sort them out.',
        },
        'funzioni': {
            'it': [
                'All\'apertura di Gesti e comandi mostra i conflitti, solo se ci sono, e dice quale comando vince.',
                'Ogni conflitto si modifica, si toglie o si ignora.',
                'Avvisa prima di assegnare un tasto già usato.',
                'Cerca per tasto: premi un tasto e vedi solo i comandi che lo usano.',
            ],
            'en': [
                'When Input gestures opens it shows the conflicts, only if there are some, and tells which command wins.',
                'Each conflict can be changed, removed or ignored.',
                'Warns before assigning a key that is already used.',
                'Search by key: press a key and see only the commands that use it.',
            ],
        },
    },
    {
        'id': 'gestore-finestre',
        'nome': {'it': 'Gestore Finestre', 'en': 'Window Manager'},
        'repository': 'NVDA-Gestore-Finestre',
        'setup': 'nvda_window_manager.nvda-addon',
        'cartella': _ADDON + r'\Gestore Finestre',
        'nvda_minimo': '2023.1',
        'frase': {
            'it': 'Con NVDA+W l\'elenco di tutte le finestre aperte, per portarle in primo piano o chiuderle.',
            'en': 'With NVDA+W, the list of all open windows, to bring them to the foreground or close them.',
        },
        'funzioni': {
            'it': [
                'Le finestre nell\'ordine di Alt+Tab, con il nome del programma, comprese finestre secondarie e dialoghi.',
                'Invio porta la finestra in primo piano, Canc la chiude.',
                'Se il programma chiede conferma prima di chiudere, porta davanti la domanda.',
                'Dice quando una finestra non si chiude o non si può portare in primo piano.',
            ],
            'en': [
                'The windows in Alt+Tab order, with the program name, including secondary windows and dialogs.',
                'Enter brings the window to the foreground, Delete closes it.',
                'If the program asks for confirmation before closing, the question is brought to the front.',
                'Tells you when a window does not close or cannot be brought to the foreground.',
            ],
        },
    },
    {
        'id': 'blocco-modificatore',
        'nome': {'it': 'Blocco Modificatore NVDA', 'en': 'NVDA Modifier Lock'},
        'repository': 'NVDA-Blocco-Modificatore',
        'setup': 'nvda_modifier_lock.nvda-addon',
        'cartella': _ADDON + r'\Blocco Modificatore NVDA',
        'nvda_minimo': '2023.1',
        'frase': {
            'it': 'Il tasto NVDA bloccato, come il tasto JAWS: lo tocchi, lo lasci e poi premi l\'altro tasto.',
            'en': 'The locked NVDA key, like the JAWS key: tap it, let it go, then press the other key.',
        },
        'funzioni': {
            'it': [
                'Un tocco del tasto NVDA lo lascia premuto per il tasto successivo, poi si sblocca da solo.',
                'Maiusc, Ctrl, Alt e Windows non sbloccano: funzionano anche combinazioni come NVDA+Maiusc+J.',
                'Un altro tocco sblocca; due tocchi veloci fanno la funzione normale del tasto, per esempio Bloc Maiusc.',
                'Avviso con suoni, voce o entrambi, e un comando per accenderlo e spegnerlo al volo.',
            ],
            'en': [
                'One tap of the NVDA key keeps it pressed for the next key, then it unlocks by itself.',
                'Shift, Control, Alt and Windows do not unlock it: combinations like NVDA+Shift+J work too.',
                'Another tap unlocks it; two quick taps do the key\'s normal function, for example Caps Lock.',
                'Feedback with beeps, speech or both, and a command to turn it on and off at any time.',
            ],
        },
    },
]
for _a in ADDON:
    _a['pagina'] = 'addon-nvda.html#' + _a['id']
    _a['novita'] = ('hdx-json', _a['cartella'] + r'\novita.json')
    _a['guide'] = {lingua: _a['cartella'] + rf'\addon\doc\{lingua}\readme.html' for lingua in ('it', 'en')}

# I testi fissi delle pagine.
T = {
    'it': {
        'lingua_nome': 'Italiano', 'altra_lingua': 'English', 'salta': 'Vai al contenuto principale',
        'menu': 'Menu principale', 'home': 'Home', 'programmi': 'Programmi', 'chi_sono': 'Chi sono', 'contatti': 'Contatti',
        'addon': 'Add-on per NVDA',
        'addon_lede': 'Piccole estensioni gratuite per lo screen reader NVDA, nate per rendere più comodo il lavoro di ogni giorno.',
        'addon_testo': 'Ognuna parla nella lingua di NVDA, italiano o inglese, e ha la sua guida, che si apre anche dal Gestore componenti aggiuntivi di NVDA.',
        'addon_per_nvda': 'Per NVDA {0} e successive.',
        'addon_guida': 'La guida di {0}, da leggere online',
        'addon_installa_titolo': 'Come si installano',
        'addon_installa': [
            'Scarica l\'add-on con il suo pulsante.',
            'Apri il file scaricato: NVDA chiede se installarlo. Rispondi Sì.',
            'Riavvia NVDA quando te lo chiede.',
        ],
        'addon_aggiorna': 'Per aggiornare un\'add-on si fa allo stesso modo: scarica la versione nuova e installala sopra quella vecchia. Le tue impostazioni restano.',
        'addon_novita_lede': 'Le versioni dalla più recente. Le novità della versione installata si leggono anche nel Gestore componenti aggiuntivi di NVDA.',
        'scrivimi': 'scrivimi',
        'home_titolo': 'Ciao, sono Andrea',
        'home_lede': 'Musica, tecnologia e la voglia di rendere le cose un po\' più semplici da usare, per tutti.',
        'home_testo': 'Questo è il mio piccolo spazio online. Qui trovi i programmi che costruisco, tutti gratuiti e pensati fin dall\'inizio per chi usa uno screen reader, alcune add-on per NVDA e, se vuoi, la mia storia nella pagina "Chi sono".',
        'i_miei_programmi': 'I miei programmi',
        'programmi_titolo': 'Programmi',
        'programmi_lede': 'Tutti gratuiti, per Windows, e pensati fin dal primo giorno per chi usa uno screen reader.',
        'programmi_testo': 'Ogni programma ha la sua pagina con il download, la guida da leggere online e le novità di ogni versione. Si aggiornano da soli quando esce una versione nuova.',
        'scopri': 'Scopri {0}', 'scarica': 'Scarica {0}', 'versione_del': 'Versione {0} del {1}',
        'in_arrivo': 'In arrivo',
        'gratuito': 'Gratuito, per Windows 10 e 11. Il link porta sempre all\'ultima versione.',
        'cosa_serve': 'Cosa serve', 'cosa_fa': 'Cosa fa',
        'guida_novita': 'Guida e novità',
        'leggi_privacy': 'Privacy: che cosa fa {0} con i tuoi dati',
        'aggiornata_il': 'Ultimo aggiornamento: {0}.',
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
            'È da questa idea che sono nati i <a href="programmi.html">miei programmi</a>: prima Gram Access per Telegram, poi HDX VM per Voicemeeter, PCloud Access per pCloud, Tube Player per YouTube e HDX Recorder per registrare e andare in diretta. Uso NVDA ogni giorno, e per renderlo più comodo ho scritto anche alcune <a href="addon-nvda.html">add-on per NVDA</a>.',
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
        'addon': 'NVDA Add-ons',
        'addon_lede': 'Small free extensions for the NVDA screen reader, made to make everyday work more comfortable.',
        'addon_testo': 'Each one speaks the language of NVDA, English or Italian, and has its own guide, which also opens from the NVDA add-on manager.',
        'addon_per_nvda': 'For NVDA {0} and later.',
        'addon_guida': 'The {0} guide, to read online',
        'addon_installa_titolo': 'How to install them',
        'addon_installa': [
            'Download the add-on with its button.',
            'Open the downloaded file: NVDA asks whether to install it. Answer Yes.',
            'Restart NVDA when it asks you to.',
        ],
        'addon_aggiorna': 'To update an add-on, do the same: download the new version and install it over the old one. Your settings are kept.',
        'addon_novita_lede': 'Versions from the most recent. What\'s new in the installed version can also be read in the NVDA add-on manager.',
        'scrivimi': 'write to me',
        'home_titolo': 'Hi, I\'m Andrea',
        'home_lede': 'Music, technology and the wish to make things a little easier to use, for everyone.',
        'home_testo': 'This is my small place online. Here you find the programs I build, all free and designed from the start for people who use a screen reader, some NVDA add-ons and, if you like, my story on the "About me" page.',
        'i_miei_programmi': 'My programs',
        'programmi_titolo': 'Programs',
        'programmi_lede': 'All free, for Windows, and designed from day one for people who use a screen reader.',
        'programmi_testo': 'Each program has its own page with the download, the guide to read online and what\'s new in every version. They update themselves when a new version comes out.',
        'scopri': 'Discover {0}', 'scarica': 'Download {0}', 'versione_del': 'Version {0}, {1}',
        'in_arrivo': 'Coming soon',
        'gratuito': 'Free, for Windows 10 and 11. The link always gets the latest version.',
        'cosa_serve': 'What you need', 'cosa_fa': 'What it does',
        'guida_novita': 'Guide and what\'s new',
        'leggi_privacy': 'Privacy: what {0} does with your data',
        'aggiornata_il': 'Last updated: {0}.',
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
            'This is the idea behind <a href="programmi.html">my programs</a>: first Gram Access for Telegram, then HDX VM for Voicemeeter, PCloud Access for pCloud, Tube Player for YouTube and HDX Recorder for recording and going live. I use NVDA every day, and to make it more comfortable I also wrote some <a href="addon-nvda.html">NVDA add-ons</a>.',
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
for _p in PROGRAMMI + ADDON:
    _p.update(_VERSIONI.get(_p['id'], {}))
