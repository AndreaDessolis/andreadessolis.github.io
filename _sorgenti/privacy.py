"""Le pagine sulla privacy dei programmi (privacy-<id>.html), in italiano e
in inglese. Per HDX Recorder la chiedono anche Google e YouTube (la verifica
dell'app per l'account YouTube): deve dire quali dati dell'account usa il
programma, per che cosa, come li protegge, dove restano e come si toglie il
permesso. Google ha chiesto (31 ott 2026) due sezioni esplicite: come si
usano i dati dell'utente Google e come sono protetti.

Ogni pagina: titolo, data dell'ultimo aggiornamento, una frase d'apertura e
le sezioni (titolo, elementi). Un elemento e' un paragrafo (testo) o un
elenco (lista di testi). I testi possono contenere collegamenti HTML.
"""

TERMINI_YOUTUBE = 'https://www.youtube.com/t/terms'
PRIVACY_GOOGLE = 'https://policies.google.com/privacy'
PERMESSI_GOOGLE = 'https://security.google.com/settings/security/permissions'
NORME_DATI_API = 'https://developers.google.com/terms/api-services-user-data-policy'


def _a(indirizzo, testo=None):
    return f'<a href="{indirizzo}">{testo or indirizzo}</a>'


PRIVACY = {
    'hdx-recorder': {
        'aggiornata': '2026-10-31',
        'it': {
            'titolo': 'Privacy di HDX Recorder',
            'lede': 'HDX Recorder è un programma che funziona sul tuo computer. Io, che lo scrivo, non raccolgo nessun dato su di te: non c\'è un server di HDX Recorder, non ci sono statistiche, pubblicità o cookie.',
            'sezioni': [
                ('Dove restano i tuoi dati', [
                    'Le registrazioni, le impostazioni, le password delle radio e i permessi restano sul tuo computer, nella cartella di HDX Recorder. Le password e i permessi sono cifrati con la protezione di Windows, per il tuo utente, e non vanno nelle copie di sicurezza delle impostazioni.',
                ]),
                ('Quando il programma si collega a Internet', [
                    'Solo quando usi una funzione che ne ha bisogno, e solo con il servizio che serve a quella funzione:',
                    [
                        'il controllo degli aggiornamenti scarica l\'elenco delle versioni, senza mandare dati personali;',
                        'la ricerca delle radio da ascoltare manda il testo che cerchi al servizio pubblico ' + _a('https://www.radio-browser.info', 'radio-browser.info') + ';',
                        'le dirette su una radio web vanno al server della radio che scegli tu, con i dati che scrivi tu;',
                        'l\'intelligenza artificiale funziona solo con una tua chiave di Google Gemini o di OpenAI: l\'audio, il testo o le immagini che scegli di far analizzare vanno a quel servizio, secondo le sue regole. I dati del tuo account YouTube non vengono mai mandati a questi servizi;',
                        'le funzioni di YouTube (dirette, video, playlist e canale) usano i servizi API di YouTube, come spiegato qui sotto.',
                    ],
                ]),
                ('YouTube e i servizi API di YouTube', [
                    'Per le funzioni di YouTube con l\'account collegato, HDX Recorder usa i servizi API di YouTube. Usando queste funzioni accetti i ' + _a(TERMINI_YOUTUBE, 'Termini di servizio di YouTube') + '. Per i dati che tratta Google valgono le ' + _a(PRIVACY_GOOGLE, 'Norme sulla privacy di Google') + '.',
                    'Quando colleghi l\'account, Google ti chiede il permesso di gestire il tuo account YouTube. È l\'unico permesso che HDX Recorder chiede: non chiede accesso alla tua posta, ai tuoi file, ai tuoi contatti o ad altri servizi di Google.',
                ]),
                ('Quali dati dell\'account Google usa HDX Recorder', [
                    'HDX Recorder legge e modifica solo i dati del tuo canale YouTube che servono alle funzioni che usi:',
                    [
                        'il nome e l\'identificativo del tuo canale;',
                        'la descrizione del canale, le parole chiave, l\'immagine di copertina e la filigrana dei video;',
                        'l\'elenco dei video che hai caricato, con titolo, descrizione, visibilità, data, durata, numero di visualizzazioni, stato dell\'elaborazione e gli eventuali problemi segnalati da YouTube (per esempio i paesi in cui un video è bloccato);',
                        'le tue playlist e i video che contengono;',
                        'le tue dirette e le dirette programmate;',
                        'i messaggi della chat delle tue dirette, con il nome e l\'identificativo del canale di chi li scrive.',
                    ],
                    'HDX Recorder non legge i tuoi iscritti, i tuoi commenti, i dati delle tue entrate o le statistiche di YouTube Analytics.',
                ]),
                ('Come HDX Recorder usa i dati dell\'account Google', [
                    'I dati del tuo account vengono usati solo per farti usare le funzioni del programma, e solo quando le usi tu:',
                    [
                        'mostrare nel programma il nome del tuo canale;',
                        'creare sul tuo canale le dirette, con il titolo, la descrizione e la visibilità che scegli, collegarle al segnale che mandi e chiuderle quando termini; cambiarne il titolo e caricarne la miniatura quando lo chiedi tu;',
                        'creare, elencare ed eliminare le dirette programmate, quando lo chiedi tu;',
                        'leggerti i messaggi della chat della diretta e mandare nella chat i messaggi che scrivi tu;',
                        'moderare la chat quando lo chiedi tu: eliminare un messaggio, mettere in pausa o bloccare chi scrive, togliere un blocco, nominare un moderatore;',
                        'mostrarti l\'elenco dei tuoi video e il loro stato; modificarne il titolo, la descrizione e la visibilità, programmarne la pubblicazione o eliminarli, quando lo chiedi tu;',
                        'caricare sul tuo canale il file video che scegli tu, con il titolo, la descrizione e la visibilità che scrivi tu, e dirti quando YouTube ha finito di elaborarlo;',
                        'creare, modificare ed eliminare le tue playlist, e aggiungere, togliere o spostare i video al loro interno, quando lo chiedi tu;',
                        'cambiare la descrizione, le parole chiave, la copertina e la filigrana del tuo canale, quando lo chiedi tu.',
                    ],
                    'Ogni modifica al tuo canale parte solo da un tuo comando: il programma non cambia, non pubblica e non elimina niente da solo. Prima di eliminare qualcosa ti chiede sempre conferma.',
                    'L\'uso e il trasferimento ad altre app delle informazioni ricevute dalle API di Google da parte di HDX Recorder rispettano le ' + _a(NORME_DATI_API, 'Norme sui dati utente dei servizi API di Google') + ', compresi i requisiti di uso limitato (Limited Use).',
                    'I dati del tuo account Google non vengono venduti, non vengono usati per pubblicità, non vengono usati per addestrare modelli di intelligenza artificiale e non vengono letti da nessuna persona: io non li ricevo mai.',
                ]),
                ('Come sono protetti i tuoi dati', [
                    [
                        'Connessione cifrata: HDX Recorder parla con Google solo attraverso connessioni cifrate (HTTPS), direttamente dal tuo computer ai server di Google. Non ci sono server intermedi, né miei né di altri.',
                        'La tua password resta a Google: l\'accesso si fa nel tuo browser, sulla pagina di Google, con il metodo standard OAuth 2.0 protetto da PKCE. HDX Recorder non vede e non salva mai la password del tuo account Google; riceve solo un permesso che puoi togliere quando vuoi.',
                        'Permesso cifrato: l\'unico dato dell\'account salvato sul disco è il permesso di Google (il "token di rinnovo"), cifrato con la protezione dati di Windows (DPAPI) e legato al tuo utente di Windows. Copiato su un altro computer o in un altro utente non si può usare. Non va nelle copie di sicurezza delle impostazioni.',
                        'Permesso di breve durata: il permesso usato per ogni richiesta a YouTube dura circa un\'ora e resta solo nella memoria del programma, mai sul disco.',
                        'Il minimo indispensabile: HDX Recorder chiede un solo permesso, quello per gestire il tuo account YouTube, e conserva solo i dati elencati nella sezione qui sotto.',
                        'Niente copie altrove: non avendo un server, HDX Recorder non manda i tuoi dati a nessun altro posto; restano tra il tuo computer e Google.',
                    ],
                ]),
                ('Che cosa resta sul tuo computer, e per quanto', [
                    [
                        'Il permesso di Google (il "token di rinnovo"): cifrato, finché non scolleghi l\'account. A ogni avvio il programma controlla che valga ancora; se l\'hai tolto da Google, lo cancella.',
                        'Il nome del canale: accanto al permesso, aggiornato a ogni avvio del programma.',
                        'Il titolo, la descrizione, la visibilità e la miniatura dell\'ultima diretta: sono quelli che scrivi tu, e il programma li propone la volta dopo.',
                        'L\'elenco dei video e delle playlist, i dati del canale, i messaggi della chat e i link: solo nella memoria del programma, mentre li stai usando. Non vengono salvati su disco e spariscono quando chiudi il programma.',
                        'I video che carichi: il programma legge il file dal tuo computer e lo manda a YouTube, senza farne copie.',
                    ],
                ]),
                ('Con chi sono condivisi', [
                    'Con nessuno. I dati del tuo account YouTube passano solo tra il tuo computer e Google, e solo per le funzioni che usi. Io non li ricevo, non li vendo e non li cedo a nessuno.',
                ]),
                ('Come togliere il permesso e cancellare i dati', [
                    [
                        'Nel programma: menu YouTube, Account YouTube, poi Scollega l\'account YouTube (lo trovi anche in Strumenti, Impostazioni, categoria Diretta, YouTube, Modifica). HDX Recorder chiede a Google di annullare il permesso e cancella subito il permesso e il nome del canale dal tuo computer.',
                        'Dal tuo account Google, nella ' + _a(PERMESSI_GOOGLE, 'pagina delle app con accesso al tuo account') + '. Alla prossima apertura HDX Recorder se ne accorge e cancella i dati dal tuo computer.',
                        'Eliminando la cartella di HDX Recorder si cancella tutto quello che il programma ha salvato.',
                    ],
                    'Togliere il permesso non cancella niente su YouTube: i video, le playlist, le dirette e i messaggi della chat restano sul tuo canale, e li gestisci da YouTube Studio.',
                ]),
                ('Domande', [
                    'Per qualunque domanda o richiesta sulla privacy puoi scrivermi a <a href="mailto:dessolisandrea@gmail.com">dessolisandrea@gmail.com</a>.',
                    'Se questa pagina cambia, la data dell\'ultimo aggiornamento qui sopra lo dice. Se cambia il modo in cui HDX Recorder usa i dati del tuo account Google, lo scrivo anche nelle novità della versione.',
                ]),
            ],
        },
        'en': {
            'titolo': 'HDX Recorder privacy',
            'lede': 'HDX Recorder is a program that runs on your computer. I, the author, do not collect any data about you: there is no HDX Recorder server, and there are no statistics, ads or cookies.',
            'sezioni': [
                ('Where your data stays', [
                    'Recordings, settings, radio passwords and permissions stay on your computer, in the HDX Recorder folder. Passwords and permissions are encrypted with Windows protection, for your user, and are not included in settings backups.',
                ]),
                ('When the program connects to the Internet', [
                    'Only when you use a feature that needs it, and only with the service that feature needs:',
                    [
                        'the update check downloads the list of versions, without sending personal data;',
                        'the search for radio stations to listen to sends the text you search for to the public service ' + _a('https://www.radio-browser.info', 'radio-browser.info') + ';',
                        'live broadcasts on a web radio go to the server of the radio you choose, with the data you type;',
                        'artificial intelligence works only with your own Google Gemini or OpenAI key: the audio, text or images you choose to have analysed go to that service, under its own rules. Your YouTube account data is never sent to these services;',
                        'the YouTube features (live broadcasts, videos, playlists and channel) use the YouTube API Services, as explained below.',
                    ],
                ]),
                ('YouTube and the YouTube API Services', [
                    'For the YouTube features with the account connected, HDX Recorder uses the YouTube API Services. By using these features you agree to the ' + _a(TERMINI_YOUTUBE, 'YouTube Terms of Service') + '. The data handled by Google is covered by the ' + _a(PRIVACY_GOOGLE, 'Google Privacy Policy') + '.',
                    'When you connect the account, Google asks you for permission to manage your YouTube account. This is the only permission HDX Recorder requests: it does not request access to your email, your files, your contacts or any other Google service.',
                ]),
                ('What Google user data HDX Recorder accesses', [
                    'HDX Recorder only reads and changes the data of your YouTube channel that the features you use need:',
                    [
                        'your channel name and ID;',
                        'the channel description, keywords, banner image and video watermark;',
                        'the list of videos you uploaded, with title, description, visibility, date, duration, view count, processing status and any problems reported by YouTube (for example the countries where a video is blocked);',
                        'your playlists and the videos they contain;',
                        'your live broadcasts and scheduled live broadcasts;',
                        'the live chat messages of your broadcasts, with the name and channel ID of who writes them.',
                    ],
                    'HDX Recorder does not read your subscribers, your comments, your revenue data or YouTube Analytics statistics.',
                ]),
                ('How HDX Recorder uses Google user data', [
                    'Your account data is used only to let you use the program\'s features, and only when you use them:',
                    [
                        'showing your channel name in the program;',
                        'creating live broadcasts on your channel, with the title, description and visibility you choose, binding them to the signal you send and ending them when you stop; changing their title and uploading their thumbnail when you ask;',
                        'creating, listing and deleting scheduled live broadcasts, when you ask;',
                        'reading the live chat messages to you and posting in the chat the messages you write;',
                        'moderating the chat when you ask: deleting a message, putting a user in timeout or banning them, removing a ban, adding a moderator;',
                        'showing you the list of your videos and their status; changing their title, description and visibility, scheduling their publication or deleting them, when you ask;',
                        'uploading to your channel the video file you choose, with the title, description and visibility you type, and telling you when YouTube has finished processing it;',
                        'creating, editing and deleting your playlists, and adding, removing or moving videos in them, when you ask;',
                        'changing your channel description, keywords, banner and watermark, when you ask.',
                    ],
                    'Every change to your channel starts only from a command of yours: the program never changes, publishes or deletes anything on its own. Before deleting anything it always asks for confirmation.',
                    'HDX Recorder\'s use and transfer to any other app of information received from Google APIs will adhere to the ' + _a(NORME_DATI_API, 'Google API Services User Data Policy') + ', including the Limited Use requirements.',
                    'Your Google user data is not sold, not used for advertising, not used to train artificial intelligence or machine learning models, and not read by any person: I never receive it.',
                ]),
                ('How your data is protected', [
                    [
                        'Encrypted connection: HDX Recorder talks to Google only over encrypted connections (HTTPS), directly from your computer to Google\'s servers. There are no intermediate servers, mine or anyone else\'s.',
                        'Your password stays with Google: you sign in in your browser, on Google\'s page, with the standard OAuth 2.0 method protected by PKCE. HDX Recorder never sees or stores your Google account password; it only receives a permission that you can revoke at any time.',
                        'Encrypted permission: the only account data saved to disk is the Google permission (the "refresh token"), encrypted with Windows data protection (DPAPI) and tied to your Windows user. If copied to another computer or another user, it cannot be used. It is not included in settings backups.',
                        'Short-lived permission: the permission used for each request to YouTube lasts about one hour and is kept only in the program\'s memory, never on disk.',
                        'Only what is needed: HDX Recorder requests a single permission, the one to manage your YouTube account, and keeps only the data listed in the section below.',
                        'No copies elsewhere: since there is no server, HDX Recorder does not send your data anywhere else; it stays between your computer and Google.',
                    ],
                ]),
                ('What stays on your computer, and for how long', [
                    [
                        'The Google permission (the "refresh token"): encrypted, until you disconnect the account. At every start the program checks that it is still valid; if you removed it from Google, the program deletes it.',
                        'The channel name: next to the permission, updated at every start of the program.',
                        'The title, description, visibility and thumbnail of the last live broadcast: the ones you type, which the program suggests the next time.',
                        'The list of videos and playlists, the channel data, chat messages and links: only in the program\'s memory, while you are using them. They are not saved to disk and disappear when you close the program.',
                        'The videos you upload: the program reads the file from your computer and sends it to YouTube, without making copies.',
                    ],
                ]),
                ('Who it is shared with', [
                    'No one. Your YouTube account data only travels between your computer and Google, and only for the features you use. I do not receive it, sell it or give it to anyone.',
                ]),
                ('How to remove the permission and delete the data', [
                    [
                        'In the program: YouTube menu, YouTube account, then Disconnect the YouTube account (also found in Tools, Settings, Live broadcast category, YouTube, Edit). HDX Recorder asks Google to revoke the permission and immediately deletes the permission and the channel name from your computer.',
                        'From your Google account, on the ' + _a(PERMESSI_GOOGLE, 'page of apps with access to your account') + '. The next time it opens, HDX Recorder notices and deletes the data from your computer.',
                        'Deleting the HDX Recorder folder deletes everything the program has saved.',
                    ],
                    'Removing the permission does not delete anything on YouTube: videos, playlists, live broadcasts and chat messages stay on your channel, and you manage them from YouTube Studio.',
                ]),
                ('Questions', [
                    'For any question or request about privacy you can write to me at <a href="mailto:dessolisandrea@gmail.com">dessolisandrea@gmail.com</a>.',
                    'If this page changes, the date of the last update above says so. If the way HDX Recorder uses your Google account data changes, I also write it in the release notes.',
                ]),
            ],
        },
    },
}
