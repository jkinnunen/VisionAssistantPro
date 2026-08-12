# Documentația Vision Assistant Pro

<!-- DOWNLOAD_COUNT_START --> Total descărcări: 61.000+ <!-- DOWNLOAD_COUNT_END -->

**Vision Assistant Pro** este un asistent AI avansat, multimodal, pentru NVDA. Folosește motoare AI de clasă mondială pentru a oferi citire inteligentă a ecranului, traducere, dictare vocală și analiză de documente.

_Acest add-on a fost lansat comunității în onoarea Zilei Internaționale a Persoanelor cu Dizabilități._

## 1. Instalare și configurare

Mergi la **Meniul NVDA > Preferințe > Setări > Vision Assistant Pro**. Dialogul de setări este organizat în 8 file accesibile: **Conexiune**, **Comportament AI**, **Limbi de traducere**, **Cititor de documente**, **Video**, **CAPTCHA**, **Prompturi** și **Avansat**.

### 1.1 Fila Conexiune
- **Furnizor:** Selectează serviciul AI preferat. Furnizorii acceptați includ **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** și **Personalizat** (servere compatibile OpenAI, precum Ollama, LM Studio, Jan.ai sau KoboldCPP).
- **Cheie API:** Introdu una sau mai multe chei API (separate prin virgule sau linii noi) pentru rotație automată.
- **Preia modelele:** Apasă acest buton după introducerea cheii API pentru a descărca cea mai recentă listă de modele disponibile de la furnizor.
- **Model AI:** Selectează modelul principal folosit pentru chat general și analiză.
- **Setări furnizor personalizat:** Configurează endpointuri locale sau personalizate. Include **Configurare AI local** (configurare dintr-o singură acțiune pentru Ollama, LM Studio, Jan.ai sau KoboldCPP) și **Configurare avansată a endpointului**.
- **Rutare avansată a modelelor (specifică sarcinilor):** Opțional, selectează modele dedicate din liste derulante pentru sarcini OCR, STT, TTS, AI Operator, Video și Live Assistant.
- **Opțiuni de conexiune și ieșire:** Configurează URL-ul proxy, verificările de actualizare la pornire, curățarea Markdown în chat, copierea răspunsurilor AI în clipboard, ieșirea directă (fără fereastră de chat) și ieșirea directă Live Assistant.

### 1.2 Fila Comportament AI
- **Creativitate (temperatură):** Controlează aleatorietatea și creativitatea AI-ului (de la 0,0 la 2,0). Valorile mai mici produc rezultate mai deterministe și mai exacte pentru traducere/OCR.

### 1.3 Fila Limbi de traducere
- **Limba sursă:** Selectează limba implicită de intrare.
- **Limba țintă:** Selectează limba principală în care vrei traducerea.
- **Limba răspunsului AI:** Selectează limba pentru răspunsurile AI generale.
- **Schimbare inteligentă:** Inversează automat limbile sursă și țintă pe baza textului detectat.

### 1.4 Fila Cititor de documente
- **Motor OCR:** Alege între **Chrome (rapid)** pentru rezultate rapide sau **AI (avansat)** pentru păstrarea superioară a layoutului.
- **Dimensiune lot OCR:** Specifică numărul de pagini per cerere (setează 0 pentru procesare într-o singură cerere).
- **Descrie imagini în linie:** Activează/dezactivează descrierile de imagini în linie în timpul extragerii textului din documente.
- **Export numere pagini:** Activează/dezactivează numerele de pagină și separatoarele în rezultatele documentelor cu mai multe pagini.
- **Voce TTS:** Selectează stilul vocal implicit pentru generarea audio.

### 1.5 Fila Video
- **Dimensiune segment video:** Durata segmentelor în minute pentru generarea descrierilor audio (setează 0 pentru a procesa întregul fișier).
- **Adaugă listă de personaje:** Opțiune pentru adăugarea dicționarului de personaje ca prima intrare de subtitrare.
- **Adaugă avertisment AI:** Opțiune pentru inserarea unui avertisment AI la începutul subtitrărilor SRT video.

### 1.6 Fila CAPTCHA
- **Activează rezolvitorul CAPTCHA vizual:** Activează/dezactivează rezolvarea automată a provocărilor vizuale (hCaptcha, reCAPTCHA).
- **Metodă CAPTCHA text:** Alege între capturarea **obiectului navigator** sau a **ecranului complet**.

### 1.7 Fila Prompturi
- **Gestionează prompturi:** Deschide un dialog dedicat pentru personalizarea prompturilor de sistem implicite sau pentru crearea, editarea, reordonarea și previzualizarea prompturilor personalizate definite de utilizator, cu variabile dinamice (de exemplu, `[selection]`, `[screen_fg_obj]`).

### 1.8 Fila Avansat și jurnalizarea globală
Navighează la fila **Avansat** pentru a configura jurnalizarea globală a add-on-ului:
- **Activează fișierul jurnal dedicat:** Activează jurnalizarea tuturor evenimentelor operaționale, traficului API și erorilor din toate modulele add-on-ului într-un fișier separat (`vision_assistant.log`).
- **Nivel jurnal:** Selectează nivelul de detaliu între **Debug (toate detaliile)**, **Info (informații generale)**, **Avertisment (doar avertismente)** și **Eroare (doar erori)**.
- **Păstrează jurnalele timp de:** Setează perioade automate de păstrare pentru curățarea intrărilor vechi din jurnal (de la 1 oră până la 90 de zile).
- **Controale pentru gestionarea jurnalelor:** Folosește **Deschide fișierul jurnal**, **Deschide folderul jurnalelor** sau **Golește fișierul jurnal** pentru a inspecta sau șterge datele jurnalului direct, fără repornirea NVDA și fără interferențe cu jurnalele standard NVDA.

## 2. Strat de comenzi și scurtături

Pentru a preveni conflictele de taste, acest add-on folosește un **strat de comenzi**.
1. Apasă **NVDA + Shift + V** (tasta principală) pentru a activa stratul (vei auzi un bip).
2. Eliberează tastele, apoi apasă una dintre următoarele taste individuale:

| Tastă           | Funcție                 | Descriere                                                                 |
|---------------|--------------------------|-----------------------------------------------------------------------------|
| **Shift + A** | **AI Operator**         | **Operare autonomă:** Spune-i AI-ului să efectueze o sarcină pe ecran. Apăsarea din nou oprește instant operațiile active. |
| **E**         | **UI Explorer**          | **Clic interactiv:** Identifică și apasă elemente UI în orice aplicație.        |
| **T**         | Traducător inteligent         | Traduce textul de sub cursorul navigator sau selecția.                        |
| **Shift + T** | Traducător clipboard     | Traduce conținutul aflat în prezent în clipboard.                              |
| **R**         | Rafinator de text             | Rezumă, corectează gramatica, explică sau rulează **prompturi personalizate**.                 |
| **V**         | Viziune obiect            | Descrie obiectul navigator curent.                                     |
| **O**         | Viziune ecran complet       | Analizează întregul layout și conținut al ecranului.                              |
| **Shift + V** | Analiză video    | Analizează fișiere video locale sau videoclipuri online de pe **YouTube**, **Instagram**, **TikTok** sau **Twitter (X)**.  |
| **Control + V** | Înregistrare video locală  | Înregistrează un videoclip silențios al ecranului și analizează acțiunile și layoutul.  |
| **D**         | Cititor de documente          | Cititor avansat pentru PDF și imagini, cu selecție interval de pagini.               |
| **F**         | **Acțiune inteligentă pentru fișiere**    | Recunoaștere contextuală din fișiere imagine, PDF sau TIFF selectate.          |
| **M**         | Transcriere și dublare media | Transcrie sau dublează fișiere audio/video (MP3, WAV, MP4 etc.) în limba ta țintă. |
| **C**         | Rezolvitor CAPTCHA           | Capturează și rezolvă CAPTCHA-uri.                        |
| **Shift + C** | Chat direct              | Deschide o interfață de chat direct, bazată pe text, cu AI-ul.                       |
| **S**         | Dictare inteligentă          | Convertește vorbirea în text. Apasă pentru a începe înregistrarea, apoi din nou pentru oprire/tastare.      |
| **Control+T** | Traducere vocală        | Transcrie, traduce și tastează rezultatul pe baza setărilor tale de limbă. |
| **Control+L** | **Live Assistant**       | **Copilot în timp real (doar Gemini):** Pornește sau oprește o conversație vocală și de ecran în direct cu asistentul AI. |
| **I**         | Raportare stare         | Anunță progresul curent (de exemplu, „Se scanează...”, „Inactiv”).                   |
| **L**         | **Etichetează obiectul**         | **Etichetare AI semantică:** Etichetează permanent elementul/pictograma focalizată curentă. |
| **Shift + L** | **Gestionează/scanează etichete**   | Deschide Managerul de etichete (dacă există etichete) sau scanează aplicația pentru elemente fără nume. |
| **U**         | Verificare actualizări             | Verifică manual pe GitHub cea mai recentă versiune a add-on-ului.                 |
| **Space**     | Reapelează ultimul rezultat       | Afișează ultimul răspuns AI într-un dialog de chat pentru revizuire sau întrebări suplimentare.        |
| **H**         | Ajutor comenzi            | Afișează o listă cu toate scurtăturile disponibile.                                 |
| **Alt + S**   | Setări                 | Deschide dialogul de setări Vision Assistant Pro.                             |
| **Alt + Q**   | Raport chei cu cotă epuizată | Raportează numărul de chei API Gemini care și-au depășit cota zilnică și ora lor de resetare. |
| **Alt + M**   | Audit rutare            | Raportează modelele AI selectate în prezent în rutarea avansată.               |
| **Up / Down** | Navigare setări rapide       | Navighează între categoriile de setări rapide (furnizor, model etc.) în strat. |
| **Left / Right**| Schimbă setarea rapidă   | Schimbă valoarea setării rapide selectate curent.                  |

## 3. AI Operator - Control autonom al computerului

**AI Operator** transformă Vision Assistant Pro dintr-un cititor pasiv într-un asistent activ care poate interacționa cu computerul în numele tău. Îi poți cere să descrie ecranul, să răspundă la întrebări despre ce vede sau chiar să preia controlul—apăsând butoane, trăgând elemente, tastând text și navigând prin aplicații folosind comenzi în limbaj natural.

Cel mai mare avantaj? Funcționează perfect în software complet inaccesibil. Dacă ești blocat într-o aplicație personalizată, un desktop remote sau un site web în care cititorul tău de ecran rămâne complet tăcut, operatorul nu este deranjat. Pentru că „vede” ecranul vizual, poate găsi, citi și interacționa cu elemente care nu au deloc etichete de accesibilitate.

### Cum funcționează
1. Apasă **NVDA + Shift + V**, apoi apasă **Shift + A** (sau folosește scurtătura directă) pentru a deschide dialogul AI Operator.
2. Tastează ce vrei să faci în limbaj simplu (de exemplu, „Apasă butonul Salvează”, „Ce spune mesajul de eroare?” sau „Redenumește fișierul în final.pdf”).
3. AI-ul va analiza ecranul, va identifica elementele relevante și va executa acțiunea sau va oferi răspunsul. Dacă o sarcină necesită mai mulți pași, operatorul va continua să lucreze până când este completă.
4. Apasă din nou **Shift + A** oricând pentru a opri instant o operație în desfășurare.

### Acțiuni acceptate
Operatorul înțelege o gamă largă de comenzi:
- **Descriere și răspuns**: „Descrie layoutul ecranului” sau „Ce spune mesajul de eroare?”
- **Clic**: „Apasă butonul Salvează”
- **Clic dreapta**: „Dă clic dreapta pe fișier”
- **Dublu clic**: „Dă dublu clic pe document”
- **Tragere și plasare**: „Trage documentul în folderul Arhivă”
- **Tastare**: „Tastează «Hello World» în caseta de căutare”
- **Derulare**: „Derulează în jos de trei ori”
- **Apăsare de tastă**: „Apasă Enter”, „Apasă Tab”, „Apasă Escape”
- **Sarcini cu mai mulți pași**: „Deschide File Explorer, găsește raportul și redenumește-l în final.pdf”

### Note importante
- **⚠️ Avertisment privind utilizarea API**: Deoarece operatorul trebuie să „vadă” exact ce se întâmplă pe ecran, trimite o captură de ecran la rezoluție înaltă la fiecare pas. Utilizarea frecventă îți va consuma cota API mult mai repede decât funcțiile standard bazate pe text.
- **Aplicații cu drepturi de administrator**: Dacă NVDA nu rulează cu privilegii de administrator, operatorul poate să nu poată interacționa cu ferestre care necesită permisiuni ridicate. Aceasta este o limitare de securitate Windows, nu o eroare a add-on-ului.
- **Recomandări**: Pentru rezultate mai bune, dă comenzi clare și specifice. „Apasă butonul albastru Trimite din partea de jos a formularului” va funcționa aproape întotdeauna mai bine decât doar „Apasă butonul”.

## 4. Analiză video și descriere audio

> **Notă:** Funcțiile Analiză video și Descriere audio sunt alimentate strict de furnizorul **Google Gemini**. Asigură-te că furnizorul activ din setările add-on-ului este setat la Google Gemini.

Vision Assistant Pro introduce capabilități puternice de procesare video, concepute special pentru utilizatorii nevăzători. Poate analiza atât videoclipuri online, cât și înregistrări locale ale ecranului, pentru a oferi descrieri vizuale foarte detaliate și pentru a genera scripturi profesionale de descriere audio (SRT).

### 4.1 Înregistrare locală a ecranului (Control + V)
Dacă întâlnești un videoclip tăcut, o animație sau un tutorial pe ecran, îl poți captura direct:
1. Apasă **NVDA + Shift + V** pentru a intra în stratul de comenzi, apoi apasă **Control + V**.
2. Add-on-ul va înregistra silențios ecranul în fundal.
3. Apasă din nou **Control + V** pentru a opri înregistrarea.
4. AI-ul va analiza apoi segmentul video înregistrat și va oferi o descriere foarte detaliată a scenei, personajelor și acțiunilor.

### 4.2 Analiză video (Shift + V)
Poți analiza atât fișiere video locale, cât și videoclipuri online. Selectează pur și simplu un fișier video local în Windows Explorer sau copiază un link video online în clipboard. Poți apăsa și **Shift + V** oriunde (de exemplu, într-un player media) pentru a deschide un dialog unde poți căuta un fișier video sau lipi manual un URL.
- **Platforme online acceptate:** YouTube, Instagram, TikTok și Twitter (X).
- AI-ul va detecta automat fișierul local sau URL-ul, va procesa videoclipul și va oferi o descriere vizuală cuprinzătoare și un rezumat audio.

### 4.3 Generare descriere audio (SRT)
Pentru o experiență mai structurată, add-on-ul poate genera scripturi profesionale de descriere audio în formatul standard SubRip (SRT). 
- **Sincronizare inteligentă pe pauze:** AI-ul ascultă pista audio și ancorează descrierile vizuale în mod specific în pauzele naturale și golurile de liniște, pentru a minimiza inteligent suprapunerea peste dialog.
- **Urmărirea personajelor:** Motorul face o trecere preliminară pentru a extrage personaje distincte pe baza trăsăturilor faciale imuabile. Construiește un dicționar global pentru a urmări și eticheta cu precizie personajele în scene diferite, fără confuzie.
- **OCR text mot-à-mot:** Orice text care apare pe ecran (semne, telefoane, generice) este citat strict mot-à-mot.
- **Cum se folosește:** Pentru a asculta subtitrarea generată, plasează pur și simplu fișierul `.srt` în același folder cu fișierul video și dă-i exact același nume. Apoi configurează playerul media (de exemplu, VLC sau PotPlayer) să trimită textul subtitrării direct către cititorul tău de ecran sau motorul TTS în timpul redării.

### 4.4 Narațiune audio sincronizată (export MP3)
Dincolo de crearea fișierelor SRT bazate pe text, add-on-ul funcționează ca un instrument complet de producție pentru descriere audio, sintetizând descrierile în vorbire și mixându-le cu videoclipul. Acum poți alege **Gemini Live TTS** ca motor vocal, care folosește API-ul Gemini Live pentru a genera narațiune vocală foarte realistă și nelimitată. Când generezi un MP3 pentru fișiere video locale, ai mai multe moduri de mixare:
- **AD standard (mixare voce):** Narațiunea este suprapusă direct peste sunetul videoclipului. Vei fi întrebat dacă vrei să aplici **Audio Ducking** (reducerea volumului de fundal în timpul descrierilor) pentru a te asigura că narațiunea este clară.
- **AD extins (pauză audio):** Motorul pune pe pauză sunetul video original în timpul descrierilor, asigurându-se că nu pierzi niciun cuvânt din dialogul original sau din narațiunea AI.
- **Videoclipuri YouTube:** Pentru sursele YouTube (care nu sunt descărcate local), exportul MP3 va conține strict pista vocală AI sincronizată, fără sunetul de fundal al videoclipului.

## 5. Transcriere și dublare media (M)
Transcriptorul audio a fost reconstruit complet pentru a accepta atât fișiere audio, cât și fișiere video (MP3, WAV, MP4, MKV etc.). Apasă **M** în stratul de comenzi pentru a selecta un fișier media și alege unul dintre cele 3 moduri de operare distincte:
1. **Transcrie (limba originală)**: Transcrie cu acuratețe vorbirea în limba sa originală.
2. **Transcrie și traduce (limba țintă)**: Transcrie vorbirea și o traduce în limba țintă configurată.
3. **Dublează și traduce (limba țintă)** *(doar Gemini)*: O funcție nouă puternică ce transcrie vorbirea, o traduce în limba ta țintă și sintetizează o dublare audio vorbită folosind motorul TTS al add-on-ului.

## 6. Cititor avansat de documente și imagini

Vision Assistant Pro include un Cititor de documente foarte optimizat, conceput pentru PDF-uri cu mai multe pagini, imagini complexe și chiar formate iPhone HEIC.

### 6.1 Procesare în lot și reluare
Nu trebuie să citești un document masiv dintr-o singură dată. Introdu un interval de pagini (de exemplu, `1-20`), iar AI-ul va procesa toate paginile în fundal. Dacă NVDA se blochează sau întrerupi scanarea, add-on-ul îți va reține progresul și îți va oferi opțiunea de **reluare** exact de unde a rămas!

### 6.2 Acțiune inteligentă pentru fișiere
Nu trebuie întotdeauna să deschizi mai întâi documentul. În Windows File Explorer, evidențiază pur și simplu un PDF sau o imagine și apasă **D** (Cititor de documente) sau **F** (Acțiune inteligentă pentru fișiere) în stratul de comenzi. Add-on-ul va ocoli instant dialogul de fișiere și va începe procesarea fișierului evidențiat.

### 6.3 Scurtături în vizualizatorul de documente
Când fereastra Cititorului de documente este deschisă, poți folosi următoarele scurtături:
- **Ctrl + PageDown:** Mută-te la pagina următoare.
- **Ctrl + PageUp:** Mută-te la pagina anterioară.
- **Alt + A:** Deschide un dialog de chat pentru a pune întrebări despre document.
- **Alt + R:** Forțează o **rescanare cu AI** folosind furnizorul activ.
- **Alt + G:** Generează și salvează un fișier audio de calitate înaltă (WAV/MP3). *(Ascuns dacă furnizorul nu acceptă TTS).*
- **Alt + S / Ctrl + S:** Salvează textul extras ca fișier TXT sau HTML.

## 7. Etichetare AI semantică și UI Explorer

Te-ai blocat într-o aplicație în care peste tot apare „buton fără etichetă”? Motorul de etichetare AI semantică rezolvă permanent acest lucru.

### 7.1 Etichetare permanentă a obiectelor (L)
Mută focusul cititorului de ecran pe un grafic sau buton fără etichetă și apasă **L** în stratul de comenzi. AI-ul va privi vizual butonul, îi va determina funcția și va aplica o etichetă permanentă. 
*Spre deosebire de instrumentele mai vechi de etichetare pentru cititoare de ecran, acest add-on folosește un sistem hibrid avansat de „semnătură a obiectului” (AutomationId/ControlID). Etichetele tale personalizate vor supraviețui redimensionării ferestrelor, schimbării monitorului și actualizărilor aplicației!*

### 7.2 Scanarea completă a aplicației (Shift + L)
Apasă **Shift + L** pentru a scana întreaga fereastră activă dintr-o dată. AI-ul va găsi toate elementele fără etichetă și le va denumi inteligent într-o singură operație. Ulterior, poți gestiona, redenumi sau șterge în lot aceste etichete din Managerul de etichete integrat.

### 7.3 UI Explorer (E)
Ai nevoie să interacționezi cu un element fără să navighezi manual până la el? Apasă **E** pentru a activa UI Explorer. AI-ul va scana ecranul și va genera o listă accesibilă cu fiecare element pe care se poate face clic (ignorând zgomotul de sistem precum bara de activități). Alege un element din listă, iar add-on-ul îl va apăsa instant pentru tine.

## 8. Asistent vocal live

Live Assistant transformă Vision Assistant Pro într-un copilot interactiv în timp real.
*(Notă: Această funcție este exclusivă pentru Google Gemini și furnizorii personalizați compatibili Gemini).*

- **Activare:** Apasă **Control + L** în stratul de comenzi pentru a deschide dialogul Live Assistant.
- **Interacțiune în timp real:** Vorbește natural prin microfon. AI-ul îți va asculta simultan vocea și va privi ecranul activ. Poți pune întrebări precum „La ce mă uit?” sau „Citește-mi al treilea paragraf.”
- **Personalizare:** În interiorul dialogului, poți schimba stilul vocal al AI-ului (de exemplu, Profesional, Prietenos, Energic) și îi poți ajusta „profunzimea gândirii” pentru a controla cât de profund raționează înainte de a răspunde.

## 9. Prompturi personalizate și variabile

Poți gestiona prompturile în **Setări > Prompturi > Gestionează prompturi...**.

### Variabile acceptate
- `[selection]`: Textul selectat curent.
- `[clipboard]`: Conținutul clipboardului.
- `[clipboard_image]`: Imaginea aflată în prezent în clipboard.
- `[screen_obj]`: Captură de ecran a obiectului navigator.
- `[screen_fg_obj]`: Captură de ecran a ferestrei active din prim-plan.
- `[screen_full]`: Captură de ecran completă.
- `[file_ocr]`: Selectează fișier imagine/PDF pentru extragerea textului.
- `[file_read]`: Selectează document pentru citire (TXT, cod, PDF).
- `[file_audio]`: Selectează fișier audio pentru analiză (MP3, WAV, OGG).
- `{target_lang}`: Limba țintă curentă.
- `{source_lang}`: Limba sursă curentă.
- `{response_lang}`: Limba curentă a răspunsului AI.
- `{swap_target}`: Limba de rezervă pentru traducerea cu schimbare inteligentă.
- `{swap_instruction}`: Blocul de instrucțiuni pentru traducerea cu schimbare inteligentă.

## 10. Cazuri reale de utilizare (Ce funcție ar trebui să folosesc?)

Vision Assistant Pro este plin de instrumente avansate. Iată câteva scenarii comune care te ajută să alegi funcția potrivită:

- **Scenariu: Vrei să înțelegi layoutul complet al unei ferestre complicate sau al unei aplicații inaccesibile.**
  *Soluție:* Apasă **O** (Viziune ecran complet). AI-ul va analiza întregul ecran și va descrie exact unde sunt poziționate elementele, textele și butoanele.

- **Scenariu: Ai găsit o imagine pe o pagină web sau un grafic fără etichetă într-un document.**
  *Soluție:* Mută obiectul navigator pe grafic și apasă **V** (Viziune obiect). AI-ul va descrie precis ce conține acea imagine.

- **Scenariu: Vrei să urmărești un film sau un videoclip cu descrieri audio.**
  *Soluție:* Apasă **Shift + V** pe videoclip și alege **„Generează descriere audio (fișier SRT)”**. Când se termină, apasă **„Generează narațiune sincronizată (MP3)”** și selectează **„AD extins”**. Add-on-ul va crea o pistă audio care pune inteligent pe pauză dialogul filmului pentru a descrie scenele vizuale.

- **Scenariu: Ai întâlnit o aplicație plină de „butoane fără etichetă”.**
  *Soluție:* Apasă **L** pentru a eticheta permanent butonul respectiv folosind AI. Sau apasă **Shift + L** pentru a scana și eticheta întreaga fereastră dintr-o dată. Dacă vrei doar să apeși ceva rapid, apasă **E** (UI Explorer) pentru a primi o listă cu toate elementele pe care se poate face clic.

- **Scenariu: Trebuie să treci de un CAPTCHA inaccesibil.**
  *Soluție:* Apasă **C** (Rezolvitor CAPTCHA). AI-ul va captura automat CAPTCHA-ul, îl va rezolva și va introduce răspunsul în câmpul corect.

- **Scenariu: Vrei să citești un document PDF lung, de 50 de pagini.**
  *Soluție:* Apasă **D** (Cititor de documente), setează furnizorul la Google Gemini și introdu intervalul de pagini `1-50`. Add-on-ul va extrage textul cu acuratețe în fundal.

- **Scenariu: Urmărești un tutorial video tăcut sau o animație pe ecran.**
  *Soluție:* Apasă **Control + V** pentru a începe înregistrarea ecranului. Lasă tutorialul să ruleze, apoi apasă din nou **Control + V**. AI-ul va explica exact ce a fost demonstrat.

- **Scenariu: Întâlnești o eroare neașteptată, o problemă de conexiune API sau vrei să diagnostichezi probleme cu servere locale personalizate.**
  *Soluție:* Mergi la **Setări > Avansat**, bifează **„Activează fișierul jurnal dedicat”** și setează **Nivel jurnal** la **„Debug”**. Execută acțiunea din nou, apoi apasă **„Deschide fișierul jurnal”** pentru a inspecta detaliile tehnice sau atașează fișierul `vision_assistant.log` la un tichet de suport.

***
**Notă:** Pentru toate funcțiile AI este necesară o conexiune activă la internet. Documentele cu mai multe pagini sunt procesate automat.

## 11. Suport și comunitate

Rămâi la curent cu cele mai recente noutăți, funcții și lansări:
- **Canal Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **Issue-uri GitHub:** Pentru raportări de erori și cereri de funcții.

### Raportarea erorilor și jurnale
Când deschizi un issue pe GitHub sau ceri suport, te rog include detalii despre furnizorul AI activ, model și versiunea NVDA. Dacă ai probleme de conexiune sau blocări neașteptate, activează fișierul jurnal dedicat din **Setări > Avansat**, recreează problema și atașează fișierul `vision_assistant.log` pentru a ne ajuta să rezolvăm problema mai repede.

## 12. Susținătorii proiectului

Mulțumiri sincere membrilor comunității care susțin dezvoltarea și mentenanța continuă a acestui proiect prin contribuțiile lor financiare generoase:

*   **@Alyabani94**
*   **Ali Alamri**
*   **Ilya**
*   **Susținător anonim** (`UQDd...CnMY`)
*   **leonardo0216**
*   **Sergei Fleytin**
*   **Suman Gayen**

*Dacă dorești să susții financiar proiectul și să îți vezi numele aici, poți găsi opțiunea **Donate** în meniul Instrumente NVDA (submeniul Vision Assistant) sau în timpul procesului de configurare de după instalare.*


---

## Modificări pentru 2026.08.06

*   **Etichetare în UI Explorer**: Acum poți adăuga etichete direct elementelor găsite în UI Explorer! A fost adăugat un nou buton „Adaugă etichetă”, iar interfața rămâne deschisă și păstrează focusul în mod inteligent, ca să poți eticheta rapid mai multe obiecte fără întrerupere.
*   **Îmbunătățire a stratului de setări rapide**: Stratul Vision Assistant (`Insert+Shift+V`) este acum persistent și foarte interactiv! Poți folosi săgețile `Sus/Jos` pentru a naviga între setările rapide (furnizor, model, limba răspunsului AI, model TTS) și săgețile `Stânga/Dreapta` pentru a le schimba instant valorile, cu feedback vocal inteligent și concis. Selecțiile tale se aplică imediat (inclusiv activarea automată a rutării avansate atunci când este necesar), iar stratul rămâne activ cât timp configurezi.
*   **Chat direct (`Shift+C`)**: A fost adăugată o comandă nouă în strat! Apasă `Shift+C` pentru a deschide instant o fereastră „Chat direct”. Aceasta oferă imediat o interfață conversațională curată, bazată pe text, cu AI-ul, fără să fie nevoie de o imagine sau de un document ca punct de pornire.
*   **Reapelare impecabilă a istoricului conversației**: A fost corectată o eroare majoră prin care apăsarea tastei `Space` pentru reapelarea ultimului rezultat pierdea istoricul conversației ulterioare. Acum, add-on-ul urmărește conversația la nivel global. Dacă discuți, închizi dialogul și apeși `Space` pentru a-l reapela, întregul istoric dus-întors este restaurat perfect! Funcționează pentru Chat direct, analiză vizuală, chat pe documente și traducere.
*   **Descrieri de imagini inline în OCR**: A fost adăugată o funcție opțională pentru descrierea imaginilor în linie în timpul OCR pentru documente. Poți comuta această setare din setările OCR ale add-on-ului, din opțiunile Cititorului de documente înainte de extragere și rapid, din mers, prin stratul de setări rapide.
*   **Traducere vocală (`Control+T`)**: A fost adăugată o funcție nouă puternică! Dictează vorbirea și traduce și tastează instant rezultatul cu AI, pe baza limbilor sursă și țintă configurate.
*   **Îmbunătățiri ale descărcătorului de actualizări**: Dialogul de descărcare a actualizării afișează acum corect progresul în procente, iar o eroare prin care apărea un mesaj fantomă „Se descarcă actualizarea” după anularea instalării a fost corectată.
*   **Îmbunătățiri ale descărcătorului eSpeak-NG**: A fost adăugată urmărirea progresului în procente pentru descărcările eSpeak-NG.
*   **Reziliență pentru OCR în lot**: A fost corectată o problemă în OCR-ul PDF în lot prin care procesul se oprea dacă cheia API activă își atingea cota la mijlocul operației; acum se comută automat la următoarea cheie disponibilă și procesul continuă.
*   **Suport pentru CAPTCHA vizual**: A fost adăugat suport robust pentru rezolvarea CAPTCHA-urilor vizuale. Încearcă să rezolve automat provocări complexe bazate pe imagini, precum hCaptcha și reCAPTCHA, îmbunătățind semnificativ accesibilitatea formularelor web dificile.
*   **Restructurarea transcriptorului audio**: Modulul Transcriptor audio a fost reconstruit complet și acceptă acum atât fișiere audio, cât și fișiere video. Include 3 moduri de operare distincte: „Transcrie (limba originală)”, „Transcrie și traduce (limba țintă)” și noua opțiune puternică „Dublează și traduce (limba țintă)” (exclusiv pentru Gemini), care generează o dublare audio tradusă a vorbirii originale.
*   **Numere de pagină opționale în Cititorul de documente**: A fost adăugată o setare nouă pentru includerea numerelor de pagină și a separatoarelor în rezultatele documentelor cu mai multe pagini. Poți gestiona ușor această opțiune din setările principale sau o poți comuta din mers prin stratul de setări rapide. Funcția se aplică atât exporturilor în fișiere text/HTML, cât și ferestrei „Vizualizare formatată” în linie, permițându-ți să citești documente combinate fără întreruperi.
*   **Gemini Live TTS nelimitat pentru descrieri video**: Acum poți selecta „Gemini Live TTS” ca motor vocal atunci când generezi narațiune audio sincronizată (MP3) pentru videoclipuri. Acesta folosește API-ul Gemini Live pentru a sintetiza descrieri audio de calitate înaltă, fără limite de caractere sau restricții de lungime.
*   **Modularizarea bazei de cod**: Structura add-on-ului a fost refactorizată dintr-un singur fișier într-o arhitectură modulară cu mai multe fișiere, pentru mentenanță îmbunătățită.
*   **Redesign al interfeței de setări**: Dialogul de setări a fost reproiectat complet pentru a folosi o interfață modernă pe file în locul unui layout grupat, oferind organizare mai bună și navigare mai ușoară, păstrând toate opțiunile existente.
*   **Jurnalizare globală și fișier jurnal dedicat**: A fost adăugat un sistem opțional de jurnalizare globală în fișier, în noua filă „Avansat”. Capturează automat evenimente operaționale, trafic API și erori din toate modulele add-on-ului într-un fișier dedicat (`vision_assistant.log`). Acceptă niveluri configurabile de detaliu pentru jurnal (Debug, Info, Avertisment, Eroare), perioade automate de păstrare (de la 1 oră până la 90 de zile) și deschiderea sau golirea directă a jurnalului din setări, fără impact asupra performanței și fără interferențe cu jurnalul NVDA.
*   **Urmărire progres încărcări Gemini**: Au fost adăugate anunțuri în timp real ale progresului procentual la încărcarea fișierelor mari (video, audio, documente) în API-ul Google Gemini.

## Modificări pentru 2026.07.15

*   **Filtrare inteligentă a modelelor API**: Sistemul de filtrare a modelelor a fost refăcut complet pentru a folosi o abordare bazată strict pe listă neagră în loc de liste albe. Au fost adăugate cuvinte-cheie de filtrare mai puternice (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`) pentru ca lista derulantă a modelului principal de chat să rămână perfect curată și pregătită pentru viitor, păstrând în același timp toate modelele specializate accesibile în secțiunea Rutare avansată.
*   **Căutare în rutarea avansată**: Toate listele derulante din Rutarea avansată a modelelor (OCR, STT, TTS, Operator, Video, Live) și selectorul de variante eSpeak pot fi acum căutate complet. Poți tasta rapid pentru a filtra și găsi modelul sau varianta dorită.
*   **Scurtături noi în stratul de comenzi**:
    *   **Setări (`Alt + S`)**: Deschide instant dialogul de setări Vision Assistant Pro.
    *   **Raport chei cu cotă epuizată (`Alt + Q`)**: Raportează numărul exact de chei API Gemini care și-au depășit cota zilnică, identifică modelul specific pe care sunt epuizate și anunță ora exactă de resetare.
    *   **Audit rutare (`Alt + M`)**: Auditează și anunță configurația curentă de Rutare avansată, citind modelele selectate activ pentru sarcini specializate și ignorând setările implicite.
*   **Revizuire completă a Analizatorului video**: Analizatorul video a fost transformat complet! Înainte oferea doar o descriere de bază a videoclipurilor online. Acum este o suită completă de procesare video, adaptată pentru utilizatorii nevăzători:
    *   **Înregistrare locală a ecranului (`Control+V`)**: Acum poți înregistra videoclipuri fără sunet direct de pe ecran. AI-ul va analiza segmentul înregistrat și va furniza o descriere foarte detaliată a scenei, structurii și acțiunilor.
    *   **Generare descriere audio (SRT)**: Add-on-ul poate genera acum scripturi de descriere audio foarte detaliate, în format SRT standard, pentru videoclipuri, cu temporizare inteligentă pe pauze, pentru a ancora descrierile în pauzele naturale ale pistei audio, și cu OCR verbatim pentru orice text de pe ecran.
    *   **Narațiune audio sincronizată (export MP3)**: Dincolo de subtitrările text, add-on-ul poate sintetiza descrierea audio în vorbire, o poate mixa automat cu pista audio originală a videoclipului, poate aplica atenuare audio (reducerea volumului de fundal în timpul descrierilor) și poate exporta rezultatul final sincronizat ca fișier MP3!
    *   **Acțiune inteligentă pentru fișiere video**: Dacă focalizezi un fișier video local și apeși scurtătura video, add-on-ul îl va detecta automat și va procesa fișierul direct.
    *   **Urmărire avansată a personajelor**: AI-ul face acum o trecere preliminară pentru extragerea personajelor. Construiește un dicționar global de personaje și urmărește personajele cu acuratețe, segment cu segment, fără a confunda identitățile.
    *   **Configurare analiză video**: Au fost adăugate setări noi pentru controlul dimensiunii segmentelor SRT, subtitrarea personajelor și avertismente.
    *   **Rutare extinsă a modelelor**: Acum poți selecta explicit modele video specializate (`gemini_video_model`, `custom_video_model`) în setările de Rutare avansată a modelelor.
*   **Gestionare inteligentă a cotelor API**: Gestionarea erorilor 429 (limită zilnică) a fost îmbunătățită prin urmărirea cotelor pe fiecare model. Dacă o cheie își atinge limita zilnică pe un model, aceasta este carantinată inteligent doar pentru acel model, rămânând disponibilă pentru alte modele.

## Modificări pentru 7.0.0

*   **Reluarea scanărilor neterminate**: A fost adăugată o funcție de reluare atât pentru Cititorul de documente, cât și pentru Acțiunile inteligente pentru fișiere. Dacă o scanare este întreruptă, acum poți continua de unde s-a oprit în loc să o iei de la început.
*   **Variabila nouă `[screen_fg_obj]`**: A fost adăugată o variabilă de prompt personalizat pentru capturarea unei capturi de ecran doar a ferestrei active din prim-plan, în locul întregului ecran.
*   **Reîncercări inteligente și rotația cheilor**: Add-on-ul reîncearcă acum în mod silențios de până la 5 ori cu aceeași cheie când apar supraîncărcări temporare ale serverului, cum ar fi „cerere ridicată” sau răspunsuri formatate incorect. Dacă reîncercările eșuează, trece automat la următoarea cheie API din listă.
*   **Detectarea Perdelei ecranului**: A fost adăugată o verificare care împiedică realizarea capturilor de ecran când Perdeaua ecranului este activă, indiferent dacă este activată permanent sau temporar cu scurtătura. Vei fi avertizat, iar operația se va opri, împiedicând trimiterea imaginilor negre și risipirea tokenilor API.
*   **Ajustări pentru Cititorul de documente**: Dialogul intervalului PDF preselectează acum automat limba țintă implicită din setările add-on-ului. De asemenea, gestionarea firelor de execuție a fost îmbunătățită pentru a asigura oprirea corectă a sarcinilor din fundal când cititorul este închis.
*   **Integrare nativă Mistral OCR**: A fost integrat API-ul nativ Document OCR de la Mistral. Documentele cu mai multe pagini sunt îmbinate, încărcate și procesate automat în loturi prin endpointul specializat `/v1/ocr` al Mistral, iar imaginile cu o singură pagină sunt procesate direct, fără conversii inutile în PDF [1].
*   **Gestionare dinamică a URL-urilor personalizate**: Modificarea URL-ului API personalizat șterge acum instantaneu lista de modele din cache și restaurează caseta de text pentru introducerea manuală a modelului. Astfel se asigură compatibilitate completă cu endpointuri personalizate, precum Cloudflare AI Gateway, care nu acceptă endpointul standard de listare `/v1/models`.
*   **Motor de intrare AI Operator reproiectat**: Sistemul de simulare a mouse-ului și tastaturii folosit de AI Operator a fost rescris complet. API-ul vechi `mouse_event` a fost înlocuit cu API-ul modern Windows `SendInput`, oferind compatibilitate mult mai bună cu aplicațiile moderne, ferestrele protejate prin UAC și ecranele cu DPI ridicat.
*   **Operații drag-and-drop remediate**: Acțiunile de tragere și plasare din AI Operator sunt acum complet stabile și fiabile. Noul motor folosește curbe naturale de accelerare și decelerare („easing”), poziționare precisă a cursorului, temporizare optimizată și o tehnică inteligentă de „nudge”, astfel încât Windows și aplicațiile să recunoască și să execute corect gesturile de tragere și plasare fără eșecuri la jumătatea acțiunii.
*   **Suport pentru mai multe monitoare**: AI Operator acceptă acum complet configurațiile cu mai multe monitoare. Mișcările și clicurile mouse-ului funcționează corect pe toate monitoarele folosind indicatorul `MOUSEEVENTF_VIRTUALDESK`, asigurând poziționarea precisă indiferent de monitorul pe care se află aplicația țintă.
*   **Simulare îmbunătățită a tastaturii**: Injectarea tastelor a fost îmbunătățită pentru a accepta complet „tastele extinse”, precum tastele săgeți, Home, End, Page Up/Down, Insert, Delete și F1-F12. Astfel, comenzile de navigare și scurtăturile trimise de AI Operator funcționează impecabil în toate aplicațiile.
*   **Suport pentru imagini HEIC/HEIF**: A fost adăugat suport nativ pentru formatele foto de iPhone. Acum poți selecta direct fișiere `.heic` și `.heif` pentru descriere AI, OCR sau citire în Cititorul de documente, fără conversie prealabilă.

## Modificări pentru 6.5.0

*   **Asistent live**: A fost adăugată o funcție de asistent vocal și de ecran în timp real, disponibilă exclusiv pentru furnizorul Google Gemini sau pentru furnizori personalizați compatibili cu Gemini. Include personalizarea interactivă a vocii și a profunzimii de gândire direct în dialog, cu reconectare automată când se modifică setările.
*   **Furnizorul AI MiniMax**: MiniMax a fost integrat ca furnizor de același nivel, cu suport multimodal complet (chat, vision, OCR), TTS personalizat folosind peste 300 de voci dinamice și eliminarea automată a blocurilor de raționament, de exemplu `<think>...</think>`, din rezultate.
*   **Traducerea în vizualizatorul de documente**: A fost corectată o eroare silențioasă de traducere pentru utilizatorii NVDA în alte limbi decât engleza, asigurând trimiterea codului standard de limbă din 2 litere către Google Translate în locul numelui localizat al limbii.
*   **Reîncercare pentru scanarea PDF în lot**: A fost implementată o logică de reîncercare foarte optimizată, separată și silențioasă pentru scanarea documentelor PDF în lot, pentru a preveni încărcările redundante și pentru a evita popup-urile de eroare deranjante în timpul reîncercărilor.
*   **Starea vizualizatorului de documente**: A fost remediată o eroare prin care starea generală a add-on-ului, verificată cu `I`, rămânea blocată pe „Procesarea lotului a început” în timpul scanărilor lungi de documente.
*   **Blocare de threading rezolvată**: A fost remediată o blocare severă cauzată de aserțiunea de fir `IsMain() failed in wxTimerImpl` la deschiderea documentelor dintr-un fir de fundal, prin trecerea cozii de callback-uri GUI la `wx.CallAfter`.

## Modificări pentru 6.1.2

*   **Preverificare pentru etichete duplicate**: A fost remediată o problemă în etichetarea individuală, unde verificarea duplicatelor folosea chei vechi bazate pe coordonate, făcând NVDA să trimită cereri AI duplicate pentru obiecte deja etichetate în loc să anunțe eticheta existentă.
*   **Chat pentru documente cu furnizori non-Gemini**: A fost remediată o verificare strictă a cheii API în Chatul pentru documente (`on_ask`), astfel încât utilizatorii cu OpenAI, Groq sau furnizori personalizați locali, precum Ollama, să poată discuta cu documentele fără să fie blocați.
*   **Traducere rapidă pentru Chrome OCR**: A fost restaurat API-ul gratuit de traducere, fără cheie, pentru Chrome OCR. Traducerea textului extras ocolește acum AI-ul Gemini, economisind cotele API și accelerând procesul de traducere.
*   **Filtru alfanumeric pentru CAPTCHA**: A fost corectată logica de filtrare din rezolvatorul CAPTCHA, pentru a se asigura că caracterele non-alfanumerice sunt curățate corect în toate situațiile.
*   **Actualizare ajutor pentru stratul de comenzi**: A fost corectată scurtătura pentru anunțarea stării din meniul de ajutor, de la `L` la `I`, și au fost adăugate în listă ambele comenzi de etichetare (`L` și `Shift+L`).

## Modificări pentru 6.1.1

*   **Remediere pentru rezultatul de gândire Gemma 4**: A fost remediată o problemă cu modelele Gemma 4, în care întregul proces intern de gândire era afișat ca răspuns final sau în care dezactivarea gândirii producea răspunsuri goale. Add-on-ul izolează și extrage acum corect doar răspunsul final curat.
*   **OCR în lot din File Explorer**: Acum poți selecta mai multe fotografii sau PDF-uri direct în Windows File Explorer și poți extrage textul sau le poți analiza în lot. Add-on-ul va filtra și procesa automat doar formatele de fișier acceptate.

## Modificări pentru 6.1.0

*   **Integrare universală cu AI local (Configurează AI local)**: A fost adăugat un nou buton **„Configurează AI local”** în Setările furnizorului personalizat. Utilizatorii pot configura automat și instant motoare AI locale, inclusiv **Ollama**, **LM Studio**, **Jan.ai** și **KoboldCPP**.
*   **Ocolire inteligentă a proxy-ului local**: Logica de conexiune a fost reconstruită cu un mecanism avansat de ocolire a proxy-ului. Add-on-ul poate acum ocoli complet proxy-urile de sistem Windows pentru conexiunile locale de tip loopback, asigurând conexiuni stabile cu AI local chiar și când VPN-ul sau proxy-ul în modul TUN este activ.
*   **Etichetare AI ultra-stabilă (v2)**: Cheile bazate pe coordonate absolute de ecran au fost înlocuite cu un sistem avansat, hibrid, de **Semnătură a obiectului**. Etichetele se bazează acum pe identificatori programatici (UIA **AutomationId** sau Win32 **ControlID**) și pe coordonate relative la fereastră, făcând etichetele tale personalizate rezistente la redimensionarea, mutarea sau scalarea ferestrei și la schimbarea monitorului.
*   **Migrare automată fără întreruperi a etichetelor**: Actualizarea este complet transparentă. Add-on-ul va migra automat etichetele tale vechi, bazate pe coordonate moștenite, în noul format stabil de amprentă în fundal, la prima focalizare, fără pierdere de date.

## Modificări pentru 6.0

*   **Introducerea etichetării AI semantice**: Utilizatorii pot eticheta permanent butoane și pictograme fără nume folosind AI. Apasă **L** pentru a eticheta obiectul curent al navigatorului, cu suport pentru focalizarea prin Tab și navigarea pe obiecte, sau **Shift+L** pentru a scana și eticheta întreaga aplicație dintr-o singură acțiune.
*   **Gestionare inteligentă a etichetelor**: A fost adăugat un dialog nou, complet accesibil, Manager de etichete, prin **Shift+L** dacă există etichete, pentru vizualizarea, redenumirea sau ștergerea în lot a etichetelor personalizate.
*   **Analiză directă a fișierelor, fără dialogul de fișiere**: Add-on-ul poate detecta acum dacă focalizezi un fișier PDF sau imagine în Windows File Explorer. Când apeși **F (Acțiune inteligentă pentru fișiere)** sau **D (Cititor de documente)** pe un fișier evidențiat, acesta va fi procesat imediat, fără dialogul standard „Deschide”.

## Modificări pentru 5.6

*   **A fost adăugat motorul OCR „None (Extract Text Layer)”**: Utilizatorii pot extrage acum text direct din PDF-uri căutabile fără a folosi credite AI. Acest lucru îmbunătățește mult viteza și confidențialitatea pentru documentele bazate pe text.
*   **A fost rafinată acuratețea UI Explorer**: Promptul UI Explorer a fost îmbunătățit pentru a identifica mai bine tipurile de elemente, cum ar fi elementele de listă, și pentru a raporta corect stări precum „(Bifat)”, „(Selectat)” sau „(Extins)”, ignorând componentele de sistem Windows precum bara de activități și ceasul.
*   **Memento pentru configurare după instalare**: A fost adăugată o notificare după instalare pentru a ghida utilizatorii către meniul de setări, unde își pot configura cheile API și preferințele.

## Modificări pentru 5.5.2

*   **A fost remediată problema de tastare din AI Operator:** A fost rezolvată o eroare prin care litera „v” era tastată în loc să se lipească textul pe anumite sisteme. Remedierea rezolvă conflictele de sincronizare care apăreau când sistemul era foarte solicitat.
*   **Stabilitate îmbunătățită:** A fost adăugată gestionare robustă a erorilor pentru operațiile cu clipboardul, pentru a preveni blocarea add-on-ului când clipboardul sistemului este blocat temporar de alte aplicații.
*   **Optimizare de sincronizare:** Au fost ajustate întârzierile interne pentru evenimentele de tastatură, pentru fiabilitate mai mare pe sisteme cu viteze diferite și compatibilitate mai bună cu manageri de clipboard terți.

## Modificări pentru 5.5 (actualizarea pentru automatizare)

*   **AI Operator (control autonom, Shift+A):** Aceasta este funcția principală din v5.5. Vision Assistant Pro a trecut de la rolul de asistent pasiv la rolul de **AI Operator** personal. Nu descrie doar ecranul, ci execută comenzi.
    *   *Cum funcționează:* Acum poți da instrucțiuni verbale pentru a opera calculatorul. De exemplu, într-o aplicație complet inaccesibilă, unde cititorul tău de ecran nu spune nimic, poți apăsa **Shift+A** și poți tasta: *„Apasă butonul Setări”* sau *„Găsește câmpul de căutare, scrie 'Latest News' și apasă Enter.”* AI-ul identifică vizual elementele, mută mouse-ul și execută sarcina pentru tine.
    *   *Notă de performanță:* Această funcție este optimizată pentru **Gemini 3.0 Flash (Preview)** și oferă răspunsuri rapide și inteligente, capabile să gestioneze chiar și structuri UI complexe.
    *   **⚠️ Avertisment privind utilizarea API:** Pentru ca AI Operator să fie precis, trebuie să „vadă” exact ce se întâmplă, deci trimite o captură de ecran de înaltă rezoluție la fiecare pas. Folosirea frecventă va consuma cota API mult mai repede decât sarcinile standard bazate pe text.
*   **Visual UI Explorer (E):** Te-ai săturat să navighezi prin „butoane fără etichetă”? Apasă **E** pentru a activa UI Explorer. AI-ul va scana întreaga fereastră și va genera o listă cu fiecare element pe care îl poate apăsa, inclusiv pictograme, grafice și meniuri. Alegi un element din listă, iar AI Operator îl va apăsa pentru tine. Funcționează ca un strat accesibil peste orice aplicație.
*   **Acțiune inteligentă pentru fișiere, adaptată contextului (F):** Tasta „F” a fost refăcută complet. Nu mai presupune că vrei doar OCR. Când selectezi o singură imagine, acum îți cere intenția: poți alege o **descriere vizuală detaliată** pentru a înțelege scena sau o **extragere structurată a textului (OCR)** pentru citire. Meniul se adaptează dinamic în funcție de tipul de fișier și motorul AI activ.
*   **Optimizare de bază:** Am curățat în profunzime logica internă a add-on-ului, eliminând funcții vechi nefolosite și cod redundant. Rezultatul este o experiență mai rapidă și mai fiabilă pentru utilizatori.

## Modificări pentru 5.0

* **Arhitectură cu mai mulți furnizori**: A fost adăugat suport complet pentru **OpenAI**, **Groq** și **Mistral**, alături de Google Gemini. Utilizatorii pot alege acum backendul AI preferat.
* **Rutare avansată a modelelor**: Utilizatorii furnizorilor nativi, precum Gemini sau OpenAI, pot selecta acum modele specifice dintr-o listă derulantă pentru sarcini diferite (OCR, STT, TTS).
* **Configurare avansată a endpointurilor**: Utilizatorii furnizorului personalizat pot introduce manual URL-uri și nume de modele pentru control detaliat asupra serverelor locale sau terțe.
* **Vizibilitate inteligentă a funcțiilor**: Meniul de setări și interfața cititorului de documente ascund acum automat funcțiile neacceptate, cum ar fi TTS, în funcție de furnizorul selectat.
* **Preluare dinamică a modelelor**: Add-on-ul preia acum lista de modele disponibile direct din API-ul furnizorului, pentru compatibilitate cu modele noi imediat după lansare.
* **OCR și traducere hibridă**: A fost optimizată logica pentru a folosi Google Translate pentru viteză când este folosit Chrome OCR și traducere prin AI când sunt folosite motoarele Gemini/Groq/OpenAI.
* **„Rescanare cu AI” universală**: Funcția de rescanare din cititorul de documente nu mai este limitată la Gemini. Acum folosește furnizorul AI activ pentru a reprocesa paginile.

## Modificări pentru 4.6
* **Reafișare interactivă a rezultatului:** A fost adăugată tasta **Space** în stratul de comenzi, permițând utilizatorilor să redeschidă imediat ultimul răspuns AI într-o fereastră de chat pentru întrebări suplimentare, chiar și când modul „Ieșire directă” este activ.
* **Hub pentru comunitatea Telegram:** A fost adăugat un link „Canal Telegram oficial” în meniul Instrumente al NVDA, pentru acces rapid la cele mai recente noutăți, funcții și lansări.
* **Stabilitate îmbunătățită a răspunsurilor:** Logica principală pentru funcțiile de traducere, OCR și Vision a fost optimizată pentru performanță mai fiabilă și experiență mai fluidă când se folosește ieșirea vocală directă.
* **Ghidare îmbunătățită în interfață:** Descrierile din setări și documentația au fost actualizate pentru a explica mai bine noul sistem de reafișare și modul în care funcționează împreună cu setările pentru ieșire directă.

## Modificări pentru 4.5
* **Manager avansat de prompturi:** A fost introdus un dialog dedicat de administrare în setări, pentru personalizarea prompturilor de sistem implicite și gestionarea prompturilor definite de utilizator, cu suport complet pentru adăugare, editare, reordonare și previzualizare.
* **Suport proxy complet:** Au fost rezolvate problemele de conexiune la rețea prin aplicarea strictă a setărilor proxy configurate de utilizator pentru toate cererile API, inclusiv traducere, OCR și generare vocală.
* **Migrare automată a datelor:** A fost integrat un sistem inteligent de migrare, care actualizează automat configurațiile vechi ale prompturilor la un format JSON v2 robust la prima rulare, fără pierdere de date.
* **Compatibilitate actualizată (2025.1):** Versiunea minimă necesară de NVDA a fost setată la 2025.1, din cauza dependențelor de bibliotecă din funcții avansate precum cititorul de documente, pentru performanță stabilă.
* **Interfață de setări optimizată:** Interfața de setări a fost simplificată prin reorganizarea gestionării prompturilor într-un dialog separat, oferind o experiență mai curată și mai accesibilă.
* **Ghid pentru variabilele prompturilor:** A fost adăugat un ghid integrat în dialogurile de prompturi pentru a ajuta utilizatorii să identifice și să folosească ușor variabile dinamice precum [selection], [clipboard] și [screen_obj].

## Modificări pentru 4.0.3
*   **Rezistență îmbunătățită a rețelei:** A fost adăugat un mecanism automat de reîncercare pentru a gestiona mai bine conexiunile instabile la internet și erorile temporare de server, asigurând răspunsuri AI mai fiabile.
*   **Dialog vizual pentru traduceri:** A fost introdusă o fereastră dedicată pentru rezultatele traducerii. Utilizatorii pot naviga și citi ușor traduceri lungi linie cu linie, similar cu rezultatele OCR.
*   **Vizualizare formatată agregată:** Funcția „Vizualizare formatată” din cititorul de documente afișează acum toate paginile procesate într-o singură fereastră organizată, cu antete clare pentru pagini.
*   **Flux OCR optimizat:** Selectarea intervalului de pagini este omisă automat pentru documentele cu o singură pagină, făcând procesul de recunoaștere mai rapid.
*   **Stabilitate API îmbunătățită:** S-a trecut la o metodă mai robustă de autentificare bazată pe antete, rezolvând posibile erori „All API Keys failed” cauzate de conflicte la rotația cheilor.
*   **Remedieri de erori:** Au fost rezolvate mai multe blocări posibile, inclusiv o problemă la închiderea add-on-ului și o eroare de focalizare în dialogul de chat.

## Modificări pentru 4.0.1
*   **Cititor de documente avansat:** Un vizualizator nou pentru PDF și imagini, cu selectare a intervalului de pagini, procesare în fundal și navigare fluentă cu `Ctrl+PageUp/Down`.
*   **Submeniu nou în Instrumente:** A fost adăugat un submeniu dedicat „Vision Assistant” în meniul Instrumente al NVDA, pentru acces mai rapid la funcțiile principale, setări și documentație.
*   **Personalizare flexibilă:** Acum poți alege motorul OCR și vocea TTS preferate direct din panoul de setări.
*   **Suport pentru mai multe chei API:** A fost adăugat suport pentru mai multe chei API Gemini. Poți introduce o cheie pe linie sau le poți separa prin virgulă în setări.
*   **Motor OCR alternativ:** A fost introdus un motor OCR nou pentru a asigura recunoaștere fiabilă a textului chiar și când sunt atinse limitele de cotă Gemini API.
*   **Rotație inteligentă a cheilor API:** Comută automat la cea mai rapidă cheie API funcțională și o reține, pentru a evita limitele de cotă.
*   **Document în MP3/WAV:** A fost integrată capacitatea de a genera și salva fișiere audio de calitate înaltă în formatele MP3 (128kbps) și WAV direct în cititor.
*   **Suport pentru Instagram Stories:** A fost adăugată capacitatea de a descrie și analiza Instagram Stories folosind URL-urile lor.
*   **Suport TikTok:** A fost introdus suport pentru videoclipuri TikTok, permițând descriere vizuală completă și transcriere audio a clipurilor.
*   **Dialog de actualizare reproiectat:** Include o interfață accesibilă nouă, cu o casetă text derulabilă pentru citirea clară a modificărilor de versiune înainte de instalare.
*   **Stare și UX unificate:** Dialogurile de fișiere au fost standardizate în tot add-on-ul, iar comanda „L” a fost îmbunătățită pentru raportarea progresului în timp real.

## Modificări pentru 3.6.0
*   **Sistem de ajutor:** A fost adăugată o comandă de ajutor (`H`) în stratul de comenzi, pentru a oferi o listă ușor accesibilă cu toate scurtăturile și funcțiile lor.
*   **Analiză video online:** Suportul a fost extins pentru a include videoclipuri **Twitter (X)**. Detectarea URL-urilor și stabilitatea au fost îmbunătățite pentru o experiență mai fiabilă.
*   **Contribuție la proiect:** A fost adăugat un dialog opțional de donație pentru utilizatorii care vor să susțină actualizările viitoare și creșterea continuă a proiectului.

## Modificări pentru 3.5.0
\*   \*\*Strat de comenzi:\*\* A fost introdus un sistem de strat de comenzi, implicit `NVDA+Shift+V`, pentru a grupa scurtăturile sub o singură tastă principală. De exemplu, în loc să apeși `NVDA+Control+Shift+T` pentru traducere, acum apeși `NVDA+Shift+V`, apoi `T`.
\*   \*\*Analiză video online:\*\* A fost adăugată o funcție nouă pentru analiza videoclipurilor YouTube și Instagram direct prin introducerea unui URL.

## Modificări pentru 3.1.0
*   **Mod ieșire directă:** A fost adăugată o opțiune pentru a omite dialogul de chat și a auzi răspunsurile AI direct prin vorbire, pentru o experiență mai rapidă.
*   **Integrare cu clipboardul:** A fost adăugată o setare nouă pentru copierea automată a răspunsurilor AI în clipboard.

## Modificări pentru 3.0

*   **Limbi noi:** Au fost adăugate traduceri în **persană** și **vietnameză**.
*   **Modele AI extinse:** Lista de selectare a modelelor a fost reorganizată cu prefixe clare (`[Free]`, `[Pro]`, `[Auto]`), pentru a ajuta utilizatorii să distingă modelele gratuite de cele limitate prin rată sau plătite. A fost adăugat suport pentru **Gemini 3.0 Pro** și **Gemini 2.0 Flash Lite**.
*   **Stabilitate pentru dictare:** Stabilitatea dictării inteligente a fost îmbunătățită mult. A fost adăugată o verificare de siguranță care ignoră clipurile audio mai scurte de 1 secundă, prevenind halucinațiile AI și erorile goale.
*   **Gestionarea fișierelor:** A fost remediată o problemă prin care încărcarea fișierelor cu nume non-englezești eșua.
*   **Optimizarea prompturilor:** Logica de traducere și rezultatele Vision structurate au fost îmbunătățite.
## Modificări pentru 2.9

*   **Au fost adăugate traduceri în franceză și turcă.**
*   **Vizualizare formatată:** A fost adăugat un buton „Vizualizare formatată” în dialogurile de chat, pentru a vedea conversația cu stilizare corectă, cum ar fi titluri, bold și cod, într-o fereastră standard navigabilă.
*   **Setare Markdown:** A fost adăugată o opțiune nouă „Curăță Markdown în chat” în Setări. Debifarea acesteia permite utilizatorilor să vadă sintaxa Markdown brută, de exemplu `**` sau `#`, în fereastra de chat.
*   **Gestionarea dialogurilor:** A fost remediată o problemă prin care ferestrele „Rafinează textul” sau chat se deschideau de mai multe ori sau nu primeau focalizarea corect.
*   **Îmbunătățiri UX:** Titlurile dialogurilor de fișiere au fost standardizate la „Deschide” și au fost eliminate anunțurile vocale redundante, de exemplu „Se deschide meniul...”, pentru o experiență mai fluidă.

## Modificări pentru 2.8
* A fost adăugată traducerea în italiană.
* **Raportare stare:** A fost adăugată o comandă nouă (NVDA+Control+Shift+I) pentru anunțarea stării curente a add-on-ului, de exemplu „Se încarcă...” sau „Se analizează...”.
* **Export HTML:** Butonul „Salvează conținutul” din dialogurile de rezultat salvează acum ieșirea ca fișier HTML formatat, păstrând stiluri precum titluri și text bold.
* **Interfață de setări:** Aspectul panoului Setări a fost îmbunătățit cu grupare accesibilă.
* **Modele noi:** A fost adăugat suport pentru gemini-flash-latest și gemini-flash-lite-latest.
* **Limbi:** A fost adăugată nepaleza la limbile acceptate.
* **Logica meniului de rafinare:** A fost remediată o eroare critică prin care comenzile „Rafinează textul” eșuau dacă limba interfeței NVDA nu era engleza.
* **Dictare:** Detectarea tăcerii a fost îmbunătățită pentru a preveni ieșiri text incorecte când nu este detectată vorbire.
* **Setări de actualizare:** „Caută actualizări la pornire” este acum dezactivată implicit pentru respectarea politicilor Add-on Store.
* Curățare cod.

## Modificări pentru 2.7
* Structura proiectului a fost migrată la șablonul oficial NV Access Add-on Template, pentru conformitate mai bună cu standardele.
* A fost implementată logica de reîncercare automată pentru erori HTTP 429 (limită de rată), pentru fiabilitate în perioade cu trafic ridicat.
* Prompturile de traducere au fost optimizate pentru acuratețe mai mare și gestionare mai bună a logicii „Smart Swap”.
* Traducerea în rusă a fost actualizată.

## Modificări pentru 2.6
* A fost adăugat suport pentru traducerea în rusă, mulțumiri nvda-ru.
* Mesajele de eroare au fost actualizate pentru feedback mai descriptiv privind conectivitatea.
* Limba țintă implicită a fost schimbată în engleză.

## Modificări pentru 2.5
* A fost adăugată comanda nativă OCR pentru fișiere (NVDA+Control+Shift+F).
* A fost adăugat butonul „Salvează chatul” în dialogurile de rezultat.
* A fost implementat suport complet pentru localizare (i18n).
* Feedbackul audio a fost migrat la modulul nativ de tonuri al NVDA.
* S-a trecut la Gemini File API pentru gestionarea mai bună a fișierelor PDF și audio.
* A fost remediată blocarea la traducerea textului care conține acolade.

## Modificări pentru 2.1.1
* A fost remediată o problemă prin care variabila [file_ocr] nu funcționa corect în prompturile personalizate.

## Modificări pentru 2.1
* Toate scurtăturile au fost standardizate pentru a folosi NVDA+Control+Shift, pentru a elimina conflictele cu aspectul Laptop al NVDA și tastele rapide de sistem.

## Modificări pentru 2.0
* A fost implementat sistemul integrat de actualizare automată.
* A fost adăugat cache inteligent pentru traduceri, pentru recuperarea instantanee a textului tradus anterior.
* A fost adăugată memorie conversațională pentru rafinarea contextuală a rezultatelor în dialogurile de chat.
* A fost adăugată o comandă dedicată pentru traducerea clipboardului (NVDA+Control+Shift+Y).
* Prompturile AI au fost optimizate pentru a impune strict ieșirea în limba țintă.
* A fost remediată blocarea cauzată de caractere speciale în textul de intrare.

## Modificări pentru 1.5
* A fost adăugat suport pentru peste 20 de limbi noi.
* A fost implementat dialogul interactiv de rafinare pentru întrebări suplimentare.
* A fost adăugată funcția nativă de dictare inteligentă.
* A fost adăugată categoria „Vision Assistant” în dialogul Gesturi de intrare al NVDA.
* Au fost remediate blocările COMError în aplicații specifice precum Firefox și Word.
* A fost adăugat mecanismul automat de reîncercare pentru erori de server.

## Modificări pentru 1.0
* Lansare inițială.
