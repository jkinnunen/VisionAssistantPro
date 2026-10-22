# Documentation de Vision Assistant Pro

<!-- DOWNLOAD_COUNT_START --> Total des téléchargements : 75 681 <!-- DOWNLOAD_COUNT_END -->

**Vision Assistant Pro** est un assistant IA multimodal et avancé pour NVDA. Il exploite des moteurs d'IA de classe mondiale pour fournir une lecture d'écran intelligente, de la traduction, de la dictée vocale et de l'analyse de documents.

_Cet add-on a été publié pour la communauté en l'honneur de la Journée internationale des personnes handicapées._

## 1. Configuration et installation

Allez dans **Menu NVDA > Préférences > Paramètres > Vision Assistant Pro**. La boîte de dialogue des paramètres est organisée en 9 onglets accessibles : **Connexion**, **Assistant en direct**, **Comportement de l'IA**, **Langues de traduction**, **Lecteur de documents**, **Vidéo**, **CAPTCHA**, **Prompts** (Invites) et **Avancé**.

### 1.1 Onglet Connexion

- **Fournisseur :** Sélectionnez votre service d'IA préféré. Les fournisseurs pris en charge incluent **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** et **Personnalisé** (serveurs compatibles OpenAI tels que Ollama, LM Studio, Jan.ai ou KoboldCPP).
- **Clé API :** Saisissez une ou plusieurs clés API (séparées par des virgules ou des retours à la ligne) pour une rotation automatique.
- **Récupérer les modèles :** Appuyez sur ce bouton après avoir saisi votre clé API pour télécharger la dernière liste des modèles disponibles auprès du fournisseur.
- **Modèle d'IA :** Sélectionnez le modèle principal utilisé pour le chat général et l'analyse.
- **Routage de modèle avancé (spécifique aux tâches) :** Sélectionnez éventuellement des modèles dédiés à partir de listes déroulantes pour les tâches d'OCR, de STT (reconnaissance vocale), de TTS (synthèse vocale), d'opérateur d'IA, de vidéo et d'assistant en direct. Pour Gemini, les modèles sont catégorisés dynamiquement par capacité sans encombrement.
- **Paramètres du fournisseur personnalisé :** Configurez des points de terminaison locaux ou personnalisés. Comprend l'option **Configurer l'IA locale** (configuration en un clic pour Ollama, LM Studio, Jan.ai ou KoboldCPP) et **Configuration avancée du point de terminaison**.
- **Configuration du proxy :** Prise en charge complète du tunneling et de la redirection de points de terminaison dans l'ensemble de l'add-on (y compris l'assistant en direct, l'observateur ambiant et la synthèse vocale). Saisissez votre **URL de proxy** et sélectionnez votre **Mode de proxy** :
  - **Détection automatique :** Détecte automatiquement si l'URL est un proxy direct ou un proxy inverse.
  - **Proxy SOCKS5 :** Force le tunneling direct via SOCKS5 avec authentification par nom d'utilisateur/mot de passe RFC 1929 et résolution de noms de domaine.
  - **Proxy HTTP :** Force le tunneling direct via un proxy HTTP avec authentification de base.
  - **Proxy inverse :** Remplacement direct du point de terminaison pour les passerelles d'IA personnalisées et les miroirs auto-hébergés (les identifiants sont désactivés dans ce mode).
- **Tester la connexion au proxy :** Un bouton non bloquant qui teste la connectivité et mesure la latence du serveur en millisecondes (annoncée vocalement par NVDA).
- **Options de connexion et de sortie :** Configurez la vérification des mises à jour au démarrage, le nettoyage du code Markdown dans le chat, la copie des réponses de l'IA dans le presse-papiers et la sortie directe (sans fenêtre de chat).
- **Enregistrer les chats dans l'historique :** Conservez vos conversations de chat dans la liste de l'historique.

### 1.2 Onglet Assistant en direct

- **Assistant en direct : Sortie directe (sans fenêtre) :** Démarrez l'assistant en direct sans sa fenêtre de conversation ; ouvrez-la ultérieurement avec la touche de rappel du dernier résultat (`Espace`).
- **Fonction Pousser pour parler (Push to Talk) :** Active ou désactive le mode « Pousser pour parler ». Lorsqu'il est activé, votre microphone n'envoie de l'audio que lorsque vous maintenez la touche assignée enfoncée.
- **Touche Pousser pour parler :** Appuyez sur les touches pour enregistrer le raccourci (par exemple `F12` ou `Ctrl+F12`) — vous pouvez même assigner un modificateur seul comme `Ctrl Gauche`. Maintenez la touche enfoncée pour parler et relâchez-la pour terminer ; un bref signal sonore confirme chaque pression et relâchement.

Remarque : Cet onglet n'apparaît que lorsque **Google Gemini** (ou un fournisseur personnalisé compatible Gemini) est votre fournisseur actif.

### 1.3 Onglet Comportement de l'IA

- **Créativité (Température) :** Contrôle l'aléa et la créativité de l'IA (de 0,0 à 2,0). Des valeurs plus faibles produisent des résultats de traduction et d'OCR plus déterministes et précis.

### 1.4 Onglet Langues de traduction

- **Langue source :** Sélectionnez votre langue d'entrée par défaut.
- **Langue cible :** Sélectionnez votre principale langue de traduction cible.
- **Langue de réponse de l'IA :** Sélectionnez la langue pour les réponses générales de l'IA.
- **Inversion intelligente :** Inverse automatiquement les langues source et cible en fonction de l'entrée détectée.

### 1.5 Onglet Lecteur de documents

- **Moteur OCR :** Choisissez entre **Chrome (Rapide)** pour des résultats rapides ou **IA (Avancé)** pour une préservation supérieure de la mise en page.
- **Taille de lot OCR :** Spécifiez le nombre de pages par requête (définissez sur 0 pour un traitement en une seule requête).
- **Décrire les images en ligne :** Active ou désactive les descriptions d'images en ligne lors de l'extraction de texte de documents.
- **Exporter les numéros de page :** Active ou désactive les numéros de page et les séparateurs dans les sorties de documents multipages.
- **Voix TTS :** Sélectionnez le style de voix par défaut pour la génération audio.
- **Enregistrer les documents dans l'historique :** Conservez les documents ouverts dans la liste de l'historique ; le texte OCR mis en cache et les données de reprise sont toujours enregistrés.

### 1.6 Onglet Vidéo

- **Taille de segment vidéo :** Durée du segment en minutes pour la génération d'audiodescription (définissez sur 0 pour traiter le fichier entier).
- **Ajouter une liste de personnages :** Option pour ajouter le dictionnaire des personnages comme première entrée de sous-titre.
- **Ajouter un avertissement d'IA :** Option pour insérer un avertissement d'IA au début des sous-titres SRT de la vidéo.
- **Gestion du dictionnaire de personnages et des séries :** Ajoutez, modifiez, importez ou gérez les noms de personnages, les descriptions physiques et les rôles par série — l'IA associe automatiquement les personnages découverts à votre dictionnaire et fusionne les nouveaux à mesure que vous analysez d'autres épisodes. Vos notes manuelles sont toujours préservées avec priorité sur les mises à jour de l'IA, tandis que les descriptions physiques restent à jour d'un épisode à l'autre.

### 1.7 Onglet CAPTCHA

- **Activer le solveur de CAPTCHA visuel :** Active ou désactive la résolution automatisée de défis visuels (hCaptcha, reCAPTCHA).
- **Méthode de CAPTCHA textuel :** Choisissez entre capturer l'**Objet Navigateur** ou l'**Écran complet**.

### 1.8 Onglet Prompts (Invites)

- **Gérer les prompts :** Ouvre une boîte de dialogue dédiée pour personnaliser les invites système par défaut ou pour créer, modifier, réordonner et prévisualiser des invites utilisateur personnalisées avec des variables dynamiques (par exemple, `[selection]`, `[screen_fg_obj]`, `[currentURL]`, `[text]`).
- **Raccourcis de prompts personnalisés :** Attribuez une touche de raccourci dédiée à n'importe quel prompt personnalisé directement dans le gestionnaire de prompts. Appuyez sur les touches pour les enregistrer — les touches seules s'exécutent dans la couche de commandes (et globalement en tant que `NVDA + Shift + touche`), tandis que les combinaisons telles que `Control + Shift + 1` s'exécutent globalement d'elles-mêmes.
- **Comportement de retour par prompt :** Choisissez la manière dont chaque prompt restitue son résultat individuellement (paramètre global, copier dans le presse-papiers, sortie directe / message NVDA, copier dans le presse-papiers + sortie directe, ou fenêtre de chat).

### 1.9 Onglet Avancé et journalisation globale

Accédez à l'onglet **Avancé** pour configurer la journalisation globale de l'add-on :

- **Activer le fichier journal dédié :** Active ou désactive la journalisation de tous les événements opérationnels, du trafic API et des erreurs de tous les modules de l'add-on dans un fichier séparé (`vision_assistant.log`).
- **Niveau de journalisation :** Sélectionnez le niveau de détail entre **Débogage (tous les détails)**, **Info (informations générales)**, **Avertissement (avertissements uniquement)** et **Erreur (erreurs uniquement)**.
- **Conserver les journaux pendant :** Définissez des périodes de rétention automatiques pour nettoyer automatiquement les anciennes entrées de journal (allant de 1 heure à 90 jours).
- **Commandes de gestion des journaux :** Utilisez **Ouvrir le fichier journal**, **Ouvrir le dossier des journaux** ou **Effacer le fichier journal** pour inspecter ou effacer les données de journal directement sans redémarrer NVDA ni interférer avec les journaux standard de NVDA.
- **Répertoire de données unifié :** Tous les fichiers de données de l'add-on (historique, séries, étiquettes, progression OCR, caches et journaux) sont stockés dans un seul dossier `VisionAssistant` situé dans votre répertoire de configuration NVDA — ce qui permet de garder le tout organisé et de faciliter grandement les sauvegardes manuelles.

### 1.10 Sauvegarde et restauration des paramètres

L'onglet **Avancé** comprend également une section **Sauvegarde et restauration** :

- **Sauvegarde :** Enregistre votre configuration dans un seul fichier JSON. Lorsque vous cliquez dessus, vous choisissez ce qu'il faut inclure : **Tout** (paramètres, étiquettes personnalisées, progression OCR et historique) ou **Paramètres uniquement**.
- **Restauration :** Charge une sauvegarde précédemment enregistrée pour restaurer votre configuration et vos données à tout moment, sur n'importe quelle machine ou après avoir réinstallé NVDA. Il vous sera demandé de confirmer au préalable, car la restauration remplace l'ensemble de vos paramètres et données actuels.

## 2. Gestionnaire de clés API Gemini

Créer une clé API Gemini sur **aistudio.google.com** était autrefois l'étape la plus difficile de l'extension. Avec un lecteur d'écran, les pages étaient déroutantes, et certaines personnes ne parvenaient tout simplement pas à créer de clé. Le **Gestionnaire de clés API Gemini** résout ce problème. Appuyez sur **G** dans la couche de commandes, ou ouvrez **Menu NVDA > Préférences > Paramètres > Vision Assistant > Connexion** et appuyez sur **Obtenir une clé API Gemini...**.

- **Connexion :** Lorsque vous ouvrez le gestionnaire, votre navigateur par défaut s'ouvre directement sur la page de connexion sécurisée de Google. Connectez-vous avec votre compte Google — aucun outil externe, SDK ou configuration en ligne de commande n'est requis. Le compte avec lequel vous êtes connecté est toujours affiché sur le bouton **Se déconnecter**.
- **Création d'une clé :** Après vous être connecté, vous pouvez créer une clé immédiatement avec **Nouveau projet et nouvelle clé** sans aucune configuration préalable. Si vous possédez déjà des projets, ils apparaissent dans une liste simple où vous pouvez en sélectionner un et appuyer sur **Créer une clé pour le projet sélectionné**.
- **Ce qui se passe ensuite :** La nouvelle clé est immédiatement copiée dans le presse-papiers, enregistrée dans l'extension pour une utilisation ultérieure, et il vous est demandé une seule fois si vous souhaitez l'ajouter à la liste des clés de l'extension. C'est tout ce dont vous avez besoin — pas de pages Web à parcourir.
- **Gestion de vos clés :** **Copier la clé du projet sélectionné** copie la clé du projet que vous avez sélectionné, **Copier la dernière clé créée** copie la clé que vous avez créée il y a un instant, et **Exporter les clés enregistrées au format CSV...** enregistre tout ce que vous avez créé dans un fichier.
- **Suppression d'une clé :** **Supprimer une clé...** affiche les clés existantes sur le projet sélectionné, vous demande laquelle supprimer, et demande une confirmation avant la suppression. La suppression d'une clé la retire également de la liste des clés de l'extension, de sorte qu'aucune clé invalide ne reste jamais dans la rotation. Les clés créées en dehors de l'extension peuvent également être supprimées, pour autant que votre compte dispose des autorisations nécessaires sur ce projet.
- **Déconnexion :** **Se déconnecter** supprime les informations de connexion stockées sur votre ordinateur, ce qui vous permet de basculer vers un autre compte quand vous le souhaitez.

## 3. Couche de commandes et raccourcis

Pour éviter les conflits de touches, cet module complémentaire utilise une **couche de commandes**.

1. Appuyez sur **NVDA + Shift + V** (Touche principale) pour activer la couche (vous entendrez un bip).
2. Relâchez les touches, puis appuyez sur l'une des touches uniques suivantes :

| Key              | Fonction                                  | Description                                                                                                                                                                                                                                                                                |
| ---------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Shift + A**    | **Opérateur IA**                          | **Opération autonome :** Demande à l'IA d'effectuer une tâche sur votre écran. Appuyer à nouveau annule instantanément les opérations en cours.                                                                                            |
| **E**            | **Explorateur d'IU**                      | **Clic interactif :** Identifie et clique sur les éléments d'interface dans n'importe quelle application.                                                                                                                                                  |
| **T**            | Traducteur intelligent                    | Traduit le texte sous le curseur du navigateur ou la sélection.                                                                                                                                                                                                            |
| **Shift + T**    | Clipboard Translator                      | Traduit le contenu actuellement présent dans le presse-papiers.                                                                                                                                                                                                            |
| **R**            | Raffineur de texte                        | Résume, corrige la grammaire, explique ou exécute des **invites personnalisées**.                                                                                                                                                                                          |
| **V**            | Vision d'objet                            | Décrit l'objet du navigateur actuel.                                                                                                                                                                                                                                       |
| **O**            | Vision plein écran                        | Analyse la disposition et le contenu de l'écran entier.                                                                                                                                                                                                                    |
| **Shift + V**    | Analyse vidéo                             | Analyse des fichiers vidéo locaux ou des vidéos en ligne **YouTube**, **Instagram**, **TikTok** ou **Twitter (X)**.                                                                                                                                     |
| **Control + V**  | Enregistrement vidéo local                | Enregistre une vidéo muette de votre écran et analyse les actions et la disposition.                                                                                                                                                                                       |
| **D**            | Lecteur de documents                      | Lecteur avancé pour les fichiers PDF, images et texte brut/HTML avec sélection de plage de pages.                                                                                                                                                                          |
| **F**            | **Action fichier intelligente**           | Reconnaissance contextuelle à partir de fichiers image, PDF ou TIFF sélectionnés.                                                                                                                                                                                          |
| **M**            | Transcription et doublage média           | Transcrit ou double des fichiers audio/vidéo (MP3, WAV, MP4, etc.) dans votre langue cible.                                                                                                                                             |
| **C**            | Résolveur de CAPTCHA                      | Capture et résout les CAPTCHAs.                                                                                                                                                                                                                                            |
| **Shift + C**    | Chat direct                               | Ouvre une interface de discussion textuelle directe avec l'IA.                                                                                                                                                                                                             |
| **S**            | Dictée intelligente                       | Convertit la parole en texte. Appuyez pour commencer l'enregistrement, à nouveau pour arrêter/saisir.                                                                                                                                                      |
| **Control+T**    | Traduction vocale                         | Transcrit, traduit et saisit le résultat en fonction de vos paramètres de langue.                                                                                                                                                                                          |
| **Control+L**    | **Assistant en direct**                   | **Copilote en temps réel (Gemini uniquement) :** Démarre ou met fin à une conversation vocale et visuelle en direct avec l'assistant IA.                                                                                                |
| **Control+A**    | **Opérateur en direct**                   | **Contrôle informatique autonome (Gemini uniquement) :** Démarre ou met fin à une session vocale en direct au cours de laquelle l'opérateur exécute vos demandes sur l'ordinateur.                                                      |
| **G**            | **Gestionnaire de clés API Gemini**       | **Créez votre clé API sans le Web (Gemini uniquement) :** Ouvre le gestionnaire qui configure les besoins de votre ordinateur, ouvre le navigateur pour se connecter, et crée, copie ou supprime une clé pour le projet de votre choix. |
| **I**            | Rapport d'état                            | Annonce la progression actuelle (par exemple, « Analyse en cours... », « Inactif »).                                                                                                                    |
| **L**            | **Étiqueter l'objet**                     | **Étiquetage sémantique par IA :** Étiquette de manière permanente l'élément/icône actuellement focalisé.                                                                                                                                                  |
| **Shift + L**    | **Gérer/Analyser les étiquettes**         | Ouvre le gestionnaire d'étiquettes (si des étiquettes existent) ou analyse l'application à la recherche d'éléments non étiquetés.                                                                                                                       |
| **U**            | Vérification des mises à jour             | Vérifie manuellement sur GitHub la dernière version du module complémentaire.                                                                                                                                                                                              |
| **Space**        | Rappeler le dernier résultat              | Affiche la dernière réponse de l'IA dans une boîte de dialogue de discussion pour révision ou suivi.                                                                                                                                                                       |
| **H**            | Aide des commandes                        | Affiche une liste de tous les raccourcis disponibles.                                                                                                                                                                                                                      |
| **Control + H**  | **Historique**                            | Ouvre la boîte de dialogue Historique listant vos discussions et documents passés, avec des filtres de type et des options de suppression/effacement.                                                                                                                      |
| **Alt + S**      | Paramètres                                | Ouvre la boîte de dialogue des paramètres de Vision Assistant Pro.                                                                                                                                                                                                         |
| **Alt + Q**      | Rapport des clés dont le quota est épuisé | Indique le nombre de clés API Gemini ayant dépassé leur quota journalier ainsi que leur heure de réinitialisation.                                                                                                                                                         |
| **Alt + M**      | Audit de routage                          | Indique les modèles d'IA actuellement sélectionnés dans le routage avancé.                                                                                                                                                                                                 |
| **Up / Down**    | Navigation dans les paramètres rapides    | Navigue entre les catégories de paramètres rapides (Fournisseur, Modèle, etc.) dans la couche.                                                                                                                                          |
| **Left / Right** | Modifier le paramètre rapide              | Modifie la valeur du paramètre rapide actuellement sélectionné.                                                                                                                                                                                                            |

## 4. Discussion et historique

Les fenêtres de discussion et la boîte de dialogue de l'historique fonctionnent avec toutes les fonctionnalités, ce qui vous permet de consulter vos conversations et de reprendre exactement là où vous vous étiez arrêté.

### 4.1 Raccourcis de la fenêtre de discussion

Lorsqu'une fenêtre de discussion est ouverte (discussion directe, discussion sur un document, raffinement et similaires), vous pouvez parcourir la conversation avec :

- **Alt + Flèche Bas :** Lire le message suivant.
- **Alt + Flèche Haut :** Lire le message précédent.
- **Alt + C :** Copier le message actuel.

### 4.2 Historique (Control + H)

Appuyez sur **Control + H** dans la couche de commandes pour ouvrir la boîte de dialogue **Historique** contenant vos discussions et documents passés, filtrables par type (Tous / Discussions / Documents). Ouvrez une discussion pour poursuivre la conversation — y compris ses fichiers joints, qui sont rattachés automatiquement — ou ouvrez un document pour continuer la lecture. Appuyez sur **Suppr** sur n'importe quel élément pour le supprimer, ou sur **Tout effacer** pour vider la liste. Pour les documents, la touche Suppr demande si vous souhaitez supprimer uniquement l'entrée de l'historique ou également effacer le texte OCR mis en cache pour ce document afin que la prochaine ouverture le réexamine entièrement, avec une option **Ne plus demander** pour mémoriser votre choix.

Vous pouvez également choisir ce que la liste mémorise. Les options **Enregistrer les discussions dans l'historique** (onglet Connexion) et **Enregistrer les documents dans l'historique** (onglet Lecteur de documents) sont toutes deux activées par défaut et peuvent être basculées dans les paramètres rapides. L'option concernant les documents affecte uniquement l'entrée de l'historique ; le texte OCR mis en cache et les données de reprise sont toujours conservés.

## 5. Opérateur IA - Contrôle informatique autonome

L'**Opérateur IA** transforme Vision Assistant Pro d'un lecteur passif en un assistant actif capable d'interagir avec votre ordinateur à votre place. Vous pouvez lui demander de décrire l'écran, de répondre à des questions sur ce qu'il voit, ou même de prendre le contrôle — en cliquant sur des boutons, en glissant des éléments, en tapant du texte et en naviguant dans les applications à l'aide de commandes en langage naturel.

Le plus grand avantage ? Il fonctionne parfaitement dans des logiciels complètement inaccessibles. Si vous êtes bloqué dans une application personnalisée, un bureau à distance ou un site Web où votre lecteur d'écran devient totalement silencieux, l'opérateur ne s'en soucie pas. Parce qu'il « voit » l'écran visuellement, il peut trouver, lire et interagir avec des éléments qui ne possèdent aucune étiquette d'accessibilité.

### 5.1 Comment ça fonctionne

1. Appuyez sur **NVDA + Shift + V**, puis sur **Shift + A** (ou utilisez le raccourci direct) pour ouvrir la boîte de dialogue de l'Opérateur IA.
2. Saisissez ce que vous souhaitez faire en langage clair (par exemple, « Cliquer sur le bouton Enregistrer », « Que dit le message d'erreur ? » ou « Renommer le fichier en final.pdf »).
3. L'IA analysera votre écran, identifiera les éléments pertinents et exécutera l'action ou fournira la réponse. Si une tâche nécessite plusieurs étapes, l'opérateur continuera à travailler jusqu'à ce qu'elle soit terminée.
4. Appuyez à nouveau sur **Shift + A** à tout moment pour interrompre instantanément une opération en cours.

### 5.2 Actions prises en charge

L'opérateur comprend un large éventail de commandes :

- **Décrire et répondre** : « Décrire la disposition de l'écran » ou « Que dit le message d'erreur ?
- **Cliquer** : « Cliquer sur le bouton Enregistrer »
- **Clic droit** : « Faire un clic droit sur le fichier »
- **Double-clic** : « Double-cliquer sur le document »
- **Glisser-déposer** : « Glisser le document vers le dossier Archive »
- **Saisir** : « Taper 'Hello World' dans la zone de recherche »
- **Faire défiler** : « Faire défiler vers le bas trois fois »
- **Appuyer sur une touche** : « Appuyer sur Entrée », « Appuyer sur Tab », « Appuyer sur Échap »
- **Tâches en plusieurs étapes** : « Ouvrir l'Explorateur de fichiers, trouver le rapport et le renommer en final.pdf »

### 5.3 Remarques importantes

- **⚠️ Avertissement sur l'utilisation de l'API** : Comme l'opérateur a besoin de « voir » exactement ce qui se passe à l'écran, il envoie une capture d'écran haute résolution à chaque étape. Une utilisation fréquente consommera votre quota d'API beaucoup plus rapidement que les fonctionnalités textuelles standard.
- **Applications administrateur** : Si NVDA ne s'exécute pas avec les privilèges d'administrateur, l'opérateur peut ne pas être en mesure d'interagir avec les fenêtres nécessitant des permissions élevées. Il s'agit d'une limitation de sécurité de Windows et non d'un bug du module complémentaire.
- **Bonnes pratiques** : Pour de meilleurs résultats, donnez des commandes claires et spécifiques. « Cliquer sur le bouton bleu Soumettre au bas du formulaire » fonctionnera presque toujours mieux que simplement « Cliquer sur le bouton ».

### 5.4 Opérateur en direct (Control+A)

L'Opérateur en direct permet à l'Assistant en direct d'exécuter ce que vous demandez sur votre ordinateur pendant que vous lui parlez, y compris dans des applications que votre lecteur d'écran ne peut pas lire.
_(Remarque : Cette fonctionnalité est exclusive à Google Gemini et aux fournisseurs personnalisés compatibles avec Gemini)._

- **Activation :** Appuyez sur **Control+A** dans la couche de commandes pour démarrer une session d'opérateur en direct ; appuyez à nouveau dessus pour l'arrêter.
- **Comment ça fonctionne :** Demandez en langage clair, par exemple « ouvrir Chrome et rechercher un site Web » ou « renommer ce fichier en final ». L'opérateur regarde l'écran, exécute les étapes une par une et continue de traiter les demandes en plusieurs étapes jusqu'à ce que la tâche soit terminée.
- **Annonces :** Chaque étape est prononcée avec la propre voix de l'Assistant en direct, et il vous indique lorsque la tâche est terminée ou pourquoi elle n'a pas pu être effectuée.
- **CAPTCHA :** Si un CAPTCHA apparaît, l'opérateur essaie d'abord d'utiliser votre **résolveur de CAPTCHA** intégré ; s'il ne peut pas le résoudre, il vous demande de compléter vous-même le défi accessible.
- **Arrêt :** Appuyez sur **Arrêter l'action de l'opérateur** dans la fenêtre de l'Assistant en direct pour annuler la tâche en cours.
- **Paramètres :** Les instructions propres à l'opérateur peuvent être modifiées dans le gestionnaire de contextes (section **En direct**, **Instruction de l'opérateur en direct**). Le commutateur **Sortie directe en direct (sans fenêtre)** est également disponible dans les paramètres rapides.

## 6. Analyse vidéo et audiodescription

> **Remarque :** Les fonctionnalités d'analyse vidéo et d'audiodescription sont exclusivement alimentées par le fournisseur **Google Gemini**. Assurez-vous que votre fournisseur actif dans les paramètres de l'add-on est défini sur Google Gemini.

Vision Assistant Pro introduit de puissantes capacités de traitement vidéo conçues spécifiquement pour les utilisateurs non-voyants. Il peut analyser à la fois les vidéos en ligne et les enregistrements d'écran locaux pour fournir des descriptions visuelles extrêmement détaillées et générer des scripts d'audiodescription professionnels (au format SRT).

### 6.1 Enregistrement d'écran local (Control + V)

Si vous rencontrez une vidéo muette, une animation ou un didacticiel sur votre écran, vous pouvez l'capturer directement :

1. Appuyez sur **NVDA + Shift + V** pour entrer dans la couche de commandes (Command Layer), puis appuyez sur **Control + V**.
2. L'add-on enregistrera discrètement votre écran en arrière-plan.
3. Appuyez de nouveau sur **Control + V** pour arrêter l'enregistrement.
4. L'IA analysera ensuite le segment vidéo enregistré et fournira une description très détaillée de la scène, des personnages et des actions.

### 6.2 Analyse vidéo (Shift + V)

Vous pouvez analyser à la fois des fichiers vidéo locaux et des vidéos en ligne. Sélectionnez simplement un fichier vidéo local dans l'Explorateur Windows, ou copiez un lien de vidéo en ligne dans votre presse-papiers. Vous pouvez également appuyer sur **Shift + V** n'importe où (par exemple à l'intérieur d'un lecteur multimédia) pour ouvrir une boîte de dialogue dans laquelle vous pouvez parcourir pour trouver un fichier vidéo ou coller une URL manuellement.

- **Plateformes en ligne prises en charge :** YouTube, Instagram, TikTok et Twitter (X).
- L'IA détectera automatiquement le fichier local ou l'URL, traitera la vidéo et fournira une description visuelle complète ainsi qu'un résumé audio.
- **Mise en cache des fichiers vidéo pendant 48 heures** : Les vidéos téléchargées sur Gemini sont désormais mises en cache pendant 48 heures ! Vous pouvez régénérer les sorties SRT ou MP3 pour la même vidéo sans la retélécharger — même après avoir redémarré NVDA. Le cache prend en compte les clés et est automatiquement invalidé lorsque votre clé API change.

### 6.3 Génération d'audiodescription (SRT)

Pour une expérience plus structurée, l'add-on peut générer des scripts d'audiodescription professionnels au format standard SubRip (SRT).

- **Gestion intelligente des silences :** L'IA écoute la piste audio et ancre spécifiquement ses descriptions visuelles sur les pauses naturelles et les silences afin de minimiser intelligemment le chevauchement avec les dialogues.
- **Suivi des personnages :** Le moteur effectue une passe préliminaire pour extraire les différents personnages en fonction de leurs traits faciaux immuables. Il construit un dictionnaire global pour suivre et étiqueter avec précision les personnages à travers différentes scènes sans confusion. Il suit également la **première apparition** de chaque personnage, décrivant son apparence physique une seule fois (au moment où il apparaît pour la première fois) et n'utilisant les noms établis que dans les scènes ultérieures pour garder la narration fraîche et naturelle.
- **OCR de texte textuel :** Tout texte apparaissant à l'écran (panneaux, téléphones, génériques) est strictement retranscrit mot pour mot.
- **Mode d'emploi :** Pour écouter le sous-titre généré, placez simplement le fichier `.srt` dans le même dossier que votre fichier vidéo et donnez-lui exactement le même nom. Ensuite, configurez votre lecteur multimédia (par exemple, VLC ou PotPlayer) pour acheminer le texte des sous-titres directement vers votre lecteur d'écran ou votre moteur TTS pendant la lecture.
- **Expérience de sauvegarde améliorée :** Lors de l'enregistrement de fichiers SRT ou MP3, la boîte de dialogue de fichier s'ouvre désormais par défaut dans le dossier de la vidéo source, que vous ayez ouvert la vidéo via la boîte de dialogue de fichier ou via Shift+V depuis l'Explorateur.

### 6.4 Narration audio synchronisée (Exportation MP3)

Au-delà de la simple création de fichiers SRT textuels, l'add-on fonctionne comme un outil de production d'audiodescription complet en synthétisant les descriptions en parole et en les mixant avec la vidéo. Vous pouvez désormais choisir **Gemini Live TTS** comme moteur vocal, qui utilise l'API Gemini Live pour générer une narration vocale extrêmement réaliste et illimitée. Lors de la génération d'un MP3 pour des fichiers vidéo locaux, vous disposez de plusieurs modes de mixage :

- **AD Standard (Mixage vocal) :** La narration est superposée directement par-dessus l'audio de la vidéo. Il vous sera demandé si vous souhaitez appliquer une **atténuation audio** (Audio Ducking, qui réduit le volume de l'arrière-plan pendant les descriptions) pour garantir la clarté de la narration. You will be prompted if you want to apply **Audio Ducking** (lowering the background volume during descriptions) to ensure the narration is clear.
- **AD Étendue (Pause audio) :** Le moteur met en pause l'audio de la vidéo d'origine pendant les descriptions, garantissant que vous ne manquiez pas un seul mot du dialogue original ou de la narration de l'IA. La détection des silences utilise désormais le modèle neuronal **Silero VAD** (téléchargé automatiquement lors de la première utilisation, tout comme ffmpeg et eSpeak) pour un minutage précis des silences, faisant la distinction entre les pauses de dialogue naturelles et la musique ou le bruit de fond.
- **Vidéos YouTube :** Pour les sources YouTube (qui ne sont pas téléchargées localement), l'exportation MP3 contiendra strictement la piste vocale IA synchronisée sans l'audio vidéo de fond.

## 7. Transcription et doublage de médias (M)

L'transcripteur audio a été entièrement reconstruit pour prendre en charge à la fois les fichiers audio et vidéo (MP3, WAV, MP4, MKV, etc.). Appuyez sur **M** dans la couche de commandes pour sélectionner un fichier média et choisir l'un des 3 modes de fonctionnement distincts :

1. **Transcrire (Langue originale)** : Transcrit avec précision la parole prononcée dans sa langue originale.
2. **Transcrire et traduire (Langue cible)** : Transcrit la parole et la traduit dans votre langue cible configurée.
3. **Doubler et traduire (Langue cible)** _(Gemini uniquement)_ : Une nouvelle fonctionnalité puissante qui transcrit la parole, la traduit dans votre langue cible et synthétise un doublage audio parlé à l'aide du moteur TTS de l'add-on.

## 8. Lecteur de documents et d'images avancé

Le **Lecteur de documents** transforme vos documents en texte propre et lisible — vous permettant ainsi de lire, traduire et écouter n'importe quoi, d'un livre numérisé à une pile de photos. Il prend en charge les PDF multipages, les images complexes, les formats iPhone HEIC, ainsi que les fichiers texte brut (`.txt`) et HTML (`.html`, `.htm`), qui s'ouvrent instantanément sans traitement par IA ni ROC (OCR). Sélectionnez plusieurs fichiers à la fois pour qu'ils soient fusionnés en un seul document continu dans l'ordre des pages. Trois moteurs de ROC sont disponibles — **Chrome (Rapide)**, **IA (Avancé)** pour une préservation supérieure de la mise en page, et **Aucun (Extraire la couche de texte)** pour les PDF interrogeables —, sélectionnables dans Paramètres → Lecteur de documents.

### Comment ça marche

1. Appuyez sur **NVDA + Shift + V**, puis sur **D** pour ouvrir le lecteur de documents — ou sélectionnez d'abord un fichier dans l'Explorateur de fichiers et appuyez sur **D** / **F** pour ignorer complètement la boîte de dialogue de fichier.
2. Choisissez un ou plusieurs PDF ou images. L'add-on les analyse et annonce le nombre total de pages.
3. Dans la boîte de dialogue **Options**, choisissez la plage de pages (De/À). Vous pouvez également cocher **Traduire le résultat** et choisir la langue cible, activer **Décrire les images en ligne pendant la ROC**, ou activer **Compresser les pages PDF avant le traitement** pour réduire l'échelle et recompresser les pages numérisées trop volumineuses avant le téléchargement.
4. L'extraction de texte démarre en arrière-plan par lots. Vous pouvez fermer la fenêtre à tout moment et continuer plus tard — rien n'est perdu.
5. Une fois les pages prêtes, lisez-les dans la visionneuse : naviguez entre les pages, accédez à n'importe quelle page, posez des questions à l'IA, enregistrez le texte ou générez une narration audio.

### 8.1 Traitement par lots et reprise

Vous n'avez pas besoin de lire un document massif d'un seul coup. Choisissez une plage de pages (par ex., `1-20`) ou conservez les valeurs par défaut pour tout traiter, et l'IA extrait toutes les pages en arrière-plan. Si NVDA plante ou si vous interrompez l'analyse, l'add-on mémorise votre progression et propose de **Reprendre** exactement là où vous vous étiez arrêté — même après un redémarrage. Les documents terminés sont également mis en cache, de sorte que leur réouverture (depuis les Documents récents ou via **D**) charge le texte instantanément sans réexécuter la ROC, sauf si les fichiers sources ont changé.

### 8.2 Action de fichier intelligente

Vous n'avez pas toujours besoin d'ouvrir le document au préalable. Dans l'Explorateur de fichiers de Windows, sélectionnez simplement un PDF, une image ou un fichier texte/HTML et appuyez sur **D** (Lecteur de documents) — ou sélectionnez un PDF ou une image et appuyez sur **F** (Action de fichier intelligente) — dans la couche de commandes. L'add-on contourne instantanément la boîte de dialogue de fichier et commence à traiter le fichier sélectionné. La sélection de plusieurs fichiers à la fois les traite ensemble comme un seul document.

### 8.3 Contrôles et raccourcis de la visionneuse de documents

Lorsque la fenêtre du lecteur de documents est ouverte, vous pouvez utiliser les éléments suivants :

#### Raccourcis clavier

- **Ctrl + PageSuivante / Ctrl + PagePrécédente :** Passer à la page suivante / précédente.
- **Flèche Bas / Haut :** Lorsque votre curseur atteint la dernière ligne d'une page, appuyez sur **Bas** pour passer à la page suivante ; appuyez sur **Haut** en haut d'une page pour revenir à la précédente.
- **Alt + A :** Ouvrir une boîte de dialogue de chat pour poser des questions sur le document.
- **Alt + R :** Forcer une **Ré-analyse avec l'IA** en utilisant votre fournisseur actif.
- **Alt + G :** Générer et enregistrer un fichier audio de haute qualité (WAV/MP3). _(Masqué si le fournisseur ne prend pas en charge la synthèse vocale)._
- **Alt + S / Ctrl + S :** Enregistrer le texte extrait sous forme de fichier TXT ou HTML.

#### Boutons et contrôles

- **Aller à :** Choisir n'importe quelle page dans le sélecteur de pages.
- **Afficher mis en forme :** Voir l'ensemble du document combiné sous forme de texte mis en forme.
- **Réessayer les pages échouées :** Réessayer uniquement les lots qui ont échoué en raison d'une erreur temporaire du serveur (par ex., forte demande). Ce bouton apparaît automatiquement si nécessaire.
- **Voix TTS / Moteur TTS :** Choisir la voix, et sur Gemini, choisir entre **TTS standard** et le streaming **Gemini Live**.
- **Précédent / Suivant :** Naviguer entre les pages (identique aux raccourcis Ctrl+PagePrécédente/Suivante).

### 8.4 Documents récents (D)

**Documents récents dans le lecteur** : Appuyer sur **D** dans la couche de commandes affiche désormais en premier vos documents récemment lus. Choisissez-en un pour reprendre à la page où vous étiez — même une fois l'OCR terminée — ou appuyez sur **Ouvrir un fichier...** (`Ctrl + O`) pour parcourir normalement.

## 9. Étiquetage sémantique par IA et Explorateur d'interface (UI Explorer)

Bloqué dans une application remplie de « bouton sans étiquette » partout ? Le moteur d'étiquetage sémantique par IA résout ce problème définitivement.

### 9.1 Étiquetage d'objet permanent (L)

Placez le focus de votre lecteur d'écran sur un graphique ou un bouton sans étiquette et appuyez sur **L** dans la couche de commandes (Command Layer). L'IA analysera visuellement le bouton, déterminera sa fonction et lui appliquera une étiquette permanente.
_Contrairement aux anciens outils d'étiquetage pour lecteurs d'écran, cet module complémentaire utilise un système hybride avancé de « Signature d'objet » (AutomationId/ControlID). Vos étiquettes personnalisées survivront au redimensionnement des fenêtres, au changement de moniteur et aux mises à jour des applications !_

### 9.2 Analyse complète de l'application (Shift + L)

Appuyez sur **Shift + L** pour analyser l'intégralité de la fenêtre active en une seule fois. L'IA trouvera tous les éléments sans étiquette et les nommera intelligemment en une seule opération. Vous pourrez ensuite gérer, renommer ou supprimer en masse ces étiquettes depuis le gestionnaire d'étiquettes intégré.

### 9.3 Explorateur d'interface - UI Explorer (E)

Besoin d'interagir avec un élément sans y naviguer manuellement ? Appuyez sur **E** pour activer l'explorateur d'interface. L'IA analysera l'écran et générera une liste accessible de chaque élément cliquable (en ignorant le bruit du système tel que la barre des tâches). Choisissez un élément dans la liste et le module complémentaire cliquera instantanément dessus pour vous.

## 10. Assistant vocal en direct

L'Assistant en direct transforme Vision Assistant Pro en un copilote interactif en temps réel.
_(Remarque : Cette fonctionnalité est exclusive à Google Gemini et aux fournisseurs personnalisés compatibles Gemini)._

- **Activation :** Appuyez sur **Control + L** dans la couche de commandes pour ouvrir la boîte de dialogue de l'Assistant en direct.
- **Interaction en temps réel :** Parlez naturellement dans votre microphone. L'IA écoutera simultanément votre voix et analysera votre écran actif. Vous pouvez poser des questions telles que "Qu'est-ce que je regarde ?" ou "Lis-moi le troisième paragraphe."
- **Fonction "Push to Talk" (Appuyer pour parler) :** Activez **Push to Talk** dans l'onglet des paramètres de l'Assistant en direct (ou basculez l'option directement dans la fenêtre de l'Assistant en direct), puis maintenez enfoncée la touche assignée pour parler et relâchez-la pour terminer. Cela maintient le microphone en sourdine jusqu'à ce que vous appuyiez sur la touche — idéal pour les environnements bruyants.
- **Entrée webcam :** Cochez **Utiliser la &webcam** dans la fenêtre de l'Assistant en direct pour envoyer le flux de votre caméra à l'IA au lieu de votre écran — posez des questions sur des objets physiques, des documents imprimés ou votre environnement. Si ffmpeg n'est pas encore installé, le fait de cocher la case le télécharge une seule fois avec votre autorisation ; l'option est désactivée lorsqu'aucun appareil photo n'est détecté ou si les paramètres de confidentialité de Windows bloquent l'accès à la caméra.
- **Personnalisation :** Dans la boîte de dialogue, vous pouvez modifier le style de voix de l'IA (par exemple, Professionnel, Amical, Dynamique) et ajuster sa « Profondeur de réflexion » pour contrôler le niveau de raisonnement avant qu'elle ne réponde.

## 11. Observateur ambiant (Assistant en arrière-plan)

L'Observateur ambiant transforme Vision Assistant Pro en vos yeux en arrière-plan, sans aucune conversation : il continue d'écouter et de surveiller pendant que vous travaillez, signale les changements et reste silencieux lorsqu'il ne se passe rien.
_(Remarque : cette fonctionnalité est exclusive à Google Gemini et aux fournisseurs personnalisés compatibles Gemini)._

- **Activation :** Appuyez sur **Maj+O** dans la couche de commandes pour ouvrir la boîte de dialogue de l'Observateur ambiant ; appuyez de nouveau pour arrêter l'observateur.
- **Modes :** **Traduction audio uniquement** traduit ce qu'il entend, **Surveillant d'écran uniquement** signale les modifications de l'écran, et **Surveillant de webcam uniquement** ouvre la fenêtre de l'Assistant en direct avec votre caméra et la fonction Appuyer pour parler, afin que vous puissiez poser des questions sur ce que voit la caméra.
- **Source audio :** En mode audio, choisissez si vous souhaitez traduire votre **microphone** ou l'**audio du système (boucle de rétroaction / loopback)**. La petite bibliothèque de boucle est téléchargée une seule fois lors de la première utilisation, avec votre autorisation.
- **Contexte :** Pour les modes écran et webcam, choisissez une option facultative **À propos de ce que je fais** (par exemple, regarder un film, suivre une réunion ou un appel, lire une étiquette ou vérifier votre apparence) pour cibler les rapports ; vous pouvez également saisir votre propre contexte.
- **Rapports :** L'add-on compare chaque nouvelle image avec la précédente et l'envoie à l'IA uniquement lorsque l'image a réellement changé, de sorte qu'un écran statique ne consomme jamais de requêtes. L'IA rapporte ensuite uniquement ce qui est nouveau et ne se répète jamais.
- **Message de bienvenue :** Sauf en mode traduction, l'observateur vous accueille brièvement au démarrage pour vous faire savoir qu'il est à l'écoute.
- **Paramètres :** Dans **Paramètres > Assistant en direct**, définissez le **Mode de l'observateur**, l'**Intervalle d'images** (1 à 10 secondes) et le **Style de rapport** (bref ou détaillé). L'instruction de l'observateur et chaque texte de contexte peuvent être modifiés dans le Gestionnaire de prompts (section **Ambiant**).

## 12. Prompts personnalisés et variables

Vous pouvez gérer les prompts dans **Paramètres > Prompts > Gérer les prompts...**.

- **Filtre :** L'onglet **Prompts par défaut** dispose d'une liste de **Filtre** située au-dessus de la liste des prompts, permettant d'afficher **Tous** les prompts ou une seule section à la fois (par exemple **Ambiance**), afin de faciliter la navigation dans les longues listes.

### Raccourcis de prompts personnalisés

Attribuez à n'importe quel prompt personnalisé sa propre touche de raccourci directement dans le gestionnaire de prompts, et exécutez-le instantanément avec votre sélection ou contexte actuel :

- **Touche unique** (par exemple `1`, `p`, ou `F3`) : Fonctionne à l'intérieur de la couche de commandes (Command Layer), et également globalement sous la forme `NVDA + Shift + touche`.
- **Combinaison de touches** (par exemple `Control + Shift + 1`, `Alt + P`, ou `Insert + 1`) : Fonctionne globalement de manière autonome.

### Comportement du retour par prompt

Chaque prompt personnalisé peut définir individuellement son comportement de restitution du résultat :

- **Paramètre global :** Suit le paramètre général de sortie de la connexion (Sortie directe ou fenêtre de discussion).
- **Copier dans le presse-papiers :** Copie la réponse de l'IA directement dans le presse-papiers sans ouvrir de fenêtre.
- **Sortie directe (message NVDA) :** Annonce/transcrit en braille la réponse de l'IA directement via la synthèse vocale de NVDA.
- **Copy to clipboard and Direct Output:** Copies the response to the clipboard and speaks it directly.
- **Fenêtre de discussion :** Ouvre toujours le résultat dans une fenêtre de conversation interactive.

### Variables prises en charge

- `[selection]` : Texte actuellement sélectionné.
- `[text]` : Contenu textuel complet du champ d'édition ayant le focus (ignore automatiquement les zones de mot de passe protégées).
- `[currentURL]` : URL de la page Web ou du document provenant des navigateurs Web pris en charge (Chrome, Edge, Firefox).
- `[clipboard]` : Contenu du presse-papiers.
- `[clipboard_image]` : Image actuellement présente dans le presse-papiers.
- `[screen_obj]` : Capture d'écran de l'objet navigateur.
- `[screen_fg_obj]` : Capture d'écran de la fenêtre active au premier plan.
- `[screen_full]` : Capture d'écran de l'écran entier.
- `[file_ocr]` : Sélectionner un fichier image/PDF pour l'extraction de texte.
- `[file_read]` : Sélectionner un document à lire (TXT, Code, PDF).
- `[file_audio]` : Sélectionner un fichier audio à analyser (MP3, WAV, OGG).
- `[ambient_screen]` : Démarre une session d'arrière-plan continue de l'observateur d'écran (Screen Observer).
- `[ambient_webcam]` : Démarre une session d'arrière-plan continue de l'observateur par webcam (Webcam Observer) (vérifie le paramètre "Appuyer pour parler" / Push to Talk).
- `[ambient_audio]` : Démarre une session de traduction en direct de l'observateur audio (Audio Observer).
- `[loopback]` : Utilise la lecture audio du système comme source sonore (pour `[ambient_audio]`).
- `[mic]` : Utilise le microphone comme source sonore (pour `[ambient_audio]` et `[ambient_webcam]`).
- `[brief]` : Définit le style de rapport de l'observateur sur bref (une seule phrase).
- `[detailed]` : Définit le style de rapport de l'observateur sur détaillé (2 à 3 phrases).
- `[lang:code]` : Spécifie le code de la langue cible pour la traduction audio (par exemple `[lang:fa]`, `[lang:en]`).
- `{target_lang}` : Langue cible actuelle.
- `{source_lang}` : Langue source actuelle.
- `{response_lang}` : Langue actuelle de la réponse de l'IA.
- `{swap_target}` : Langue de repli pour la traduction par permutation intelligente.
- `{swap_instruction}` : Bloc d'instructions pour la traduction par permutation intelligente.

_Remarque sur les prompts d'ambiance :_ Les prompts contenant des variables d'ambiance agissent comme un commutateur (toggle) — appuyer sur le raccourci alors qu'ils sont actifs arrête immédiatement la session. Les combinaisons incompatibles (telles que l'association de variables de capture d'écran statiques comme `[screen_full]` avec des modes d'observateur ambiant, la combinaison de plusieurs modes ambiants, ou l'ajout d'instructions de prompt à `[ambient_audio]`) font l'objet d'une validation stricte et sont empêchées lors de l'enregistrement.

## 13. Cas d'utilisation concrets (Quelle fonctionnalité dois-je utiliser ?)

Vision Assistant Pro regorge d'outils avancés. Voici quelques scénarios courants pour vous aider à choisir le bon :

- **Scénario : Vous souhaitez comprendre la disposition complète d'une fenêtre complexe ou d'une application inaccessible.**
  _Solution :_ Appuyez sur **O** (Vision plein écran). L'IA analysera l'ensemble de l'écran et décrira précisément où se trouvent les éléments, les textes et les boutons.

- **Scénario : Vous avez trouvé une image sur une page Web ou un graphique sans étiquette dans un document.**
  _Solution :_ Déplacez votre objet navigateurs sur le graphique et appuyez sur **V** (Vision par objet). L'IA décrira précisément ce que contient cette image.

- **Scénario : Vous souhaitez regarder un film ou un clip vidéo avec des audiodescriptions.**
  _Solution :_ Appuyez sur **Shift + V** sur votre vidéo et choisissez **"Générer une audiodescription (fichier SRT)"**. Une fois l'opération terminée, cliquez sur **"Générer une narration synchronisée (MP3)"** et sélectionnez **"AD étendue"**. L'add-on créera une piste audio qui met intelligemment en pause les dialogues du film pour décrire les scènes visuelles.

- **Scénario : Vous rencontrez une application remplie de "boutons sans étiquette".**
  _Solution :_ Appuyez sur **L** pour étiqueter définitivement le bouton spécifique à l'aide de l'IA. Ou appuyez sur **Shift + L** pour analyser et étiqueter toute la fenêtre en une seule fois. Si vous souhaitez simplement cliquer rapidement sur quelque chose, appuyez sur **E** (Explorateur d'interface utilisateur) pour obtenir la liste de tous les éléments cliquables.

- **Scénario : Vous devez contourner un CAPTCHA inaccessible.**
  _Solution :_ Appuyez sur **C** (Résolveur de CAPTCHA). L'IA capturera automatiquement le CAPTCHA, le résoudra et injectera la réponse dans le champ approprié.

- **Scénario : Vous souhaitez lire un long document PDF de 50 pages.**
  _Solution :_ Appuyez sur **D** (Lecteur de documents), définissez votre fournisseur sur Google Gemini et entrez la plage de pages `1-50`. L'add-on extraira le texte avec précision en arrière-plan.

- **Scénario : Vous regardez un tutoriel vidéo silencieux ou une animation sur votre écran.**
  _Solution :_ Appuyez sur **Control + V** pour commencer l'enregistrement de l'écran. Laissez le tutoriel se dérouler, puis appuyez à nouveau sur **Control + V**. L'IA expliquera exactement ce qui a été démontré.

- **Scénario : Vous rencontrez une erreur inattendue, un échec de connexion API, ou vous souhaitez diagnostiquer des problèmes avec des serveurs locaux personnalisés.**
  _Solution :_ Allez dans **Paramètres > Avancé**, cochez **"Activer le fichier journal dédié"** et définissez le **Niveau de journalisation** sur **"Débogage"** (Debug). Répétez l'action, puis cliquez sur **"Ouvrir le fichier journal"** pour inspecter les détails techniques ou joindre le fichier `vision_assistant.log` à un ticket de support.

***

**Remarque :** Une connexion Internet active est requise pour toutes les fonctionnalités d'IA. Les documents de plusieurs pages sont traités automatiquement.

## 14. Support et communauté

Restez informé des dernières actualités, fonctionnalités et versions :

- **Canal Telegram :** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **Problèmes GitHub :** Pour les rapports de bugs et les demandes de fonctionnalités.

### Signaler des bugs et des journaux

Lors de l'ouverture d'un problème sur GitHub ou d'une demande d'assistance, veuillez inclure des détails sur votre fournisseur d'IA actif, votre modèle et votre version de NVDA. Si vous rencontrez des problèmes de connexion ou des plantages inattendus, activez le fichier journal dédié dans **Paramètres > Avancé**, reproduisez le problème et joignez votre fichier `vision_assistant.log` pour nous aider à résoudre le problème plus rapidement.

## 15. Soutiens du projet

Un grand merci aux membres de notre communauté qui soutiennent le développement continu et la maintenance de ce projet par leurs généreuses contributions financières :

- **@Alyabani94**
- **Ali Alamri**
- **Ilya**
- **leonardo0216**
- **Sergei Fleytin**
- **Arne Siebert**
- **Schalkefan**
- **Rainer Brell**
- **[avalai.org](https://avalai.org)**

_Si vous souhaitez soutenir financièrement le projet et voir votre nom ici, vous trouverez l'option **Faire un don** dans le menu Outils de NVDA (sous-menu Vision Assistant) ou pendant le processus de configuration après l'installation._

---

## Modifications pour 2026.10.15

- **La correction la plus demandée : créer une clé API Gemini est enfin un jeu d'enfant** : Obtenait une clé API sur **aistudio.google.com** était auparavant l'étape la plus difficile. Avec un lecteur d'écran, les pages portaient à confusion et certaines personnes ne pouvaient tout simplement pas créer de clé. Ce problème est désormais résolu directement au sein de l'extension. Appuyez sur **G** dans la couche de commandes (ou utilisez **Obtenir une clé API Gemini...** dans les Paramètres), connectez-vous via votre navigateur par défaut sans configuration externe, et votre clé sera créée et configurée en une seule confirmation — même si vous n'aviez jamais eu de projet auparavant.
- **Observateur ambiant** : L'assistant en arrière-plan est arrivé. Appuyez sur **Maj+O** dans la couche de commandes pour le démarrer, et appuyez à nouveau pour l'arrêter. Il peut traduire ce qu'il entend (votre microphone ou le son du système), surveiller l'écran et vous dire ce qui a changé, ou ouvrir l'assistant en direct avec votre webcam et la fonction Push to Talk pour que vous puissiez poser des questions sur ce que voit la caméra. Il n'envoie une image que lorsque quelque chose a réellement changé, de sorte qu'un écran fixe ne vous coûte rien, et il reste silencieux lorsqu'il ne se passe rien. Vous pouvez également lancer et basculer l'observateur directement via des invites personnalisées et des touches de raccourci dédiées en utilisant `[ambient_screen]`, `[ambient_webcam]` ou `[ambient_audio]` ainsi que des modificateurs (`[loopback]`, `[mic]`, `[brief]`, `[detailed]`, `[lang:code]`), avec une validation automatique contre les combinaisons de variables en conflit.
- **Opérateur en direct** : L'assistant en direct peut désormais exécuter ce que vous demandez sur votre ordinateur pendant que vous lui parlez. Appuyez sur **Ctrl+A** dans la couche de commandes pour démarrer une session d'opérateur en direct, puis demandez simplement en langage clair. Il traite des requêtes en plusieurs étapes, énonce chaque étape avec la propre voix de l'assistant en direct, prend en charge les combinaisons de touches nécessaires et décide de lui-même lorsque la tâche est terminée. **Sortie directe en direct (sans fenêtre)** est également disponible dans les Paramètres rapides.
- **Dictionnaire des personnages et gestion des séries** : La boîte de dialogue Analyse vidéo inclut désormais un puissant système de **dictionnaire des personnages** ! Ajoutez, modifiez, importez ou gérez les noms des personnages, leurs descriptions physiques et leurs rôles par série — l'IA associe automatiquement les personnages découverts à votre dictionnaire et fusionne les nouveaux à mesure que vous analysez plus d'épisodes. Vos notes manuelles sont toujours préservées avec priorisation sur les mises à jour de l'IA, tandis que les descriptions physiques restent à jour d'un épisode à l'autre. Le dictionnaire est enregistré par série et réutilisé pour chaque vidéo de cette série. Dans la liste des personnages, appuyez sur **F2** pour modifier le personnage sélectionné et sur **Suppr** pour le supprimer.
- **Prise en charge de SOCKS5, HTTP et du proxy inversé avec test de latence** : Contournez de manière transparente les restrictions réseau grâce à une prise en charge complète des proxys dans toute l'extension, y compris l'assistant en direct, l'observateur ambiant et la génération TTS ! Choisissez parmi 4 modes de fonctionnement dans les paramètres Généraux : **Détection automatique**, **Proxy SOCKS5**, **Proxy HTTP** ou **Proxy inversé**. SOCKS5 prend en charge l'authentification par nom d'utilisateur/mot de passe RFC 1929 et le tunneling de domaine ; le proxy HTTP prend en charge l'authentification de base. Un nouveau bouton **Tester la connexion au proxy** s'exécute en arrière-plan et annonce la latence de votre connexion en millisecondes.
- **Mise en cache des fichiers vidéo pendant 48 heures :** Les vidéos importées sur Gemini sont mises en cache pendant 48 heures ! Vous pouvez régénérer les sorties SRT ou MP3 pour la même vidéo sans avoir à la réimporter, même après avoir redémarré NVDA. Le cache prend en compte les clés et est automatiquement invalidé lorsque votre clé API change.
- **Détection de silence alimentée par l'IA (Silero VAD)** : L'extension AD utilise désormais le modèle neuronal Silero VAD pour une détection précise des silences — distinguant les pauses naturelles du dialogue de la musique et du bruit de fond. Le modèle est téléchargé automatiquement lors de la première utilisation (avec votre permission), tout comme ffmpeg et eSpeak.
- **Vidéo de webcam pour l'assistant en direct** : La fenêtre de l'assistant en direct dispose désormais d'une case à cocher **Utiliser la webcam** pour envoyer le flux de votre webcam à l'IA au lieu de votre écran — idéal pour poser des questions sur des objets physiques, des documents ou votre environnement. Si ffmpeg n'est pas encore installé, le fait de cocher la case le télécharge (en une seule fois, avec votre permission). L'option est désactivée lorsqu'aucune caméra n'est détectée ou que les paramètres de confidentialité de Windows bloquent l'accès à la caméra, avec un bouton pour ouvrir les paramètres de confidentialité de la caméra. Si la caméra est activée mais ne produit aucune image, le problème est consigné dans le journal NVDA pour diagnostic au lieu de basculer silencieusement vers l'écran.
- **Sélection du périphérique de sortie audio** : Vous pouvez désormais sélectionner un périphérique de sortie audio dédié pour l'assistant en direct et l'observateur ambiant. Choisissez entre la sortie par défaut de NVDA, le Mappeur de sons Windows ou toute carte son physique connectée (comme un casque USB ou des haut-parleurs externes) dans l'onglet Paramètres en direct, directement dans la boîte de dialogue de l'assistant en direct, ou à la volée via les Paramètres rapides (NVDA+Maj+V puis Haut/Bas/Gauche/Droite).
- **Gestionnaire d'invites** : L'onglet Invites par défaut dispose désormais d'une liste de **filtres**, vous permettant d'afficher toutes les invites ou une seule section (par exemple **Ambiant**). Vous pouvez également y modifier les textes de contexte de l'observateur et la nouvelle **Instruction d'opérateur en direct**.
- **Filtrage intelligent des modèles dans le routage avancé** : Les menus déroulants du routage avancé des modèles catégorisent désormais dynamiquement les modèles Gemini par capacité sans encombrement. L'assistant en direct n'affiche que les véritables modèles en direct bidirectionnels et à audio natif, le TTS n'affiche que les modèles de synthèse vocale dédiés, le STT donne la priorité aux modèles de transcription et multimodaux, et l'analyse vidéo, l'OCR et l'opérateur IA filtrent proprement les modèles utilitaires à usage unique (tels que la génération d'images, la génération de vidéos et les modèles d'incorporation). Les futurs modèles sont détectés automatiquement en fonction de leurs capacités sans nécessiter de mises à jour de version.
- **Suivi de la première apparition des personnages** : L'IA décrit désormais l'apparence physique de chaque personnage une seule fois — lors de sa première apparition dans la vidéo. Les apparitions ultérieures n'utilisent que les noms, éliminant les descriptions répétitives d'un segment à l'autre tout en gardant le récit frais et naturel.
- **Répertoire de données unifié** : Tous les fichiers de données de l'extension (historique, séries, étiquettes, progression de l'OCR, caches et journaux) ont été migrés vers un seul dossier `VisionAssistant` dans votre répertoire de configuration NVDA — ce qui permet de garder tout organisé et de faciliter les sauvegardes manuelles.
- **Expérience d'enregistrement vidéo améliorée** : Lors de l'enregistrement de fichiers SRT ou MP3, la boîte de dialogue de fichier s'ouvre désormais par défaut dans le dossier de la vidéo source, que vous ouvriez la vidéo via la boîte de dialogue de fichier ou Maj+V depuis l'Explorateur.
- **Supprimer des documents avec ou sans leur texte mis en cache** : La boîte de dialogue Historique (`Ctrl + H`) offre désormais deux façons de supprimer un document — appuyez sur Suppr et choisissez **Supprimer de l'historique uniquement** ou **Supprimer de l'historique et du texte mis en cache**. La deuxième option efface le texte OCR mis en cache pour ce document, de sorte que la prochaine ouverture le rescannera à partir de zéro — idéal après un mauvais scan. Une case à cocher **Ne plus demander** mémorise votre choix pour les suppressions futures. Vos données de reprise d'opération interrompue ne sont jamais touchées.
- **Cache OCR intelligent et fusionnel dans le lecteur de documents** : Le texte OCR mis en cache est désormais stocké par moteur OCR, de sorte que le changement de moteur OCR réanalyse toujours avec le nouveau moteur au lieu de rejouer l'ancien résultat. La réouverture d'un document affiche à nouveau la boîte de dialogue de plage de pages (pré-remplie avec votre dernier choix), réutilisant instantanément les pages déjà scannées et ne scannant que celles qui manquent — le cache fusionne page par page au lieu d'être remplacé, de sorte que chaque plage que vous lisez est conservée pour plus tard.
- **Compression PDF dans le lecteur de documents** : Ajout d'un paramètre optionnel **Compresser les pages PDF avant le traitement** dans la boîte de dialogue de plage de pages du lecteur de documents. Lors du téléchargement de documents PDF scannés volumineux ou haute résolution vers Gemini ou Mistral, les pages sont automatiquement réduites et recompressées pour réduire considérablement la taille de la charge utile de téléchargement, accélérer le traitement et éviter les délais d'attente réseau. L'option est désactivée par défaut et automatiquement masquée lors de l'utilisation du moteur Chrome ou de fournisseurs d'images basés sur base64.
- **Personnalisation du comportement des commentaires par invite** : Personnalisez la façon dont chaque invite personnalisée fournit son résultat individuellement ! Dans l'éditeur d'invites personnalisées, choisissez entre **Paramètre global**, **Copier dans le presse-papiers**, **Sortie directe (message NVDA)**, **Copier dans le presse-papiers et sortie directe** ou **Fenêtre de discussion**. Cela permet à des invites spécifiques de s'exprimer directement sans ouvrir de fenêtre tandis que d'autres ouvrent une discussion complète.
- **Nouvelles variables d'invite dynamiques (`[currentURL]` et `[text]`)** : Les invites personnalisées prennent désormais en charge `[currentURL]` pour capturer l'URL du document actif dans Google Chrome, Mozilla Firefox et Microsoft Edge, et `[text]` pour insérer dynamiquement le contenu textuel complet du champ de saisie actuellement ciblé (en ignorant les boîtes de mot de passe protégées).
- **Refonte du téléchargeur de vidéos Twitter/X** : Rétablissement du téléchargement et de l'analyse des vidéos Twitter/X suite à des pannes des scrapers en amont. L'extraction vidéo utilise désormais l'API robuste FixTweet pour récupérer directement les flux MP4 de plus haute qualité depuis le CDN de Twitter, avec en plus une solution de repli automatique TwitSave et la prise en charge des proxys.
- **Correction du téléchargeur de vidéos Instagram** : Rétablissement du téléchargement et de l'analyse des Reels Instagram et des URL de vidéos suite à des modifications de formulaires en amont sur le service de téléchargement.
- **Corrections et performances** : Push to Talk répond dès que vous appuyez sur la touche, l'assistant en direct ne commence plus une réponse au milieu d'une phrase, l'observateur ne signale plus l'image précédente et la liste de profondeur de réflexion ne propose que ce que votre modèle prend réellement en charge. L'opérateur IA peut également faire défiler horizontalement (gauche et droite). Correction d'une erreur `AttributeError` lors de l'analyse de vidéos en ligne, et empêchement des invites personnalisées sans sélection de texte d'injecter accidentellement des titres de fenêtres d'arrière-plan dans les requêtes IA.

## Modifications pour 2026.09.01

- **Historique (Control + H)** : La couche de commandes inclut désormais une boîte de dialogue **Historique** (`Control + H`) qui répertorie vos chats et documents passés avec des filtres pour Tout, Chats et Documents. Rouvrez n'importe quel chat avec sa conversation complète — les fichiers joints sont rattachés automatiquement — ou rouvrez un document et poursuivez votre lecture. Appuyez sur **Delete** sur n'importe quel élément pour le supprimer, ou effacez tout en une seule fois.
- Appuyer sur **D** dans la couche de commandes affiche d'abord la liste de vos documents récemment lus. Choisissez-en un pour reprendre la lecture à la page où vous étiez — même si la ROC est déjà terminée — ou appuyez sur **Ouvrir un fichier...** (`Ctrl + O`) pour rechercher un fichier comme d'habitude.
- **Fonction Pousser pour parler pour l'Assistant en direct** : Prenez le contrôle total de vos conversations en direct ! Activez **Pousser pour parler** dans le nouvel onglet de paramètres de l'Assistant en direct et assignez n'importe quelle touche — ou même un modificateur seul comme `Ctrl Gauche` — pour parler. Maintenez la touche enfoncée pour parler et relâchez-la lorsque vous avez terminé, avec un bref bip à chaque pression et relâchement. Un commutateur correspondant apparaît également directement dans la fenêtre de l'Assistant en direct, ce qui vous permet de basculer entre le mode pousser pour parler et le mode micro ouvert sans quitter la conversation.
- **Audio natif Gemini 2.5 Flash** : L'Assistant en direct prend désormais en charge le modèle audio natif de Gemini 2.5 Flash (`gemini-2.5-flash-native-audio-preview-12-2025`) pour des conversations vocales naturelles et à faible latence. Vous pouvez y basculer depuis **Paramètres → Routage de modèle avancé → Modèle de l'Assistant en direct (Gemini uniquement)**, ou laisser « Auto » pour conserver le modèle recommandé.
- **Sauvegarde et restauration des paramètres** : Ajout d'un système de sauvegarde et de restauration puissant dans l'onglet **Avancé** ! Vous pouvez désormais enregistrer tous les paramètres de votre add-on — y compris les clés API, les modèles, les invites personnalisées et les préférences — dans un seul fichier JSON, et les restaurer parfaitement à tout moment, sur n'importe quelle machine, ou après avoir réinstallé NVDA. Lors de la sauvegarde, vous choisissez ce qu'il faut inclure : **Tout** (paramètres, étiquettes personnalisées, progression de l'OCR et historique) ou **Paramètres uniquement**.
- **Lecture directe de texte et HTML** : Le lecteur de documents peut désormais ouvrir directement les fichiers texte brut (`.txt`) et HTML (`.html`, `.htm`) ! Il détecte automatiquement l'encodage du fichier, supprime les scripts et le superflu de formatage, et découpe intelligemment le contenu en pages lisibles — réimportant même ses propres fichiers exportés tout en préservant la structure des pages — afin que vous puissiez les lire instantanément sans OCR ni traitement par IA !
- **Synthèse vocale (TTS) Gemini Live pour le lecteur de documents** : Le bouton « Générer de l'audio » prend désormais en charge Gemini Live, un moteur de synthèse vocale en streaming de haute qualité et au rythme naturel ! Lorsque Gemini est votre fournisseur actif, vous pouvez choisir entre la synthèse vocale standard et Gemini Live directement dans le lecteur, et votre sélection est mémorisée pour la prochaine fois !
- **Raccourcis d'invites personnalisées** : Vous pouvez désormais assigner une touche de raccourci à n'importe laquelle de vos invites personnalisées directement depuis le Gestionnaire d'invites ! Attribuez à chaque invite sa propre touche dédiée ou combinaison de touches pour l'exécuter instantanément, en capturant automatiquement votre sélection ou votre contexte actuel sans aucune étape supplémentaire !
- **Navigation dans les messages du chat** : Révisez n'importe quelle conversation les mains libres ! Dans n'importe quelle fenêtre de chat (Chat direct, chat sur document, affinement, etc.), appuyez sur `Alt + Bas` pour entendre le message suivant et `Alt + Haut` pour entendre le précédent — avec des préfixes clairs « Vous » / « IA » et des limites annoncées telles que « Premier message » / « Dernier message » au fil de votre navigation.
- **Copier le message du chat (Alt + C)** : Lors de la révision d'une conversation avec `Alt + Haut/Bas`, appuyez sur `Alt + C` pour copier le message sur lequel vous vous trouvez dans le Presse-papiers — en respectant votre paramètre de balisage propre (Clean Markdown) — avec une confirmation vocale.
- **Invite système du chat direct** : Le chat direct (`Shift+C`) possède désormais sa propre invite système modifiable — « Instruction du chat direct » — qui définit la personnalité de l'assistant et la langue de réponse pour chaque conversation. Vous pouvez la personnaliser depuis l'onglet Invites par défaut du Gestionnaire d'invites.
- **Navigation par page du curseur du lecteur de documents** : La lecture de documents de plusieurs pages est devenue plus fluide ! Dans la visionneuse de documents, lorsque votre curseur atteint la dernière ligne d'une page et que vous appuyez sur `Bas`, le lecteur passe automatiquement à la page suivante. Appuyer sur `Haut` au début d'une page vous ramène de manière transparente à la précédente — plus besoin de changer de page manuellement pendant la lecture !
- **Nouveaux commutateurs de paramètres rapides** : La copie des réponses de l'IA dans le Presse-papiers, la sortie directe (sans fenêtre de chat), le balisage propre dans le chat et l'échange intelligent (Smart Swap) peuvent désormais être activés et désactivés instantanément depuis les paramètres rapides de la couche de commandes !
- **Onglet de paramètres de l'Assistant en direct** : L'Assistant en direct dispose désormais de son propre onglet de paramètres dédié ! L'option « Assistant en direct : Sortie directe (pas de fenêtre) » a été déplacée ici depuis l'onglet Connexion, et cet onglet n'apparaît que lorsque Google Gemini (ou un fournisseur personnalisé compatible Gemini) est votre fournisseur actif.

## Modifications pour 2026.08.06

- **Étiquetage dans l'explorateur d'interface (UI Explorer)** : Vous pouvez désormais ajouter des étiquettes directement aux éléments trouvés dans l'explorateur d'interface ! Un nouveau bouton « Ajouter une étiquette » a été ajouté, et l'interface reste intelligemment ouverte tout en préservant le focus, ce qui vous permet d'étiqueter rapidement plusieurs objets sans interruption.
- **Amélioration de la couche des paramètres rapides** : La couche de Vision Assistant (`Insert+Shift+V`) est désormais persistante et hautement interactive ! Vous pouvez utiliser les flèches `Haut/Bas` pour naviguer entre les paramètres rapides (Fournisseur, Modèle, Langue de réponse de l'IA, Modèle TTS) et les flèches `Gauche/Droite` pour modifier instantanément leurs valeurs avec un retour vocal intelligent et concis. Vos sélections prennent effet immédiatement (incluant l'activation automatique du routage avancé si nécessaire), et la couche reste active pendant que vous configurez.
- **Chat direct (`Shift+C`)** : Ajout d'une nouvelle commande à la couche ! Appuyez sur `Shift+C` pour ouvrir instantanément une fenêtre de « Chat direct ». Cela fournit immédiatement une interface de conversation textuelle claire avec l'IA, sans nécessiter d'image ou de document comme point de départ.
- **Rappel parfait de l'historique de chat** : Correction d'un bug majeur où l'appui sur la touche `Space` pour rappeler le dernier résultat faisait perdre l'historique de chat suivant. Désormais, l'add-on suit globalement votre conversation. Si vous discutez, fermez la boîte de dialogue et appuyez sur `Space` pour la rappeler, l'intégralité de votre historique d'échange est parfaitement restaurée ! Fonctionne pour le Chat direct, l'analyse visuelle, le chat sur documents et la traduction.
- **Descriptions d'images en ligne dans l'OCR** : Ajout d'une fonctionnalité optionnelle pour décrire les images en ligne lors de l'OCR de documents. Vous pouvez activer ou désactiver ce paramètre dans les options OCR de l'add-on, dans les options du lecteur de documents avant l'extraction, et rapidement à la volée via la couche des paramètres rapides.
- **Traduction vocale (`Control+T`)** : Ajout d'une nouvelle fonctionnalité puissante ! Dictez de la parole et traduisez-la et saisissez-la instantanément à l'aide de l'IA en fonction de vos langues source et cible configurées.
- **Améliorations du téléchargeur de mises à jour** : La boîte de dialogue de téléchargement des mises à jour affiche désormais correctement la progression du téléchargement en pourcentage, et un bug où un message fantôme « Téléchargement de la mise à jour » apparaissait lors de l'annulation de l'installation a été corrigé.
- **Améliorations du téléchargeur eSpeak-NG** : Ajout du suivi de la progression en pourcentage pour les téléchargements d'eSpeak-NG.
- **Résilience de l'OCR par lot** : Correction d'un problème dans l'OCR PDF par lot où le processus s'arêtait si la clé API active atteignait son quota en cours de route ; l'add-on bascule désormais automatiquement vers la clé suivante disponible et reprend le processus.
- **Prise en charge des Captchas visuels** : Ajout d'une prise en charge robuste pour la résolution de captchas visuels. L'add-on tente de résoudre automatiquement les défis d'images complexes tels que hCaptcha et reCAPTCHA, améliorant considérablement l'accessibilité sur les formulaires web difficiles.
- **Refonte du transcripteur audio** : Le module de transcription audio a été entièrement reconstruite et prend désormais en charge les fichiers audio et vidéo. Il propose 3 modes de fonctionnement distincts : « Transcrire (Langue originale) », « Transcrire et traduire (Langue cible) », et une nouvelle option puissante « Doubler et traduire (Langue cible) » (exclusive à Gemini) qui génère un doublage audio traduit de la parole d'origine. It features 3 distinct operation modes: "Transcribe (Original Language)", "Transcribe and Translate (Target Language)", and a new powerful "Dub and Translate (Target Language)" option (exclusive to Gemini) that generates a translated audio dub of the original speech.
- **Numéros de page optionnels dans le lecteur de documents** : Ajout d'un nouveau paramètre pour activer ou désactiver l'inclusion des numéros de page et des séparateurs dans les sorties de documents multipages. Vous pouvez facilement gérer cette option depuis les paramètres principaux ou l'activer/désactiver à la volée via la couche des paramètres rapides. Cette fonctionnalité s'applique à la fois aux exportations de fichiers texte/HTML et à la fenêtre en ligne « Afficher mis en forme », vous permettant de lire des documents combinés de manière transparente.
- **TTS Gemini Live illimité pour les descriptions vidéo** : Vous pouvez désormais sélectionner « Gemini Live TTS » comme moteur vocal lors de la génération d'une narration audio synchronisée (MP3) pour les vidéos. Cela utilise l'API Gemini Live pour synthétiser des descriptions audio de haute qualité sans aucune limite de caractères ni restriction de longueur.
- **Modularisation de la base de code** : Refactorisation de la structure de l'add-on, passant d'un fichier unique à une architecture modulaire multi-fichiers pour une meilleure maintenabilité.
- **Refonte de l'interface des paramètres** : Refonte complète de la boîte de dialogue des paramètres pour utiliser une interface moderne basée sur des onglets au lieu d'une disposition groupée, offrant une meilleure organisation et une navigation plus aisée tout en conservant toutes les options existantes.
- **Journalisation de fichiers globale et dédiée** : Ajout d'un système optionnel de journalisation globale dans le nouvel onglet de paramètres « Avancé ». Capture automatiquement les événements opérationnels, le trafic API et les erreurs de tous les modules de l'add-on dans un fichier dédié (`vision_assistant.log`). Prend en charge des niveaux de verbosité des journaux configurables (Débogage, Info, Avertissement, Erreur), des périodes de rétention automatisées (1 heure à 90 jours), ainsi que l'ouverture directe ou l'effacement des journaux depuis les paramètres sans impact sur les performances ni interférence avec le journal NVDA.
- **Suivi de la progression du téléversement Gemini** : Ajout d'annonces de progression en pourcentage en temps réel lors du téléversement de fichiers volumineux (vidéo, audio, documents) vers l'API Google Gemini.

## Modifications pour la version 2026.07.15

- **Filtrage intelligent des modèles d'API** : Refonte complète du système de filtrage des modèles pour utiliser une approche par liste noire pure au lieu de listes blanches. Ajout de mots-clés de filtrage plus stricts (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`) pour garantir que la liste déroulante principale des modèles de discussion reste parfaitement propre et pérenne, tout en maintenant l'accessibilité de tous les modèles spécialisés dans la section de routage avancé.
- **Recherche dans le routage avancé** : Toutes les listes déroulantes de routage de modèles avancé (OCR, STT, TTS, Opérateur, Vidéo, Direct) ainsi que le sélecteur de variante eSpeak sont désormais entièrement interrogeables. Vous pouvez taper rapidement du texte pour filtrer et trouver le modèle ou la variante souhaité.
- **Nouveaux raccourcis de la couche de commandes** :
  - **Paramètres (`Alt + S`)** : Ouvre instantanément la boîte de dialogue des paramètres de Vision Assistant Pro.
  - **Rapport des clés dont le quota est épuisé (`Alt + Q`)** : Indique le nombre exact de clés d'API Gemini qui ont dépassé leur quota journalier, précise le modèle spécifique pour lequel elles sont épuisées, et annonce leur heure exacte de réinitialisation.
  - **Audit du routage (`Alt + M`)** : Audite et annonce votre configuration de routage avancé actuelle, en énumérant les modèles activement sélectionnés pour les tâches spécialisées (en ignorant les paramètres par défaut).
- **Refonte complète de l'analyseur vidéo** : L'analyseur vidéo a été entièrement transformé ! Auparavant, il se contentait de fournir une description basique des vidéos en ligne. Il s'agit désormais d'une suite de traitement vidéo complète conçue pour les utilisateurs non-voyants :
  - **Enregistrement d'écran local (`Control+V`)** : Vous pouvez désormais enregistrer des vidéos silencieuses directement depuis votre écran. L'IA analysera le segment enregistré et fournira une description très détaillée de la scène, de la mise en page et des actions.
  - **Génération de descriptions audio (SRT)** : L'add-on peut désormais générer des scripts de description audio très détaillés (au format standard SRT) pour les vidéos, dotés d'une gestion intelligente de l'espacement temporel pour ancrer judicieusement les descriptions sur les pauses naturelles de la piste audio, ainsi que d'une reconnaissance optique de caractères (OCR) textuelle exacte.
  - **Narration audio synchronisée (Exportation MP3)** : Au-delà des sous-titres textuels, l'add-on peut synthétiser la description audio en parole, la mélanger automatiquement avec la piste audio originale de la vidéo, appliquer une atténuation audio (baisse du volume de fond pendant les descriptions) et exporter le résultat final synchronisé sous forme de fichier MP3 !
  - **Action intelligente sur les fichiers vidéo** : Si vous vous placez sur un fichier vidéo local et appuyez sur le raccourci vidéo, l'add-on le détectera automatiquement et traitera le fichier directement.
  - **Suivi avancé des personnages** : L'IA effectue désormais une pré-passe d'extraction des personnages. Elle établit un dictionnaire global des personnages et suit ces derniers avec précision, segment par segment, sans confusion d'identité.
  - **Configuration de l'analyse vidéo** : Ajout de nouveaux paramètres pour contrôler la taille des segments SRT, le sous-titrage des personnages et les avertissements.
  - **Routage de modèles étendu** : Vous pouvez désormais sélectionner explicitement des modèles vidéo spécialisés (`gemini_video_model`, `custom_video_model`) dans les paramètres de routage de modèles avancé.
- **Gestion intelligente des quotas d'API** : Amélioration de la gestion des erreurs 429 (limite journalière) en suivant les quotas par modèle. Si une clé atteint sa limite journalière sur un modèle, elle est intelligemment mise en quarantaine pour ce modèle spécifique uniquement, ce qui laisse la clé disponible pour une utilisation avec d'autres modèles.

## Modifications pour la version 7.0.0

- **Reprise des analyses inachevées** : Ajout d'une fonction de reprise pour le Lecteur de documents et les Actions intelligentes sur les fichiers. Si une analyse est interrompue, vous pouvez désormais continuer là où elle s'est arrêtée au lieu de recommencer depuis le début.
- **Nouvelle variable `[screen_fg_obj]`** : Ajout d'une variable de invite personnalisée pour capturer une capture d'écran de la fenêtre active au premier plan uniquement, plutôt que de tout l'écran.
- **Nouvelles tentatives intelligentes et rotation des clés** : L'add-on réessaye désormais silencieusement jusqu'à 5 fois avec la même clé en cas de surcharge temporaire du serveur (telle qu'une "forte demande" ou des réponses mal formées). Si les tentatives échouent, il bascule automatiquement sur la clé API suivante de votre liste.
- **Détection du rideau d'écran** : Ajout d'une vérification pour empêcher la prise de captures d'écran lorsque le Rideau d'écran est actif (qu'il soit activé en permanence ou basculé temporairement via le raccourci clavier). Il vous avertira et s'arrêtera, évitant ainsi d'envoyer des images noires et de gaspiller des jetons API.
- **Ajustements du Lecteur de documents** : La boîte de dialogue de plage de pages PDF pré-sélectionne désormais automatiquement la langue cible par défaut définie dans les paramètres de votre add-on. La gestion des threads a également été améliorée pour garantir que les tâches en arrière-plan s'arrêtent proprement lorsque le lecteur est fermé.
- **Intégration native de l'OCR Mistral** : Intégration de l'API Document OCR native de Mistral. Les documents de plusieurs pages sont automatiquement fusionnés, téléchargés et traités par lots à l'aide de l'endpoint spécialisé `/v1/ocr` de Mistral, tandis que les images d'une seule page sont traitées directement sans conversions PDF inutiles [1].
- **Gestionnaires d'URL personnalisés dynamiques** : La modification de l'URL d'API personnalisée efface instantanément la liste des modèles mis en cache et restaure la zone de texte de saisie manuelle du modèle. Cela garantit une compatibilité totale avec les endpoints personnalisés (tels que Cloudflare AI Gateway) qui ne prennent pas en charge l'endpoint de liste standard `/v1/models`.
- **Refonte du moteur de saisie de l'Opérateur IA** : Réécriture complète du système sous-jacent de simulation de la souris et du clavier pour l'Opérateur IA. Remplacement de l'ancienne API `mouse_event` par l'API moderne Windows `SendInput`, apportant une compatibilité nettement supérieure avec les applications modernes, les fenêtres protégées par l'UAC et les écrans à haute résolution (DPI).
- **Correction des opérations de Glisser-Déposer** : Les actions de glisser-déposer dans l'Opérateur IA sont désormais parfaitement stables et fiables. Le nouveau moteur utilise des courbes d'accélération/décélération ("easing") naturelles, un positionnement précis du curseur, des temporisations optimisées et une technique de "légère poussée" (nudge) intelligente pour garantir que Windows et les applications reconnaissent et exécutent correctement les gestes de glisser-déposer sans échec en cours de route.
- **Prise en charge multi-moniteur** : L'Opérateur IA prend désormais entièrement en charge les configurations multi-moniteurs. Les mouvements de souris et les clics fonctionnent correctement sur tous les moniteurs grâce à l'indicateur `MOUSEEVENTF_VIRTUALDESK`, garantissant un positionnement précis quel que soit le moniteur sur lequel se trouve l'application cible.
- **Simulation de clavier améliorée** : Amélioration de l'injection de frappes pour prendre entièrement en charge les "touches étendues" (telles que les flèches directionnelles, Début, Fin, Page précédente/suivante, Insertion, Suppression et F1-F12). Cela garantit que les commandes de navigation et les raccourcis envoyés par l'Opérateur IA fonctionnent parfaitement dans toutes les applications.
- **Prise en charge des images HEIC/HEIF** : Ajout d'une prise en charge native des formats de photo iPhone. Vous pouvez désormais sélectionner directement les fichiers `.heic` et `.heif` pour la description par IA, l'OCR ou la lecture de documents sans conversion préalable.

## Modifications pour la version 6.5.0

- **Assistant en direct** : Ajout d'une fonctionnalité d'assistant vocal et d'écran en temps réel, disponible exclusivement pour le fournisseur Google Gemini (ou les fournisseurs personnalisés compatibles avec Gemini). Comprend une voix interactive et une personnalisation de la profondeur de réflexion directement dans la boîte de dialogue, avec une reconnexion automatique lors de la modification des paramètres.
- **Fournisseur d'IA MiniMax** : Intégration de MiniMax en tant que fournisseur pair avec prise en charge multimodale complète (chat, vision, OCR), synthèse vocale (TTS) personnalisée utilisant plus de 300 voix dynamiques, et suppression automatique des blocs de raisonnement (par ex., ` thinking... response`) des sorties.
- **Traduction de la visionneuse de documents** : Correction d'un échec de traduction silencieux pour les utilisateurs de NVDA non anglophones en veillant à ce que le code de langue standard à 2 lettres soit envoyé à Google Translate au lieu du nom de la langue localisée.
- **Nouvelle tentative de numérisation par lots de PDF** : Implémentation d'une logique de nouvelle tentative hautement optimisée, séparée et silencieuse pour la numérisation par lots de documents PDF afin d'éviter les téléchargements redondants et d'éliminer les fenêtres contextuelles d'erreur gênantes lors des nouvelles tentatives.
- **État de la visionneuse de documents** : Correction d'un bogue où l'état global du module complémentaire (vérifié via `I`) restait bloqué sur « Traitement par lots démarré » lors de la numérisation de documents longs.
- **Correction d'un plantage de thread** : Correction d'un plantage grave par assertion de thread `IsMain() failed in wxTimerImpl` lors de l'ouverture de documents à partir d'un thread d'arrière-plan en faisant transiter la file d'attente des rappels de l'interface graphique vers `wx.CallAfter`.

## Modifications de la version 6.1.2

- **Vérification préalable des doublons d'étiquettes** : Correction d'un problème lors de l'étiquetage unique où la vérification des doublons utilisait d'anciennes clés de coordonnées, ce qui amenait NVDA à effectuer des requêtes IA dupliquées pour des objets déjà étiquetés au lieu d'annoncer l'étiquette existante.
- **Discussion sur les documents pour les fournisseurs autres que Gemini** : Correction d'une vérification stricte de la clé API dans la discussion sur les documents (`on_ask`) pour garantir que les utilisateurs d'OpenAI, de Groq ou de fournisseurs personnalisés locaux (comme Ollama) peuvent discuter avec des documents sans être bloqués.
- **Traduction rapide par OCR pour Chrome** : Restauration de l'API de traduction gratuite et sans clé pour l'OCR de Chrome. La traduction du texte extrait contourne désormais l'IA Gemini, ce qui permet d'économiser les quotas d'API et d'accélérer le processus de traduction.
- **Filtre alphanumérique pour CAPTCHA** : Correction de la logique de filtrage dans le résolveur de CAPTCHA pour s'assurer que les caractères non alphanumériques sont correctement nettoyés dans toutes les situations.
- **Mise à jour de l'aide de la couche de commandes** : Correction du raccourci d'annonce d'état dans le menu d'aide, qui passe de `L` à `I`, et ajout des deux commandes d'étiquetage (`L` et `Shift+L`) à la liste.

## Modifications pour la version 6.1.1

- **Correction de la sortie de réflexion pour Gemma 4** : Correction d'un problème avec les modèles Gemma 4 où l'ensemble du processus de réflexion interne était affiché comme réponse finale, ou où la désactivation de la réflexion entraînait des réponses vides. L'add-on isole et extrait désormais correctement uniquement la réponse textuelle finale et propre.
- **OCR par lot depuis l'Explorateur de fichiers** : Vous pouvez désormais sélectionner plusieurs photos ou PDF directement dans l'Explorateur de fichiers de Windows et en extraire le texte ou les analyser par lot. L'add-on filtrera et traitera automatiquement uniquement les formats de fichiers pris en charge.

## Modifications pour la version 6.1.0

- **Intégration universelle d'IA locale (Configuration d'IA locale)** : Ajout d'un nouveau bouton **« Configurer l'IA locale »** dans les paramètres du fournisseur personnalisé. Les utilisateurs peuvent désormais configurer automatiquement des moteurs d'IA locaux, notamment **Ollama**, **LM Studio**, **Jan.ai** et **KoboldCPP** instantanément.
- **Contournement intelligent du proxy local** : Refonte de la logique de connexion avec un mécanisme avancé de contournement de proxy. L'extension est désormais suffisamment intelligente pour contourner complètement les proxys système Windows pour les connexions de bouclage local (loopback), garantissant des connexions d'IA locales stables même lorsque votre VPN ou mode TUN est actif.
- **Étiquetage d'IA ultra-stable (v2)** : Remplacement des clés de coordonnées absolues de l'écran par un système hybride avancé de **signature d'objets** (Object Signature). Les étiquettes reposent désormais sur des identifiants programmatiques (**AutomationId** UIA ou **ControlID** Win32) et des coordonnées relatives à la fenêtre, rendant vos étiquettes personnalisées totalement résistantes au redimensionnement, au déplacement, au changement de moniteur ou à la mise à l'échelle des fenêtres.
- **Migration automatique et transparente des étiquettes** : La mise à niveau est totalement transparente. L'extension migrera automatiquement vos anciennes étiquettes basées sur des coordonnées vers le nouveau format d'empreinte stable en arrière-plan dès la première prise de focus, sans aucune perte de données.

## Modifications pour la version 6.0

- **Introduction de l'étiquetage IA sémantique** : Les utilisateurs peuvent désormais étiqueter de manière permanente les boutons et icônes sans nom à l'aide de l'IA. Appuyez sur **L** pour étiqueter l'objet du navigateur actuel (prenant en charge à la fois le focus Tabulation et la navigation par objets) ou sur **Shift+L** pour analyser et étiqueter l'application entière en une seule fois.
- **Gestion intelligente des étiquettes** : Ajout d'une nouvelle boîte de dialogue de gestion des étiquettes entièrement accessible (via **Shift+L** si des étiquettes existent) pour afficher, renommer ou supprimer par lot des étiquettes personnalisées.
- **Analyse directe de fichiers (contournement de la boîte de dialogue de fichier)** : L'add-on est désormais suffisamment intelligent pour détecter si vous avez actuellement le focus sur un fichier PDF ou une image dans l'Explorateur Windows. Appuyer sur **F (Action intelligente sur fichier)** ou **D (Lecteur de documents)** sur un fichier mis en surbrillance le traitera immédiatement, en contournant entièrement la boîte de dialogue « Ouvrir » standard.

## Modifications pour la version 5.6

- **Ajout du moteur OCR "Aucun (Extraire la couche de texte)"** : Les utilisateurs peuvent désormais extraire du texte directement à partir de PDF interrogeables sans utiliser de crédits d'IA, ce qui améliore considérablement la vitesse et la confidentialité pour les documents textuels.
- **Précision affinée de l'Explorateur d'interface utilisateur** : Amélioration de l'invite (prompt) de l'Explorateur d'interface utilisateur pour mieux identifier les types d'éléments (tels que les éléments de liste) et signaler avec précision les états tels que "(Coché)", "(Sélectionné)" ou "(Développé)", tout en ignorant les composants système de Windows tels que la barre des tâches et l'horloge.
- **Rappel de configuration de l'installation** : Ajout d'une notification après l'installation pour guider les utilisateurs vers le menu des paramètres afin de configurer leurs clés API et leurs préférences.

## Modifications pour la version 5.5.2

- **Correction du problème de saisie de l'opérateur IA :** Résolution d'un bogue où la lettre « v » était tapée au lieu de coller du texte sur certains systèmes. Cette correction résout les conflits de minutage qui se produisaient lors d'une charge système élevée.
- **Stabilité améliorée :** Ajout d'une gestion robuste des erreurs pour les opérations du presse-papiers afin d'éviter les plantages de l'add-on lorsque le presse-papiers du système est temporairement verrouillé par d'autres applications.
- **Optimisation du minutage :** Ajustement des délais internes pour les événements de clavier afin d'garantir une plus grande fiabilité sur différentes vitesses de système et une meilleure compatibilité avec les gestionnaires de presse-papiers tiers.

## Changements de la version 5.5 (La mise à jour de l'automatisation)

- **Opérateur IA (Contrôle autonome - Shift+A) :** C'est le joyau de la version 5.5. Vision Assistant Pro a évolué, passant d'un assistant passif à votre propre **Opérateur IA**. Il ne se contente plus de décrire l'écran, il prend le contrôle.
  - _Fonctionnement :_ Vous pouvez désormais donner des instructions textuelles ou vocales pour utiliser votre PC. Par exemple, dans une application complètement inaccessible où votre lecteur d'écran reste silencieux, vous pouvez appuyer sur **Shift+A** et taper : _"Clique sur le bouton Paramètres"_ ou _"Trouve le champ de recherche, tape 'Dernières nouvelles' et appuie sur Entrée"_. L'IA identifie visuellement les éléments, déplace la souris et exécute la tâche pour vous.
  - _Note de performance :_ Cette fonctionnalité est optimisée pour **Gemini 3.0 Flash (Preview)**, offrant des réponses incroyablement rapides et intelligentes capables de gérer les interfaces utilisateur les plus complexes.
  - **⚠️ Avertissement sur l'utilisation de l'API :** Puisque l'Opérateur IA a besoin de "voir" exactement ce qui se passe pour être précis, il envoie une capture d'écran haute résolution à chaque étape. Veuillez noter qu'une utilisation fréquente consommera votre quota d'API beaucoup plus rapidement que les tâches textuelles standard.
- **Explorateur d'interface visuelle (E) :** Fatigué de naviguer à travers des "boutons sans étiquette" ? Appuyez sur **E** pour activer l'Explorateur d'interface. L'IA va analyser toute la fenêtre et générer une liste de chaque élément cliquable visible, y compris les icônes, les graphiques et les menus. Choisissez simplement un élément dans la liste, et l'Opérateur IA cliquera dessus pour vous. C'est comme avoir une "couche accessible" par-dessus n'importe quelle application.
- **Action intelligente sur les fichiers adaptée au contexte (F) :** La touche "F" a été entièrement repensée. Elle ne part plus du principe que vous souhaitez uniquement faire de l'OCR. Lorsque vous sélectionnez une seule image, elle vous demande désormais intelligemment votre intention : vous pouvez choisir une **Description visuelle détaillée** pour comprendre la scène ou une **Extraction de texte structurée (OCR)** pour la lecture. Le menu s'adapte dynamiquement en fonction du type de fichier et de votre moteur d'IA actif.
- **Optimisation du noyau :** Nous avons effectué un nettoyage en profondeur de la logique interne de l'add-on, en supprimant les anciennes fonctions inutilisées et le code redondant. Il en résulte une expérience plus légère, plus rapide et plus fiable pour tous les utilisateurs.

## Modifications pour la version 5.0

- **Architecture multi-fournisseur** : Ajout d'une prise en charge complète pour **OpenAI**, **Groq** et **Mistral** aux côtés de Google Gemini. Les utilisateurs peuvent désormais choisir leur moteur IA préféré.
- **Routage de modèles avancé** : Les utilisateurs de fournisseurs natifs (Gemini, OpenAI, etc.) peuvent désormais sélectionner des modèles spécifiques dans une liste déroulante pour différentes tâches (OCR, STT, TTS).
- **Configuration avancée des points de terminaison** : Les utilisateurs de fournisseurs personnalisés peuvent saisir manuellement des URL spécifiques et des noms de modèles pour un contrôle granulaire des serveurs locaux ou tiers.
- **Visibilité intelligente des fonctionnalités** : Le menu des paramètres et l'interface du lecteur de documents masquent désormais automatiquement les fonctionnalités non prises en charge (comme la TTS) en fonction du fournisseur sélectionné.
- **Récupération dynamique des modèles** : L'add-on récupère désormais la liste des modèles disponibles directement depuis l'API du fournisseur, garantissant la compatibilité avec les nouveaux modèles dès leur sortie.
- **OCR et traduction hybrides** : Optimisation de la logique pour utiliser Google Translate pour plus de rapidité lors de l'utilisation de l'OCR de Chrome, et une traduction propulsée par l'IA lors de l'utilisation des moteurs Gemini/Groq/OpenAI.
- **« Re-analyser avec l'IA » universel** : La fonction de re-analyse du lecteur de documents n'est plus limitée à Gemini. Elle utilise désormais le fournisseur d'IA actuellement actif pour re-traiter les pages.

## Changements pour 4.6

- **Rappel interactif des résultats :** Ajout de la touche **Espace** à la couche de commandes, permettant aux utilisateurs de rouvrir instantanément la dernière réponse de l'IA dans une fenêtre de discussion pour poser des questions de suivi, même lorsque le mode « Sortie directe » est actif.
- **Carrefour de la communauté Telegram :** Ajout d'un lien vers le « Canal Telegram officiel » dans le menu Outils de NVDA, offrant un moyen rapide de se tenir informé des dernières actualités, fonctionnalités et versions.
- **Stabilité des réponses améliorée :** Optimisation de la logique principale pour les fonctionnalités de Traduction, d'OCR et de Vision afin de garantir des performances plus fiables et une expérience plus fluide lors de l'utilisation de la synthèse vocale directe.
- **Guidage de l'interface amélioré :** Mise à jour des descriptions des paramètres et de la documentation pour mieux expliquer le nouveau système de rappel et son fonctionnement avec les paramètres de sortie directe.

## Changes for 4.5

- **Advanced Prompt Manager:** Introduced a dedicated management dialog in settings to customize default system prompts and manage user-defined prompts with full support for adding, editing, reordering, and previewing.
- **Comprehensive Proxy Support:** Resolved network connectivity issues by ensuring that user-configured proxy settings are strictly applied to all API requests, including translation, OCR, and speech generation.
- **Automated Data Migration:** Integrated a smart migration system to automatically upgrade legacy prompt configurations to a robust v2 JSON format upon the first run without data loss.
- **Updated Compatibility (2025.1):** Set the minimum required NVDA version to 2025.1 due to library dependencies in advanced features like the Document Reader to ensure stable performance.
- **Optimized Settings Interface:** Streamlined the settings interface by reorganizing prompt management into a separate dialog, providing a cleaner and more accessible user experience.
- **Prompt Variables Guide:** Added a built-in guide within the prompt dialogs to help users easily identify and use dynamic variables such as [selection], [clipboard], and [screen_obj].

## Modifications pour la version 4.0.3

- **Résilience réseau améliorée :** Ajout d'un mécanisme de nouvelle tentative automatique pour mieux gérer les connexions Internet instables et les erreurs de serveur temporaires, garantissant des réponses de l'IA plus fiables.
- **Boîte de dialogue de traduction visuelle :** Introduction d'une fenêtre dédiée aux résultats de traduction. Les utilisateurs peuvent désormais naviguer facilement et lire les traductions longues ligne par ligne, de la même manière que les résultats de l'OCR.
- **Vue formatée agrégée :** La fonction « Afficher le format » du lecteur de documents affiche désormais toutes les pages traitées dans une seule fenêtre organisée, avec des en-têtes de page clairs.
- **Flux de travail OCR optimisé :** Ignore automatiquement la sélection de la plage de pages pour les documents d'une seule page, ce qui rend le processus de reconnaissance plus rapide et plus fluide.
- **Stabilité de l'API améliorée :** Passage à une méthode d'authentification par en-tête plus robuste, résolvant les erreurs potentielles « Toutes les clés API ont échoué » causées par des conflits de rotation des clés.
- **Corrections de bugs :** Résolution de plusieurs plantages potentiels, notamment un problème lors de la fermeture de l'extension et une erreur de focus dans la boîte de dialogue de discussion.

## Modifications pour la version 4.0.1

- **Lecteur de documents avancé :** Un nouveau visionneur puissant pour les fichiers PDF et les images, doté d'une sélection de plage de pages, d'un traitement en arrière-plan et d'une navigation fluide avec `Ctrl+PageUp`/`PageDown`.
- **Nouveau sous-menu Outils :** Ajout d'un sous-menu dédié « Vision Assistant » dans le menu Outils de NVDA pour un accès plus rapide aux fonctionnalités principales, aux paramètres et à la documentation.
- **Personnalisation flexible :** Vous pouvez désormais choisir votre moteur OCR préféré et votre voix TTS directement depuis le panneau des paramètres.
- **Prise en charge de clés API multiples :** Ajout de la prise en charge de plusieurs clés API Gemini. Vous pouvez saisir une clé par ligne ou les séparer par des virgules dans les paramètres.
- **Moteur OCR alternatif :** Introduction d'un nouveau moteur OCR pour garantir une reconnaissance de texte fiable même en cas de dépassement des limites de quota de l'API Gemini.
- **Rotation intelligente des clés API :** Bascule automatiquement sur la clé API fonctionnelle la plus rapide et mémorise celle-ci pour contourner les limites de quota.
- **Document vers MP3/WAV :** Capacité intégrée pour générer et enregistrer des fichiers audio de haute qualité aux formats MP3 (128 kbps) et WAV directement depuis le lecteur.
- **Prise en charge des Stories Instagram :** Ajout de la possibilité de décrire et d'analyser les Stories Instagram à l'aide de leurs URL.
- **Prise en charge de TikTok :** Introduction de la prise en charge des vidéos TikTok, permettant une description visuelle complète et une transcription audio des clips.
- **Fenêtre de mise à jour repensée :** Propose une nouvelle interface accessible avec une zone de texte défilante pour lire clairement les modifications de la version avant l'installation.
- **État et expérience utilisateur unifiés :** Standardisation des boîtes de dialogue de fichiers dans l'ensemble de l'add-on et amélioration de la commande `L` pour annoncer la progression en temps réel.

## Modifications pour la version 3.6.0

- **Système d'aide :** Ajout d'une commande d'aide (`H`) dans la couche de commandes (Command Layer) pour fournir une liste facilement accessible de tous les raccourcis et de leurs fonctions.
- **Analyse de vidéos en ligne :** Extension de la prise en charge pour inclure les vidéos de **Twitter (X)**. Amélioration également de la détection des URL et de la stabilité pour une expérience plus fiable.
- **Contribution au projet :** Ajout d'une boîte de dialogue de don optionnelle pour les utilisateurs qui souhaitent soutenir les futures mises à jour et la croissance continue du projet.

## Modifications pour la version 3.5.0

\*   \*\*Couche de commandes :\*\* Introduction d'un système de couche de commandes (par défaut : `NVDA+Shift+V`) pour regrouper les raccourcis sous une seule touche principale. Par exemple, au lieu d'appuyer sur `NVDA+Control+Shift+T` pour la traduction, vous appuyez désormais sur `NVDA+Shift+V` suivi de `T`.
\*   \*\*Analyse de vidéos en ligne :\*\* Ajout d'une nouvelle fonctionnalité permettant d'analyser directement des vidéos YouTube et Instagram en fournissant une URL.

## Modifications pour la version 3.1.0

- **Mode de sortie directe :** Ajout d'une option pour ignorer la boîte de dialogue de discussion et entendre les réponses de l'IA directement par synthèse vocale pour une expérience plus rapide et fluide.
- **Intégration du presse-papiers :** Ajout d'un nouveau paramètre pour copier automatiquement les réponses de l'IA dans le presse-papiers.

## Modifications pour la version 3.0

- **Nouvelles langues :** Ajout des traductions en **persian** et en **vietnamien**.
- **Modèles d'IA élargis :** Réorganisation de la liste de sélection des modèles avec des préfixes clairs (`[Gratuit]`, `[Pro]`, `[Auto]`) pour aider les utilisateurs à faire la distinction entre les modèles gratuits et ceux soumis à des limites de taux (payants). Ajout du support pour **Gemini 3.0 Pro** et **Gemini 2.0 Flash Lite**.
- **Stabilité de la dictée :** Amélioration significative de la stabilité de la dictée intelligente. Ajout d'une vérification de sécurité pour ignorer les clips audio de moins d'1 seconde, ce qui évite les hallucinations de l'IA et les erreurs dues à des fichiers vides.
- **Gestion des fichiers :** Correction d'un problème où le téléchargement de fichiers portant des noms non anglophones échouait.
- **Optimisation des invites :** Amélioration de la logique de traduction et structuration des résultats de la vision.

## Changements pour la version 2.9

- **Ajout des traductions en français et en turc.**
- **Vue mise en forme :** Ajout d'un bouton "Afficher mis en forme" dans les boîtes de dialogue de discussion pour afficher la conversation avec un style approprié (titres, gras, code) dans une fenêtre de navigation standard.
- **Paramètre Markdown :** Ajout d'une nouvelle option "Nettoyer le Markdown dans la discussion" dans les paramètres. Décocher cette option permet aux utilisateurs de voir la syntaxe Markdown brute (par exemple, `**`, `#`) dans la fenêtre de discussion.
- **Gestion des boîtes de dialogue :** Correction d'un problème où les fenêtres "Affiner le texte" ou de discussion s'ouvraient plusieurs fois ou ne prenaient pas correctement le focus.
- **Améliorations de l'expérience utilisateur (UX) :** Standardisation des titres des boîtes de dialogue de fichiers sur "Ouvrir" et suppression des annonces vocales redondantes (par exemple, "Ouverture du menu...") pour une expérience plus fluide.

## Changes for 2.8

- Ajout de la traduction italienne.
- **Rapport d'état :** Ajout d'une nouvelle commande (`NVDA+Control+Shift+I`) pour annoncer l'état actuel de l'add-on (par exemple, "Téléversement...", "Analyse en cours...").
- **Exportation HTML :** Le bouton "Enregistrer le contenu" dans les boîtes de dialogue de résultats enregistre désormais la sortie sous forme de fichier HTML formaté, en préservant les styles tels que les titres et le texte en gras.
- **Interface des paramètres :** Amélioration de la disposition du panneau des paramètres avec un regroupement accessible.
- **Nouveaux modèles :** Ajout de la prise en charge de `gemini-flash-latest` et `gemini-flash-lite-latest`.
- **Langues :** Ajout du népalais aux langues prises en charge.
- **Correction de la logique du menu :** Correction d'un bug critique où les commandes "Affiner le texte" échouaient si la langue de l'interface NVDA n'était pas l'anglais.
- **Dictée :** Amélioration de la détection du silence pour éviter une sortie de texte incorrecte lorsqu'aucun discours n'est prononcé.
- **Paramètres de mise à jour :** L'option "Vérifier les mises à jour au démarrage" est désormais désactivée par défaut pour se conformer aux politiques du Magasin des add-ons.
- Nettoyage du code.

## Modifications pour la version 2.7

- Migration de la structure du projet vers le modèle officiel d'extension NVDA (Add-on Template) pour une meilleure conformité aux normes.
- Implémentation d'une logique de nouvelle tentative automatique pour les erreurs HTTP 429 (limite de taux / Rate Limit) afin de garantir la fiabilité en cas de trafic élevé.
- Optimisation des invites de traduction pour une plus grande précision et une meilleure gestion de la logique de « Permutation intelligente » (Smart Swap).
- Mise à jour de la traduction russe.

## Modifications pour la version 2.6

- Ajout du support pour la traduction en russe (Merci à nvda-ru).
- Mise à jour des messages d'erreur pour fournir des retours plus explicites concernant la connectivité.
- Modification de la langue cible par défaut en anglais.

## Modifications pour la version 2.5

- Ajout d'une commande de reconnaissance optique de caractères (OCR) de fichiers natifs (`NVDA+Control+Shift+F`).
- Ajout d'un bouton « Enregistrer la discussion » dans les boîtes de dialogue de résultats.
- Implémentation d'un support complet pour la localisation (i18n).
- Migration du retour audio vers le module de tonalités natif de NVDA.
- Passage à l'API de fichiers Gemini pour une meilleure prise en charge des fichiers PDF et audio.
- Correction d'un plantage lors de la traduction de textes contenant des accolades.

## Modifications pour la version 2.1.1

- Correction d'un problème où la variable [file_ocr] ne fonctionnait pas correctement dans les invites personnalisées (Custom Prompts).

## Nouveautés de la version 2.1

- Standardisation de tous les raccourcis pour utiliser `NVDA+Ctrl+Maj` afin d'éliminer les conflits avec la disposition de clavier Ordinateur portable de NVDA et les raccourcis système.

## Modifications pour la version 2.0

- Implantation d'un système de mise à jour automatique intégré.
- Ajout d'un cache de traduction intelligent pour une récupération instantanée du texte déjà traduit.
- Ajout d'une mémoire de conversation pour affiner contextuellement les résultats dans les boîtes de dialogue de discussion.
- Ajout d'une commande dédiée à la traduction du presse-papiers (`NVDA+Control+Shift+Y`).
- Optimisation des invites (prompts) de l'IA pour imposer strictement la langue cible en sortie.
- Correction d'un plantage provoqué par des caractères spéciaux dans le texte saisi.

## Changements pour la version 1.5

- Ajout du support pour plus de 20 nouvelles langues.
- Implémentation d'une boîte de dialogue de raffinement interactif pour les questions de suivi.
- Ajout de la fonctionnalité de dictée intelligente native.
- Ajout de la catégorie « Vision Assistant » dans la boîte de dialogue Gestes de commande de NVDA.
- Correction des plantages de type COMError dans des applications spécifiques telles que Firefox et Word.
- Ajout d'un mécanisme de nouvelle tentative automatique en cas d'erreur de serveur.

## Modifications pour la version 1.0

- Version initiale.
