"""Le pagine sulla privacy dei programmi (privacy-<id>.html), in italiano e
in inglese. Per HDX Recorder la chiedono anche Google e YouTube (la verifica
dell'app per l'account YouTube): deve dire che cosa fa il programma con i
dati dell'account, dove restano e come si toglie il permesso.

Ogni pagina: titolo, data dell'ultimo aggiornamento, una frase d'apertura e
le sezioni (titolo, elementi). Un elemento e' un paragrafo (testo) o un
elenco (lista di testi). I testi possono contenere collegamenti HTML.
"""

TERMINI_YOUTUBE = 'https://www.youtube.com/t/terms'
PRIVACY_GOOGLE = 'https://policies.google.com/privacy'
PERMESSI_GOOGLE = 'https://security.google.com/settings/security/permissions'


def _a(indirizzo, testo=None):
    return f'<a href="{indirizzo}">{testo or indirizzo}</a>'


PRIVACY = {
    'hdx-recorder': {
        'aggiornata': '2026-10-30',
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
                        'l\'intelligenza artificiale funziona solo con una tua chiave di Google Gemini o di OpenAI: l\'audio, il testo o le immagini che scegli di far analizzare vanno a quel servizio, secondo le sue regole;',
                        'le dirette su YouTube usano i servizi API di YouTube, come spiegato qui sotto.',
                    ],
                ]),
                ('YouTube e i servizi API di YouTube', [
                    'Per le dirette su YouTube con l\'account collegato, HDX Recorder usa i servizi API di YouTube. Usando queste funzioni accetti i ' + _a(TERMINI_YOUTUBE, 'Termini di servizio di YouTube') + '. Per i dati che tratta Google valgono le ' + _a(PRIVACY_GOOGLE, 'Norme sulla privacy di Google') + '.',
                    'Quando colleghi l\'account, Google ti chiede il permesso di gestire il tuo account YouTube. HDX Recorder lo usa solo per le funzioni delle dirette, e solo quando le usi tu:',
                    [
                        'legge il nome del tuo canale, per mostrarlo nel programma;',
                        'crea sul tuo canale le dirette, con il titolo, la descrizione e la visibilità che scegli, le collega al segnale che mandi e le chiude quando termini;',
                        'cambia il titolo della diretta quando lo chiedi tu;',
                        'carica la miniatura che scegli tu;',
                        'legge i messaggi della chat della diretta, per farteli ascoltare, e manda nella chat i messaggi che scrivi tu;',
                        'crea, elenca ed elimina le dirette programmate, quando lo chiedi tu.',
                    ],
                    'HDX Recorder non legge i tuoi video, i tuoi iscritti, le statistiche o altri dati del tuo account.',
                ]),
                ('Che cosa resta sul tuo computer, e per quanto', [
                    [
                        'Il permesso di Google (il "token di rinnovo"): cifrato, finché non scolleghi l\'account. A ogni avvio il programma controlla che valga ancora; se l\'hai tolto da Google, lo cancella.',
                        'Il nome del canale: accanto al permesso, aggiornato a ogni avvio del programma.',
                        'Il titolo, la descrizione, la visibilità e la miniatura dell\'ultima diretta: sono quelli che scrivi tu, e il programma li propone la volta dopo.',
                        'I messaggi della chat e il link della diretta: solo nella memoria del programma, finché è aperto e al massimo fino alla diretta seguente. Non vengono salvati su disco.',
                    ],
                ]),
                ('Con chi sono condivisi', [
                    'Con nessuno. I dati del tuo account YouTube passano solo tra il tuo computer e Google. Io non li ricevo, non li vendo e non li uso per pubblicità o per addestrare intelligenze artificiali.',
                ]),
                ('Come togliere il permesso e cancellare i dati', [
                    [
                        'Nel programma: Strumenti, Impostazioni, categoria Diretta, YouTube, Modifica, poi Scollega l\'account YouTube. HDX Recorder chiede a Google di annullare il permesso e cancella subito il permesso e il nome del canale dal tuo computer.',
                        'Dal tuo account Google, nella ' + _a(PERMESSI_GOOGLE, 'pagina delle app con accesso al tuo account') + '. Alla prossima apertura HDX Recorder se ne accorge e cancella i dati dal tuo computer.',
                        'Eliminando la cartella di HDX Recorder si cancella tutto quello che il programma ha salvato.',
                    ],
                    'Togliere il permesso non cancella niente su YouTube: le dirette e i messaggi della chat restano sul tuo canale, e li gestisci da YouTube Studio.',
                ]),
                ('Domande', [
                    'Per qualunque domanda o richiesta sulla privacy puoi scrivermi a <a href="mailto:dessolisandrea@gmail.com">dessolisandrea@gmail.com</a>.',
                    'Se questa pagina cambia, la data dell\'ultimo aggiornamento qui sopra lo dice.',
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
                        'artificial intelligence works only with your own Google Gemini or OpenAI key: the audio, text or images you choose to have analysed go to that service, under its own rules;',
                        'YouTube live broadcasts use the YouTube API Services, as explained below.',
                    ],
                ]),
                ('YouTube and the YouTube API Services', [
                    'For YouTube live broadcasts with the account connected, HDX Recorder uses the YouTube API Services. By using these features you agree to the ' + _a(TERMINI_YOUTUBE, 'YouTube Terms of Service') + '. The data handled by Google is covered by the ' + _a(PRIVACY_GOOGLE, 'Google Privacy Policy') + '.',
                    'When you connect the account, Google asks you for permission to manage your YouTube account. HDX Recorder uses it only for the live broadcast features, and only when you use them:',
                    [
                        'it reads your channel name, to show it in the program;',
                        'it creates live broadcasts on your channel, with the title, description and visibility you choose, binds them to the signal you send and ends them when you stop;',
                        'it changes the title of the live broadcast when you ask;',
                        'it uploads the thumbnail you choose;',
                        'it reads the live chat messages, so you can hear them, and posts in the chat the messages you write;',
                        'it creates, lists and deletes scheduled live broadcasts, when you ask.',
                    ],
                    'HDX Recorder does not read your videos, your subscribers, your statistics or any other data of your account.',
                ]),
                ('What stays on your computer, and for how long', [
                    [
                        'The Google permission (the "refresh token"): encrypted, until you disconnect the account. At every start the program checks that it is still valid; if you removed it from Google, the program deletes it.',
                        'The channel name: next to the permission, updated at every start of the program.',
                        'The title, description, visibility and thumbnail of the last live broadcast: the ones you type, which the program suggests the next time.',
                        'Chat messages and the live broadcast link: only in the program\'s memory, while it is open and at most until the next live broadcast. They are not saved to disk.',
                    ],
                ]),
                ('Who it is shared with', [
                    'No one. Your YouTube account data only travels between your computer and Google. I do not receive it, sell it or use it for advertising or to train artificial intelligence.',
                ]),
                ('How to remove the permission and delete the data', [
                    [
                        'In the program: Tools, Settings, Live broadcast category, YouTube, Edit, then Disconnect the YouTube account. HDX Recorder asks Google to revoke the permission and immediately deletes the permission and the channel name from your computer.',
                        'From your Google account, on the ' + _a(PERMESSI_GOOGLE, 'page of apps with access to your account') + '. The next time it opens, HDX Recorder notices and deletes the data from your computer.',
                        'Deleting the HDX Recorder folder deletes everything the program has saved.',
                    ],
                    'Removing the permission does not delete anything on YouTube: live broadcasts and chat messages stay on your channel, and you manage them from YouTube Studio.',
                ]),
                ('Questions', [
                    'For any question or request about privacy you can write to me at <a href="mailto:dessolisandrea@gmail.com">dessolisandrea@gmail.com</a>.',
                    'If this page changes, the date of the last update above says so.',
                ]),
            ],
        },
    },
}
