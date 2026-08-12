# KI Assistent pro Dokumentation

**KI Assistent pro** ist ein fortschrittlicher, multimodaler KI-Assistent für NVDA. Er nutzt erstklassige KI-Engines, um intelligentes Screenreading, Übersetzungen, Sprachdiktate und Dokumentenanalysen zu ermöglichen.

*Dieses Add-on wurde zu Ehren des Internationalen Tages der Menschen mit Behinderungen für die Community veröffentlicht.*

## 1. Einrichtung & Konfiguration

Gehen Sie zu **NVDA-Menü > Optionen > Einstellungen > KI Assistent pro**. Das Einstellungsfenster ist in 8 barrierefreie Reiter unterteilt: **Verbindung**, **KI-Verhalten**, **Übersetzungssprachen**, **Dokumentenleser**, **Video**, **CAPTCHA**, **Prompts** und **Erweitert**.

### 1.1 Verbindung Reiter

* **Anbieter:** Wählen Sie Ihren bevorzugten KI-Dienst. Unterstützte Anbieter sind **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** und **Benutzerdefiniert** (OpenAI-kompatible Server wie Ollama, LM Studio, Jan.ai oder KoboldCPP).


* **API-Schlüssel:** Erforderlich. Sie können mehrere Schlüssel eingeben (getrennt durch Kommas oder neue Zeilen), um eine automatische Rotation zu ermöglichen.


* **Modelle abrufen:** Nachdem Sie Ihren API-Schlüssel eingegeben haben, drücken Sie diese Schaltfläche, um die aktuelle Liste der verfügbaren Modelle vom Anbieter herunterzuladen.


* **KI-Modell:** Wählen Sie das Hauptmodell aus, das für den allgemeinen Chat und die Analysen verwendet werden soll.


* **Einstellungen für benutzerdefinierte Anbieter:** Konfigurieren Sie lokale oder benutzerdefinierte Endpunkte. Enthält **Lokale KI einrichten** (Ein-Klick-Konfiguration für Ollama, LM Studio, Jan.ai oder KoboldCPP) und die **Erweiterte Endpunkt-Konfiguration**.


* **Erweitertes Modell-Routing (Aufgabenspezifisch):** Wählen Sie optional spezifische Modelle aus Dropdown-Listen für OCR, STT, TTS, KI-Operator, Video und den Live-Assistenten.


* **Verbindungs- & Ausgabeoptionen:** Konfigurieren Sie Proxy-URL, Update-Prüfung beim Start, Bereinigtes Markdown im Chat, KI-Antworten in die Zwischenablage kopieren, Direkte Ausgabe (Kein Chat-Fenster) und Direkte Ausgabe für den Live-Assistenten.



### 1.2 KI-Verhalten Reiter

* **Kreativität (Temperatur):** Steuert die Zufälligkeit und Kreativität der KI (von 0.0 bis 2.0). Niedrigere Werte sind besser für genaue Übersetzungen/OCR.



### 1.3 Übersetzungssprachen Reiter

* **Quellsprache:** Wählen Sie Ihre Standard-Eingabesprache.


* **Zielsprache:** Wählen Sie Ihre primäre Übersetzungssprache.


* **KI-Antwortsprache:** Wählen Sie die Sprache für allgemeine KI-Antworten.


* **Smart Swap (Intelligenter Tausch):** Tauscht Quell- und Zielsprache automatisch basierend auf der erkannten Eingabe.



### 1.4 Dokumentenleser Reiter

* **OCR-Engine:** Wählen Sie zwischen **Chrome (Schnell)** für schnelle Ergebnisse oder **KI (Erweitert)** für eine überlegene Beibehaltung des Layouts.


* **OCR-Stapelgröße:** Geben Sie die Seiten pro Anfrage an (auf 0 setzen für Einzelanfragen-Verarbeitung).


* **Bilder inline beschreiben:** Schaltet die Beschreibung von Bildern direkt im Textfluss während der Textextraktion ein oder aus.


* **Seitenzahlen exportieren:** Schaltet Seitenzahlen und Trennlinien bei mehrseitigen Dokumenten ein oder aus.


* **TTS-Stimme:** Wählen Sie Ihren bevorzugten Stimmenstil für die Audioerzeugung.



### 1.5 Video Reiter

* **Video-Segmentgröße:** Dauer der Abschnitte in Minuten für die Erstellung von Audiobeschreibungen (auf 0 setzen, um die gesamte Datei auf einmal zu verarbeiten).


* **Charakterliste hinzufügen:** Option, das Charakter-Wörterbuch als ersten Untertiteleintrag einzufügen.


* **KI-Haftungsausschluss hinzufügen:** Option, einen Hinweis auf KI-Generierung am Anfang von SRT-Untertiteln einzufügen.



### 1.6 CAPTCHA Reiter

* **Visuellen CAPTCHA-Löser aktivieren:** Schaltet das automatische Lösen visueller Aufgaben (hCaptcha, reCAPTCHA) ein oder aus.


* **Text-CAPTCHA-Methode:** Wählen Sie zwischen der Erfassung des **Navigator-Objekts** oder des **Vollbilds**.



### 1.7 Prompts Reiter

* **Prompts verwalten:** Öffnet einen eigenen Dialog zum Anpassen von Standard-System-Prompts oder zum Erstellen, Bearbeiten, Sortieren und Testen benutzerdefinierter Prompts mit dynamischen Variablen (z. B. `[selection]`, `[screen_fg_obj]`).



### 1.8 Erweitert Reiter & Globales Logging

Navigieren Sie zum Reiter **Erweitert**, um das globale Logging des Add-ons zu konfigurieren:

* **Dedizierte Log-Datei aktivieren:** Schaltet die Protokollierung aller betrieblichen Ereignisse, API-Anfragen und Fehler über alle Module hinweg in eine separate Datei (`vision_assistant.log`) ein.


* **Log-Level:** Wählen Sie die Detailtiefe zwischen **Debug (Alle Details)**, **Info (General Information)**, **Warning (Nur Warnungen)** und **Error (Nur Fehler)**.


* **Logs aufbewahren für:** Legen Sie automatische Aufbewahrungsfristen fest, um ältere Log-Einträge automatisch zu bereinigen (von 1 Stunde bis 90 Tage).


* **Log-Verwaltung:** Nutzen Sie **Log-Datei öffnen**, **Log-Ordner öffnen** oder **Log-Datei löschen**, um Protokolldaten direkt zu überprüfen oder zu bereinigen, ohne NVDA neu zu starten oder reguläre NVDA-Protokolle zu beeinträchtigen.



---

## 2. Befehlsebene & Tastenkombinationen

Um Tastaturkonflikte zu vermeiden, verwendet dieses Add-on eine **Befehlsebene**.

1. Drücken Sie **NVDA + Umschalt + V** (Haupttaste), um die Ebene zu aktivieren (Sie hören einen Signalton).


2. Lassen Sie die Tasten los und drücken Sie dann eine der folgenden Einzeltasten:



| Taste | Funktion | Beschreibung |
| --- | --- | --- |
| **Umschalt+A** | **KI-Operator** | **Autonome Steuerung:** Weisen Sie die KI an, eine Aufgabe auf Ihrem Bildschirm auszuführen. Erneutes Drücken bricht die Aktion sofort ab.

 |
| **E** | **UI-Explorer** | **Interaktiver Klick:** Identifiziert und klickt auf UI-Elemente in jeder Anwendung. Beschriftungen können direkt hinzugefügt werden.

 |
| **T** | Intelligenter Übersetzer | Übersetzt Text unter dem Navigator-Objekt oder der Markierung.

 |
| **Umschalt+T** | Zwischenablage-Übersetzer | Übersetzt den aktuellen Inhalt der Zwischenablage.

 |
| **R** | Text-Optimierer | Zusammenfassen, Grammatik korrigieren, Erklären oder **Eigene Prompts**.

 |
| **V** | Objekt-Vision | Beschreibt das aktuelle Navigator-Objekt.

 |
| **O** | Vollbild-Vision | Analysiert das gesamte Bildschirmlayout und den Inhalt.

 |
| **Umschalt+V** | Videoanalyse | Analysiert lokale Videodateien oder Online-Videos von **YouTube**, **Instagram**, **TikTok** oder **Twitter (X)**.

 |
| **Strg+V** | Lokale Videoaufnahme | Nimmt ein lautloses Video Ihres Bildschirms auf und analysiert die Aktionen und das Layout.

 |
| **D** | Dokumentenleser | Fortgeschrittener Leser für PDF und Bilder mit Seitenbereichsauswahl.

 |
| **F** | **Smarte Datei-Aktion** | Kontextabhängige Erkennung aus ausgewählten Bild-, PDF- oder TIFF-Dateien.

 |
| **M** | Medien-Transkription & Synchronisation | Transkribiert oder synchronisiert Audio-/Videodateien (MP3, WAV, MP4 usw.) in Ihre Zielsprache.

 |
| **C** | CAPTCHA-Löser | Erfasst und löst visuelle sowie textbasierte CAPTCHAs.

 |
| **Umschalt+C** | Direkter Chat | Öffnet direkt ein Text-Chat-Fenster mit der KI ohne vorherige Bild- oder Dokumentauswahl.

 |
| **S** | Intelligentes Diktat | Wandelt Sprache in Text um. Drücken zum Starten, erneut drücken zum Stoppen/Einfügen.

 |
| **Strg+T** | Sprach-Übersetzung | Diktieren Sie Sprache, die sofort übersetzt und als Text eingefügt wird.

 |
| **Strg+L** | **Live-Assistent** | **Echtzeit-Copilot (nur Gemini):** Startet oder beendet ein Live-Sprach- und Bildschirmgespräch mit dem KI-Assistenten.

 |
| **I** | Statusbericht | Meldet den aktuellen Fortschritt (z. B. "Scannen...", "Bereit").

 |
| **L** | **Objekt beschriften** | **Semantische KI-Beschriftung:** Beschriftet das aktuell fokussierte Element/Symbol dauerhaft.

 |
| **Umschalt+L** | **Beschriftungen verwalten/scannen** | Öffnet den Beschriftungs-Manager (falls Beschriftungen existieren) oder scannt die App nach unbenannten Elementen.

 |
| **U** | Update-Prüfung | Prüft manuell auf GitHub nach der neuesten Version des Add-ons.

 |
| **Leertaste** | Letztes Ergebnis abrufen | Zeigt den vollständigen Verlauf der letzten KI-Antwort in einem Chat-Dialog zur Überprüfung an.

 |
| **H** | Befehlshilfe | Zeigt eine Liste aller verfügbaren Kürzel innerhalb der Befehlsebene an.

 |
| **Alt+S** | Einstellungen | Öffnet direkt den Einstellungsdialog von KI Assistent pro.

 |
| **Alt+Q** | Bericht über erschöpfte Kontingente | Meldet die Anzahl der Gemini-API-Schlüssel, die ihr tägliches Kontingent überschritten haben, für welches Modell dies gilt und deren genaue Zurücksetzungszeit.

 |
| **Alt+M** | Routing-Prüfung | Meldet die aktuell im erweiterten Modell-Routing ausgewählten KI-Modelle.

 |
| **Pfeil hoch / runter** | Schnelleinstellung Navigation | Wechselt zwischen den Schnelleinstellungskategorien (Anbieter, Modell etc.) direkt in der Befehlsebene.

 |
| **Pfeil links / rechts** | Schnelleinstellung ändern | Ändert den Wert der aktuell ausgewählten Schnelleinstellung mit sofortigem Sprachfeedback.

 |

### 2.1 Tastenkombinationen im Dokumentenleser (Innerhalb des Viewers)

* **Strg + BildAb:** Zur nächsten Seite wechseln.


* **Strg + BildAuf:** Zur vorherigen Seite wechseln.


* **Alt + A:** Öffnet einen Chat-Dialog, um Fragen zum Dokument zu stellen.


* **Alt + R:** Erzwingt einen **erneuten Scan mit KI** über Ihren aktiven Anbieter.


* **Alt + G:** Erzeugt und speichert eine hochwertige Audiodatei (WAV/MP3). *Ausgeblendet, wenn der Anbieter kein TTS unterstützt.*


* **Alt + S / Strg + S:** Speichert den extrahierten Text als TXT- oder HTML-Datei.



---

## 3. KI-Operator - Autonome Computersteuerung

Der **KI-Operator** macht aus dem KI Assistent pro von einem passiven Leser einen aktiven Assistenten, der in Ihrem Namen mit Ihrem Computer interagieren kann. Sie können ihn bitten, den Bildschirm zu beschreiben, Fragen zu dem zu beantworten, was er sieht, oder sogar die Kontrolle zu übernehmen – Knöpfe anklicken, Elemente ziehen, Text tippen und durch Anwendungen navigieren, indem Sie ganz normale Alltagssprache verwenden.

Der größte Vorteil? Es funktioniert perfekt in absolut unzugänglicher Software. Wenn Sie in einer benutzerdefinierten Anwendung, einer Remotedesktop-Verbindung oder auf einer Website feststecken, bei der Ihr Screenreader völlig stumm bleibt, stört das den Operator nicht. Da er den Bildschirm visuell „sieht“, kann er Elemente finden, lesen und mit ihnen interagieren, die keinerlei Barrierefreiheits-Labels besitzen.

### Wie es funktioniert

1. Drücken Sie **NVDA + Umschalt + V** und dann **Umschalt + A** (oder nutzen Sie die direkte Tastenkombination), um den KI-Operator-Dialog zu öffnen.


2. Tippen Sie in verständlicher Sprache ein, was Sie tun möchten (z. B. „Klicke auf die Schaltfläche Speichern“, „Was sagt die Fehlermeldung?“ oder „Benenne die Datei in endgueltig.pdf um“).


3. Die KI analysiert Ihren Bildschirm, identifiziert die relevanten Elemente und führt die Aktion aus oder liefert die Antwort. Wenn eine Aufgabe mehrere Schritte erfordert, arbeitet der Operator so lange weiter, bis sie abgeschlossen ist.


4. Drücken Sie jederzeit erneut **Umschalt + A**, um eine laufende Aktion sofort abzubrechen.



### Unterstützte Aktionen

Der Operator versteht eine Vielzahl von Befehlen:

* **Beschreiben & Antworten:** „Beschreibe das Bildschirmlayout“ oder „Was sagt die Fehlermeldung?“


* **Klicken:** „Klicke auf die Schaltfläche Speichern“


* **Rechtsklick:** „Mache einen Rechtsklick auf die Datei“


* **Doppelklick:** „Doppelklicke auf das Dokument“


* **Ziehen & Ablegen (Drag & Drop):** „Ziehe das Dokument in den Archiv-Ordner“


* **Tippen:** „Tippe 'Hallo Welt' in das Suchfeld“


* **Scrollen:** „Scrolle dreimal nach unten“


* **Tastendruck:** „Drücke Enter“, „Drücke Tab“, „Drücke Escape“


* **Mehrschrittige Aufgaben:** „Öffne den Datei-Explorer, suche den Bericht und benenne ihn in endgueltig.pdf um“



### Wichtige Hinweise

* **⚠️ Warnung zur API-Nutzung:** Da der Operator genau „sehen“ muss, was auf dem Bildschirm passiert, um präzise zu sein, sendet er bei jedem Schritt einen hochauflösenden Screenshot. Eine häufige Nutzung verbraucht Ihr API-Kontingent viel schneller als standardmäßige textbasierte Aufgaben.


* **Administrator-Anwendungen:** Wenn NVDA nicht mit Administratorrechten ausgeführt wird, kann der Operator möglicherweise nicht mit Fenstern interagieren, die erhöhte Rechte erfordern. Dies ist eine Sicherheitsbeschränkung von Windows, kein Fehler im Add-on.


* **Best Practices:** Um die besten Ergebnisse zu erzielen, geben Sie klare und spezifische Befehle. „Klicke auf die blaue Senden-Schaltfläche unten im Formular“ funktioniert fast immer besser als nur „Klicke auf die Schaltfläche“.



---

## 4. Videoanalyse & Audiobeschreibung

> **Hinweis:** Die Funktionen zur Videoanalyse und Audiobeschreibung werden ausschließlich durch den Anbieter **Google Gemini** unterstützt. Stellen Sie sicher, dass Ihr aktiver Anbieter in den Add-on-Einstellungen auf Google Gemini eingestellt ist.
> 
> 

KI Assistent pro führt leistungsstarke Videoverarbeitungsfunktionen ein, die speziell für blinde und sehbehinderte Benutzer entwickelt wurden. Es kann sowohl Online-Videos als auch lokale Bildschirmaufnahmen analysieren, um hochdetaillierte visuelle Beschreibungen zu liefern und professionelle Audiobeschreibungs-Skripte (SRT) zu erstellen.

### 4.1 Lokale Bildschirmaufnahme (Strg + V)

Wenn Sie auf ein stummes Video, eine Animation oder eine Anleitung auf Ihrem Bildschirm stoßen, können Sie diese direkt aufnehmen:

1. Drücken Sie **NVDA + Umschalt + V**, um die Befehlsebene zu aktivieren, und drücken Sie dann **Strg + V**.


2. Das Add-on nimmt Ihren Bildschirm geräuschlos im Hintergrund auf.


3. Drücken Sie erneut **Strg + V**, um die Aufnahme zu stoppen.


4. Die KI analysiert den aufgenommenen Videoabschnitt und liefert eine hochdetaillierte Beschreibung der Szene, des Layouts und der Aktionen.



### 4.2 Videoanalyse (Umschalt + V)

Sie können sowohl lokale Videodateien als auch Online-Videos analysieren. Wählen Sie einfach eine lokale Videodatei im Windows-Explorer aus oder kopieren Sie einen Online-Videolink in Ihre Zwischenablage. Sie können auch überall **Umschalt + V** drücken (z. B. in einem Media-Player), um einen Dialog zu öffnen, in dem Sie nach einer Videodatei suchen oder eine URL manuell einfügen können.

* **Unterstützte Online-Plattformen:** YouTube, Instagram, TikTok und Twitter (X).


* Die KI erkennt die lokale Datei oder URL automatisch, verarbeitet das Video und liefert eine umfassende visuelle Beschreibung und Audio-Zusammenfassung.



### 4.3 Erstellung von Audiobeschreibungen (SRT)

Für ein strukturierteres Erlebnis kann das Add-on professionelle Audiobeschreibungs-Skripte im Standard-SubRip-Format (SRT) generieren.

* **Smarte Pausen-Anpassung (Gap-Timing):** Die KI hört sich die Tonspur an und verankert ihre visuellen Beschreibungen gezielt in natürlichen Pausen und stillen Lücken, um Überschneidungen mit Dialogen intelligent zu minimieren.


* **Charakter-Verfolgung:** Die Engine führt vorab eine Analyse durch, um Personen anhand unveränderlicher Gesichtsmerkmale zu erkennen. Sie baut ein globales Wörterbuch auf, um Charaktere über verschiedene Szenen hinweg fehlerfrei zu verfolgen und zu benennen.


* **Wortgetreues Text-OCR:** Jeder Text, der auf dem Bildschirm erscheint (Schilder, Telefone, Abspanne), wird streng wortgetreu zitiert.


* **Nutzung:** Um die generierte Untertiteldatei anzuhören, legen Sie die `.srt`-Datei einfach in denselben Ordner wie Ihre Videodatei und geben Sie ihr exakt denselben Namen. Konfigurieren Sie dann Ihren Media-Player (z. B. VLC oder PotPlayer) so, dass der Untertiteltext während der Wiedergabe direkt an Ihren Screenreader oder Ihre TTS-Engine weitergeleitet wird.



### 4.4 Synchronisierte Audio-Sprachausgabe (MP3-Export)

Das Add-on geht über die Erstellung textbasierter SRT-Dateien hinaus und fungiert als vollständiges Werkzeug zur Erstellung von Audiobeschreibungen, indem es die Beschreibungen in Sprache synthetisiert und mit dem Video abmischt. Sie können nun **Gemini Live TTS** als Sprach-Engine wählen, um unbegrenzte und realistischere Beschreibungen ohne Längenbeschränkungen zu erzeugen. Beim Generieren einer MP3-Datei für lokale Videodateien stehen Ihnen mehrere Mischmodi zur Verfügung:

* **Standard-AD (Ton mischen):** Die Sprachbeschreibung wird direkt über den Originalton des Videos gelegt. Sie werden gefragt, ob Sie **Audio-Ducking** aktivieren möchten (wodurch die Lautstärke des Hintergrunds während der Beschreibungen abgesenkt wird), um eine klare Sprachausgabe zu gewährleisten.


* **Erweiterte AD (Ton pausieren):** Die Engine pausiert den Originalton des Videos während der Beschreibungen. So verpassen Sie weder ein Wort des Originaldialogs noch die KI-Sprachausgabe.


* **YouTube-Videos:** Bei YouTube-Quellen (die nicht lokal heruntergeladen werden) enthält der MP3-Export ausschließlich die synchronisierte KI-Stimme ohne den Hintergrundton des Videos.



---

## 5. Medien-Transkription & Synchronisation (M)

Das Modul zur Audio-Transkription wurde komplett überarbeitet und unterstützt nun sowohl Audio- als auch Videodateien (MP3, WAV, MP4, MKV etc.). Drücken Sie **M** in der Befehlsebene, um eine Mediendatei auszuwählen und eine von 3 Betriebsarten zu wählen:

1. **Transkribieren (Originalsprache):** Transkribiert die gesprochene Sprache präzise in ihrer Originalsprache.


2. **Transkribieren und Übersetzen (Zielsprache):** Transkribiert die Sprache und übersetzt sie in Ihre konfigurierte Zielsprache.


3. **Synchronisieren und Übersetzen (Zielsprache) *(nur Gemini)*:** Eine leistungsstarke neue Funktion, die Sprache transkribiert, übersetzt und mit der TTS-Engine des Add-ons eine neu eingesprochene Audio-Synchronfassung erzeugt.



---

## 6. Fortgeschrittener Dokumenten- & Bildleser

KI Assistent pro enthält einen hochoptimierten Dokumentenleser, der für mehrseitige PDFs, komplexe Bilder und sogar iPhone-HEIC-Formate entwickelt wurde.

### 6.1 Stapelverarbeitung & Fortsetzen

Sie müssen ein riesiges Dokument nicht auf einmal lesen. Geben Sie einen Seitenbereich ein (z. B. `1-20`), und die KI verarbeitet alle Seiten im Hintergrund. Wenn NVDA abstürzt oder Sie den Scan unterbrechen, merkt sich das Add-on Ihren Fortschritt und bietet an, genau dort **fortzufahren**, wo Sie aufgehört haben!

### 6.2 Smarte Datei-Aktion

Sie müssen das Dokument nicht immer zuerst öffnen. Markieren Sie im Windows-Explorer einfach eine PDF- oder Bilddatei und drücken Sie **D** (Dokumentenleser) oder **F** (Smarte Datei-Aktion) in der Befehlsebene. Das Add-on umgeht den Dateidialog sofort und beginnt direkt mit der Verarbeitung der markierten Datei.

### 6.3 Tastenkombinationen im Dokumenten-Viewer

Wenn das Fenster des Dokumentenlesers geöffnet ist, können Sie folgende Tastenkombinationen verwenden:

* **Strg + BildAb:** Zur nächsten Seite wechseln.


* **Strg + BildAuf:** Zur vorherigen Seite wechseln.


* **Alt + A:** Öffnet einen Chat-Dialog, um Fragen zum Dokument zu stellen.


* **Alt + R:** Erzwingt einen **erneuten Scan mit KI** über Ihren aktiven Anbieter.


* **Alt + G:** Erzeugt und speichert eine hochwertige Audiodatei (WAV/MP3). *Ausgeblendet, wenn der Anbieter kein TTS unterstützt.*


* **Alt + S / Strg + S:** Speichert den extrahierten Text als TXT- oder HTML-Datei.



---

## 7. Semantische KI-Beschriftung & UI-Explorer

Stecken Sie in einer Anwendung fest, in der überall nur „unbenannte Schaltfläche“ angesagt wird? Die semantische KI-Beschriftungs-Engine löst dieses Problem dauerhaft.

### 7.1 Permanente Objektbeschriftung (L)

Fokussieren Sie Ihren Screenreader auf eine unbenannte Grafik oder Schaltfläche und drücken Sie **L** in der Befehlsebene. Die KI schaut sich die Schaltfläche visuell an, ermittelt ihre Funktion und vergibt eine dauerhafte Beschriftung.
Im Gegensatz zu älteren Beschriftungswerkzeugen verwendet dieses Add-on ein fortschrittliches, hybrides „Objektsignatur-System“ (AutomationId/ControlID). Ihre benutzerdefinierten Beschriftungen überstehen das Ändern der Fenstergröße, Monitorwechsel und Anwendungs-Updates!

### 7.2 Vollständiger Anwendungs-Scan (Umschalt + L)

Drücken Sie **Umschalt + L**, um das gesamte aktive Fenster auf einmal zu scannen. Die KI findet alle unbeschrifteten Elemente und benennt sie intelligent in einem Rutsch. Sie können diese Beschriftungen später im integrierten Beschriftungs-Manager anzeigen, umbenennen oder im Stapel löschen.

### 7.3 UI-Explorer (E)

Möchten Sie mit einem Element interagieren, ohne manuell dorthin zu navigieren? Drücken Sie **E**, um den UI-Explorer zu aktivieren. Die KI scannt den Bildschirm und generiert eine barrierefreie Liste aller anklickbaren Elemente (und ignoriert dabei System-Rauschen wie die Taskleiste). Wählen Sie ein Element aus der Liste, und das Add-on klickt es sofort für Sie an. Zudem können Sie Elemente direkt aus der Liste heraus beschriften.

---

## 8. Live-Sprachassistent

Der Live-Assistent macht KI Assistent pro zu einem interaktiven Echtzeit-Copiloten.
*(Hinweis: Diese Funktion ist exklusiv für Google Gemini und Gemini-kompatible benutzerdefinierte Anbieter verfügbar)*.

* **Aktivierung:** Drücken Sie **Strg + L** in der Befehlsebene, um den Live-Assistenten-Dialog zu öffnen.


* **Echtzeit-Interaktion:** Sprechen Sie ganz natürlich durch Ihr Mikrofon. Die KI hört gleichzeitig auf Ihre Stimme und schaut auf Ihren aktiven Bildschirm. Sie können Fragen stellen wie „Was sehe ich hier?“ oder „Lies mir den dritten Absatz vor.“


* **Anpassung:** Direkt im Dialog können Sie den Sprachstil der KI ändern (z. B. Professionell, Freundlich, Aufgeweckt) und die „Denktiefe“ anpassen, um zu steuern, wie gründlich die KI vor einer Antwort nachdenkt.



---

## 9. Eigene Prompts & Variablen

Sie können Prompts unter **Einstellungen > Prompts > Prompts verwalten...** verwalten.

### Unterstützte Variablen

* `[selection]`: Aktuell markierter Text.


* `[clipboard]`: Inhalt der Zwischenablage.


* `[clipboard_image]`: Aktuell in der Zwischenablage befindliches Bild.


* `[screen_obj]`: Screenshot des Navigator-Objekts.


* `[screen_fg_obj]`: Screenshot des aktiven Vordergrundfensters.


* `[screen_full]`: Vollbild-Screenshot.


* `[file_ocr]`: Bild-/PDF-Datei für Textextraktion auswählen.


* `[file_read]`: Dokument zum Lesen auswählen (TXT, Code, PDF).


* `[file_audio]`: Audiodatei zur Analyse auswählen (MP3, WAV, OGG).


* `{target_lang}`: Aktuelle Zielsprache.


* `{source_lang}`: Aktuelle Quellsprache.


* `{response_lang}`: Aktuelle KI-Antwortsprache.


* `{swap_target}`: Ausweichsprache für die intelligente Übersetzung mit automatischem Tausch.


* `{swap_instruction}`: Anweisungsblock für die intelligente Übersetzung mit automatischem Tausch.



---

## 10. Praktische Anwendungsfälle (Welche Funktion soll ich nutzen?)

KI Assistent pro ist vollgepackt mit fortschrittlichen Werkzeugen. Hier sind einige häufige Szenarien, die Ihnen bei der Auswahl der richtigen Funktion helfen:

* **Szenario: Sie möchten das komplette Layout eines komplizierten Fensters oder einer unzugänglichen App verstehen.**
*Lösung:* Drücken Sie **O** (Vollbild-Vision). Die KI analysiert den gesamten Bildschirm und beschreibt genau, wo Elemente, Texte und Schaltflächen positioniert sind.


* **Szenario: Sie haben ein Bild auf einer Webseite oder eine unbeschriftete Grafik in einem Dokument gefunden.**
*Lösung:* Bewegen Sie Ihr Navigator-Objekt auf die Grafik und drücken Sie **V** (Objekt-Vision). Die KI beschreibt speziell, was dieses Bild enthält.


* **Szenario: Sie möchten einen Film oder Videoclip mit Audiobeschreibungen ansehen.**
*Lösung:* Drücken Sie **Umschalt + V** auf Ihrem Video und wählen Sie **„Audiobeschreibung generieren (SRT-Datei)“**. Wenn der Vorgang abgeschlossen ist, klicken Sie auf **„Synchronisierte Sprachausgabe generieren (MP3)“** und wählen Sie **„Erweiterte AD“**. Das Add-on erstellt eine Tonspur, die den Filmdialog intelligent pausiert, um die visuellen Szenen zu beschreiben.


* **Szenario: Sie stoßen auf eine App voller „unbenannter Schaltflächen“.**
*Lösung:* Drücken Sie **L**, um die spezifische Schaltfläche mithilfe von KI dauerhaft zu beschriften. Oder drücken Sie **Umschalt + L**, um das gesamte Fenster auf einmal zu scannen und zu beschriften. Wenn Sie nur schnell auf etwas klicken möchten, drücken Sie **E** (UI-Explorer), um eine Liste aller anklickbaren Elemente zu erhalten.


* **Szenario: Sie müssen ein unzugängliches CAPTCHA umgehen.**
*Lösung:* Drücken Sie **C** (CAPTCHA-Löser). Die KI erfasst das CAPTCHA automatisch, löst es und trägt die Antwort in das richtige Feld ein.


* **Szenario: Sie möchten ein langes, 50-seitiges PDF-Dokument lesen.**
*Lösung:* Drücken Sie **D** (Dokumentenleser), stellen Sie Ihren Anbieter auf Google Gemini ein und geben Sie den Seitenbereich `1-50` ein. Das Add-on extrahiert den Text im Hintergrund fehlerfrei.


* **Szenario: Sie sehen sich eine stumme Videoanleitung oder Animation auf Ihrem Bildschirm an.**
*Lösung:* Drücken Sie **Strg + V**, um die Aufnahme des Bildschirms zu starten. Lassen Sie die Anleitung laufen und drücken Sie dann erneut **Strg + V**. Die KI erklärt Ihnen genau, was gezeigt wurde.


* **Szenario: Sie stoßen auf unerwartete Fehler, API-Verbindungsabbrüche oder möchten lokale Server analysieren.**
*Lösung:* Gehen Sie zu **Einstellungen > Erweitert**, aktivieren Sie **"Dedizierte Log-Datei aktivieren"** und stellen Sie das **Log-Level** auf **"Debug"**. Führen Sie die Aktion erneut aus und klicken Sie auf **"Log-Datei öffnen"**, um technische Details einzusehen oder die Datei `vision_assistant.log` an ein Support-Ticket anzuhängen.



---

**Hinweis:** Für alle KI-Funktionen ist eine aktive Internetverbindung erforderlich. Mehrseitige Dokumente werden automatisch verarbeitet.

---

## 11. Support & Community

Bleiben Sie auf dem Laufenden über Neuigkeiten, Funktionen und Veröffentlichungen:

* **Telegram-Kanal:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)

* **GitHub Issues:** Für Fehlermeldungen und Funktionsanfragen.



### Fehlerbehebung & Protokolle melden

Wenn Sie ein Issue auf GitHub erstellen oder Support anfragen, geben Sie bitte Details zu Ihrem aktiven KI-Anbieter, Modell und der NVDA-Version an. Wenn Sie Verbindungsprobleme oder unerwartete Abstürze haben, aktivieren Sie die dedizierte Log-Datei unter **Einstellungen > Erweitert**, stellen Sie das Problem nach und hängen Sie Ihre `vision_assistant.log`-Datei an.

---

## 12. Projekt-Unterstützer

Ein herzliches Dankeschön an unsere Community-Mitglieder, die die kontinuierliche Entwicklung und Pflege dieses Projekts durch ihre großzügigen finanziellen Beiträge unterstützen:

* **@Alyabani94**

* **Ali Alamri**

* **Ilya**

* **Anonymer Unterstützer** (`UQDd...CnMY`)


* **leonardo0216**

* **Sergei Fleytin**

* **Suman Gayen**


*Wenn Sie das Projekt finanziell unterstützen und Ihren Namen hier sehen möchten, finden Sie die Option **Spenden** im NVDA-Werkzeuge-Menü (Untermenü KI-Assistent) oder während des Einrichtungsprozesses nach der Installation.*

---

## Änderungen für 06.08.2026

* **Beschriftung im UI-Explorer:** Elemente können nun direkt innerhalb des UI-Explorers beschriftet werden! Eine neue Schaltfläche "Beschriftung hinzufügen" wurde ergänzt, und das Fenster bleibt geöffnet, damit mehrere Objekte nacheinander barrierefrei beschriftet werden können.


* **Erweiterte Schnelleinstellungs-Ebene:** Die Befehlsebene (`NVDA+Umschalt+V`) bleibt nun aktiv und interaktiv! Sie können `Pfeil hoch/runter` nutzen, um zwischen Schnelleinstellungen (Anbieter, Modell, KI-Antwortsprache, TTS-Modell) zu navigieren, und `Pfeil links/rechts`, um Werte sofort mit Sprachausgabe zu ändern.


* **Direkter Chat (`Umschalt+C`):** Neuer Befehl in der Befehlsebene! Öffnet sofort ein sauberes, textbasiertes Chat-Fenster mit der KI, ohne dass ein Bild oder Dokument erforderlich ist.


* **Nahtloser Chat-Verlauf beim Abrufen:** Ein Fehler beim Abrufen der letzten KI-Antwort (`Leertaste`) wurde behoben. Das Add-on verfolgt den Konversationsverlauf nun global, sodass frühere Nachrichten und Folgefragen beim Abrufen vollständig wiederhergestellt werden.


* **Inline-Bildbeschreibungen bei OCR:** Optionale Funktion zur Beschreibung von Bildern direkt im OCR-Textfluss hinzugefügt. Dies kann in den Einstellungen, vor der Extraktion im Dokumentenleser oder spontan über die Schnelleinstellungs-Ebene umgeschaltet werden.


* **Sprach-Übersetzung (`Strg+T`):** Neues Feature zum Diktieren von Sprache, die mittels KI sofort übersetzt und direkt an der Cursorposition eingefügt wird.


* **Fortschrittsanzeige bei Updates & eSpeak-NG:** Der Download-Dialog für Add-on-Updates sowie eSpeak-NG zeigt nun den genauen Fortschritt in Prozent an.


* **Resilientes Stapel-OCR:** Behebt Unterbrechungen bei der Stapel-PDF-Verarbeitung; wenn ein API-Schlüssel sein Limit erreicht, wird automatisch zum nächsten Schlüssel gewechselt und der Scan fortgesetzt.


* **Visuelle CAPTCHA-Unterstützung:** Unterstützung für das automatische Lösen komplexer visueller Aufgaben wie hCaptcha und reCAPTCHA hinzugefügt.


* **Überarbeitung der Audio-Transkription:** Das Modul unterstützt nun Audio- und Videodateien und bietet 3 Modi: Transkribieren, Transkribieren & Übersetzen sowie eine neue Sprach-Synchronfassung ("Dub and Translate", exklusiv für Gemini).


* **Optionale Seitenzahlen im Dokumentenleser:** Neue Einstellung zum Ein- oder Ausblenden von Seitenzahlen und Trennlinien in exportierten Texten/HTML-Dateien sowie in der formatierten Ansicht.


* **Gemini Live TTS für Videobeschreibungen:** Gemini Live TTS kann nun als Stimme für synchronisierte Sprachausgaben (MP3) gewählt werden, um unbegrenzte und hochwertige Beschreibungen ohne Längenbeschränkung zu generieren.


* **Codebase-Modularisierung:** Das Add-on wurde von einer einzelnen Datei in eine modulare Architektur mit mehreren Dateien aufgeteilt.


* **Neugestaltung der Einstellungen:** Das Einstellungsfenster wurde auf ein modernes Layout mit Reitern umgestellt.


* **Globales & Dediziertes File-Logging:** Neues optionales Protokollierungssystem im Reiter "Erweitert" zur Aufzeichnung aller Aktionen in eine separate Datei (`vision_assistant.log`) mit konfigurierbaren Log-Levels und Aufbewahrungsfristen.


* **Gemini Upload-Fortschritt:** Echtzeit-Fortschrittsanzeigen in Prozent beim Hochladen großer Dateien (Video, Audio, Dokumente) zur Gemini API.



---

## Änderungen für 15.07.2026

* **Intelligente API-Modellfilterung:** Komplette Überarbeitung des Modellfilterungssystems hin zu einem reinen Blacklist-Ansatz anstelle von Whitelists. Es wurden stärkere Filter-Schlüsselwörter eingeführt (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`), um sicherzustellen, dass die Haupt-Chat-Modellauswahl sauber und zukunftssicher bleibt, während alle spezialisierten Modelle im erweiterten Routing-Bereich weiterhin verfügbar sind.


* **Durchsuchbares erweitertes Routing:** Alle Dropdown-Menüs im erweiterten Modell-Routing (OCR, STT, TTS, Operator, Video, Live) sowie die eSpeak-Variantenauswahl sind nun vollständig durchsuchbar. Sie können tippen, um das gewünschte Modell oder die Variante schnell zu filtern und zu finden.


* **Neue Tastenkombinationen in der Befehlsebene:**
* **Einstellungen (`Alt + S`):** Öffnet sofort den Einstellungsdialog von KI Assistent pro.


* **Bericht über erschöpfte Kontingente (`Alt + Q`):** Meldet die genaue Anzahl der Gemini-API-Schlüssel, die ihr tägliches Kontingent überschritten haben, identifiziert das betroffene Modell und sagt die genaue Zurücksetzungszeit an.


* **Routing-Prüfung (`Alt + M`):** Überprüft und meldet Ihre aktuelle Konfiguration des erweiterten Modell-Routings und liest vor, welche Modelle aktiv für spezialisierte Aufgaben ausgewählt sind (Standardeinstellungen werden übersprungen).




* **Komplette Überarbeitung der Videoanalyse:** Die Videoanalyse wurde von Grund auf transformiert! Zuvor bot sie nur eine einfache Beschreibung von Online-Videos. Jetzt ist sie eine umfassende Videoverarbeitungssuite, die speziell für blinde Nutzer entwickelt wurde:


* **Lokale Bildschirmaufnahme (`Strg+V`):** Sie können jetzt stumme Videos direkt von Ihrem Bildschirm aufnehmen. Die KI analysiert den aufgezeichneten Abschnitt und liefert eine hochdetaillierte Beschreibung der Szene, des Layouts und der Aktionen.


* **Erstellung von Audiobeschreibungen (SRT):** Das Add-on kann nun hochdetaillierte Audiobeschreibungs-Skripte (im Standard-SRT-Format) für Videos generieren, komplett mit intelligentem Gap-Timing zur Pausenerkennung und wortgetreuem OCR für Bildschirmtexte.


* **Synchronisierte Sprachausgabe (MP3-Export):** Neben textbasierten Untertiteln kann das Add-on die Audiobeschreibung in Sprache umwandeln, diese automatisch mit dem Originalton des Videos mischen, Audio-Ducking anwenden und das synchronisierte Ergebnis als MP3-Datei exportieren!


* **Smarte Video-Datei-Aktion:** Wenn Sie eine lokale Videodatei fokussieren und die Video-Tastenkombination drücken, erkennt das Add-on diese automatisch und verarbeitet die Datei direkt.


* **Fortgeschrittene Charakter-Verfolgung:** Die KI führt vorab eine Charakter-Erkennung durch. Sie erstellt ein globales Charakter-Wörterbuch und verfolgt Personen Abschnitt für Abschnitt fehlerfrei, ohne Identitäten zu verwechseln.


* **Konfiguration der Videoanalyse:** Neue Einstellungen zur Steuerung von SRT-Blockgrößen, Charakter-Untertiteln und Haftungsausschlüssen wurden hinzugefügt.


* **Erweitertes Modell-Routing:** Sie können nun explizit spezialisierte Videomodelle (`gemini_video_model`, `custom_video_model`) in den Einstellungen für das erweiterte Modell-Routing auswählen.




* **Smarte API-Kontingentverwaltung:** Verbesserte Handhabung von 429-Fehlern (Tägliches Limit) durch Modell-spezifische Erfassung. Wenn ein Schlüssel das Limit für ein bestimmtes Modell erreicht, wird er intelligent nur für dieses Modell gesperrt, bleibt aber für andere Modelle weiterhin einsatzbereit.



---

## Änderungen in 7.0.0

* **Fortsetzen nicht beendeter Scans:** Eine Fortsetzungsfunktion wurde sowohl für den Dokumentenleser als auch für die Smarten Datei-Aktionen hinzugefügt. Wenn ein Scan unterbrochen wird, können Sie nun an der Stelle weitermachen, an der er gestoppt wurde, anstatt von vorne beginnen zu müssen.


* **Neue Variable `[screen_fg_obj]`:** Eine neue Variable für eigene Prompts wurde hinzugefügt, um einen Screenshot ausschließlich des aktiven Vordergrundfensters anstelle des gesamten Bildschirms aufzunehmen.


* **Smarte Wiederholungen & Schlüsselrotation:** Das Add-on versucht nun bei temporären Serverüberlastungen (wie hoher Auslastung oder fehlerhaften Antworten) bis zu 5-mal unbemerkt eine Wiederholung mit demselben Schlüssel. Schlagen die Versuche fehl, wird automatisch zum nächsten API-Schlüssel in Ihrer Liste gewechselt.


* **Bildschirmvorhang-Erkennung:** Eine Prüfung wurde hinzugefügt, die verhindert, dass Screenshots aufgenommen werden, wenn der NVDA-Bildschirmvorhang aktiv ist (egal ob dauerhaft oder temporär über die Tastenkombination aktiviert). Das Add-on warnt Sie und bricht ab, um das Senden schwarzer Bilder und das Verschwenden von API-Tokens zu verhindern.


* **Verbesserungen im Dokumentenleser:** Der PDF-Seitenbereichsdialog wählt nun automatisch die in den Add-on-Einstellungen festgelegte Zielsprache vor. Zudem wurde die Thread-Verarbeitung optimiert, um sicherzustellen, dass Hintergrundaufgaben sauber beendet werden, wenn der Leser geschlossen wird.


* **Native Mistral OCR-Integration:** Die native Document OCR API von Mistral wurde integriert. Mehrseitige Dokumente werden automatisch zusammengeführt, hochgeladen und in Stapeln über den spezialisierten `/v1/ocr`-Endpunkt von Mistral verarbeitet, während einseitige Bilder ohne unnötige PDF-Konvertierung direkt verarbeitet werden.


* **Dynamische Handhabung benutzerdefinierter URLs:** Das Ändern der benutzerdefinierten API-URL löscht nun sofort die zwischengespeicherte Modellliste und stellt das manuelle Texteingabefeld für Modelle wieder her. Dies gewährleistet volle Kompatibilität mit benutzerdefinierten Endpunkten (wie Cloudflare AI Gateway), die den Standard-Endpunkt `/v1/models` nicht unterstützen.


* **Überarbeitete Eingabe-Engine für den KI-Operator:** Das zugrundeliegende Maus- und Tastatursimulationssystem für den KI-Operator wurde komplett neu geschrieben. Die veraltete `mouse_event`-API wurde durch die moderne Windows `SendInput`-API ersetzt, was eine deutlich höhere Kompatibilität mit modernen Anwendungen, benutzerkontengesteuerten Fenstern (UAC) und High-DPI-Displays mit sich bringt.


* **Stabile Drag & Drop-Aktionen:** Drag-and-Drop-Aktionen im KI-Operator laufen nun absolut stabil und zuverlässig. Die neue Engine nutzt natürliche Bewegungskurven, präzise Cursorpositionierung, optimiertes Timing und eine intelligente Anstups-Technik, um sicherzustellen, dass Windows und Anwendungen Drag-and-Drop-Gesten fehlerfrei erkennen.


* **Mehrere Monitore unterstützt:** Der KI-Operator unterstützt nun vollständig Setups mit mehreren Monitoren. Mausbewegungen und Klicks funktionieren über das `MOUSEEVENTF_VIRTUALDESK`-Flag korrekt auf allen Bildschirmen, was eine präzise Positionierung unabhängig vom Monitor der Zielanwendung garantiert.


* **Verbesserte Tastatursimulation:** Die Tastatureingabe wurde verbessert, um "Erweiterte Tasten" (wie Pfeiltasten, Pos1, Ende, BildAuf/Ab, Einfügen, Entf und F1-F12) vollständig zu unterstützen. Dies stellt sicher, dass Navigations- und Tastaturbefehle des KI-Operators in allen Anwendungen fehlerfrei funktionieren.


* **HEIC/HEIF-Bildunterstützung:** Native Unterstützung für iPhone-Fotoformate wurde hinzugefügt. Sie können nun `.heic`- und `.heif`-Dateien direkt für KI-Beschreibungen, OCR oder den Dokumentenleser auswählen, ohne sie vorher konvertieren zu müssen.



---

## Änderungen in 6.5.0

* **Live-Assistent:** Echtzeit-Sprach- und Bildschirmassistent hinzugefügt, der exklusiv für Google Gemini (oder Gemini-kompatible benutzerdefinierte Anbieter) verfügbar ist. Beinhaltet eine interaktive Anpassung von Stimme und Denktiefe direkt im Dialog, mit automatischer Wiederverbindung nach Einstellungsänderungen.


* **MiniMax KI-Anbieter:** MiniMax wurde als gleichwertiger Anbieter mit vollständiger multimodaler Unterstützung (Chat, Vision, OCR), benutzerdefiniertem TTS mit über 300+ dynamischen Stimmen und automatischem Entfernen von Denkblöcken (z. B. `<think>...</think>`) aus den Ausgaben integriert.


* **Übersetzung im Dokumentenleser:** Ein stiller Übersetzungsfehler für nicht-englische NVDA-Benutzer wurde behoben, indem sichergestellt wird, dass der standardmäßige zweistellige Sprachcode an Google Translate gesendet wird anstelle des lokalisierten Sprachnamens.


* **PDF-Stapelscan-Wiederholung:** Eine hochoptimierte, separate und stille Wiederholungslogik für das Scannen von PDF-Dokumentenstapeln wurde implementiert, um redundante Uploads zu vermeiden und störende Fehler-Popups während der Wiederholungen zu verhindern.


* **Status des Dokumentenlesers:** Ein Fehler wurde behoben, bei dem der Gesamtstatus des Plugins (überprüft mit `I`) während langer Dokumentenscans auf „Stapelverarbeitung gestartet“ hängen blieb.


* **Threading-Absturz behoben:** Ein schwerwiegender Thread-Assertion-Absturz (`IsMain() failed in wxTimerImpl`) beim Öffnen von Dokumenten aus einem Hintergrund-Thread wurde behoben, indem die GUI-Callback-Warteschlange auf `wx.CallAfter` umgestellt wurde.



---

## Änderungen in 6.1.2

* **Vorabprüfung auf doppelte Beschriftungen:** Ein Problem bei der Einzelbeschriftung wurde behoben, bei dem die Prüfung auf Duplikate alte Koordinatenschlüssel verwendete. Dies führte dazu, dass NVDA doppelte KI-Anfragen für bereits beschriftete Objekte stellte, anstatt die vorhandene Beschriftung anzusagen.


* **Dokumenten-Chat für Nicht-Gemini-Anbieter:** Eine strikte API-Schlüsselprüfung im Dokumenten-Chat (`on_ask`) wurde korrigiert, um sicherzustellen, dass Benutzer von OpenAI, Groq oder lokalen benutzerdefinierten Anbietern (wie Ollama) erfolgreich mit Dokumenten chatten können, ohne blockiert zu werden.


* **Schnelle Chrome-OCR-Übersetzung:** Die kostenlose, schlüssellose Übersetzungs-API für Chrome-OCR wurde wiederhergestellt. Das Übersetzen von extrahiertem Text umgeht nun Gemini-KI, was API-Kontingente spart und den Übersetzungsprozess beschleunigt.


* **Alphanumerischer Filter für CAPTCHAs:** Die Filterlogik im CAPTCHA-Löser wurde korrigiert, um sicherzustellen, dass nicht-alphanumerische Zeichen in allen Situationen ordnungsgemäß bereinigt werden.


* **Aktualisierung der Hilfe für die Befehlsebene:** Die Tastenkombination für die Statusansage im Hilfemenü wurde von `L` auf `I` korrigiert und beide Beschriftungsbefehle (`L` und `Umschalt+L`) wurden zur Liste hinzugefügt.



---

## Änderungen in 6.1.1

* **Korrektur der Denkausgabe bei Gemma 4:** Ein Problem mit Gemma 4-Modellen wurde behoben, bei dem der gesamte interne Denkprozess als endgültige Antwort angezeigt wurde oder das Deaktivieren des Denkens zu leeren Antworten führte. Das Add-on isoliert und extrahiert nun korrekt nur die finale, bereinigte Textantwort.


* **Stapel-OCR aus dem Datei-Explorer:** Sie können nun mehrere Fotos oder PDFs direkt im Windows Datei-Explorer auswählen und als Stapel Text extrahieren oder analysieren lassen. Das Add-on filtert und verarbeitet automatisch nur die unterstützten Dateiformate.



---

## Änderungen in 6.1.0

* **Universelle lokale KI-Integration (Lokale KI einrichten):** Eine neue Schaltfläche **"Lokale KI einrichten"** wurde in den Einstellungen für benutzerdefinierte Anbieter hinzugefügt. Benutzer können nun lokale KI-Engines wie **Ollama**, **LM Studio**, **Jan.ai** und **KoboldCPP** sofort automatisch konfigurieren.


* **Intelligenter lokaler Proxy-Bypass:** Die Verbindungslogik wurde mit einem fortschrittlichen Proxy-Bypass-Mechanismus neu aufgebaut. Das Add-on ist nun intelligent genug, um Windows-System-Proxys für lokale Loopback-Verbindungen vollständig zu umgehen, was stabile lokale KI-Verbindungen gewährleistet, selbst wenn Ihr VPN/TUN-Modus aktiv ist.


* **Ultra-stabile KI-Beschriftung (v2):** Absolute Bildschirmkoordinatenschlüssel wurden durch ein fortschrittliches, hybrides **Objektsignatur-System** ersetzt. Beschriftungen basieren nun auf programmgesteuerten Identifikatoren (UIA **AutomationId** oder Win32 **ControlID**) und fensterrelativen Koordinaten. Dadurch sind Ihre benutzerdefinierten Beschriftungen völlig resistent gegen das Ändern der Fenstergröße, Verschieben, Monitorwechsel oder Skalierungen.


* **Nahtlose automatische Beschriftungsmigration:** Das Upgrade erfolgt völlig transparent. Das Add-on migriert Ihre älteren, auf Legacy-Koordinaten basierenden Beschriftungen beim ersten Fokussieren automatisch im Hintergrund in das neue, stabile Fingerabdruckformat – ganz ohne Datenverlust.



---

## Änderungen in 6.0

* **Einführung der semantischen KI-Beschriftung:** Benutzer können nun unbenannte Schaltflächen und Symbole mithilfe von KI dauerhaft beschriften. Drücken Sie **L**, um das aktuelle Navigator-Objekt zu beschriften (unterstützt sowohl den Tab-Fokus als auch die Objektnavigation), oder **Umschalt+L**, um die gesamte Anwendung auf einmal zu scannen und zu beschriften.


* **Intelligente Beschriftungsverwaltung:** Ein neuer, vollständig barrierefreier Beschriftungs-Manager-Dialog wurde hinzugefügt (erreichbar über **Umschalt+L**, falls Beschriftungen existieren), um benutzerdefinierte Beschriftungen anzuzeigen, umzubenennen oder im Stapel zu löschen.


* **Direkte Dateianalyse (Dateidialog umgehen):** Das Add-on ist nun intelligent genug, um zu erkennen, ob Sie gerade eine PDF- oder Bilddatei im Windows Datei-Explorer fokussieren. Das Drücken von **F (Smarte Datei-Aktion)** oder **D (Dokumentenleser)** auf einer markierten Datei verarbeitet diese sofort und umgeht den Standard-"Öffnen"-Dialog komplett.



---

## Änderungen in 5.6

* **OCR-Engine "Keine (Textschicht extrahieren)" hinzugefügt:** Benutzer können nun Text direkt aus durchsuchbaren PDFs extrahieren, ohne KI-Guthaben zu verbrauchen, was die Geschwindigkeit und den Datenschutz bei textbasierten Dokumenten erheblich verbessert.


* **Verfeinerte UI-Explorer-Genauigkeit:** Die UI-Explorer-Eingabeaufforderung wurde verbessert, um Elementtypen (wie Listeneinträge) besser zu identifizieren und Zustände wie „(Aktiviert)“, „(Ausgewählt)“ oder „(Erweitert)“ korrekt zu melden, während Windows-Systemkomponenten wie die Taskleiste und die Uhr ignoriert werden.


* **Installations-Einrichtungshinweis:** Nach der Installation wurde eine Benachrichtigung hinzugefügt, um Benutzer zum Einstellungsmenü zu führen, damit sie ihre API-Schlüssel und Präferenzen konfigurieren können.



---

## Änderungen in 5.5.2

* **Problem beim Tippen des KI-Operators behoben:** Ein Fehler wurde behoben, bei dem auf bestimmten Systemen der Buchstabe 'v' getippt wurde, anstatt Text einzufügen. Diese Korrektur behebt Timing-Konflikte, die bei hoher Systemlast auftraten.


* **Erhöhte Stabilität:** Es wurde eine robuste Fehlerbehandlung für Zwischenablage-Operationen hinzugefügt, um Abstürze des Add-ons zu verhindern, wenn die Systemzwischenablage vorübergehend durch andere Anwendungen gesperrt ist.


* **Timing-Optimierung:** Interne Verzögerungen für Tastaturereignisse wurden angepasst, um eine höhere Zuverlässigkeit bei unterschiedlichen Systemgeschwindigkeiten und eine bessere Kompatibilität mit Zwischenablage-Managern von Drittanbietern zu gewährleisten.



---

## Änderungen in 5.5 (Das Automatisierungs-Update)

* **KI-Operator (Autonome Steuerung - Umschalt+A):** Dies ist das Herzstück von v5.5. KI Assistent pro hat sich von einem passiven Assistenten zu Ihrem persönlichen **KI-Operator** weiterentwickelt. Er beschreibt nicht mehr nur den Bildschirm – er übernimmt das Kommando.


* *Wie es funktioniert:* Sie können jetzt sprachliche oder schriftliche Anweisungen geben, um Ihren PC zu steuern. In einer völlig unzugänglichen Anwendung, in der Ihr Screenreader stumm bleibt, können Sie beispielsweise **Umschalt+A** drücken und eingeben: *„Klicke auf die Schaltfläche Einstellungen“* oder *„Suche das Suchfeld, tippe 'Aktuelle Nachrichten' ein und drücke Enter.“* Die KI identifiziert die Elemente visuell, bewegt die Maus und führt die Aufgabe für Sie aus.


* *Leistungshinweis:* Diese Funktion ist für **Gemini 3.0 Flash (Preview)** optimiert und liefert unglaublich schnelle und intelligente Antworten, die selbst mit komplexesten UI-Layouts umgehen können.


* **⚠️ Warnung zur API-Nutzung:** Da der KI-Operator genau „sehen“ muss, was passiert, um präzise zu sein, sendet er bei jedem Schritt einen hochauflösenden Screenshot. Bitte beachten Sie, dass eine häufige Nutzung Ihr API-Kontingent viel schneller verbraucht als standardmäßige textbasierte Aufgaben.




* **Visueller UI-Explorer (E):** Müde davon, durch „unbenannte Schaltflächen“ zu navigieren? Drücken Sie **E**, um den UI-Explorer zu aktivieren. Die KI scannt das gesamte Fenster und erstellt eine Liste aller anklickbaren Elemente, die sie sieht – einschließlich Symbolen, Grafiken und Menüs. Wählen Sie einfach ein Element aus der Liste aus, und der KI-Operator klickt es für Sie an. Es ist wie eine „barrierefreie Schicht“ über jeder App.


* **Kontextabhängige smarte Datei-Aktion (F):** Die Taste „F“ wurde komplett überarbeitet. Sie geht nicht mehr pauschal davon aus, dass Sie nur OCR möchten. Wenn Sie eine einzelne Bilddatei auswählen, fragt sie nun intelligent nach Ihrer Absicht: Sie können eine **Detaillierte visuelle Beschreibung** wählen, um die Szene zu verstehen, oder eine **Strukturierte Textextraktion (OCR)** zum Lesen. Das Menü passt sich dynamisch an den Dateityp und Ihre aktive KI-Engine an.


* **Kernoptimierung:** Wir haben die interne Logik des Add-ons gründlich bereinigt, ungenutzte Legacy-Funktionen und redundanten Code entfernt. Dies führt zu einer schlankeren, schnelleren und zuverlässigeren Benutzererfahrung für alle.



---

## Änderungen in 5.0

* **Multi-Anbieter-Architektur**: Volle Unterstützung für **OpenAI**, **Groq** und **Mistral** neben Google Gemini hinzugefügt. Benutzer können nun ihr bevorzugtes KI-Backend wählen.


* **Erweitertes Modell-Routing**: Benutzer nativer Anbieter (Gemini, OpenAI etc.) können nun spezifische Modelle für verschiedene Aufgaben (OCR, STT, TTS) aus einer Liste wählen.


* **Erweiterte Endpunkt-Konfiguration**: Benutzerdefinierte Anbieter können URLs und Modellnamen manuell eingeben, um die volle Kontrolle über lokale oder Drittanbieter-Server zu haben.


* **Intelligente Sichtbarkeit von Funktionen**: Das Einstellungsmenü und die Benutzeroberfläche des Dokumentenlesers blenden nicht unterstützte Funktionen (wie TTS) basierend auf dem gewählten Anbieter automatisch aus.


* **Dynamisches Abrufen von Modellen**: Das Add-on ruft die Liste der verfügbaren Modelle nun direkt über die API des Anbieters ab, um Kompatibilität mit neuen Modellen sofort nach deren Erscheinen sicherzustellen.


* **Hybrid-OCR & Übersetzung**: Die Logik wurde optimiert, um Google Translate für Geschwindigkeit bei Chrome-OCR zu nutzen und KI-basierte Übersetzung bei Gemini/Groq/OpenAI-Engines zu verwenden.


* **Universelles "Erneuter Scan mit KI"**: Die Re-Scan-Funktion des Dokumentenlesers ist nicht mehr auf Gemini beschränkt. Sie nutzt nun den jeweils aktiven KI-Anbieter zur Neuverarbeitung von Seiten.



---

## Änderungen in 4.6

* **Interaktives Abrufen von Ergebnissen:** Die **Leertaste** wurde zur Befehlsebene hinzugefügt, wodurch Benutzer die letzte KI-Antwort sofort in einem Chat-Fenster für Folgefragen öffnen können, auch wenn der Modus "Direkte Ausgabe" aktiv ist.


* **Telegram Community-Hub:** Link zum "Offiziellen Telegram-Kanal" im NVDA-Werkzeuge-Menü hinzugefügt.


* **Erhöhte Antwortstabilität:** Kernlogik für Übersetzung, OCR und Vision optimiert, um eine zuverlässigere Leistung bei direkter Sprachausgabe zu gewährleisten.


* **Verbesserte Benutzerführung:** Beschreibungen in den Einstellungen aktualisiert, um das neue Abrufsystem besser zu erklären.



---

## Änderungen in 4.5

* **Erweiterter Prompt-Manager:** Separater Verwaltungsdialog in den Einstellungen zum Anpassen von System-Prompts und Verwalten benutzerdefinierter Prompts (Hinzufügen, Bearbeiten, Sortieren, Vorschau).


* **Umfassende Proxy-Unterstützung:** Sichergestellt, dass Proxy-Einstellungen strikt auf alle API-Anfragen angewendet werden.


* **Automatisierte Datenmigration:** System zur automatischen Aktualisierung alter Prompt-Konfigurationen auf das v2 JSON-Format beim ersten Start.


* **Aktualisierte Kompatibilität (2025.1):** Erforderliche Mindestversion von NVDA auf 2025.1 gesetzt.


* **Optimierte Benutzeroberfläche:** Bereinigung der Einstellungen durch Auslagerung der Prompt-Verwaltung in einen eigenen Dialog.


* **Leitfaden für Prompt-Variablen:** Integrierter Leitfaden in den Prompt-Dialogen zur Verwendung von Variablen wie [selection], [clipboard] und [screen_obj].



---

## Änderungen in 4.0.3

* **Verbesserte Netzwerk-Resilienz:** Automatischer Wiederholungsmechanismus bei instabilen Verbindungen hinzugefügt.


* **Visueller Übersetzungsdialog:** Neues Fenster für Übersetzungsergebnisse, das zeilenweises Lesen langer Texte ermöglicht.


* **Aggregierte formatierte Ansicht:** Die Funktion "Formatiert anzeigen" im Dokumentenleser zeigt nun alle verarbeiteten Seiten in einem einzigen, organisierten Fenster an.


* **Optimierter OCR-Workflow:** Überspringt die Seitenbereichsauswahl bei einseitigen Dokumenten automatisch.


* **Verbesserte API-Stabilität:** Umstellung auf Header-basierte Authentifizierung zur Vermeidung von Fehlern bei der Schlüsselrotation.



---

## Änderungen in 4.0.1

* **Fortgeschrittener Dokumentenleser:** Neuer Viewer für PDF und Bilder mit Seitenbereichsauswahl und Hintergrundverarbeitung.


* **Neues Werkzeuge-Untermenü:** Untermenü "KI Assistent" unter NVDA-Werkzeuge für schnelleren Zugriff hinzugefügt.


* **Flexible Anpassung:** OCR-Engine und TTS-Stimme direkt in den Einstellungen wählbar.


* **Unterstützung mehrerer API-Schlüssel:** Unterstützung für mehrere Gemini-Schlüssel (einer pro Zeile oder durch Komma getrennt).


* **Alternative OCR-Engine:** Neue Engine zur Texterkennung hinzugefügt, falls das Gemini-Kontingent erschöpft ist.


* **Dokument zu MP3/WAV:** Fähigkeit zur Erzeugung hochwertiger Audiodateien direkt im Reader integriert.


* **Instagram Stories & TikTok Support:** Analyse von Stories und TikTok-Videos über deren URLs hinzugefügt.



---

## Änderungen in 3.6.0

* **Hilfesystem:** Hilfe-Befehl (`H`) innerhalb der Befehlsebene hinzugefügt.


* **Online-Videoanalyse:** Unterstützung für **Twitter (X)** Videos hinzugefügt sowie URL-Erkennung verbessert.



---

## Änderungen in 3.5.0

* **Befehlsebene:** Einführung der Befehlsebene (Standard: `NVDA+Umschalt+V`), um Kürzel unter einer Haupttaste zu gruppieren.


* **Online-Videoanalyse:** Neue Funktion zur Analyse von YouTube- und Instagram-Videos per URL.



---

## Änderungen in 3.1.0

* **Direkter Ausgabemodus:** Option zum Überspringen des Chat-Dialogs, um KI-Antworten sofort per Sprache zu hören.


* **Zwischenablage-Integration:** Einstellung zum automatischen Kopieren von KI-Antworten in die Zwischenablage.



---

## Änderungen in 3.0

* **Neue Sprachen:** Persisch und Vietnamesisch hinzugefügt.


* **Erweiterte KI-Modelle:** Modellliste mit Präfixen (`[Free]`, `[Pro]`, `[Auto]`) neu organisiert. Unterstützung für **Gemini 3.0 Pro** und **Gemini 2.0 Flash Lite**.


* **Diktat-Stabilität:** Ignoriert nun Audioclips unter 1 Sekunde, um Halluzinationen zu vermeiden.


* **Dateihandhabung:** Fehler beim Hochladen von Dateien mit nicht-englischen Namen behoben.



---

## Änderungen in 2.9

* **Französische und türkische Übersetzungen hinzugefügt.**

* **Formatierte Ansicht:** Schaltfläche "Formatiert anzeigen" in Chat-Dialogen hinzugefügt (Überschriften, Fettdruck, Code).


* **Markdown-Einstellung:** Option "Bereinigtes Markdown im Chat" hinzugefügt.



---

## Änderungen in 2.8

* Italienische Übersetzung hinzugefügt.


* **Statusbericht:** Neuer Befehl (NVDA+Strg+Umschalt+I) zum Ansagen des aktuellen Status.


* **HTML-Export:** Speichern-Schaltfläche exportiert nun als formatiertes HTML.


* **Sprachen:** Nepali hinzugefügt.



---

## Änderungen in 2.7

* Projektstruktur auf die offizielle NV Access Vorlage migriert.


* Automatisches Retry bei HTTP 429 (Rate Limit) Fehlern.


* Optimierte Übersetzungs-Prompts.



---

## Änderungen in 2.6

* Russische Übersetzung hinzugefügt.


* Standard-Zielsprache auf Englisch geändert.



---

## Änderungen in 2.5

* Native Datei-OCR (NVDA+Strg+Umschalt+F) hinzugefügt.


* "Chat speichern" Schaltfläche hinzugefügt.


* Umstellung auf Gemini File API für bessere PDF- und Audio-Handhabung.



---

## Änderungen in 2.1

* Standardisierung aller Kürzel auf NVDA+Strg+Umschalt, um Konflikte mit dem Laptop-Layout zu vermeiden.



---

## Änderungen in 2.0

* Integriertes Auto-Update-System.


* Intelligenter Übersetzungscache hinzugefügt.


* Konversationsgedächtnis für Kontext im Chat hinzugefügt.


* Separater Befehl für Zwischenablage-Übersetzung (NVDA+Strg+Umschalt+Y).



---

## Änderungen in 1.5

* Unterstützung für über 20 neue Sprachen.


* Interaktiver Optimierungs-Dialog für Folgefragen.


* Native "Intelligentes Diktat" Funktion.



---

## Änderungen in 1.0

* Erstveröffentlichung.



---

## Übersetzung

* Übersetzt von **BFW Würzburg** im Rahmen des Projekts "NVDA Nachhaltig"