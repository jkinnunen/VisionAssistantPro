# Documentazione di Vision Assistant Pro

<!-- DOWNLOAD_COUNT_START --> Total Downloads: 75,451 <!-- DOWNLOAD_COUNT_END -->

Vision Assistant Pro è un assistente IA multimodale avanzato per NVDA. Utilizza motori di intelligenza artificiale di alto livello per fornire lettura intelligente dello schermo, traduzione, dettatura vocale e analisi dei documenti.

_Questo componente aggiuntivo è stato rilasciato alla comunità in occasione della Giornata internazionale delle persone con disabilità._

## 1. Configurazione e impostazioni

Vai al **Menu NVDA > Preferenze > Impostazioni > Vision Assistant Pro**. La finestra di dialogo delle impostazioni è organizzata in 9 schede accessibili: **Connessione**, **Assistente in tempo reale**, **Comportamento IA**, **Lingue di traduzione**, **Lettore documenti**, **Video**, **CAPTCHA**, **Prompt** e **Avanzate**.

### 1.1 Impostazioni di connessione

- **Provider:** selezionare il servizio IA preferito. I provider supportati includono **Google Gemini**, **OpenAI**, **Mistral**, **Groq** e **Personalizzato** (server compatibili OpenAI come Ollama o LM Studio).
- **Chiave API:** obbligatoria. È possibile inserire più chiavi (separate da virgole o nuove righe) per consentire la rotazione automatica.
- **Recupera modelli:** dopo aver inserito la chiave API, premere questo pulsante per scaricare dal provider l’elenco aggiornato dei modelli disponibili.
- **Modello IA:** selezionare il modello principale utilizzato per la chat generale e l’analisi.
- **Routing avanzato dei modelli (specifico per attività):** Seleziona opzionalmente i modelli dedicati dai menu a discesa per le attività di OCR, STT, TTS, Operatore IA, Video e Assistente in tempo reale. Per Gemini, i modelli sono categorizzati dinamicamente per capacità senza risultare caotici.
- **Impostazioni fornitore personalizzato:** Configura endpoint locali o personalizzati. Include **Configura IA locale** (configurazione con un clic per Ollama, LM Studio, Jan.ai o KoboldCPP) e **Configurazione avanzata degli endpoint**.
- **Configurazione proxy:** Supporto completo per il tunneling e il reindirizzamento degli endpoint in tutto il componente aggiuntivo (inclusi Assistente in tempo reale, Osservatore ambientale e TTS). Inserisci l'**URL del proxy** e seleziona la **Modalità proxy**:
  - **Rilevamento automatico:** Rileva automaticamente se l'URL è un proxy diretto o inverso.
  - **Proxy SOCKS5:** Forza il tunneling diretto tramite SOCKS5 con autenticazione nome utente/password RFC 1929 e risoluzione dei nomi di dominio.
  - **Proxy HTTP:** Forza il tunneling diretto tramite un proxy HTTP con autenticazione Basic.
  - **Proxy inverso:** Sostituzione diretta dell'endpoint per gateway IA personalizzati e mirror ospitati autonomamente (le credenziali sono disabilitate in questa modalità).
- **Testa connessione proxy:** Un pulsante non bloccante che verifica la connettività e misura la latenza del server in millisecondi (letta tramite NVDA).
- **Opzioni di connessione e output:** Configura i controlli degli aggiornamenti all'avvio, Pulisci Markdown nella chat, Copia le risposte dell'IA negli appunti e Output diretto (nessuna finestra di chat).
- **Salva chat nella cronologia:** Mantieni le tue conversazioni di chat nell'elenco della Cronologia.

### 1.2 Scheda Assistente in tempo reale

- **Assistente in tempo reale: Output diretto (nessuna finestra):** Avvia l'assistente in tempo reale senza la sua finestra di conversazione; aprilo in seguito con il tasto Richiama ultimo risultato (`Spazio`).
- **Premi per parlare (Push to Talk):** Attiva/disattiva la modalità premi per parlare. Quando è abilitata, il microfono invia l'audio solo mentre tieni premuto il tasto assegnato.
- **Tasto Premi per parlare:** Premi i tasti per registrare la scorciatoia (ad esempio `F12` o `Ctrl+F12`) — puoi anche assegnare un tasto modificatore singolo come `Ctrl sinistro`. Tieni premuto il tasto per parlare e rilascialo per finire; un breve segnale acustico conferma ogni pressione e rilascio.

Nota: Questa scheda viene visualizzata solo quando **Google Gemini** (o un fornitore personalizzato compatibile con Gemini) è il tuo fornitore attivo.

### 1.3 Scheda Comportamento IA

- **Creatività (temperatura):** controlla il livello di casualità dell’IA. Valori più bassi sono preferibili per traduzioni e OCR accurati.

### 1.4 Scheda Lingue di traduzione

- **Lingua di origine:** Seleziona la lingua di input predefinita.
- **Lingua di arrivo:** Seleziona la lingua di traduzione di arrivo principale.
- **Lingua di risposta IA:** Seleziona la lingua per le risposte generali dell'IA.
- **Scambio intelligente:** Scambia automaticamente la lingua di origine e di arrivo in base all'input rilevato.

### 1.5 Scheda Lettore documenti

- **Motore OCR:** scegliere tra **Chrome (veloce)** per risultati rapidi oppure **IA (avanzato)** per una migliore conservazione del layout.
- **Dimensione batch OCR:** Specifica le pagine per richiesta (imposta su 0 per l'elaborazione a richiesta singola).
- **Descrivi immagini inline:** Attiva/disattiva le descrizioni delle immagini inline durante l'estrazione del testo del documento.
- **Esporta numeri di pagina:** Attiva/disattiva numeri di pagina e separatori negli output di documenti multipagina.
- **Text-to-Speech (TTS):** scegliere un modello per la generazione dell’audio.
- **Salva documenti nella cronologia:** Mantieni i documenti aperti nell'elenco della Cronologia; il testo OCR memorizzato nella cache e i dati di ripresa vengono comunque salvati.

### 1.6 Scheda Video

- **Dimensione blocchi video:** Durata del segmento in minuti per la generazione della descrizione audio (imposta su 0 per elaborare l'intero file).
- **Aggiungi elenco personaggi:** Opzione per aggiungere il dizionario dei personaggi come prima voce dei sottotitoli.
- **Aggiungi disclaimer IA:** Opzione per inserire un disclaimer dell'IA all'inizio dei sottotitoli video in formato SRT.
- **Dizionario personaggi e gestione serie:** Aggiungi, modifica, importa o gestisci nomi di personaggi, descrizioni fisiche e ruoli per serie — l'IA abbina automaticamente i personaggi scoperti al tuo dizionario e ne unisce di nuovi man mano che analizzi più episodi. Le tue note manuali vengono sempre preservate con priorità rispetto agli aggiornamenti dell'IA, mentre le descrizioni fisiche rimangono aggiornate tra gli episodi.

### 1.2 Instradamento avanzato dei modelli

- **Abilita risolutore CAPTCHA visivo:** Attiva/disattiva la risoluzione automatica delle sfide visive (hCaptcha, reCAPTCHA).
- **Metodo CAPTCHA di testo:** Scegli tra l'acquisizione dell'**Oggetto navigatore** o dello **Schermo intero**.

### 1.8 Scheda Prompt

- **Gestisci prompt:** Apre una finestra di dialogo dedicata per personalizzare i prompt di sistema predefiniti o per creare, modificare, riordinare e visualizzare in anteprima prompt personalizzati definiti dall'utente con variabili dinamiche (ad es., `[selection]`, `[screen_fg_obj]`, `[currentURL]`, `[text]`).
- **Scorciatoie prompt personalizzati:** Assegna un tasto di scelta rapida dedicato a qualsiasi prompt personalizzato direttamente all'interno del gestore dei prompt. Premi i tasti per registrarli: i tasti singoli vengono eseguiti all'interno del livello di comando (e globalmente come `NVDA + Shift + tasto`), mentre combinazioni come `Control + Shift + 1` vengono eseguite globalmente per conto proprio.
- **Comportamento dei feedback per prompt:** Scegli come ciascun prompt emette il proprio risultato individualmente (impostazione globale, Copia negli appunti, Output diretto / Messaggio NVDA, Copia negli appunti + Output diretto o Finestra di chat).

### 1.9 Scheda Avanzate e registrazione globale

Vai alla scheda **Avanzate** per configurare la registrazione globale del componente aggiuntivo:

- **Abilita file di log dedicato:** Attiva la registrazione di tutti gli eventi operativi, del traffico API e degli errori in tutti i moduli del componente aggiuntivo in un file separato (`vision_assistant.log`).
- **Livello di log:** Seleziona la verbosità tra **Debug (Tutti i dettagli)**, **Info (Informazioni generali)**, **Avviso (Solo avvisi)** e **Errore (Solo errori)**.
- **Conserva i log per:** Imposta periodi di conservazione automatici per ripulire automaticamente le voci di log meno recenti (da 1 ora a 90 giorni).
- **Controlli di gestione dei log:** Usa **Apri file di log**, **Apri cartella dei log** o **Pulisci file di log** per ispezionare o cancellare i dati di log direttamente senza riavviare NVDA o interferire con i log standard di NVDA.
- **Directory dati unificata:** Tutti i file di dati del componente aggiuntivo (cronologia, serie, etichette, avanzamento OCR, cache e log) vengono archiviati in un'unica cartella `VisionAssistant` all'interno della directory di configurazione di NVDA, mantenendo tutto organizzato e rendendo i backup manuali semplicissimi.

### 1.10 Backup e ripristino delle impostazioni

La scheda **Avanzate** include anche una sezione **Backup e ripristino**:

- **Backup:** Salva la tua configurazione in un unico file JSON. Quando fai clic su di esso, scegli cosa includere: **Tutto** (impostazioni, etichette personalizzate, avanzamento OCR e cronologia) o **Solo impostazioni**.
- **Ripristina:** Carica un backup salvato in precedenza per ripristinare la configurazione e i dati in qualsiasi momento, su qualsiasi macchina o dopo aver reinstallato NVDA. Ti verrà chiesto di confermare prima, poiché il ripristino sostituisce tutte le tue impostazioni e i tuoi dati attuali.

## 2. Gestore delle chiavi API Gemini

Creare una chiave API di Gemini su **aistudio.google.com** era un tempo la fase più complessa dell'add-on. Con uno screen reader le pagine risultavano confuse e alcune persone non riuscivano affatto a creare una chiave. Il **Gestore della chiave API di Gemini** risolve questo problema. Premi **G** nel Livello di Comando, oppure apri il **Menu NVDA > Preferenze > Impostazioni > Vision Assistant > Connessione** e premi **Ottieni una chiave API di Gemini...**.

- **Accesso:** Quando apri il gestore, il tuo browser predefinito si apre direttamente sulla pagina di accesso sicuro di Google. Accedi con il tuo account Google — non sono richiesti strumenti esterni, SDK o configurazioni da riga di comando. L'account con cui hai effettuato l'accesso viene sempre mostrato sul pulsante **Disconnettiti**.
- **Creazione di una chiave:** Dopo aver effettuato l'accesso, puoi creare immediatamente una chiave con **Nuovo progetto e chiave** senza alcuna configurazione preliminare. Se possiedi già dei progetti esistenti, questi compaiono in un semplice elenco da cui puoi selezionarne uno e premere **Crea chiave per il progetto selezionato**.
- **Cosa succede dopo:** La nuova chiave viene copiata immediatamente negli appunti, salvata all'interno dell'add-on per un uso successivo e ti viene chiesto una sola volta se desideri aggiungerla all'elenco delle chiavi dell'add-on. Questo è tutto ciò di cui hai bisogno — niente pagine web da cercare faticosamente.
- **Gestione delle chiavi:** **Copia chiave per il progetto selezionato** copia la chiave del progetto evidenziato, **Copia l'ultima chiave creata** copia la chiave generata poco fa, e **Esporta le chiavi salvate in CSV...** salva tutto ciò che hai creato in un file.
- **Eliminazione di una chiave:** **Elimina una chiave...** mostra le chiavi presenti sul progetto selezionato, ti chiede quale rimuovere e chiede conferma prima dell'eliminazione. L'eliminazione di una chiave la rimuove anche dall'elenco delle chiavi dell'add-on, evitando così di mantenere chiavi non funzionanti nella rotazione. È possibile eliminare anche le chiavi create al di fuori dell'add-on, purché il tuo account disponga dei permessi necessari su quel progetto.
- **Disconnessione:** **Disconnettiti** rimuove dal computer le informazioni di accesso memorizzate, consentendoti di passare a un altro account ogni volta che lo desideri.

## 3. Livello comandi e scorciatoie da tastiera

Per evitare conflitti da tastiera, questo componente aggiuntivo utilizza un **livello comandi**.

1. Premere **NVDA + Shift + V** (tasto principale) per attivare il livello (verrà emesso un segnale acustico).
2. Rilasciare i tasti, quindi premere uno dei seguenti tasti singoli:

| Tasto                 | Funzione                                                                  | Descrizione                                                                                                                                                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Shift + A**         | **Operatore IA**                                                          | **Autonomous Operation:** Tell the AI to perform a task on your screen. Pressing it again instantly aborts active operations.                                                                                                 |
| **E**                 | **Esploratore interfaccia**                                               | **Clic interattivo:** identifica e fa clic sugli elementi dell’interfaccia in qualsiasi applicazione.                                                                                                                                         |
| **T**                 | Traduttore intelligente                                                   | Traduce il testo sotto il cursore navigatore o la selezione.                                                                                                                                                                                                  |
| **Shift + T**         | Traduttore appunti                                                        | Traduce il contenuto attualmente presente negli appunti.                                                                                                                                                                                                      |
| **R**                 | Rifinitore testo                                                          | Riassume, corregge la grammatica, spiega o esegue **prompt personalizzati**.                                                                                                                                                                                  |
| **V**                 | Visione oggetto                                                           | Descrive l’oggetto navigatore corrente.                                                                                                                                                                                                                       |
| **O**                 | Visione schermo intero                                                    | Analizza il layout e il contenuto dell’intero schermo.                                                                                                                                                                                                        |
| **Shift + V**         | Analisi video online                                                      | Analizza video di **YouTube**, **Instagram**, **TikTok** o **Twitter (X)**.                                                                                                                                                                |
| **Control + V**       | Local Video Recording                                                     | Records a silent video of your screen and analyzes the actions and layout.                                                                                                                                                                                    |
| **D**                 | Lettore documenti                                                         | Lettore avanzato per PDF e immagini con selezione dell’intervallo di pagine.                                                                                                                                                                                  |
| **F**                 | **Azione file intelligente**                                              | Riconoscimento contestuale di immagini, PDF o file TIFF selezionati.                                                                                                                                                                                          |
| **A**                 | Media Transcription & Dubbing                         | Transcribe or Dub audio/video files (MP3, WAV, MP4, etc.) into your target language.                                                                                                                                       |
| **C**                 | Risolutore CAPTCHA                                                        | Cattura e risolve CAPTCHA (supporta portali governativi).                                                                                                                                                                                  |
| **Shift + C**         | Direct Chat                                                               | Opens a direct text-based chat interface with the AI.                                                                                                                                                                                                         |
| **S**                 | Dettatura intelligente                                                    | Converte il parlato in testo. Premere per avviare la registrazione, di nuovo per interrompere e scrivere.                                                                                                                                     |
| **Control+T**         | Trascrizione audio                                                        | Transcribes, translates, and types the result based on your language settings.                                                                                                                                                                                |
| **Control+L**         | _Disponibile solo quando è selezionato “Personalizzato”._ | **Real-time Copilot (Gemini only):** Starts or ends a live voice and screen conversation with the AI assistant.                                                                                                            |
| **Control+A**         | **Operatore in tempo reale**                                              | **Controllo autonomo del computer (solo Gemini):** Avvia o termina una sessione dell'operatore in tempo reale per delegare schermo e azioni all'IA.                                                                        |
| **G**                 | **Gestore delle chiavi API Gemini**                                       | **Crea la tua chiave API senza il web (solo Gemini):** Apre il gestore che configura le impostazioni necessarie sul computer, apre il browser per accedere e crea, copia o elimina una chiave per il progetto selezionato. |
| **I**                 | Segnalazione dello stato                                                  | Annuncia l'avanzamento corrente (ad es. "Scansione in corso...", "Inattivo").                                                                                              |
| **L**                 | **Etichetta oggetto**                                                     | **Etichettatura semantica con IA:** Assegna un'etichetta permanente all'oggetto del navigatore o all'icona correntemente focalizzata.                                                                                                         |
| **Shift + L**         | **Gestisci/Scansiona etichette**                                          | Apre il Gestore etichette (se presenti) o analizza l'applicazione per individuare elementi non etichettati.                                                                                                                                |
| **U**                 | Controllo aggiornamenti                                                   | Controlla manualmente su GitHub la disponibilità della versione più recente del componente aggiuntivo.                                                                                                                                                        |
| **Spazio**            | Richiama l'ultimo risultato                                               | Mostra l'ultima risposta dell'IA in una finestra di chat per la revisione o ulteriori domande.                                                                                                                                                                |
| **H**                 | Guida ai comandi                                                          | Mostra un elenco di tutti i tasti di scelta rapida disponibili.                                                                                                                                                                                               |
| **Control + H**       | **Cronologia**                                                            | Apre la finestra di dialogo della cronologia con l'elenco delle chat e dei documenti passati, con filtri per tipo e opzioni di eliminazione.                                                                                                                  |
| **Alt + S**           | Impostazioni                                                              | Apre la finestra di dialogo delle impostazioni di Vision Assistant Pro.                                                                                                                                                                                       |
| **Alt + Q**           | Rapporto sulle chiavi con quota esaurita                                  | Segnala il numero di chiavi API Gemini che hanno superato la quota giornaliera, quali modelli sono interessati e l'orario di ripristino.                                                                                                                      |
| **Alt + M**           | Verifica dell'instradamento                                               | Segnala i modelli di IA attualmente selezionati nell'instradamento avanzato per attività specializzate (saltando quelli predefiniti).                                                                                                      |
| **Su / Giù**          | Navigazione impostazioni rapide                                           | Consente di navigare tra le categorie di impostazioni rapide (Provider, Modello, Uscita)... in the layer.                                                                                  |
| **Sinistra / Destra** | Change Quick Setting                                                      | Changes the value of the currently selected quick setting.                                                                                                                                                                                                    |

## 4. Chat e cronologia

Le finestre di chat e la finestra di dialogo della cronologia funzionano in tutte le funzionalità, consentendoti di rivedere le conversazioni e riprendere esattamente da dove avevi interrotto.

### 4.1 Scorciatoie della finestra di chat

Quando una finestra di chat è aperta (Chat diretta, chat con i documenti, perfezionamento e simili), puoi esaminare la conversazione con:

- **Speech-to-Text (STT):** scegliere un modello specifico per la dettatura.
- **URL elenco modelli:** endpoint utilizzato per recuperare i modelli disponibili.
- **Alt + C:** Copia il messaggio corrente.

### 4.2 Cronologia (Control + H)

Premi **Control + H** nel livello dei comandi per aprire la finestra di dialogo **Cronologia** con le tue chat e i tuoi documenti passati, filtrabili per tipo (Tutte / Chat / Documenti). Apri una chat per continuare la conversazione — inclusi i file allegati, che vengono riallegati automaticamente — oppure apri un documento e continua la lettura. Premi **Canc** su qualsiasi elemento per rimuoverlo, oppure **Cancella tutto** per svuotare l'elenco. Per i documenti, Canc chiede se desideri rimuovere solo la voce della cronologia o anche cancellare il testo OCR memorizzato nella cache di quel documento, in modo che la successiva apertura lo riesamini da zero — con un'opzione **Non chiedere più** per ricordare la tua scelta.

Puoi anche scegliere cosa deve ricordare l'elenco. **Salva le chat nella cronologia** (scheda Connessione) e **Salva i documenti nella cronologia** (scheda Lettore di documenti) sono entrambe abilitate per impostazione predefinita ed entrambe possono essere attivate o disattivate nelle Impostazioni rapide. L'opzione relativa ai documenti influisce solo sulla voce della cronologia; il testo OCR memorizzato nella cache e i dati di ripresa vengono sempre conservati.

## 5. Operatore IA - Controllo autonomo del computer

L'**Operatore AI** trasforma Vision Assistant Pro da un lettore passivo in un assistente attivo in grado di interagire con il computer per vostro conto. Potete chiedergli di descrivere lo schermo, rispondere a domande su ciò che vede o persino prendere il controllo: fare clic sui pulsanti, trascinare elementi, digitare testo e navigare tra le applicazioni utilizzando comandi in linguaggio naturale.

Il vantaggio principale? Funziona perfettamente in software completamente inaccessibili. Se vi trovate bloccati in un'applicazione personalizzata, in un desktop remoto o in un sito Web in cui il vostro screen reader diventa totalmente silenzioso, l'operatore non ha problemi. Poiché "vede" lo schermo visivamente, può trovare, leggere e interagire con elementi che hanno zero etichette di accessibilità.

### 5.1 Come funziona

1. Premete **NVDA + Shift + V**, quindi premete **Shift + A** (o usate la scorciatoia diretta) per aprire la finestra di dialogo dell'Operatore AI.
2. Digitate ciò che desiderate fare in linguaggio semplice (ad es., "Fai clic sul pulsante Salva", "Cosa dice il messaggio di errore?" o "Rinomina il file in final.pdf").
3. L'IA analizzerà lo schermo, identificherà gli elementi pertinenti ed eseguirà l'azione o fornirà la risposta. Se un'attività richiede più passaggi, l'operatore continuerà a lavorare fino al suo completamento.
4. Premete nuovamente **Shift + A** in qualsiasi momento per interrompere immediatamente un'operazione in corso.

### 5.2 Azioni supportate

L'operatore comprende un'ampia gamma di comandi:

- **Descrivi e Rispondi**: "Descrivi il layout dello schermo" o "Cosa dice il messaggio di errore?"
- **Fai clic**: "Fai clic sul pulsante Salva"
- **Clic destro**: "Fai clic con il tasto destro sul file"
- **Doppio clic**: "Fai doppio clic sul documento"
- **Trascina e rilascia**: "Trascina il documento nella cartella Archivio"
- **Digita**: "Digita 'Hello World' nella casella di ricerca"
- **Scorri**: "Scorri verso il basso tre volte"
- **Pressione di tasti**: "Premi Invio", "Premi Tab", "Premi Escape"
- **Attività in più passaggi**: "Apri Esplora file, trova il report e rinominalo in final.pdf"

### 5.3 Note importanti

- **⚠️ API Usage Warning:** Because the AI Operator needs to "see" exactly what's happening to be accurate, it sends a high-resolution screenshot with every step. Please note that frequent use will consume your API quota much faster than standard text-based tasks.
- **Applicazioni con privilegi di amministratore**: Se NVDA non è avviato con privilegi di amministratore, l'operatore potrebbe non essere in grado di interagire con finestre che richiedono autorizzazioni elevate. Si tratta di una limitazione di sicurezza di Windows, non di un bug del componente aggiuntivo.
- **Best practice**: Per risultati ottimali, fornite comandi chiari e specifici. "Fai clic sul pulsante blu Invia in fondo al modulo" funzionerà quasi sempre meglio del semplice "Fai clic sul pulsante".

### 5.4 Operatore in tempo reale (Control+A)

L'Operatore in tempo reale consente all'Assistente in tempo reale di eseguire sul computer ciò che richiedete mentre ci parlate, incluse le applicazioni che il vostro screen reader non è in grado di leggere.
_(Nota: questa funzionalità è esclusiva di Google Gemini e dei provider personalizzati compatibili con Gemini)._

- **Attivazione:** Premete **Control+A** nel Layer di comandi per avviare una sessione dell'operatore in tempo reale; premetelo nuovamente per terminarla.
- **Come funziona:** Chiedete in linguaggio semplice, ad esempio "apri Chrome e cerca un sito web" o "rinomina questo file in final". L'operatore osserva lo schermo, esegue i passaggi uno per uno e continua a elaborare le richieste in più passaggi fino al completamento dell'attività.
- **Annunci:** Ogni passaggio viene pronunciato con la voce dell'Assistente in tempo reale, che vi avviserà quando l'attività sarà completata o spiegherà il motivo per cui non è stato possibile eseguirla.
- **CAPTCHA:** Se compare un CAPTCHA, l'operatore proverà prima a utilizzare il vostro **risolutore CAPTCHA** integrato; se non riesce a risolverlo, vi chiederà di completare autonomamente la sfida accessibile.
- **Interruzione:** Premete **Interrompi azione operatore** nella finestra dell'Assistente in tempo reale per annullare l'attività corrente.
- **Impostazioni:** Le istruzioni specifiche dell'operatore possono essere modificate nel Gestore dei Prompt (sezione **Live**, **Istruzione Operatore in tempo reale**). L'interruttore **Output diretto live (senza finestra)** è disponibile anche nelle Impostazioni rapide.

## 6. Analisi video e audiodescrizione

> **Nota:** Le funzioni di Analisi Video e Audiodescrizione sono alimentate esclusivamente dal provider **Google Gemini**. Assicurati che il provider attivo nelle impostazioni dell'add-on sia impostato su Google Gemini.

Vision Assistant Pro introduce potenti funzionalità di elaborazione video progettate specificamente per gli utenti non vedenti. È in grado di analizzare sia video online che registrazioni dello schermo locali per fornire descrizioni visive estremamente dettagliate e generare script di audiodescrizione professionali (SRT).

### 6.1 Registrazione schermo locale (Control + V)

Se incontri un video silenzioso, un'animazione o un tutorial sullo schermo, puoi catturarlo direttamente:

1. **Modelli personalizzati:** digitare manualmente il nome del modello (ad esempio `llama3:8b`) per ogni attività.
2. L'add-on registrerà silenziosamente lo schermo in background.
3. Premi nuovamente **Control + V** per interrompere la registrazione.
4. L'IA analizzerà quindi il segmento video registrato e fornirà una descrizione estremamente dettagliata della scena, dei personaggi e delle azioni.

### 6.2 Analisi video (Shift + V)

Puoi analizzare sia file video locali che video online. Ti basta selezionare un file video locale in Esplora File di Windows o copiare il link di un video online negli appunti. Puoi anche premere **Shift + V** ovunque (ad esempio all'interno di un media player) per aprire una finestra di dialogo in cui cercare un file video o incollare manualmente un URL.

- _Disponibile per tutti i provider, inclusi Gemini, OpenAI, Groq, Mistral e Personalizzato._
- L'IA rileverà automaticamente il file locale o l'URL, elaborerà il video e fornirà una descrizione visiva completa e un riassunto audio.
- **Caching dei File Video per 48 Ore:** I video caricati su Gemini vengono memorizzati nella cache per 48 ore! Puoi rigenerare gli output SRT o MP3 per lo stesso video senza doverlo ricaricare, anche dopo aver riavviato NVDA. La cache riconosce la chiave e viene invalidata automaticamente quando la tua chiave API cambia.

### 6.3 Generazione audiodescrizione (SRT)

Per un'esperienza più strutturata, l'add-on può generare script di audiodescrizione professionali nel formato standard SubRip (SRT).

- **Tempistiche Intelligenti delle Pause:** L'IA ascolta la traccia audio e ancora specificamente le sue descrizioni visive a pause naturali e spazi vuoti silenziosi, così da ridurre al minimo e in modo intelligente la sovrapposizione dei dialoghi.
- **Tracciamento dei Personaggi:** Il motore esegue una fase preliminare per estrarre personaggi distinti in base a tratti facciali immutabili. Costruisce un dizionario globale per tracciare ed etichettare accuratamente i personaggi nelle diverse scene senza confusione. Traccia inoltre la **prima apparizione** di ciascun personaggio, descrivendone l'aspetto fisico una sola volta (nel momento in cui compare per la prima volta) e utilizzando i nomi stabiliti solo nelle scene successive per mantenere la narrazione fresca e naturale.
- **OCR di Testo Letterale:** Qualsiasi testo che appare sullo schermo (insegne, telefoni, titoli di coda) viene riportato rigorosamente parola per parola.
- **Come Usare:** Per ascoltare i sottotitoli generati, posiziona semplicemente il file `.srt` nella stessa cartella del file video e assegnagli esattamente lo stesso nome. Quindi, configura il tuo lettore multimediale (ad esempio VLC o PotPlayer) per reindirizzare il testo dei sottotitoli direttamente al tuo screen reader o al motore TTS durante la riproduzione.
- **Esperienza di Salvataggio Migliorata:** Quando salvi file SRT o MP3, la finestra di dialogo del file si apre ora per impostazione predefinita nella cartella del video sorgente, sia che tu abbia aperto il video tramite la finestra di dialogo dei file sia tramite Shift+V da Esplora File.

### 6.4 Narrazione audio sincronizzata (esportazione MP3)

Oltre alla semplice creazione di file SRT basati su testo, l'add-on funziona come uno strumento di produzione di audiodescrizioni completo, sintetizzando le descrizioni in parlato e miscelandole con il video. Ora puoi scegliere **Gemini Live TTS** come motore vocale, che utilizza l'API Gemini Live per generare una narrazione vocale estremamente realista e illimitata. Quando generi un MP3 per file video locali, hai a disposizione diverse modalità di missaggio:

- **AD Standard (Mix Vocale):** La narrazione viene sovrapposta direttamente all'audio del video. Ti verrà chiesto se desideri applicare l'**Audio Ducking** (riducendo il volume di sottofondo durante le descrizioni) per garantire che la narrazione sia chiara.
- **AD Estesa (Pausa Audio):** Il motore mette in pausa l'audio originale del video durante le descrizioni, assicurandoti di non perdere neppure una parola del dialogo originale o della narrazione dell'IA. Il rilevamento del silenzio utilizza ora il modello neurale **Silero VAD** (scaricato automaticamente al primo utilizzo, proprio come ffmpeg e eSpeak) per una temporizzazione precisa delle pause, distinguendo le pause naturali dei dialoghi dalla musica e dal rumore di fondo.
- **Video di YouTube:** Per le sorgenti YouTube (che non vengono scaricate localmente), l'esportazione MP3 conterrà rigorosamente la traccia vocale IA sincronizzata senza l'audio video di sottofondo.

## 7. Trascrizione e doppiaggio multimediale (M)

L'Audio Transcriber è stato completamente riprogettato per supportare sia file audio che video (MP3, WAV, MP4, MKV, ecc.). Premi **M** nel Livello di Comando per selezionare un file multimediale e scegliere tra 3 diverse modalità operative:

1. **Trascrivi (Lingua Originale)**: Trascrive accuratamente il parlato nella sua lingua originale.
2. **Trascrivi e Traduci (Lingua di Arrivo)**: Trascrive il parlato e lo traduce nella lingua di arrivo configurata.
3. **Doppia e Traduci (Lingua di Arrivo)** _(Solo Gemini)_: Una nuova e potente funzionalità che trascrive il parlato, lo traduce nella lingua di arrivo e sintetizza un doppiaggio audio vocale utilizzando il motore TTS del componente aggiuntivo.

## 8. Lettore avanzato di documenti e immagini

Il **Document Reader** trasforma i tuoi documenti in testo pulito e leggibile, consentendoti di leggere, tradurre e ascoltare qualsiasi cosa, da un libro scansionato a un mucchio di foto. Gestisce PDF multipagina, immagini complesse, formati HEIC di iPhone e persino file di testo semplice (`.txt`) e HTML (`.html`, `.htm`), che vengono aperti istantaneamente senza elaborazione OCR o IA. Seleziona più file contemporaneamente e questi verranno uniti in un unico documento continuo nell'ordine delle pagine. Sono disponibili tre motori OCR: **Chrome (Fast)**, **AI (Advanced)** per una superiore conservazione del layout e **None (Extract Text Layer)** per i PDF ricercabili, selezionabili in Impostazioni → Document Reader.

### Come funziona

1. Premi **NVDA + Shift + V**, quindi **D** per aprire il Document Reader, oppure evidenzia prima un file in Esplora file e premi **D** / **F** per saltare completamente la finestra di dialogo dei file.
2. Scegli uno o più PDF o immagini. Il componente aggiuntivo li scansiona e annuncia il conteggio totale delle pagine.
3. Nella finestra di dialogo **Opzioni**, scegli l'intervallo di pagine (Da/A). Puoi anche spuntare **Translate Output** e scegliere la lingua di destinazione, attivare o disattivare **Describe images inline during OCR** oppure abilitare **Compress PDF pages before processing** per ridurre la scala e ricomprimere le pagine scansionate di grandi dimensioni prima del caricamento.
4. L'estrazione del testo si avvia in background a blocchi. Puoi chiudere la finestra in qualsiasi momento e continuare più tardi: nulla andrà perduto.
5. Una volta pronte le pagine, leggile nel visualizzatore: spostati tra le pagine, salta a qualsiasi pagina, fai domande all'IA, salva il testo o genera una narrazione audio.

### 8.1 Elaborazione in batch e ripresa

Non è necessario leggere un documento di grandi dimensioni tutto in una volta. Scegli un intervallo di pagine (es. `1-20`) o mantieni le impostazioni predefinite per elaborare tutto, e l'IA estrarrà tutte le pagine in background. Se NVDA si blocca o interrompi la scansione, il componente aggiuntivo ricorda i tuoi progressi e offre la possibilità di **Riprendere** esattamente da dove eri rimasto, anche dopo i riavvii. I documenti completati vengono anche memorizzati nella cache, quindi la loro riapertura (dai Documenti recenti o tramite **D**) carica il testo all'istante senza rieseguire l'OCR, a meno che i file sorgente non siano cambiati.

### 8.2 Azione intelligente sui file

Non è sempre necessario aprire prima il documento. In Esplora file di Windows, evidenzia semplicemente un PDF, un'immagine o un file di testo/HTML e premi **D** (Document Reader), oppure evidenzia un PDF o un'immagine e premi **F** (Smart File Action), all'interno del livello di comandi (Command Layer). Il componente aggiuntivo ignora istantaneamente la finestra di dialogo dei file e avvia l'elaborazione del file evidenziato. La selezione di più file contemporaneamente li elabora insieme come un unico documento.

### 8.3 Controlli e scorciatoie del visualizzatore documenti

Quando la finestra del Document Reader è aperta, puoi utilizzare i seguenti comandi:

#### 1.4 Preferenze generali

- **Ctrl + Pagina su:** passa alla pagina precedente.
- **URL endpoint OCR/STT/TTS:** URL completi per servizi specifici (ad esempio `http://localhost:11434/v1/audio/speech`).
- **Alt + A:** apre una finestra chat per porre domande sul documento.
- **Alt + R:** forza una **nuova scansione con IA** utilizzando il provider attivo.
- **Alt + G:** genera e salva un file audio di alta qualità (WAV/MP3). _Nascosto se il provider non supporta il TTS._
- **Alt + S / Ctrl + S:** salva il testo estratto come file TXT o HTML.

#### Pulsanti e controlli

- **Modello OCR / Visione:** scegliere un modello specializzato per l’analisi delle immagini.
- **Visualizza formattato (View Formatted):** Visualizza l'intero documento combinato come testo formattato.
- **Riprova le pagine nonriuscite (Retry Failed Pages):** Riprova solo i blocchi che non sono riusciti a causa di un errore temporaneo del server (es. traffico elevato). Questo pulsante compare automaticamente quando necessario.
- **Voce TTS:** selezionare lo stile vocale preferito.
- **Ctrl + Pagina giù:** passa alla pagina successiva.

### 8.4 Documenti recenti (D)

**Documenti recenti nel lettore**: Premendo **D** nel livello dei comandi vengono ora mostrati per primi i documenti letti di recente. Scegline uno per continuare dalla pagina in cui ti trovavi — anche quando l'OCR ha già terminato — oppure premi **Apri file...** (`Ctrl + O`) per esplorare come al solito.

## 9. Etichettatura semantica con IA ed esploratore interfaccia utente

Bloccato in un'applicazione piena di "pulsante senza etichetta"? Il motore di Etichettatura AI Semantica risolve questo problema in modo permanente.

### 9.1 Etichettatura permanente degli oggetti (L)

Posiziona il fuoco del tuo screen reader su un'immagine o un anello senza etichetta e premi **L** nel Livello di Comandi. L'AI analizzerà visivamente il pulsante, ne determinerà la funzione e applicherà un'etichetta permanente.
_A differenza dei vecchi strumenti di etichettatura per screen reader, questo componente aggiuntivo utilizza un avanzato sistema ibrido di "Firma Oggetto" (AutomationId/ControlID). Le tue etichette personalizzate resisteranno al ridimensionamento delle finestre, al cambio di monitor e agli aggiornamenti delle applicazioni!_

### 9.2 Scansione completa dell'applicazione (Shift + L)

Premi **Shift + L** per scansionare l'intera finestra attiva in una sola volta. L'AI individuerà tutti gli elementi privi di etichetta e li nominerà in modo intelligente in un unico passaggio. In seguito potrai gestire, rinominare o eliminare in blocco queste etichette dal Gestore Etichette integrato.

### 9.3 Esploratore interfaccia utente (E)

Hai bisogno di interagire con un elemento senza dovervi navigare manualmente? Premi **E** per attivare l'Esploratore Interfaccia Utente. L'AI scansionerà lo schermo e genererà un elenco accessibile di ogni elemento cliccabile (ignorando i disturbi di sistema come le barre delle applicazioni). Scegli un elemento dall'elenco e il componente aggiuntivo cicliccherà sopra all'istante per te.

## 10. Assistente vocale in tempo reale

L'Assistente in Tempo Reale trasforma Vision Assistant Pro in un copilota interattivo in tempo reale.
_(Nota: questa funzione è esclusiva di Google Gemini e dei provider personalizzati compatibili con Gemini)._

- **Attivazione:** Premi **Control + L** nel Livello dei Comandi per aprire la finestra di dialogo dell'Assistente in Tempo Reale.
- **Interazione in Tempo Reale:** Parla in modo naturale tramite il microfono. L'intelligenza artificiale ascolterà contemporaneamente la tua voce e osserverà lo schermo attivo. Puoi fare domande come "Cosa sto guardando?" o "Leggimi il terzo paragrafo."
- **Premi per Parlare (Push to Talk):** Abilita **Premi per Parlare** nella scheda delle impostazioni dell'Assistente in Tempo Reale (o attivalo direttamente all'interno della finestra dell'Assistente), quindi tieni premuto il tasto assegnato per parlare e rilascialo per terminare. Questo mantiene il microfono disattivato finché non premi il tasto, ideale per ambienti rumorosi.
- **Ingresso Webcam:** Spunta **Usa &Webcam** nella finestra dell'Assistente in Tempo Reale per inviare il flusso della fotocamera all'intelligenza artificiale anziché lo schermo; puoi fare domande su oggetti fisici, documenti stampati o ciò che ti circonda. Se ffmpeg non è ancora installato, selezionando la casella verrà scaricato una sola volta previa autorizzazione; l'opzione è disattivata se non viene rilevata alcuna fotocamera o se le impostazioni sulla privacy di Windows bloccano l'accesso alla fotocamera.
- **Personalizzazione:** All'interno della finestra di dialogo, puoi modificare lo Stile Vocale dell'intelligenza artificiale (ad esempio, Professionale, Amichevole, Vivace) e regolare la "Profondità di ragionamento" per controllare quanto a fondo elabora i pensieri prima di rispondere.

## 11. Osservatore ambientale (assistente in background)

L'Osservatore Ambientale trasforma Vision Assistant Pro nei tuoi occhi in background, senza alcuna conversazione: continua ad ascoltare e guardare mentre lavori, segnala cosa cambia e rimane in silenzio quando non succede nulla.
_(Nota: questa funzione è esclusiva di Google Gemini e dei provider personalizzati compatibili con Gemini)._

- **Attivazione:** Premi **Shift+O** nel Layer dei Comandi per aprire la finestra di dialogo dell'Osservatore Ambientale; premilo di nuovo per arrestare l'osservatore.
- **Modalità:** **Solo traduzione audio** traduce ciò che ascolta, **Solo osservatore schermo** segnala le modifiche dello schermo e **Solo osservatore webcam** apre la finestra dell'Assistente in tempo reale con la tua fotocamera e il tasto "Trattieni per parlare" (Push to Talk), in modo da poter fare domande su ciò che la fotocamera inquadra.
- **Fonte audio:** Nella modalità audio, scegli se tradurre il tuo **Microfono** o l'**Audio di sistema (Loopback)**. La piccola libreria di loopback viene scaricata una sola volta al primo utilizzo, previa tua autorizzazione.
- **Contesto:** Per le modalità schermo e webcam, seleziona un'opzione opzionale **Informazioni su ciò che sto facendo** (ad esempio, guardare un film, seguire una riunione o una chiamata, leggere un'etichetta o controllare il proprio aspetto) per focalizzare i resoconti; puoi anche digitare un tuo contesto personalizzato.
- **Segnalazione:** L'add-on confronta ogni nuovo fotogramma con quello precedente e lo invia all'intelligenza artificiale solo quando l'immagine è effettivamente cambiata, in modo che uno schermo statico non consumi mai richieste. L'IA segnala quindi solo ciò che è nuovo e non si ripete mai.
- **Messaggio di benvenuto:** Tranne che nella modalità di traduzione, l'osservatore ti saluta brevemente all'avvio, per farti sapere che è in ascolto.
- **Impostazioni:** In **Impostazioni > Assistente in tempo reale**, imposta la **Modalità osservatore**, l'**Intervallo fotogrammi** (da 1 a 10 secondi) e lo **Stile di segnalazione** (breve o dettagliato). L'istruzione dell'osservatore e ciascun testo di contesto possono essere modificati nel Gestore dei Prompt (sezione **Ambient**).

## 12. Prompt personalizzati e variabili

È possibile gestire i prompt in **Impostazioni > Prompt > Gestisci prompt...**.

- **Filtro:** La scheda **Prompt predefiniti** dispone di un elenco **Filtro** sopra l'elenco dei prompt che mostra **Tutti** i prompt o solo una sezione alla volta (ad esempio **Ambiente**), in modo che gli elenchi lunghi rimangano facili da esplorare.

### Scorciatoie per i prompt personalizzati

Assegna a qualsiasi prompt personalizzato una sua combinazione di tasti direttamente nel Gestore prompt ed eseguilo all'istante con la selezione o il contesto corrente:

- **Tasto singolo** (es. `1`, `p` o `F3`): Funziona all'interno del livello di comandi e anche a livello globale come `NVDA + Shift + tasto`.
- **Combinazione di tasti** (es. `Control + Shift + 1`, `Alt + P` o `Insert + 1`): Funziona autonomamente a livello globale.

### Comportamento di feedback per singolo prompt

Ciascun prompt personalizzato può definire individualmente il comportamento di restituzione dell'output:

- **Impostazione globale:** Segue l'impostazione generale dell'output della connessione (Output diretto o Finestra di chat).
- **Copia negli appunti:** Copia la risposta dell'IA direttamente negli appunti senza aprire una finestra.
- **Output diretto (messaggio di NVDA):** Legge/invia al braille la risposta dell'IA direttamente tramite la sintesi vocale di NVDA.
- **Copia negli appunti e Output diretto:** Copia la risposta negli appunti e la legge direttamente.
- **Finestra di chat:** Apre sempre il risultato in una finestra di conversazione interattiva.

### Variabili supportate

- `[selection]`: testo attualmente selezionato.
- `[clipboard]`: contenuto degli appunti.
- `[screen_obj]`: schermata dell’oggetto navigatore.
- `[clipboard]`: contenuto degli appunti.
- 2.1 Scorciatoie del lettore documenti (all’interno del visualizzatore)
- `[screen_obj]`: schermata dell’oggetto navigatore.
- `[file_audio]`: seleziona un file audio da analizzare (MP3, WAV, OGG).
- `[screen_full]`: schermata completa dello schermo.
- `[file_ocr]`: seleziona un file immagine/PDF per l’estrazione del testo.
- `[file_read]`: seleziona un documento da leggere (TXT, codice, PDF).
- `[file_audio]`: seleziona un file audio da analizzare (MP3, WAV, OGG).
- `[ambient_screen]`: Avvia la sessione in background continua dell'Osservatore dello schermo.
- `[ambient_webcam]`: Avvia la sessione in background continua dell'Osservatore della webcam (verifica la funzione "Premi per parlare" dalle impostazioni).
- `[ambient_audio]`: Avvia la sessione di traduzione in tempo reale dell'Osservatore audio.
- `[loopback]`: Utilizza la riproduzione audio di sistema come sorgente sonora (per `[ambient_audio]`).
- `[mic]`: Utilizza il microfono come sorgente sonora (per `[ambient_audio]` e `[ambient_webcam]`).
- `[brief]`: Imposta lo stile di resoconto dell'osservatore su sintetico (una singola frase).
- `[detailed]`: Imposta lo stile di resoconto dell'osservatore su dettagliato (2-3 frasi).
- `[lang:code]`: Specifica il codice della lingua di destinazione per la traduzione audio (es. `[lang:fa]`, `[lang:en]`).
- `{target_lang}`: Lingua di destinazione corrente.
- `{source_lang}`: Lingua di origine corrente.
- `{response_lang}`: Lingua della risposta dell'IA corrente.
- `{swap_target}`: Lingua di fallback per la traduzione con inversione intelligente.
- `{swap_instruction}`: Blocco di istruzioni per la traduzione con inversione intelligente.

_Nota sui prompt ambientali:_ I prompt contenenti variabili ambientali agiscono come un interruttore a levetta (toggle): premendo la scorciatoia mentre sono attivi, la sessione viene interrotta immediatamente. Le combinazioni incompatibili (come la combinazione di variabili di screenshot statici come `[screen_full]` con le modalità di osservazione ambientale, la combinazione di più modalità ambientali o l'aggiunta di istruzioni del prompt a `[ambient_audio]`) vengono rigorosamente validate e impedite al momento del salvataggio.

## 13. Casi d'uso reali (Quale funzione dovrei usare?)

Vision Assistant Pro è ricco di strumenti avanzati. Ecco alcuni scenari comuni per aiutarti a scegliere quello giusto:

- **Scenario: Vuoi comprendere la disposizione completa di una finestra complicata o di un'applicazione inaccessibile.**
  _Soluzione:_ Premi **O** (Visione a schermo intero). L'IA analizzerà l'intero schermo e descriverà esattamente dove sono posizionati elementi, testi e pulsanti.

- **Scenario: Hai trovato un'immagine su una pagina web o una grafica non etichettata in un documento.**
  _Soluzione:_ Sposta il tuo oggetto navigatore sulla grafica e premi **V** (Visione oggetto). L'IA descriverà specificamente cosa contiene quell'immagine.

- **Scenario: Vuoi guardare un film o un video clip con audiodescrizioni.**
  _Soluzione:_ Premi **Shift + V** sul tuo video e scegli **"Genera audiodescrizione (file SRT)"**. Quando ha finito, fai clic su **"Genera narrazione sincronizzata (MP3)"** e seleziona **"AD estesa"**. Il componente aggiuntivo creerà una traccia audio che metterà in pausa in modo intelligente i dialoghi del film per descrivere le scene visive.

- **Scenario: Ti sei imbattuto in un'app piena di "pulsanti senza etichetta".**
  _Soluzione:_ Premi **L** per etichettare permanentemente lo specifico pulsante usando l'IA. Oppure, premi **Shift + L** per scansionare ed etichettare l'intera finestra in una sola volta. Se vuoi solo fare clic su qualcosa rapidamente, premi **E** (Esplora interfaccia utente) per ottenere un elenco di tutti gli elementi cliccabili.

- **Scenario: Devi superare un CAPTCHA inaccessibile.**
  _Soluzione:_ Premi **C** (Risolutore CAPTCHA). L'IA catturerà automaticamente il CAPTCHA, lo risolverà e inserirà la risposta nel campo corretto.

- **Scenario: Vuoi leggere un lungo documento PDF di 50 pagine.**
  _Soluzione:_ Premi **D** (Lettore di documenti), imposta il tuo provider su Google Gemini e inserisci l'intervallo di pagine `1-50`. Il componente aggiuntivo estrarrà il testo con precisione in background.

- **Scenario: Stai guardando un video tutorial silenzioso o un'animazione sullo schermo.**
  _Soluzione:_ Premi **Control + V** per avviare la registrazione dello schermo. Lascia riprodurre il tutorial, quindi premi di nuovo **Control + V**. L'IA spiegherà esattamente cosa è stato dimostrato.

- **Scenario: Incontri un errore imprevisto, un errore di connessione API o desideri diagnosticare problemi con server locali personalizzati.**
  _Soluzione:_ Vai su **Impostazioni > Avanzate**, spunta **"Abilita file di log dedicato"** e imposta il **Livello di log** su **"Debug"**. Esegui nuovamente l'azione, quindi fai clic su **"Apri file di log"** per ispezionare i dettagli tecnici o allegare `vision_assistant.log` a un ticket di supporto.

***

**Nota:** è necessaria una connessione Internet attiva per tutte le funzioni IA. I documenti multipagina vengono elaborati automaticamente.

## 14. Supporto e comunità

Rimani aggiornato sulle ultime notizie, funzionalità e versioni:

- **Canale Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **Segnalazioni GitHub:** per segnalazioni di bug e richieste di nuove funzionalità.

### Reporting Bugs & Logs

When opening a GitHub issue or asking for support, please include details about your active AI provider, model, and NVDA version. If you are experiencing connection issues or unexpected crashes, enable the dedicated log file in **Settings > Advanced**, recreate the issue, and attach your `vision_assistant.log` file to help us resolve the problem faster.

## 15. Sostenitori del progetto

Un sentito ringraziamento ai membri della comunità che supportano lo sviluppo e la manutenzione continui di questo progetto tramite i loro generosi contributi economici:

- **@Alyabani94**
- **Ali Alamri**
- _Nota:_ se viene selezionato “IA (avanzato)” mentre il provider attivo è OpenAI o Groq, il componente aggiuntivo instraderà automaticamente l’immagine verso il modello di visione del provider attivo.
- **leonardo0216**
- **URL proxy:** configurare questa opzione se i servizi IA sono limitati nella propria area geografica (supporta proxy locali come `127.0.0.1` oppure URL bridge).
- **Arne Siebert**
- **Schalkefan**
- **Rainer Brell**
- **[avalai.org](https://avalai.org)**

_Se desideri sostenere economicamente il progetto e vedere il tuo nome qui, puoi trovare l’opzione **Dona** nel menu Strumenti di NVDA (sottomenu Vision Assistant) oppure durante la procedura di configurazione dopo l’installazione._

---

## Modifiche per 2026.10.15

- **La correzione più richiesta: creare una chiave API di Gemini è finalmente facile**: Ottenere una chiave API su **aistudio.google.com** era solitamente il passaggio più difficile in assoluto. Con uno screen reader le pagine risultavano confuse e alcune persone non riuscivano proprio a creare una chiave. Questo problema è ora risolto direttamente all'interno dell'add-on. Premi **G** nel livello dei comandi (o usa **Ottieni una chiave API di Gemini...** nelle Impostazioni), accedi tramite il tuo browser predefinito senza alcuna configurazione esterna, e la tua chiave verrà creata e configurata con una sola conferma, anche se non hai mai avuto un progetto prima d'ora.
- **Osservatore Ambientale**: L'assistente in background è arrivato. Premi **Shift+O** nel livello dei comandi per avviarlo e premilo di nuovo per fermarlo. Può tradurre ciò che sente (dal tuo microfono o dall'audio di sistema), osservare lo schermo e dirti cosa è cambiato, oppure aprire l'Assistente dal vivo con la tua webcam e la funzione "Premi per parlare" (Push to Talk), così puoi fare domande su qualunque cosa la webcam stia inquadrando. Invia un'immagine solo quando qualcosa è realmente cambiato, quindi uno schermo statico non consuma risorse, e rimane silenzioso quando non accade nulla. Puoi anche avviare e attivare/disattivare l'osservatore direttamente tramite i Prompt personalizzati e tasti di scelta rapida dedicati usando `[ambient_screen]`, `[ambient_webcam]` o `[ambient_audio]` insieme ai modificatori (`[loopback]`, `[mic]`, `[brief]`, `[detailed]`, `[lang:code]`), con convalida automatica contro combinazioni di variabili in conflitto.
- **Operatore dal vivo**: L'Assistente dal vivo può ora eseguire ciò che chiedi sul tuo computer mentre parli con lui. Premi **Control+A** nel livello dei comandi per avviare una sessione di operatore dal vivo, quindi chiedi semplicemente in linguaggio naturale. Gestisce richieste in più passaggi, pronuncia ogni fase con la voce propria dell'Assistente dal vivo, si occupa delle combinazioni di tasti necessarie e decide autonomamente quando l'attività è completata. Anche l'opzione **Output diretto dal vivo (nessuna finestra)** è disponibile nelle Impostazioni rapide.
- **Dizionario dei personaggi e gestione delle serie**: La finestra di dialogo Analisi video include ora un potente sistema di **Dizionario dei personaggi**! Aggiungi, modifica, importa o gestisci i nomi dei personaggi, le descrizioni fisiche e i ruoli per singola serie: l'IA associa automaticamente i personaggi scoperti al tuo dizionario e unisce quelli nuovi man mano che analizzi più episodi. Le tue note manuali sono sempre preservate con priorità rispetto agli aggiornamenti dell'IA, mentre le descrizioni fisiche rimangono aggiornate tra i vari episodi. Il dizionario viene salvato per ogni serie e riutilizzato per ogni video di quella serie. Nell'elenco dei personaggi, premi **F2** per modificare il personaggio selezionato e **Canc** per rimuoverlo.
- **Supporto SOCKS5, HTTP e Reverse Proxy con test di latenza**: Bypassa senza problemi le restrizioni di rete con il supporto proxy completo in tutto l'add-on, inclusi Assistente dal vivo, Osservatore ambientale e generazione TTS! Scegli tra 4 modalità operative nelle impostazioni Generali: **Rilevamento automatico**, **Proxy SOCKS5**, **Proxy HTTP** o **Reverse Proxy**. SOCKS5 supporta l'autenticazione nome utente/password RFC 1929 e il tunneling di dominio; il proxy HTTP supporta l'autenticazione Base. Un nuovo pulsante **Testa connessione proxy** viene eseguito in background e annuncia la latenza di connessione in millisecondi.
- **Caching dei file video per 48 ore**: I video caricati su Gemini vengono ora memorizzati nella cache per 48 ore! Puoi rigenerare gli output SRT o MP3 per lo stesso video senza doverlo ricaricare, anche dopo aver riavviato NVDA. La cache riconosce la chiave e viene invalidata automaticamente quando la tua chiave API cambia.
- **Rilevamento del silenzio basato su IA (Silero VAD)**: Extended AD utilizza ora il modello neurale Silero VAD per un rilevamento preciso del silenzio, distinguendo le pause naturali del dialogo dalla musica e dal rumore di fondo. Il modello viene scaricato automaticamente al primo utilizzo (previa tua autorizzazione), proprio come ffmpeg ed eSpeak.
- **Video da webcam per l'Assistente dal vivo**: La finestra dell'Assistente dal vivo ha ora una casella di controllo **Usa la &webcam** per inviare il flusso della tua webcam all'IA invece dello schermo, perfetto per fare domande su oggetti fisici, documenti o sull'ambiente circostante. Se ffmpeg non è ancora installato, selezionare la casella lo scaricherà (una tantum, previa tua autorizzazione). L'opzione è disattivata se non viene rilevata alcuna fotocamera o se le impostazioni sulla privacy di Windows bloccano l'accesso alla fotocamera, con un pulsante per aprire le impostazioni sulla privacy della fotocamera. Se la fotocamera è abilitata ma non produce fotogrammi, il problema viene registrato nel log di NVDA per la diagnosi anziché passare silenziosamente allo schermo.
- **Selezione del dispositivo di output audio**: Ora puoi selezionare un dispositivo di output audio dedicato per l'Assistente dal vivo e l'Osservatore ambientale. Scegli tra l'output predefinito di NVDA, il Mapper audio di Windows o qualsiasi scheda audio fisica collegata (come cuffie USB o altoparlanti esterni) nella scheda Impostazioni dal vivo, direttamente all'interno della finestra di dialogo dell'Assistente dal vivo, o al volo tramite le Impostazioni rapide (NVDA+Shift+V poi Su/Giù/Sinistra/Destra).
- **Gestore dei prompt**: La scheda Prompt predefiniti include ora un elenco di **Filtro**, così puoi mostrare tutti i prompt o solo una sezione specifica (ad esempio **Ambient**). Puoi anche modificare i testi di contesto dell'osservatore e la nuova **Istruzione operatore dal vivo** in questa sezione.
- **Filtraggio intelligente dei modelli nel routing avanzato**: I menu a discesa del Routing avanzato dei modelli ora categorizzano dinamicamente i modelli Gemini in base alle funzionalità senza creare disordine. L'Assistente dal vivo mostra solo modelli bidirezionali dal vivo e nativi audio autentici, il TTS mostra solo modelli dedicati alla sintesi vocale, l'STT dà priorità ai modelli di trascrizione e multimodali, e Analisi video, OCR e Operatore IA filtrano accuratamente i modelli di utilità a scopo singolo (come la generazione di immagini, la generazione di video e i modelli di embedding). I modelli futuri vengono rilevati automaticamente in base alle funzionalità senza richiedere aggiornamenti di versione.
- **Tracciamento della prima apparizione dei personaggi**: L'IA ora descrive l'aspetto fisico di ciascun personaggio una sola volta, alla loro prima apparizione nel video. Le apparizioni successive utilizzano solo i nomi, eliminando descrizioni ripetitive tra i segmenti e mantenendo la narrazione fresca e naturale.
- **Directory dati unificata**: Tutti i file di dati dell'add-on (cronologia, serie, etichette, stato dell'OCR, cache e log) sono stati migrati in un'unica cartella `VisionAssistant` all'interno della tua directory di configurazione di NVDA, mantenendo tutto organizzato e rendendo i backup manuali estremamente semplici.
- **Esperienza di salvataggio video migliorata**: Durante il salvataggio di file SRT o MP3, la finestra di dialogo dei file ora si apre per impostazione predefinita nella cartella del video sorgente, sia che tu apra il video tramite la finestra di dialogo dei file sia tramite Shift+V da Esplora file.
- **Eliminazione di documenti con o senza il relativo testo memorizzato nella cache**: La finestra di dialogo della Cronologia (`Control + H`) offre ora due modi per eliminare un documento: premi Canc e scegli **Elimina solo dalla cronologia** o **Elimina dalla cronologia e dal testo memorizzato nella cache**. La seconda opzione cancella il testo OCR memorizzato nella cache per quel documento, in modo che la prossima apertura lo riesamini da zero, ideale dopo una scansione non riuscita. Una casella di controllo **Non chiedere più** memorizza la tua scelta per le eliminazioni future. I dati di ripresa delle operazioni interrotte non vengono mai toccati.
- **Cache OCR con unione e consapevolezza del motore nel lettore di documenti**: Il testo OCR memorizzato nella cache viene ora salvato per singolo motore OCR, quindi il cambio di motore OCR riesamina sempre con il nuovo motore anziché riprodurre il vecchio risultato. La riapertura di un documento mostra nuovamente la finestra di dialogo dell'intervallo di pagine (precompilata con la tua ultima scelta), riutilizzando istantaneamente le pagine già scansionate e scansionando solo quelle mancanti: la cache unisce le pagine una per una anziché essere sostituita, così ogni intervallo letto viene conservato per dopo.
- **Compressione PDF nel lettore di documenti**: Aggiunta un'impostazione opzionale **Comprimi le pagine PDF prima dell'elaborazione** nella finestra di dialogo dell'intervallo di pagine del lettore di documenti. Quando si caricano documenti PDF scansionati di grandi dimensioni o ad alta risoluzione su Gemini o Mistral, le pagine vengono automaticamente ridimensionate e ricompresse per ridurre drasticamente le dimensioni del payload di caricamento, velocizzare l'elaborazione e prevenire i timeout di rete. L'opzione è disattivata per impostazione predefinita e nascosta automaticamente quando si utilizza il motore Chrome o provider di immagini basati su base64.
- **Personalizzazione del comportamento di feedback per singolo prompt**: Personalizza il modo in cui ogni prompt personalizzato restituisce il suo output individualmente! Nell'editor dei prompt personalizzati, scegli tra **Impostazione globale**, **Copia negli appunti**, **Output diretto (messaggio di NVDA)**, **Copia negli appunti e output diretto** o **Finestra chat**. Ciò consente a prompt specifici di parlare direttamente senza aprire una finestra mentre altri aprono una chat completa.
- **Nuove variabili di prompt dinamiche (`[currentURL]` e `[text]`)**: I prompt personalizzati supportano ora `[currentURL]` per catturare l'URL del documento attivo in Google Chrome, Mozilla Firefox e Microsoft Edge, e `[text]` per inserire dinamicamente l'intero contenuto di testo del campo di modifica attualmente focalizzato (ignorando le caselle di password protette).
- **Revisione del downloader di video per Twitter/X**: Ripristinato il download e l'analisi dei video di Twitter/X a seguito di guasti nei sistemi di scraping a monte. L'estrazione video ora utilizza la robusta API FixTweet per recuperare direttamente flussi MP4 della massima qualità dalla CDN di Twitter, completi di fallback automatico TwitSave e supporto proxy.
- **Correzione del downloader di video per Instagram**: Ripristinato il download e l'analisi dei Reel di Instagram e degli URL video in seguito a modifiche dei moduli a monte sul servizio di download.
- **Correggi & Prestazioni**: La funzione "Premi per parlare" risponde nel momento in cui premi il tasto, l'Assistente dal vivo non avvia più una risposta a metà frase, l'osservatore non segnala più l'immagine precedente e l'elenco della profondità di pensiero offre solo ciò che il tuo modello supporta effettivamente. L'operatore IA può scorrere anche a sinistra e a destra. Risolto un errore `AttributeError` durante l'analisi di video online e impedito ai prompt personalizzati senza selezione di testo di iniettare accidentalmente titoli di finestre in background nelle richieste all'IA.

## Modifiche per 2026.09.01

- **Cronologia (Control + H)**: Il livello dei comandi include ora una finestra di dialogo **Cronologia** (`Control + H`) che elenca le chat e i documenti passati con filtri per Tutti, Chat e Documenti. Riapri qualsiasi chat con la sua conversazione completa (i file allegati vengono riallegati automaticamente) oppure riapri un documento e continua la lettura. Premi **Canc** su qualsiasi elemento per rimuoverlo, o cancella tutto in una volta.
- Premendo **D** nel livello dei comandi verranno elencati per primi i documenti letti di recente. Scegline uno per continuare dalla pagina in cui ti trovavi (anche se l'OCR è già terminato) oppure premi **Apri file...** (`Ctrl + O`) per cercare un file come di consueto.
- **Premi per parlare per l'Assistente dal vivo**: Prendi il controllo totale delle tue conversazioni dal vivo! Abilita **Premi per parlare** nella nuova scheda delle impostazioni dell'Assistente dal vivo e assegna un tasto qualsiasi — o anche un singolo modificatore come `Ctrl Sinistro` — per parlare. Tieni premuto il tasto per parlare e rilascialo quando hai finito, con un breve segnale acustico a ogni pressione e rilascio. Un interruttore corrispondente compare anche direttamente nella finestra dell'Assistente dal vivo, così puoi passare dalla modalità premi per parlare alla modalità microfono aperto senza lasciare la conversazione.
- **Audio nativo Gemini 2.5 Flash**: L'Assistente dal vivo supporta ora il modello audio nativo di Gemini 2.5 Flash (`gemini-2.5-flash-native-audio-preview-12-2025`) per conversazioni vocali naturali e a bassa Latenza. Puoi passare ad esso da **Impostazioni → Routing avanzato del modello → Modello Assistente dal vivo (solo Gemini)**, oppure mantenere "Automatico" per rimanere sul modello consigliato.
- **Backup e ripristino delle impostazioni**: Aggiunto un potente sistema di backup e ripristino nella scheda **Avanzate**! Ora puoi salvare tutte le impostazioni del componente aggiuntivo — incluse chiavi API, modelli, prompt personalizzati e preferenze — in un unico file JSON e ripristinarle perfettamente in qualsiasi momento, su qualsiasi computer o dopo aver reinstallato NVDA. Durante il backup, puoi scegliere cosa includere: **Tutto** (impostazioni, etichette personalizzate, avanzamento OCR e cronologia) o **Solo impostazioni**.
- **Lettura diretta di testo ed HTML**: Il lettore di documenti può ora aprire direttamente file di testo semplice (`.txt`) e HTML (`.html`, `.htm`)! Rileva automaticamente la codifica del file, rimuove script e elementi di formattazione superflui e suddivide intelligentemente il contenuto in pagine leggibili — reimportando persino i suoi file esportati preservando la struttura della pagina — così puoi leggerli all'istante senza elaborazione OCR o IA!
- **TTS Gemini Live per il lettore di documenti**: Il pulsante "Genera audio" supporta ora Gemini Live, un motore di sintesi vocale in streaming di alta qualità e a ritmo naturale! Quando Gemini è il tuo provider attivo, puoi scegliere tra TTS standard e Gemini Live direttamente nel lettore, e la tua selezione verrà memorizzata per la volta successiva!
- **Scorciatoie per prompt personalizzati**: Ora puoi assegnare un tasto di scelta rapida a qualsiasi tuo prompt personalizzato direttamente dal Gestore dei prompt! Assegna a ogni prompt il suo tasto o combinazione di tasti dedicati per eseguirlo all'istante, acquisendo automaticamente la selezione o il contesto corrente senza passaggi extra!
- **Navigazione dei messaggi della chat**: Rivedi qualsiasi conversazione senza usare le mani! All'interno di qualsiasi finestra di chat (Chat diretta, chat documento, affina e altro), premi `Alt + Giù` per ascoltare il messaggio successivo e `Alt + Su` per ascoltare quello precedente, con chiari prefissi "Tu" / "IA" e limiti "Primo messaggio" / "Ultimo messaggio" annunciati man mano che procedi.
- **Copia messaggio della chat (Alt + C)**: Durante la revisione di una conversazione con `Alt + Su/Giù`, premi `Alt + C` per copiare negli appunti il messaggio su cui ti trovi attualmente — rispettando l'impostazione Markdown pulito — con una conferma vocale.
- **Prompt di sistema per la chat diretta**: La Chat diretta (`Shift+C`) ha ora un proprio prompt di sistema modificabile — "Istruzione chat diretta" — che definisce il ruolo dell'assistente e la lingua di risposta per ogni conversazione. Puoi personalizzarlo dalla scheda Prompt predefiniti del Gestore dei prompt.
- **Navigazione per pagina con il cursore nel lettore di documenti**: Leggere documenti multipagina è diventato ancora più semplice! Nel Visualizzatore documenti, quando il cursore raggiunge l'ultima riga di una pagina e premi `Giù`, il lettore passa automaticamente alla pagina successiva. Premendo `Su` all'inizio di una pagina verrai riportato senza problemi a quella precedente — niente più cambi pagina manuali durante la lettura!
- **Nuovi interruttori per le impostazioni rapide**: Copia le risposte dell'IA negli appunti, Output diretto (nessuna finestra di chat), Markdown pulito nella chat e Scambio intelligente possono ora essere attivati e disattivati all'istante dalle impostazioni rapide del livello dei comandi!
- **Scheda Impostazioni Assistente dal vivo**: L'Assistente dal vivo ha ora una propria scheda di impostazioni dedicata! L'opzione "Assistente dal vivo: Output diretto (Nessuna finestra)" è stata spostata qui dalla scheda Connessione, e la scheda viene visualizzata solo quando Google Gemini (o un provider personalizzato compatibile con Gemini) è il tuo provider attivo.

## Modifiche per 2026.08.06

- **Etichettatura Esplora Interfaccia (UI Explorer)**: Ora è possibile aggiungere etichette direttamente agli elementi trovati all'interno di Esplora Interfaccia! È stato aggiunto un nuovo pulsante "Aggiungi etichetta" e l'interfaccia rimane intelligentemente aperta e preserva il focus in modo da poter etichettare rapidamente più oggetti senza interruzioni.
- **Miglioramento del livello Impostazioni rapide**: Il livello di Vision Assistant (`Insert+Shift+V`) è ora persistente e altamente interattivo! Puoi usare i tasti freccia `Su/Giù` per navigare tra le impostazioni rapide (Provider, Modello, Lingua risposta IA, Modello TTS) e i tasti freccia `Sinistra/Destra` per cambiarne istantaneamente i valori con un feedback vocale intelligente e conciso. Le tue selezioni hanno effetto immediato (inclusa l'attivazione automatica del routing avanzato quando necessario), e il livello rimane attivo durante la configurazione.
- **Chat diretta (`Shift+C`)**: Aggiunto un nuovo comando al livello! Premi `Shift+C` per aprire istantaneamente una finestra di "Chat diretta". Questo fornisce un'interfaccia di conversazione pulita e basata su testo direttamente con l'IA, senza bisogno di un'immagine o di un documento come punto di partenza.
- **Recupero cronologia chat impeccabile**: Risolto un bug importante in cui la pressione di `Spazio` per richiamare l'ultimo risultato faceva perdere la cronologia della chat successiva. Ora, il componente aggiuntivo tiene traccia della conversazione a livello globale. Se chatti, chiudi la finestra di dialogo e premi `Spazio` per richiamarla, l'intera cronologia della conversazione bidirezionale viene ripristinata perfettamente! Funziona per Chat diretta, Analisi visiva, Chat documenti e Traduzione.
- **Descrizioni di immagini in linea nell'OCR**: Aggiunta una funzione opzionale per descrivere le immagini in linea durante l'OCR dei documenti. Puoi attivare/disattivare questa impostazione nelle impostazioni OCR del componente aggiuntivo, all'interno delle opzioni del Lettore di documenti prima dell'estrazione, e rapidamente al volo tramite il livello Impostazioni rapide.
- **Traduzione vocale (`Control+T`)**: Aggiunta una nuova e potente funzione! Dettatate il discorso e traducetelo e digitatelo istantaneamente usando l'IA in base alle lingue di origine e di arrivo configurate.
- **Miglioramenti al programma di download degli aggiornamenti**: La finestra di dialogo di download dell'aggiornamento ora mostra correttamente l'avanzamento del download in percentuale ed è stato risolto un bug per cui appariva un messaggio fantasma "Scaricamento aggiornamento" all'annullamento dell'installazione.
- **Miglioramenti al downloader di eSpeak-NG**: Aggiunto il tracciamento della percentuale di avanzamento per i download di eSpeak-NG.
- **Resilienza dell'OCR in batch**: Risolto un problema nell'OCR PDF in batch in cui il processo si interrompeva se la chiave API attiva raggiungeva la sua quota a metà; ora passa automaticamente alla chiave successiva disponibile e riprende il processo.
- **Supporto ai Captcha visivi**: Aggiunto un solido supporto per la risoluzione dei captcha visivi. Tenta di risolvere automaticamente sfide di immagini complesse come hCaptcha e reCAPTCHA, migliorando significativamente l'accessibilità sui moduli Web difficili.
- **Revisione del trascrivitore audio**: Il modulo del Trascrivitore audio è stato completamente ricostruito e ora supporta sia file audio che video. Presenta 3 distinte modalità operative: "Trascrivi (Lingua originale)", "Trascrivi e traduci (Lingua di arrivo)" e una nuova e potente opzione "Doppia e traduci (Lingua di arrivo)" (esclusiva di Gemini) che genera un doppiaggio audio tradotto del discorso originale.
- **Numeri di pagina opzionali nel Lettore di documenti**: Aggiunta una nuova impostazione per attivare o disattivare l'inclusione di numeri di pagina e separatori negli output di documenti multipagina. Puoi gestire facilmente questa opzione dalle impostazioni principali o attivarla/disattivarla al volo tramite il livello Impostazioni rapide. Questa funzione si applica sia alle esportazioni di file di testo/HTML che alla finestra in linea "Visualizza formattato", consentendoti di leggere documenti combinati senza interruzioni.
- **Gemini Live TTS illimitato per le descrizioni video**: Ora puoi selezionare "Gemini Live TTS" come motore vocale durante la generazione della narrazione audio sincronizzata (MP3) per i video. Questo sfrutta l'API di Gemini Live per sintetizzare descrizioni audio di alta qualità senza limiti di caratteri o restrizioni di lunghezza.
- **Modularizzazione della codebase**: Riorganizzata la struttura del componente aggiuntivo da un file singolo a un'architettura modulare a più file per una migliore manutenibilità.
- **Progettazione dell'interfaccia delle impostazioni**: La finestra di dialogo Impostazioni è stata completamente ridisegnata per utilizzare un'interfaccia moderna basata su schede anziché un layout raggruppato, fornendo una migliore organizzazione e una navigazione più semplice mantenendo tutte le opzioni esistenti.
- **Registrazione file globale e dedicata**: Aggiunto un sistema di registrazione file globale opzionale nella nuova scheda di impostazione "Avanzate". Cattura automaticamente gli eventi operativi, il traffico API e gli errori in tutti i moduli del componente aggiuntivo in un file dedicato (`vision_assistant.log`). Supporta livelli di dettaglio dei log configurabili (Debug, Info, Avviso, Errore), periodi di conservazione automatizzati (da 1 ora a 90 giorni) e apertura o cancellazione diretta dei log dalle impostazioni con impatto zero sulle prestazioni o interferenza con i log di NVDA.
- **Tracciamento dell'avanzamento del caricamento su Gemini**: Aggiunti annunci in tempo reale della percentuale di avanzamento durante il caricamento di file di grandi dimensioni (video, audio, documenti) sull'API Google Gemini.

## Modifiche per 2026.07.15

- **Filtraggio intelligente del modello API**: Revisione completa del sistema di filtraggio dei modelli per utilizzare un approccio basato puramente su una blacklist anziché su whitelist. Aggiunte parole chiave di filtro più rigorose (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`) per garantire che il menu a discesa del modello di chat principale rimanga perfettamente pulito e a prova di futuro, mantenendo al contempo tutti i modelli specializzati accessibili nella sezione di Routing Avanzato.
- **Ricerca nel Routing Avanzato**: Tutti i menu a discesa del Routing Avanzato dei Modelli (OCR, STT, TTS, Operatore, Video, Live) e il selettore della variante eSpeak sono ora completamente ricercabili. È possibile digitare rapidamente per filtrare e trovare il modello o la variante desiderati.
- **Nuove scorciatoie del livello di comandi**:
  - Andare in **Menu NVDA > Preferenze > Impostazioni > Vision Assistant Pro**.
  - **Rapporto chiavi quota esaurita (`Alt + Q`)**: Segnala il numero esatto di chiavi API di Gemini che hanno superato la loro quota giornaliera, identificando su quale modello specifico sono esaurite e annunciando il loro esatto orario di reset.
  - Selezionare **“Instradamento avanzato dei modelli (specifico per attività)”** per sbloccare i controlli dettagliati.
- **Revisione completa dell'Analizzatore Video**: L'Analizzatore Video è stato completamente trasformato! In precedenza, forniva solo una descrizione di base dei video online. Ora è una suite di elaborazione video completa su misura per gli utenti non vedenti:
  - **Registrazione dello schermo locale (`Control+V`)**: Ora è possibile registrare video silenziosi direttamente dallo schermo. L'IA analizzerà il segmento registrato e fornirà una descrizione altamente dettagliata della scena, del layout e delle azioni.
  - **Generazione di audiodescrizione (SRT)**: L'add-on ora può generare script di audiodescrizione altamente dettagliati (in formato SRT standard) per i video, completi di temporizzazione intelligente degli intervalli per ancorare in modo intelligente le descrizioni alle pause naturali nella traccia audio, e OCR letterale per qualsiasi testo sullo schermo.
  - **Narrazione audio sincronizzata (Esportazione MP3)**: Oltre ai sottotitoli basati su testo, l'add-on può sintetizzare l'audiodescrizione in parlato, mescolarla automaticamente con la traccia audio originale del video, applicare il ducking audio (abbassando il volume di sottofondo durante le descrizioni) ed esportare il risultato finale sincronizzato come file MP3!
  - **Azione intelligente sul file video**: Se ci si posiziona su un file video locale e si preme la scorciatoia video, l'add-on lo rileverà automaticamente ed elaborerà il file direttamente.
  - **Tracciamento avanzato dei personaggi**: L'IA ora esegue una pre-passata di estrazione dei personaggi. Costruisce un dizionario globale dei personaggi e traccia i personaggi accuratamente segmento per segmento senza confondere le identità.
  - **Configurazione dell'analisi video**: Aggiunte nuove impostazioni per controllare le dimensioni dei chunk SRT, la sottotitolazione dei personaggi e le esclusioni di responsabilità.
  - **Routing esteso dei modelli**: Ora è possibile selezionare esplicitamente modelli video specializzati (`gemini_video_model`, `custom_video_model`) nelle impostazioni di Routing Avanzato dei Modelli.
- **Gestione intelligente della quota API**: Gestione migliorata degli errori 429 (Limite Giornaliero) tracciando le quote per singolo modello. Se una chiave raggiunge il limite giornaliero su un modello, viene messa intelligentemente in quarantena solo per quel modello specifico, lasciando la chiave disponibile per l'uso con altri modelli.

## Modifiche per la versione 7.0.0

- **Ripresa delle scansioni non completate**: Aggiunta una funzione di ripresa sia per il Lettore di Documenti che per le Azioni Intelligenti sui File. Se una scansione viene interrotta, ora è possibile continuare dal punto in cui si è fermata anziché ricominciare da capo.
- **Nuova variabile `[screen_fg_obj]`**: Aggiunta una variabile di prompt personalizzata per catturare uno screenshot della sola finestra in primo piano attiva anziché dell'intero schermo.
- **Nuovi Tentativi Intelligenti e Rotazione delle Chiavi**: Il componente aggiuntivo ora riprova silenziosamente fino a 5 volte con la stessa chiave quando si verificano sovraccarichi temporanei del server (come "elevata richiesta" o risposte nonformate). Se i tentativi falliscono, passa automaticamente alla chiave API successiva nell'elenco.
- **Rilevamento della Tenda dello Schermo**: Aggiunto un controllo per impedire l'acquisizione di screenshot quando la Tenda dello Schermo è attiva (sia che sia permanentemente abilitata o attivata temporaneamente tramite la combinazione di tasti). Verrà visualizzato un avviso e l'operazione verrà interrotta, evitando l'invio di immagini nere e lo spreco di token API.
- **Ottimizzazioni del Lettore di Documenti**: La finestra di dialogo per l'intervallo PDF ora pre-seleziona automaticamente la lingua di destinazione predefinita dalle impostazioni del componente aggiuntivo. È stata inoltre migliorata la gestione dei thread per garantire che le attività in background vengano interrotte correttamente alla chiusura del lettore.
- **Integrazione nativa di Mistral OCR**: Integrata l'API OCR per documenti nativa di Mistral. I documenti multipagina vengono automaticamente uniti, caricati ed elaborati in batch utilizzando l'endpoint specializzato `/v1/ocr` di Mistral, mentre le immagini a pagina singola vengono elaborate direttamente senza conversioni PDF non necessarie [1].
- **Gestori di URL personalizzati dinamici**: La modifica dell'URL API personalizzato cancella istantaneamente l'elenco dei modelli memorizzati nella cache e ripristina la casella di testo per l'inserimento manuale del modello. Ciò garantisce la piena compatibilità con endpoint personalizzati (come Cloudflare AI Gateway) che non supportano l'endpoint standard per l'elenco `/v1/models`.
- **Motore di input dell'AI Operator rinnovato**: Completamente riscritto il sistema sottostante di simulazione di mouse e tastiera per l'AI Operator. Sostituita la precedente API `mouse_event` con la moderna API Windows `SendInput`, offrendo una compatibilità notevolmente superiore con le applicazioni moderne, le finestre protette da UAC e i display ad alta risoluzione (Hi-DPI).
- **Risolte le operazioni di Trascina e Rilascia (Drag & Drop)**: Le azioni di trascinamento e rilascio nell'AI Operator sono ora perfettamente stabili e affidabili. Il nuovo motore utilizza curve di movimento "naturale" (easing), posizionamento preciso del cursore, tempistiche ottimizzate e una tecnica di "spintarella" intelligente per garantire che Windows e le applicazioni riconoscano ed eseguano correttamente i gesti di trascinamento senza interruzioni a metà percorso.
- **Supporto Multi-Monitor**: L'AI Operator supporta ora pienamente le configurazioni multi-monitor. I movimenti e i clic del mouse funzionano correttamente su tutti i monitor grazie all'utilizzo del flag `MOUSEEVENTF_VIRTUALDESK`, garantendo un posizionamento accurato indipendentemente dal monitor su cui si trova l'applicazione di destinazione.
- **Simulazione della tastiera migliorata**: Migliorata l'iniezione di sequenze di tasti per supportare completamente i "Tasti Estesi" (come i tasti freccia, Inizio/Home, Fine/End, Pagina su/giù, Ins, Canc e F1-F12). Ciò garantisce che i comandi di navigazione e le scorciatoie inviati dall'AI Operator funzionino in modo impeccabile in tutte le applicazioni.
- **Supporto per immagini HEIC/HEIF**: Aggiunto il supporto nativo per i formati fotografici di iPhone. Ora è possibile selezionare direttamente i file `.heic` e `.heif` per la descrizione tramite IA, l'OCR o la lettura di documenti senza necessità di conversioni preventive.

## Modifiche per la versione 6.5.0

- **Assistente dal vivo**: Aggiunta una funzionalità di assistente vocale e dello schermo in tempo reale, disponibile esclusivamente per il provider Google Gemini (o provider personalizzati compatibili con Gemini). Include la personalizzazione interattiva della voce e della profondità di riflessione direttamente all'interno della finestra di dialogo, con riconnessione automatica alla modifica delle impostazioni.
- **Provider IA MiniMax**: Integrato MiniMax come provider paritario con pieno supporto multimodale (chat, visione, OCR), TTS personalizzato che utilizza oltre 300 voci dinamiche e rimozione automatica dei blocchi di ragionamento (es. ` thinking... response`) dagli output.
- **Traduzione nel Visualizzatore documenti**: Corretto un errore di traduzione silenzioso per gli utenti NVDA non di lingua inglese, assicurando che a Google Translate venga inviato il codice lingua standard a 2 lettere anziché il nome della lingua localizzato.
- **Nuovo tentativo per la scansione batch di PDF**: Implementata una logica di nuovo tentativo separata, altamente ottimizzata e silenziosa per la scansione batch di documenti PDF, al fine di evitare caricamenti ridondanti ed fastidiosi popup di errore durante i tentativi.
- **Stato del Visualizzatore documenti**: Risolto un bug per cui lo stato generale del componente aggiuntivo (verificato tramite `I`) rimaneva bloccato su "Elaborazione batch avviata" durante le scansioni di documenti lunghi.
- **Risolto arresto anomalo dei thread**: Risolto un grave arresto anomalo per asserzione di thread `IsMain() failed in wxTimerImpl` durante l'apertura di documenti da un thread in background, trasferendo la coda di callback della GUI a `wx.CallAfter`.

## Modifiche per la versione 6.1.2

- **Pre-controllo etichette duplicate**: Risolto un problema nell'etichettatura singola in cui il controllo dei duplicati utilizzava vecchie chiavi di coordinate, causando l'invio da parte di NVDA di richieste AI duplicate per oggetti già etichettati anziché annunciare l'etichetta esistente.
- **Chat sui documenti per provider non Gemini**: Risolto un controllo rigoroso sulla chiave API nella Chat sui documenti (`on_ask`) per garantire che gli utenti che utilizzano OpenAI, Groq o provider personalizzati locali (come Ollama) possano chattare con i documenti senza essere bloccati.
- **Traduzione OCR rapida per Chrome**: Ripristinata l'API di traduzione gratuita e senza chiave per l'OCR di Chrome. La traduzione del testo estratto ora bypassa l'AI di Gemini, consentendo di risparmiare quote API e di accelerare il processo di traduzione.
- **Filtro alfanumerico CAPTCHA**: Corretta la logica di filtraggio nel risolutore di CAPTCHA per garantire che i caratteri non alfanumerici vengano ripuliti correttamente in tutte le situazioni.
- **Aggiornamento della guida al livello di comandi**: Corretta la scorciatoia per l'annuncio dello stato nel menu della guida da `L` a `I`, e aggiunti entrambi i comandi di etichettatura (`L` e `Shift+L`) all'elenco.

## Modifiche per la versione 6.1.1

- **Correzione dell'output di pensiero per Gemma 4**: Risolto un problema con i modelli Gemma 4 in cui l'intero processo di pensiero interno veniva visualizzato come risposta finale, o in cui la disattivazione del pensiero produceva risposte vuote. Ora il componente aggiuntivo isola ed estrae correttamente solo la risposta testuale finale pulita.
- **OCR in batch da Esplora file**: Ora è possibile selezionare più foto o PDF direttamente in Esplora file di Windows ed estrarre il testo o analizzarli in batch. Il componente aggiuntivo filtrerà ed elaborerà automaticamente solo i formati di file supportati.

## Modifiche per la versione 6.1.0

- **Integrazione IA locale universale (Configura IA locale)**: È stato aggiunto un nuovo pulsante **"Configura IA locale"** nelle impostazioni del provider personalizzato. Ora gli utenti possono configurare automaticamente i motori di IA locale, tra cui **Ollama**, **LM Studio**, **Jan.ai** e **KoboldCPP**, in modo istantaneo.
- **Bypass intelligente del proxy locale**: La logica di connessione è stata ricostruita con un meccanismo avanzato di bypass del proxy. Il componente aggiuntivo è ora abbastanza intelligente da aggirare completamente i proxy di sistema di Windows per le connessioni di loopback locali, garantendo connessioni di IA locale stabili anche quando la VPN o la modalità TUN sono attive.
- **Etichettatura IA ultra-stabile (v2)**: Le chiavi con coordinate assolute dello schermo sono state sostituite con un sistema ibrido e avanzato di **Firma dell'oggetto** (Object Signature). Le etichette ora si basano su identificatori programmatici (**AutomationId** di UIA o **ControlID** di Win32) e su coordinate relative alla finestra, rendendo le etichette personalizzate completamente resistenti al ridimensionamento, allo spostamento, al cambio di monitor o al ridimensionamento dei DPI della finestra.
- **Migrazione automatica e trasparente delle etichette**: L'aggiornamento è completamente trasparente. Al primo avvio e focalizzazione, il componente aggiuntivo migrerà automaticamente in background le vecchie etichette basate sulle coordinate al nuovo formato stabile con impronta digitale, senza alcuna perdita di dati.

## Changes for 6.0

- **Introducing Semantic AI Labeling**: Users can now permanently label unnamed buttons and icons using AI. Press **L** to label the current navigator object (supporting both Tab focus and object navigation) or **Shift+L** to scan and label the entire application at once.
- **Intelligent Label Management**: Added a new, fully accessible Label Manager dialog (via **Shift+L** if labels exist) to view, rename, or batch-delete custom labels.
- **Direct File Analysis (Bypass File Dialog)**: The add-on is now smart enough to detect if you are currently focusing on a PDF or image file in Windows File Explorer. Pressing **F (Smart File Action)** or **D (Document Reader)** on a highlighted file will immediately process it, bypassing the standard "Open" dialog entirely.

## Changes for 5.6

- **Added "None (Extract Text Layer)" OCR Engine**: Users can now extract text directly from searchable PDFs without using AI credits, significantly improving speed and privacy for text-based documents.
- **Refined UI Explorer Accuracy**: Improved the UI Explorer prompt to better identify element types (like List Items) and accurately report states such as "(Checked)", "(Selected)", or "(Expanded)" while ignoring Windows system components like the Taskbar and Clock.
- **Installation Setup Reminder**: Added a notification after installation to guide users to the settings menu for configuring their API keys and preferences.

## Changes for 5.5.2

- **Fixed AI Operator Typing Issue:** Resolved a bug where the letter 'v' was typed instead of pasting text on certain systems. This fix addresses timing conflicts that occurred during high system load.
- **Enhanced Stability:** Added robust error handling for clipboard operations to prevent addon crashes when the system clipboard is temporarily locked by other applications.
- **Timing Optimization:** Adjusted internal delays for keyboard events to ensure higher reliability across different system speeds and better compatibility with third-party Clipboard Managers.

## Changes for 5.5 (The Automation Update)

- **AI Operator (Autonomous Control - Shift+A):** This is the crown jewel of v5.5. Vision Assistant Pro has graduated from being a passive assistant to becoming your personal **AI Operator**. It doesn't just describe the screen—it takes command.
  - _How it works:_ You can now give verbal instructions to operate your PC. For example, in a completely inaccessible application where your screen reader stays silent, you can press **Shift+A** and type: _"Click on the Settings button"_ or _"Find the search field, type 'Latest News' and press enter."_ The AI visually identifies the elements, moves the mouse, and executes the task for you.
  - _Performance Note:_ This feature is optimized for **Gemini 3.0 Flash (Preview)**, delivering incredibly fast and intelligent responses that can handle even the most complex UI layouts.
  - **⚠️ Avviso sull'utilizzo delle API:** Poiché l'Operatore IA deve "vedere" esattamente cosa sta accadendo per essere accurato, invia uno screenshot ad alta risoluzione a ogni passaggio. Tieni presente che un uso frequente consumerà la tua quota API molto più velocemente rispetto ai normali compiti basati su testo.
- **Visual UI Explorer (E):** Tired of navigating through "unlabeled buttons"? Press **E** to activate the UI Explorer. The AI will scan the entire window and generate a list of every clickable element it sees—including icons, graphics, and menus. Simply pick an item from the list, and the AI Operator will click it for you. It’s like having an "accessible layer" on top of any app.
- **Context-Aware Smart File Action (F):** The "F" key has been completely overhauled. It no longer assumes you only want OCR. When you select a single image, it now intelligently asks for your intent: you can choose a **Detailed Visual Description** to understand the scene or a **Structured Text Extraction (OCR)** for reading. The menu adapts dynamically based on the file type and your active AI engine.
- **Core Optimization:** We've performed a deep cleanup of the add-on’s internal logic, removing unused legacy functions and redundant code. This results in a leaner, faster, and more reliable experience for all users.

## Changes for 5.0

- **Multi-Provider Architecture**: Added full support for **OpenAI**, **Groq**, and **Mistral** alongside Google Gemini. Users can now choose their preferred AI backend.
- **Advanced Model Routing**: Users of native providers (Gemini, OpenAI, etc.) can now select specific models from a dropdown list for different tasks (OCR, STT, TTS).
- **Advanced Endpoint Configuration**: Custom provider users can manually input specific URLs and model names for granular control over local or third-party servers.
- **Smart Feature Visibility**: The settings menu and Document Reader UI now automatically hide unsupported features (like TTS) based on the selected provider.
- **Dynamic Model Fetching**: The addon now fetches the available model list directly from the provider's API, ensuring compatibility with new models as soon as they are released.
- **Hybrid OCR & Translation**: Optimized the logic to use Google Translate for speed when using Chrome OCR, and AI-powered translation when using Gemini/Groq/OpenAI engines.
- **Universal "Re-scan with AI"**: The Document Reader's re-scan feature is no longer limited to Gemini. It now utilizes whatever AI provider is currently active to re-process pages.

## Changes for 4.6

- **Interactive Result Recall:** Added the **Space** key to the command layer, allowing users to instantly reopen the last AI response in a chat window for follow-up questions, even when "Direct Output" mode is active.
- **Telegram Community Hub:** Added an "Official Telegram Channel" link to the NVDA Tools menu, providing a quick way to stay updated with the latest news, features, and releases.
- **Enhanced Response Stability:** Optimized the core logic for Translation, OCR, and Vision features to ensure more reliable performance and a smoother experience when using direct speech output.
- **Improved Interface Guidance:** Updated the settings descriptions and documentation to better explain the new recall system and how it works alongside the direct output settings.

## Changes for 4.5

- **Advanced Prompt Manager:** Introduced a dedicated management dialog in settings to customize default system prompts and manage user-defined prompts with full support for adding, editing, reordering, and previewing.
- **Comprehensive Proxy Support:** Resolved network connectivity issues by ensuring that user-configured proxy settings are strictly applied to all API requests, including translation, OCR, and speech generation.
- **Automated Data Migration:** Integrated a smart migration system to automatically upgrade legacy prompt configurations to a robust v2 JSON format upon the first run without data loss.
- **Updated Compatibility (2025.1):** Set the minimum required NVDA version to 2025.1 due to library dependencies in advanced features like the Document Reader to ensure stable performance.
- **Optimized Settings Interface:** Streamlined the settings interface by reorganizing prompt management into a separate dialog, providing a cleaner and more accessible user experience.
- **Prompt Variables Guide:** Added a built-in guide within the prompt dialogs to help users easily identify and use dynamic variables such as [selection], [clipboard], and [screen_obj].

## Changes for 4.0.3

- **Enhanced Network Resilience:** Added an automatic retry mechanism to better handle unstable internet connections and temporary server errors, ensuring more reliable AI responses.
- **Visual Translation Dialog:** Introduced a dedicated window for translation results. Users can now easily navigate and read long translations line-by-line, similar to OCR results.
- **Aggregated Formatted View:** The "View Formatted" feature in the Document Reader now displays all processed pages in a single, organized window with clear page headers.
- **Optimized OCR Workflow:** Automatically skips the page range selection for single-page documents, making the recognition process faster and more seamless.
- **Improved API Stability:** Switched to a more robust header-based authentication method, resolving potential "All API Keys failed" errors caused by key rotation conflicts.
- **Bug Fixes:** Resolved several potential crashes, including an issue during add-on termination and a focus error in the chat dialog.

## Changes for 4.0.1

- **Advanced Document Reader:** A powerful new viewer for PDF and images with page range selection, background processing, and seamless `Ctrl+PageUp/Down` navigation.
- **New Tools Submenu:** Added a dedicated "Vision Assistant" submenu under NVDA's Tools menu for quicker access to core features, settings, and documentation.
- **Flexible Customization:** You can now choose your preferred OCR engine and TTS voice directly from the settings panel.
- **Multiple API Key Support:** Added support for multiple Gemini API keys. You can enter one key per line or separate them with commas in the settings.
- **Alternative OCR Engine:** Introduced a new OCR engine to ensure reliable text recognition even when hitting Gemini API quota limits.
- **Smart API Key Rotation:** Automatically switches to and remembers the fastest working API key to bypass quota limits.
- **Document to MP3/WAV:** Integrated capability to generate and save high-quality audio files in both MP3 (128kbps) and WAV formats directly within the reader.
- **Instagram Stories Support:** Added the ability to describe and analyze Instagram Stories using their URLs.
- **TikTok Support:** Introduced support for TikTok videos, allowing for full visual description and audio transcription of clips.
- **Redesigned Update Dialog:** Features a new accessible interface with a scrollable text box to clearly read version changes before installing.
- **Unified Status & UX:** Standardized file dialogs across the add-on and enhanced the 'L' command to report real-time progress.

## Changes for 3.6.0

- **Help System:** Added a help command (`H`) within the Command Layer to provide an easy-to-access list of all shortcuts and their functions.
- **Online Video Analysis:** Expanded support to include **Twitter (X)** videos. Also improved URL detection and stability for a more reliable experience.
- **Project Contribution:** Added an optional donation dialog for users who wish to support the project’s future updates and continuous growth.

## Changes for 3.5.0

\*   \*\*Command Layer:\*\* Introduced a Command Layer system (default: `NVDA+Shift+V`) to group shortcuts under a single master key. For example, instead of pressing `NVDA+Control+Shift+T` for translation, you now press `NVDA+Shift+V` followed by `T`.
\*   \*\*Online Video Analysis:\*\* Added a new feature to analyze YouTube and Instagram videos directly by providing a URL.

## Changes for 3.1.0

- **Direct Output Mode:** Added an option to skip the chat dialog and hear AI responses directly via speech for a faster and more seamless experience.
- **Clipboard Integration:** Added a new setting to automatically copy AI responses to the clipboard.

## Changes for 3.0

- **New Languages:** Added **Persian** and **Vietnamese** translations.
- **Expanded AI Models:** Reorganized the model selection list with clear prefixes (`[Free]`, `[Pro]`, `[Auto]`) to help users distinguish between free and rate-limited (paid) models. Added support for **Gemini 3.0 Pro** and **Gemini 2.0 Flash Lite**.
- **Dictation Stability:** Significantly improved Smart Dictation stability. Added a safety check to ignore audio clips shorter than 1 second, preventing AI hallucinations and empty errors.
- **File Handling:** Fixed an issue where uploading files with non-English names would fail.
- **Prompt Optimization:** Improved Translation logic and structured Vision results.

## Changes for 2.9

- **Added French and Turkish translations.**
- **Formatted View:** Added a "View Formatted" button in chat dialogs to view the conversation with proper styling (Headings, Bold, Code) in a standard browseable window.
- **Markdown Setting:** Added a new option "Clean Markdown in Chat" in Settings. Unchecking this allows users to see raw Markdown syntax (e.g., `**`, `#`) in the chat window.
- **Dialog Management:** Fixed an issue where the "Refine Text" or chat windows would open multiple times or fail to focus correctly.
- **UX Improvements:** Standardized file dialog titles to "Open" and removed redundant speech announcements (e.g., "Opening menu...") for a smoother experience.

## Changes for 2.8

- Added Italian translation.
- **Status Reporting:** Added a new command (NVDA+Control+Shift+I) to announce the current status of the add-on (e.g., "Uploading...", "Analyzing...").
- **HTML Export:** The "Save Content" button in result dialogs now saves output as a formatted HTML file, preserving styles like headings and bold text.
- **Settings UI:** Improved the Settings panel layout with accessible grouping.
- **New Models:** Added support for gemini-flash-latest and gemini-flash-lite-latest.
- **Languages:** Added Nepali to supported languages.
- **Refine Menu Logic:** Fixed a critical bug where "Refine Text" commands would fail if the NVDA interface language was not English.
- **Dictation:** Improved silence detection to prevent incorrect text output when no speech is input.
- **Update Settings:** "Check for updates on startup" is now disabled by default to comply with Add-on Store policies.
- Code Cleanup.

## Changes for 2.7

- Migrated project structure to the official NV Access Add-on Template for better standards compliance.
- Implemented automatic retry logic for HTTP 429 (Rate Limit) errors to ensure reliability during high traffic.
- Optimized translation prompts for higher accuracy and better "Smart Swap" logic handling.
- Updated Russian translation.

## Changes for 2.6

- Added Russian translation support (Thanks to nvda-ru).
- Updated error messages to provide more descriptive feedback regarding connectivity.
- Changed default target language to English.

## Changes for 2.5

- Added Native File OCR Command (NVDA+Control+Shift+F).
- Added "Save Chat" button to result dialogs.
- Implemented full localization support (i18n).
- Migrated audio feedback to NVDA's native tones module.
- Switched to Gemini File API for better handling of PDF and audio files.
- Fixed crash when translating text containing curly braces.

## Changes for 2.1.1

- Fixed an issue where the [file_ocr] variable was not functioning correctly within Custom Prompts.

## Changes for 2.1

- Standardized all shortcuts to use NVDA+Control+Shift to eliminate conflicts with NVDA's Laptop layout and system hotkeys.

## Changes for 2.0

- Implemented built-in Auto-Update system.
- Added Smart Translation Cache for instant retrieval of previously translated text.
- Added Conversation Memory to contextually refine results in chat dialogs.
- Added Dedicated Clipboard Translation command (NVDA+Control+Shift+Y).
- Optimized AI prompts to strictly enforce target language output.
- Fixed crash caused by special characters in input text.

## Changes for 1.5

- Added support for over 20 new languages.
- Implemented Interactive Refine Dialog for follow-up questions.
- Added Native Smart Dictation feature.
- Added "Vision Assistant" category to NVDA's Input Gestures dialog.
- Fixed COMError crashes in specific applications like Firefox and Word.
- Added automatic retry mechanism for server errors.

## Changes for 1.0

- Initial release.
