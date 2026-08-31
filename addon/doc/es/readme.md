# Documentación de Vision Assistant Pro

**Vision Assistant Pro** es un asistente de IA avanzado y multimodal para NVDA. Utiliza motores de IA de primer nivel para proporcionar lectura de pantalla inteligente, traducción, dictado por voz y análisis de documentos.

_Este complemento fue lanzado a la comunidad en honor al Día Internacional de las Personas con Discapacidad._

## 1. Configuración

Ve a **Menú de NVDA > Preferencias > Configuración > Vision Assistant Pro**. El diálogo de configuración está organizado en 9 pestañas accesibles: **Conexión**, **Asistente en vivo**, **Comportamiento de IA**, **Idiomas de traducción**, **Lector de documentos**, **Vídeo**, **CAPTCHA**, **Indicaciones** y **Avanzado**.

### 1.1 Pestaña Conexión
- **Proveedor:** Selecciona tu servicio de IA preferido. Los proveedores compatibles incluyen **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** y **Personalizado** (servidores compatibles con OpenAI como Ollama, LM Studio, Jan.ai o KoboldCPP).
- **Clave API:** Introduce una o varias claves API (separadas por comas o saltos de línea) para rotación automática.
- **Obtener modelos:** Presiona este botón después de introducir tu clave API para descargar la lista de modelos disponibles más reciente del proveedor.
- **Modelo de IA:** Selecciona el modelo principal utilizado para el chat general y análisis.
- **Configuración del proveedor personalizado:** Configura puntos de acceso locales o personalizados. Incluye **Configurar IA local** (configuración en un clic para Ollama, LM Studio, Jan.ai o KoboldCPP) y **Configuración avanzada de punto de acceso**.
- **Enrutamiento avanzado de modelos (específico por tarea):** Selecciona opcionalmente modelos dedicados desde desplegables para tareas de OCR, STT, TTS, Operador de IA, Vídeo y Asistente en vivo.
- **Opciones de conexión y salida:** Configura URL del proxy, comprobaciones de actualización al inicio, limpiar Markdown en el chat, copiar respuestas de IA al portapapeles y salida directa (sin ventana de chat).

### 1.2 Pestaña Asistente en vivo
- **Asistente en vivo: Salida directa (sin ventana):** Inicia el Asistente en vivo sin su ventana de conversación; ábrela después con la tecla Recuperar último resultado (`Espacio`).
- **Pulsar para hablar:** Activa el modo de pulsar para hablar. Cuando está activado, el micrófono solo envía audio mientras mantienes presionada la tecla asignada.
- **Tecla de pulsar para hablar:** Presiona las teclas para registrar el atajo (por ejemplo, `F12` o `Ctrl+F12`) — incluso puedes asignar un modificador solo como `Ctrl izquierdo`. Mantén la tecla para hablar y suéltala al terminar; un pitido corto confirma cada pulsación y suelta.

Nota: Esta pestaña aparece solo cuando **Google Gemini** (o un proveedor personalizado compatible con Gemini) es tu proveedor activo.

### 1.3 Pestaña Comportamiento de IA
- **Creatividad (Temperatura):** Controla la aleatoriedad y creatividad de la IA (de 0,0 a 2,0). Los valores más bajos producen resultados de traducción/OCR más deterministas y precisos.

### 1.4 Pestaña Idiomas de traducción
- **Idioma de origen:** Selecciona tu idioma de entrada predeterminado.
- **Idioma de destino:** Selecciona tu idioma de traducción de destino principal.
- **Idioma de respuesta de la IA:** Selecciona el idioma para las respuestas generales de la IA.
- **Intercambio inteligente:** Intercambia automáticamente los idiomas de origen y destino según el idioma detectado.

### 1.5 Pestaña Lector de documentos
- **Motor OCR:** Elige entre **Chrome (Rápido)** para resultados rápidos o **IA (Avanzado)** para una mejor conservación del diseño.
- **Tamaño del lote OCR:** Especifica páginas por solicitud (configura en 0 para procesamiento en una sola solicitud).
- **Describir imágenes en línea:** Activa o desactiva las descripciones de imágenes en línea durante la extracción de texto de documentos.
- **Incluir números de página al exportar:** Activa o desactiva los números de página y separadores en las salidas de documentos de varias páginas.
- **Voz TTS:** Selecciona el estilo de voz predeterminado para la generación de audio.

### 1.6 Pestaña Vídeo
- **Tamaño de fragmento de vídeo:** Duración del segmento en minutos para la generación de audiodescripción (configura en 0 para procesar el archivo completo).
- **Añadir lista de personajes:** Opción para añadir el diccionario de personajes como primera entrada de subtítulo.
- **Añadir aviso de IA:** Opción para insertar un aviso de IA al principio de los subtítulos SRT del vídeo.

### 1.7 Pestaña CAPTCHA
- **Habilitar solucionador visual de CAPTCHA:** Activa o desactiva la resolución automática de desafíos visuales (hCaptcha, reCAPTCHA).
- **Método de CAPTCHA de texto:** Elige entre capturar el **Objeto del navegador** o la **Pantalla completa**.

### 1.8 Pestaña Indicaciones
- **Administrar indicaciones:** Abre un diálogo dedicado para personalizar las indicaciones predeterminadas del sistema o crear, editar, reordenar y previsualizar indicaciones personalizadas con variables dinámicas (por ejemplo, `[selection]`, `[screen_fg_obj]`).
- **Atajos para indicaciones personalizadas:** Asigna una tecla de atajo dedicada a cualquier indicación personalizada directamente en el Administrador de indicaciones. Presiona las teclas para registrarlas — las teclas simples funcionan dentro de la Capa de comandos (y globalmente como `NVDA + Shift + tecla`), mientras que las combinaciones como `Control + Shift + 1` funcionan globalmente por sí solas.

### 1.9 Pestaña Avanzado y registro global
Navega a la pestaña **Avanzado** para configurar el registro global del complemento:
- **Habilitar archivo de registro dedicado:** Activa el registro de todos los eventos operativos, tráfico de API y errores en todos los módulos del complemento en un archivo separado (`vision_assistant.log`).
- **Nivel de registro:** Selecciona la verbosidad entre **Depuración (todos los detalles)**, **Información (información general)**, **Advertencia (solo advertencias)** y **Error (solo errores)**.
- **Conservar registros durante:** Configura períodos de retención automática para limpiar entradas de registro antiguas (desde 1 hora hasta 90 días).
- **Controles de gestión de registros:** Usa **Abrir archivo de registro**, **Abrir carpeta de registro** o **Limpiar archivo de registro** para inspeccionar o borrar datos de registro directamente sin reiniciar NVDA.

### 1.10 Copia de seguridad y restauración de configuración
La pestaña **Avanzado** también incluye una sección de **Copia de seguridad y restauración**:
- **Copia de seguridad:** Guarda tu configuración en un único archivo JSON. Al hacer clic, eliges qué incluir: **Todo** (configuración, etiquetas personalizadas, progreso de OCR e historial) o **Solo configuración**.
- **Restaurar:** Carga una copia de seguridad guardada previamente para restaurar tu configuración y datos en cualquier momento, en cualquier equipo o después de reinstalar NVDA. Se te pedirá confirmación primero, ya que la restauración reemplaza toda la configuración y datos actuales.

## 2. Capa de comandos y atajos

Para evitar conflictos de teclado, este complemento usa una **Capa de comandos**.
1. Presiona **NVDA + Shift + V** (tecla maestra) para activar la capa (escucharás un pitido).
2. Suelta las teclas, luego presiona una de las siguientes teclas individuales:

| Tecla             | Función                          | Descripción                                                                 |
|-------------------|----------------------------------|-----------------------------------------------------------------------------|
| **Shift + A**     | **Operador de IA**               | **Operación autónoma:** Indica a la IA que realice una tarea en tu pantalla. Presionarlo de nuevo cancela las operaciones activas al instante. |
| **E**             | **Explorador de interfaz**       | **Clic interactivo:** Identifica y hace clic en elementos de la interfaz en cualquier aplicación. |
| **T**             | Traductor inteligente            | Traduce el texto bajo el cursor del navegador o la selección.               |
| **Shift + T**     | Traductor del portapapeles       | Traduce el contenido que hay actualmente en el portapapeles.                |
| **R**             | Refinador de texto               | Resume, corrige gramática, explica o ejecuta **Indicaciones personalizadas**. |
| **V**             | Visión de objeto                 | Describe el objeto del navegador actual.                                    |
| **O**             | Visión de pantalla completa      | Analiza el diseño y contenido completo de la pantalla.                      |
| **Shift + V**     | Análisis de vídeo                | Analiza archivos de vídeo locales o vídeos en línea de **YouTube**, **Instagram**, **TikTok** o **Twitter (X)**. |
| **Control + V**   | Grabación de vídeo local         | Graba un vídeo silencioso de tu pantalla y analiza las acciones y el diseño. |
| **D**             | Lector de documentos             | Lector avanzado de PDF, imágenes y archivos de texto/HTML con selección de rango de páginas. |
| **F**             | **Acción inteligente de archivo**| Reconocimiento contextual desde imagen, PDF o archivos TIFF seleccionados.  |
| **M**             | Transcripción y doblaje de medios| Transcribe o dobla archivos de audio/vídeo (MP3, WAV, MP4, etc.) a tu idioma de destino. |
| **C**             | Solucionador de CAPTCHA          | Captura y resuelve CAPTCHAs.                                                |
| **Shift + C**     | Chat directo                     | Abre una interfaz de chat de texto directo con la IA.                       |
| **S**             | Dictado inteligente              | Convierte voz a texto. Presiona para iniciar la grabación, vuelve a presionar para detener/escribir. |
| **Control+T**     | Traducción de voz                | Transcribe, traduce y escribe el resultado según la configuración de idioma. |
| **Control+L**     | **Asistente en vivo**            | **Copiloto en tiempo real (solo Gemini):** Inicia o finaliza una conversación de voz y pantalla en vivo con el asistente de IA. |
| **I**             | Informe de estado                | Anuncia el progreso actual (por ejemplo, "Escaneando...", "Inactivo").      |
| **L**             | **Etiquetar objeto**             | **Etiquetado semántico con IA:** Etiqueta permanentemente el elemento/icono enfocado actualmente. |
| **Shift + L**     | **Administrar/Escanear etiquetas**| Abre el administrador de etiquetas (si existen etiquetas) o escanea la aplicación en busca de elementos sin nombre. |
| **U**             | Buscar actualizaciones           | Busca manualmente en GitHub la última versión del complemento.              |
| **Espacio**       | Recuperar último resultado       | Muestra la última respuesta de IA en un diálogo de chat para revisión o seguimiento. |
| **H**             | Ayuda de comandos                | Muestra una lista de todos los atajos disponibles.                          |
| **Control + H**   | **Historial**                    | Abre el diálogo de historial con tus chats y documentos anteriores, con filtros por tipo y opciones de eliminar/borrar. |
| **Alt + S**       | Configuración                    | Abre el diálogo de configuración de Vision Assistant Pro.                   |
| **Alt + Q**       | Informe de claves con cuota agotada | Informa sobre el número de claves API de Gemini que han superado su cuota diaria y su hora de restablecimiento. |
| **Alt + M**       | Auditoría de enrutamiento        | Informa sobre los modelos de IA actualmente seleccionados en el enrutamiento avanzado. |
| **Arriba / Abajo**| Navegar configuración rápida     | Navega entre categorías de configuración rápida (Proveedor, Modelo, etc.) en la capa. |
| **Izquierda / Derecha** | Cambiar configuración rápida | Cambia el valor de la configuración rápida actualmente seleccionada.      |

## 3. Chat e Historial

Las ventanas de chat y el diálogo de historial funcionan en todas las funciones, para que puedas revisar conversaciones y continuar exactamente donde lo dejaste.

### 3.1 Atajos de la ventana de chat
Cuando hay una ventana de chat abierta (Chat directo, chat de documento, refinar y similares), puedes revisar la conversación con:
- **Alt + Abajo:** Leer el siguiente mensaje.
- **Alt + Arriba:** Leer el mensaje anterior.
- **Alt + C:** Copiar el mensaje actual.

### 3.2 Historial (Control + H)
Presiona **Control + H** en la Capa de comandos para abrir el diálogo de **Historial** con tus chats y documentos anteriores, filtrables por tipo (Todo / Chats / Documentos). Abre un chat para continuar la conversación — incluyendo sus archivos adjuntos, que se vuelven a adjuntar automáticamente — o abre un documento y sigue leyendo. Presiona **Eliminar** en cualquier elemento para quitarlo, o **Borrar todo** para vaciar la lista.

## 4. Operador de IA — Control autónomo del equipo

El **Operador de IA** convierte Vision Assistant Pro de un lector pasivo en un asistente activo capaz de interactuar con tu equipo en tu nombre. Puedes pedirle que describa la pantalla, responda preguntas sobre lo que ve, o tome el control: hacer clic en botones, arrastrar elementos, escribir texto y navegar por aplicaciones mediante comandos en lenguaje natural.

La mayor ventaja es que funciona perfectamente en software completamente inaccesible. Si estás atascado en una aplicación personalizada, un escritorio remoto o un sitio web donde tu lector de pantalla permanece en silencio, al Operador no le importa. Como "ve" la pantalla visualmente, puede encontrar, leer e interactuar con elementos que no tienen ninguna etiqueta de accesibilidad.

### Cómo funciona
1. Presiona **NVDA + Shift + V**, luego presiona **Shift + A** para abrir el diálogo del Operador de IA.
2. Escribe lo que quieres hacer en lenguaje natural (por ejemplo, "Haz clic en el botón Guardar", "¿Qué dice el mensaje de error?" o "Cambia el nombre del archivo a final.pdf").
3. La IA analizará tu pantalla, identificará los elementos relevantes y realizará la acción o proporcionará la respuesta. Si una tarea requiere varios pasos, el Operador continuará trabajando hasta completarla.
4. Presiona **Shift + A** de nuevo en cualquier momento para cancelar una operación en curso al instante.

### Acciones compatibles
- **Describir y responder**: "Describe el diseño de la pantalla" o "¿Qué dice el mensaje de error?"
- **Clic**: "Haz clic en el botón Guardar"
- **Clic derecho**: "Haz clic derecho en el archivo"
- **Doble clic**: "Haz doble clic en el documento"
- **Arrastrar y soltar**: "Arrastra el documento a la carpeta Archivo"
- **Escribir**: "Escribe 'Hola Mundo' en el cuadro de búsqueda"
- **Desplazar**: "Desplázate hacia abajo tres veces"
- **Tecla**: "Presiona Enter", "Presiona Tab", "Presiona Escape"
- **Tareas de varios pasos**: "Abre el Explorador de archivos, encuentra el informe y cámbiale el nombre a final.pdf"

### Notas importantes
- **⚠️ Advertencia de uso de API:** El Operador envía una captura de pantalla de alta resolución con cada paso. El uso frecuente consumirá tu cuota de API mucho más rápido que las funciones estándar.
- **Aplicaciones de administrador:** Si NVDA no se ejecuta con privilegios de administrador, es posible que el Operador no pueda interactuar con ventanas que requieren permisos elevados.
- **Mejores prácticas:** Da comandos claros y específicos. "Haz clic en el botón azul Enviar en la parte inferior del formulario" funcionará mejor que simplemente "Haz clic en el botón".

## 5. Análisis de vídeo y audiodescripción

> **Nota:** Las funciones de análisis de vídeo y audiodescripción funcionan exclusivamente con el proveedor **Google Gemini**. Asegúrate de que tu proveedor activo sea Google Gemini.

### 5.1 Grabación de pantalla local (Control + V)
1. Presiona **NVDA + Shift + V** para entrar en la Capa de comandos, luego presiona **Control + V**.
2. El complemento grabará silenciosamente tu pantalla en segundo plano.
3. Presiona **Control + V** de nuevo para detener la grabación.
4. La IA analizará el segmento de vídeo grabado y proporcionará una descripción muy detallada.

### 5.2 Análisis de vídeo (Shift + V)
Selecciona un archivo de vídeo local en el Explorador de Windows, o copia un enlace en línea al portapapeles. También puedes presionar **Shift + V** en cualquier lugar para abrir un diálogo donde examinar un archivo o pegar una URL.
- **Plataformas en línea compatibles:** YouTube, Instagram, TikTok y Twitter (X).

### 5.3 Generación de audiodescripción (SRT)
- **Temporización inteligente de pausas:** La IA ancla las descripciones a los silencios naturales del audio para minimizar la superposición con el diálogo.
- **Seguimiento de personajes:** Pre-pasada de extracción de personajes con diccionario global para rastrearlos con precisión entre escenas.
- **OCR textual literal:** Cualquier texto en pantalla (carteles, teléfonos, créditos) se cita literalmente.
- **Cómo usar:** Coloca el archivo `.srt` en la misma carpeta que tu vídeo con el mismo nombre. Configura tu reproductor multimedia (VLC, PotPlayer) para enrutar los subtítulos a tu lector de pantalla durante la reproducción.

### 5.4 Narración de audio sincronizada (exportación a MP3)
Puedes elegir **TTS de Gemini en vivo** como motor de voz para narración de alta calidad y sin límites de caracteres. Modos de mezcla disponibles para vídeos locales:
- **AD estándar (mezclar voz):** La narración se superpone sobre el audio del vídeo. Puedes aplicar **Atenuación de audio** para bajar el volumen de fondo.
- **AD extendida (pausar audio):** El motor pausa el audio original durante las descripciones.
- **Vídeos de YouTube:** El MP3 contendrá solo la pista de voz de la IA sincronizada, sin el audio de fondo.

## 6. Transcripción y doblaje de medios (M)

El transcriptor de audio ha sido completamente reconstruido para admitir archivos de audio y vídeo (MP3, WAV, MP4, MKV, etc.). Presiona **M** en la Capa de comandos para seleccionar un archivo multimedia y elegir uno de los 3 modos de operación:
1. **Transcribir (idioma original)**: Transcribe con precisión el habla en su idioma original.
2. **Transcribir y traducir (idioma de destino)**: Transcribe el habla y la traduce al idioma de destino configurado.
3. **Doblar y traducir (idioma de destino)** *(solo Gemini)*: Transcribe el habla, la traduce al idioma de destino y sintetiza un doblaje de audio hablado usando el motor TTS del complemento.

## 7. Lector avanzado de documentos e imágenes

El **Lector de documentos** convierte tus documentos en texto legible y limpio. Maneja PDFs de varias páginas, imágenes complejas, formatos HEIC de iPhone y archivos de texto sin formato (`.txt`) y HTML (`.html`, `.htm`), que se abren instantáneamente sin OCR ni IA. Selecciona varios archivos a la vez y se fusionan en un único documento continuo. Hay tres motores OCR disponibles — **Chrome (Rápido)**, **IA (Avanzado)** y **Ninguno (Extraer capa de texto)** para PDFs con capacidad de búsqueda — seleccionables en Configuración → Lector de documentos.

### Cómo funciona
1. Presiona **NVDA + Shift + V**, luego **D** para abrir el Lector de documentos — o resalta primero un archivo en el Explorador de archivos y presiona **D** / **F** para omitir el diálogo de archivo.
2. Elige uno o más PDFs o imágenes. El complemento los escanea y anuncia el número total de páginas.
3. En el diálogo **Opciones**, elige el rango de páginas. También puedes marcar **Traducir salida** y elegir el idioma de destino, o activar **Describir imágenes en línea durante el OCR**.
4. La extracción de texto comienza en segundo plano por lotes. Puedes cerrar la ventana en cualquier momento y continuar después.
5. Una vez que las páginas estén listas, léelas en el visor: muévete entre páginas, salta a cualquier página, hazle preguntas a la IA, guarda el texto o genera una narración de audio.

### 7.1 Procesamiento en lotes y reanudación
Elige un rango de páginas (por ejemplo, `1-20`) y la IA extrae todas las páginas en segundo plano. Si NVDA se bloquea o interrumpes el escaneo, el complemento recuerda tu progreso y ofrece **Reanudar** exactamente donde lo dejaste. Los documentos completados también se guardan en caché, por lo que volver a abrirlos carga el texto instantáneamente sin volver a ejecutar el OCR.

### 7.2 Acción inteligente de archivo
En el Explorador de archivos de Windows, resalta un PDF, imagen o archivo de texto/HTML y presiona **D** (Lector de documentos) o **F** (Acción inteligente de archivo) dentro de la Capa de comandos. El complemento omite instantáneamente el diálogo de archivo y comienza a procesar el archivo resaltado. Seleccionar varios archivos a la vez los procesa juntos como un único documento.

### 7.3 Controles y atajos del visor de documentos

#### Atajos de teclado
- **Ctrl + AvPág / Ctrl + RePág:** Ir a la página siguiente / anterior.
- **Flecha Abajo / Arriba:** Al llegar al final de una página, presiona **Abajo** para saltar a la siguiente; presiona **Arriba** al principio de una página para volver a la anterior.
- **Alt + A:** Abrir un diálogo de chat para hacer preguntas sobre el documento.
- **Alt + R:** Forzar un **Nuevo escaneo con IA** usando tu proveedor activo.
- **Alt + G:** Generar y guardar un archivo de audio de alta calidad (WAV/MP3). *Oculto si el proveedor no admite TTS.*
- **Alt + S / Ctrl + S:** Guardar el texto extraído como archivo TXT o HTML.

#### Botones y controles
- **Ir a:** Elige cualquier página desde el selector de páginas.
- **Ver formateado:** Ver el documento completo combinado como texto formateado.
- **Reintentar páginas fallidas:** Reintenta solo los lotes que fallaron por un error temporal del servidor. Este botón aparece automáticamente cuando es necesario.
- **Voz TTS / Motor TTS:** Elige la voz y, en Gemini, selecciona entre **TTS estándar** y **Gemini en vivo** (streaming).
- **Anterior / Siguiente:** Muévete entre páginas.

### 7.4 Documentos recientes (D)
Presionar **D** en la Capa de comandos lista primero tus documentos leídos recientemente. Elige uno para continuar desde la página donde lo dejaste, o presiona **Abrir archivo...** (`Ctrl + O`) para explorar un archivo como siempre.

## 8. Etiquetado semántico con IA y Explorador de interfaz

### 8.1 Etiquetado permanente de objetos (L)
Enfoca tu lector de pantalla en un gráfico o botón sin etiquetar y presiona **L** en la Capa de comandos. La IA determinará su función y aplicará una etiqueta permanente usando un sistema avanzado híbrido de "firma de objeto" (AutomationId/ControlID) que sobrevive al redimensionamiento de ventanas, cambio de monitor y actualizaciones de la aplicación.

### 8.2 Escaneo completo de la aplicación (Shift + L)
Presiona **Shift + L** para escanear toda la ventana activa de una vez. La IA encontrará todos los elementos sin etiquetar y los nombrará inteligentemente. Luego puedes administrar, renombrar o eliminar en lote estas etiquetas desde el Administrador de etiquetas incorporado.

### 8.3 Explorador de interfaz (E)
Presiona **E** para activar el Explorador de interfaz. La IA escaneará la pantalla y generará una lista accesible de cada elemento en el que se puede hacer clic (ignorando el ruido del sistema como las barras de tareas). Elige un elemento de la lista y el complemento hará clic en él instantáneamente. Ahora también puedes añadir etiquetas directamente a los elementos encontrados mediante el botón **Añadir etiqueta**.

## 9. Asistente en vivo

El Asistente en vivo convierte Vision Assistant Pro en un copiloto interactivo en tiempo real.
*(Nota: Esta función es exclusiva de Google Gemini y los proveedores personalizados compatibles con Gemini).*

- **Activación:** Presiona **Control + L** en la Capa de comandos.
- **Interacción en tiempo real:** Habla naturalmente a través de tu micrófono. La IA escuchará tu voz y mirará simultáneamente tu pantalla activa.
- **Pulsar para hablar:** Activa **Pulsar para hablar** en la pestaña de configuración del Asistente en vivo (o actívalo dentro de la ventana del Asistente en vivo), luego mantén la tecla asignada para hablar y suéltala al terminar. Mantiene el micrófono silenciado hasta que presionas la tecla.
- **Personalización:** Dentro del diálogo, puedes cambiar el estilo de voz de la IA y ajustar su "Profundidad de razonamiento".

## 10. Indicaciones personalizadas y variables

Puedes administrar las indicaciones en **Configuración > Indicaciones > Administrar indicaciones...**.

### Atajos para indicaciones personalizadas
Asigna a cualquier indicación personalizada su propia tecla de atajo directamente en el Administrador de indicaciones:
- **Tecla simple** (por ejemplo, `1`, `p` o `F3`): Funciona dentro de la Capa de comandos, y también globalmente como `NVDA + Shift + tecla`.
- **Combinación de teclas** (por ejemplo, `Control + Shift + 1`, `Alt + P` o `Insert + 1`): Funciona globalmente por sí sola.

### Variables compatibles
- `[selection]`: Texto seleccionado actualmente.
- `[clipboard]`: Contenido del portapapeles.
- `[clipboard_image]`: Imagen actualmente en el portapapeles.
- `[screen_obj]`: Captura de pantalla del objeto del navegador.
- `[screen_fg_obj]`: Captura de pantalla de la ventana activa en primer plano.
- `[screen_full]`: Captura de pantalla completa.
- `[file_ocr]`: Seleccionar imagen/PDF para extracción de texto.
- `[file_read]`: Seleccionar documento para leer (TXT, Código, PDF).
- `[file_audio]`: Seleccionar archivo de audio para análisis (MP3, WAV, OGG).
- `{target_lang}`: Idioma de destino actual.
- `{source_lang}`: Idioma de origen actual.
- `{response_lang}`: Idioma actual de respuesta de la IA.
- `{swap_target}`: Idioma alternativo para traducción con intercambio inteligente.
- `{swap_instruction}`: Bloque de instrucción de traducción con intercambio inteligente.

## 11. Casos de uso reales (¿Qué función debo usar?)

- **Quieres entender el diseño completo de una ventana complicada o inaccesible.**
  *Presiona **O** (Visión de pantalla completa).*

- **Encontraste una imagen en una página web o un gráfico sin etiquetar en un documento.**
  *Mueve tu objeto del navegador al gráfico y presiona **V** (Visión de objeto).*

- **Quieres ver una película o un videoclip con audiodescripción.**
  *Presiona **Shift + V** en tu vídeo, elige **"Generar audiodescripción (archivo SRT)"**. Cuando termine, haz clic en **"Generar narración sincronizada (MP3)"** y selecciona **"AD extendida"**.*

- **Encontraste una aplicación llena de "botones sin etiqueta".**
  *Presiona **L** para etiquetar permanentemente el botón específico. O presiona **Shift + L** para escanear toda la ventana. Si solo quieres hacer clic en algo rápidamente, presiona **E** (Explorador de interfaz).*

- **Necesitas superar un CAPTCHA inaccesible.**
  *Presiona **C** (Solucionador de CAPTCHA).*

- **Quieres leer un documento PDF largo de 50 páginas.**
  *Presiona **D** (Lector de documentos), configura el proveedor como Google Gemini e introduce el rango de páginas `1-50`.*

- **Estás viendo un tutorial de vídeo silencioso o una animación en tu pantalla.**
  *Presiona **Control + V** para comenzar a grabar la pantalla. Deja que el tutorial se reproduzca, luego presiona **Control + V** de nuevo.*

- **Encuentras un error inesperado, fallo de conexión a la API o quieres diagnosticar problemas con servidores locales personalizados.**
  *Ve a **Configuración > Avanzado**, marca **"Habilitar archivo de registro dedicado"** y configura el **Nivel de registro** en **"Depuración"**. Realiza la acción de nuevo, luego haz clic en **"Abrir archivo de registro"** para inspeccionar los detalles técnicos o adjunta `vision_assistant.log` a un ticket de soporte.*

***
**Nota:** Se requiere una conexión a Internet activa para todas las funciones de IA. Los documentos de varias páginas se procesan automáticamente.

## 12. Soporte y comunidad

- **Canal de Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **GitHub Issues:** Para informes de errores y solicitudes de funciones.

### Informar errores y registros
Al abrir un issue en GitHub o pedir soporte, incluye detalles sobre tu proveedor de IA activo, modelo y versión de NVDA. Si experimentas problemas de conexión o fallos inesperados, habilita el archivo de registro dedicado en **Configuración > Avanzado**, reproduce el problema y adjunta tu archivo `vision_assistant.log`.

## 13. Colaboradores del proyecto

Un agradecimiento de corazón a los miembros de nuestra comunidad que apoyan el desarrollo continuo y el mantenimiento de este proyecto con sus generosas contribuciones económicas:

*   **@Alyabani94**
*   **Ali Alamri**
*   **Ilya**
*   **Colaborador anónimo** (`UQDd...CnMY`)
*   **leonardo0216**
*   **Sergei Fleytin**
*   **Suman Gayen**

*Si deseas apoyar el proyecto económicamente y ver tu nombre aquí, puedes encontrar la opción **Donar** en el menú Herramientas de NVDA (submenú Vision Assistant) o durante el proceso de configuración después de la instalación.*

---
## Cambios para 2026.09.01

*   **Historial (Control + H)**: La Capa de comandos ahora incluye un diálogo de **Historial** (`Control + H`) que lista tus chats y documentos anteriores con filtros para Todo, Chats y Documentos. Reabre cualquier chat con toda la conversación — los archivos adjuntos se vuelven a adjuntar automáticamente — o reabre un documento y sigue leyendo. Presiona **Eliminar** en cualquier elemento para quitarlo, o borra todo de una vez.
*   **Documentos recientes en el Lector**: Presionar **D** en la Capa de comandos ahora muestra primero tus documentos leídos recientemente. Elige uno para continuar desde la página donde lo dejaste, o presiona **Abrir archivo...** (`Ctrl + O`) para explorar como siempre.
*   **Pulsar para hablar en el Asistente en vivo**: Activa **Pulsar para hablar** en la nueva pestaña de configuración del Asistente en vivo y asigna cualquier tecla — incluso un modificador solo como `Ctrl izquierdo` — para hablar. Mantén la tecla para hablar y suéltala al terminar, con un pitido corto en cada pulsación y suelta. También aparece un activador en la propia ventana del Asistente en vivo.
*   **Audio nativo de Gemini 2.5 Flash**: El Asistente en vivo ahora admite el modelo de audio nativo de Gemini 2.5 Flash (`gemini-2.5-flash-native-audio-preview-12-2025`) para conversaciones de voz naturales y con baja latencia.
*   **Copia de seguridad y restauración de configuración**: Se añadió un potente sistema de copia de seguridad y restauración en la pestaña **Avanzado**. Guarda toda la configuración del complemento — incluidas claves API, modelos, indicaciones personalizadas y preferencias — en un único archivo JSON y restáurala en cualquier momento, en cualquier equipo o después de reinstalar NVDA.
*   **Lectura directa de texto y HTML**: El Lector de documentos ahora puede abrir archivos de texto sin formato (`.txt`) y HTML (`.html`, `.htm`) directamente, sin OCR ni IA.
*   **TTS de Gemini en vivo para el Lector de documentos**: El botón "Generar audio" ahora admite Gemini en vivo — un motor TTS de streaming de alta calidad y ritmo natural. Cuando Gemini es tu proveedor activo, puedes elegir entre TTS estándar y Gemini en vivo directamente en el lector.
*   **Atajos para indicaciones personalizadas**: Ahora puedes asignar una tecla de atajo a cualquiera de tus indicaciones personalizadas desde el Administrador de indicaciones.
*   **Navegación por mensajes del chat**: Dentro de cualquier ventana de chat, presiona `Alt + Abajo` para escuchar el siguiente mensaje y `Alt + Arriba` para el anterior — con prefijos claros "Tú" / "IA" y límites "Primer mensaje" / "Último mensaje" anunciados.
*   **Copiar mensaje del chat (Alt + C)**: Mientras revisas una conversación, presiona `Alt + C` para copiar el mensaje actual al portapapeles.
*   **Indicación del sistema del Chat directo**: El Chat directo (`Shift+C`) ahora tiene su propia indicación del sistema editable — "Instrucción de chat directo" — que establece la personalidad del asistente y el idioma de respuesta para cada conversación.
*   **Navegación por cursor en el Lector de documentos**: Al llegar al final de una página y presionar `Abajo`, el lector salta automáticamente a la siguiente página. Presionar `Arriba` al principio de una página regresa a la anterior.
*   **Nuevos activadores de configuración rápida**: Copiar respuestas de IA al portapapeles, salida directa (sin ventana de chat), limpiar Markdown en el chat e intercambio inteligente ya se pueden activar y desactivar al instante desde la configuración rápida de la capa de comandos.
*   **Pestaña de configuración del Asistente en vivo**: El Asistente en vivo ahora tiene su propia pestaña de configuración dedicada. La opción "Asistente en vivo: Salida directa (sin ventana)" se movió aquí desde la pestaña Conexión, y la pestaña aparece solo cuando Google Gemini (o un proveedor personalizado compatible con Gemini) es tu proveedor activo.

## Cambios para 2026.08.06

*   **Etiquetado en el Explorador de interfaz**: Ahora puedes añadir etiquetas directamente a los elementos encontrados dentro del Explorador de interfaz. Se ha añadido un nuevo botón "Añadir etiqueta", y la interfaz permanece abierta y conserva el foco para que puedas etiquetar rápidamente varios objetos sin interrupciones.
*   **Mejora de la capa de configuración rápida**: La capa de Vision Assistant (`Insert+Shift+V`) es ahora persistente y muy interactiva. Puedes usar las flechas `Arriba/Abajo` para navegar entre configuraciones rápidas (Proveedor, Modelo, Idioma de respuesta de la IA, Modelo TTS) y las flechas `Izquierda/Derecha` para cambiar sus valores al instante con retroalimentación de voz concisa. Tus selecciones tienen efecto inmediato y la capa permanece activa mientras configuras.
*   **Chat directo (`Shift+C`)**: Se añadió un nuevo comando a la capa. Presiona `Shift+C` para abrir instantáneamente una ventana de "Chat directo". Proporciona una interfaz conversacional limpia y basada en texto con la IA de inmediato, sin necesitar una imagen o documento como punto de partida.
*   **Recuperación de historial de chat sin fallos**: Se corrigió un error importante donde presionar `Espacio` para recuperar el último resultado perdía el historial de chat subsiguiente. Ahora, el complemento realiza un seguimiento global de tu conversación. Si chateas, cierras el diálogo y presionas `Espacio` para recuperarlo, todo tu historial de ida y vuelta se restaura perfectamente. Funciona para Chat directo, Análisis de visión, Chat de documento y Traducción.
*   **Descripciones de imágenes en línea en el OCR**: Se añadió una función opcional para describir imágenes en línea durante el OCR de documentos. Puedes activar esta configuración en las opciones del complemento, dentro de las opciones del Lector de documentos antes de la extracción, y rápidamente sobre la marcha mediante la capa de configuración rápida.
*   **Traducción de voz (`Control+T`)**: Se añadió una nueva y poderosa función. Dicta habla e instantáneamente tradúcela y escríbela usando IA según los idiomas de origen y destino configurados.
*   **Mejoras en el descargador de actualizaciones**: El diálogo de descarga de actualizaciones ahora muestra correctamente el progreso de descarga en porcentajes, y se corrigió un error donde aparecía un mensaje fantasma "Descargando actualización" al cancelar la instalación.
*   **Mejoras en el descargador de eSpeak-NG**: Se añadió seguimiento de progreso en porcentaje para las descargas de eSpeak-NG.
*   **Resistencia del OCR en lotes**: Se corrigió un problema en el OCR de PDF en lotes donde el proceso se detenía si la clave API activa alcanzaba su cuota a mitad del proceso; ahora cambia automáticamente a la siguiente clave disponible y reanuda el proceso.
*   **Soporte de CAPTCHA visual**: Se añadió soporte robusto para la resolución de CAPTCHA visual. Intenta resolver automáticamente desafíos de imagen complejos como hCaptcha y reCAPTCHA.
*   **Revisión completa del transcriptor de audio**: El módulo transcriptor de audio se ha reconstruido completamente y ahora admite archivos de audio y vídeo. Presenta 3 modos de operación distintos: "Transcribir (idioma original)", "Transcribir y traducir (idioma de destino)" y el nuevo y poderoso "Doblar y traducir (idioma de destino)" (exclusivo de Gemini).
*   **Números de página opcionales en el Lector de documentos**: Se añadió una nueva configuración para activar o desactivar la inclusión de números de página y separadores en las salidas de documentos de varias páginas.
*   **TTS de Gemini en vivo ilimitado para descripciones de vídeo**: Ahora puedes seleccionar "TTS de Gemini en vivo" como motor de voz al generar Narración de audio sincronizada (MP3) para vídeos.
*   **Modularización del código**: Se refactorizó la estructura del complemento de un único archivo a una arquitectura modular de múltiples archivos.
*   **Rediseño de la interfaz de configuración**: Se rediseñó completamente el diálogo de configuración para usar una interfaz moderna basada en pestañas.
*   **Registro global en archivo dedicado**: Se añadió un sistema opcional de registro global en archivo bajo la nueva pestaña "Avanzado". Compatible con niveles de verbosidad configurables (Depuración, Información, Advertencia, Error) y períodos de retención automatizados (1 hora a 90 días).
*   **Seguimiento del progreso de carga en Gemini**: Se añadieron anuncios de progreso en porcentaje en tiempo real al cargar archivos grandes (vídeo, audio, documentos) a la API de Google Gemini.

## Cambios para 2026.07.15

*   **Filtrado inteligente de modelos de API**: Revisión completa del sistema de filtrado de modelos. Se añadieron palabras clave de filtrado más potentes para mantener el desplegable principal limpio y preparado para el futuro, mientras que todos los modelos especializados siguen siendo accesibles en el Enrutamiento avanzado.
*   **Búsqueda en enrutamiento avanzado**: Todos los desplegables de Enrutamiento avanzado de modelos (OCR, STT, TTS, Operador, Vídeo, En vivo) y el selector de variante de eSpeak son ahora completamente buscables.
*   **Nuevos atajos de capa de comandos**: Alt+S (Configuración), Alt+Q (Informe de claves con cuota agotada), Alt+M (Auditoría de enrutamiento).
*   **Revisión completa del Analizador de vídeo**: Transformado en una suite completa de procesamiento de vídeo con grabación de pantalla local, generación de audiodescripción SRT, narración sincronizada MP3, seguimiento avanzado de personajes y enrutamiento de modelos de vídeo especializados.
*   **Gestión inteligente de cuotas de API**: Cuarentena por modelo para errores 429 de límite diario.

## Cambios para 7.0.0

*   **Reanudación de escaneos no finalizados**: Continúa desde donde se detuvo si un escaneo se interrumpe.
*   **Nueva variable `[screen_fg_obj]`**: Captura solo la ventana activa en primer plano.
*   **Reintentos inteligentes y rotación de claves**: Hasta 5 reintentos silenciosos y cambio automático de clave API.
*   **Detección de cortina de pantalla**: Evita capturas cuando la Cortina de pantalla está activa.
*   **Ajustes del Lector de documentos**: Pre-selección de idioma de destino y manejo de hilos mejorado.
*   **Integración OCR nativa de Mistral**: Procesamiento en lotes usando el punto de acceso `/v1/ocr`.
*   **Controladores de URL personalizados dinámicos**: Borrado instantáneo de caché de modelos al cambiar URL.
*   **Motor de entrada del Operador de IA renovado**: API `SendInput` de Windows en lugar de `mouse_event`.
*   **Arrastrar y soltar corregido**: Operaciones de arrastrar y soltar completamente estables.
*   **Soporte multimonitor**: Funciona correctamente en configuraciones de varios monitores.
*   **Simulación de teclado mejorada**: Soporte completo para teclas extendidas.
*   **Soporte de imágenes HEIC/HEIF**: Compatibilidad nativa con formatos de foto de iPhone.

## Cambios para 6.5.0

*   **Asistente en vivo**: Asistente de voz y pantalla en tiempo real, exclusivo de Google Gemini.
*   **Proveedor de IA MiniMax**: Integrado como proveedor par con soporte multimodal completo.
*   **Traducción del visor de documentos**: Corrección de error de traducción silencioso para usuarios que no usan inglés.
*   **Reintento de escaneo en lotes de PDF**: Lógica de reintento optimizada y silenciosa.
*   **Estado del visor de documentos**: Corrección del estado bloqueado en "Procesamiento por lotes iniciado".
*   **Fallo de hilo resuelto**: Corrección del fallo `IsMain() failed in wxTimerImpl`.

## Cambios para 6.1.2

*   **Verificación previa de etiquetas duplicadas**: Corregida.
*   **Chat de documentos para proveedores que no son Gemini**: Corregida verificación estricta de clave API.
*   **Traducción rápida de OCR de Chrome**: Restaurada la API de traducción gratuita.
*   **Filtro alfanumérico de CAPTCHA**: Corregida la lógica de filtrado.
*   **Actualización de ayuda de la capa de comandos**: Corrección del atajo de anuncio de estado de `L` a `I`.

## Cambios para 6.1.1

*   **Corrección de salida de Gemma 4 Thinking**: Extracción correcta del texto de respuesta final.
*   **OCR en lotes desde el Explorador de archivos**: Selección múltiple de fotos o PDFs para procesamiento en lote.

## Cambios para 6.1.0

*   **Integración universal de IA local**: Botón "Configurar IA local" para Ollama, LM Studio, Jan.ai y KoboldCPP.
*   **Omisión inteligente de proxy local**: Omisión completa de proxies del sistema para conexiones locales.
*   **Etiquetado de IA ultraestable (v2)**: Sistema híbrido de firma de objeto basado en AutomationId/ControlID.
*   **Migración automática de etiquetas**: Migración transparente al nuevo formato de huella digital.

## Cambios para 6.0

*   **Etiquetado semántico con IA**: Tecla **L** para etiquetar el objeto actual, **Shift+L** para escanear toda la aplicación.
*   **Gestión inteligente de etiquetas**: Nuevo administrador de etiquetas completamente accesible.
*   **Análisis directo de archivos**: Procesamiento inmediato desde el Explorador de archivos sin diálogo.

## Cambios para 5.6

*   **Motor "Ninguno (Extraer capa de texto)"**: Extracción directa de PDFs con capacidad de búsqueda sin créditos de IA.
*   **Precisión mejorada del Explorador de interfaz**: Mejor identificación de tipos de elementos y estados.
*   **Recordatorio de configuración de instalación**: Notificación post-instalación para configurar claves API.

## Cambios para 5.5.2

*   **Error de escritura del Operador de IA corregido**.
*   **Estabilidad mejorada**: Manejo robusto de errores para operaciones del portapapeles.
*   **Optimización de temporización**: Ajuste de retrasos internos para eventos de teclado.

## Cambios para 5.5 (La actualización de automatización)

*   **Operador de IA (Shift+A)**: Control autónomo de PC mediante comandos en lenguaje natural.
*   **Explorador visual de interfaz (E)**: Lista de todos los elementos en los que se puede hacer clic.
*   **Acción inteligente de archivo contextual (F)**: Pregunta por la intención al seleccionar una imagen.
*   **Optimización del núcleo**: Limpieza profunda de la lógica interna del complemento.

## Cambios para 5.0

*   Soporte para OpenAI, Groq y Mistral junto a Google Gemini.
*   Enrutamiento avanzado de modelos por tarea.
*   Configuración avanzada de punto de acceso para servidores locales o de terceros.
*   Visibilidad inteligente de funciones según el proveedor.
*   Obtención dinámica de modelos directamente desde la API del proveedor.

## Cambios para 4.6
*   Tecla **Espacio** para recuperar el último resultado de IA en la capa de comandos.
*   Enlace al canal oficial de Telegram en el menú Herramientas de NVDA.

## Cambios para 4.5
*   Administrador avanzado de indicaciones con edición, reordenamiento y vista previa.
*   Soporte de proxy completo para todas las solicitudes de API.
*   Migración automática al formato JSON v2.
*   Versión mínima de NVDA: 2025.1.

## Cambios para 4.0.3
*   Mecanismo de reintento automático para conexiones inestables.
*   Diálogo visual de traducción con navegación línea por línea.
*   Vista formateada con todas las páginas en una sola ventana.
*   Omisión automática de selección de rango para documentos de una sola página.

## Cambios para 4.0.1
*   Lector de documentos avanzado con procesamiento en segundo plano.
*   Nuevo submenú "Vision Assistant" en el menú Herramientas de NVDA.
*   Soporte de múltiples claves API de Gemini con rotación inteligente.
*   Generación de audio MP3/WAV directamente dentro del lector.
*   Soporte de Historias de Instagram, TikTok y Twitter (X).

## Cambios para 3.6.0
*   Comando de ayuda (`H`) dentro de la capa de comandos.
*   Soporte para vídeos de Twitter (X).
*   Diálogo de donación opcional.

## Cambios para 3.5.0
\*   Sistema de capa de comandos (`NVDA+Shift+V`).
\*   Análisis de vídeos de YouTube e Instagram por URL.

## Cambios para 3.1.0
*   Modo de salida directa sin ventana de chat.
*   Integración para copiar respuestas automáticamente al portapapeles.

## Cambios para 3.0
*   Traducciones al persa y vietnamita.
*   Lista de modelos reorganizada con prefijos `[Gratis]`, `[Pro]`, `[Auto]`.
*   Mejoras de estabilidad en el Dictado inteligente.

## Cambios para 2.9
*   Traducciones al francés y turco.
*   Botón "Ver formateado" en los diálogos de chat.
*   Opción "Limpiar Markdown en el chat".

## Cambios para 2.8
*   Traducción al italiano.
*   Comando de informe de estado (NVDA+Control+Shift+I).
*   Exportación HTML desde el botón "Guardar contenido".

## Cambios para 2.7
*   Migración a la plantilla oficial de complementos de NV Access.
*   Reintento automático para errores HTTP 429.

## Cambios para 2.6
*   Traducción al ruso (gracias a nvda-ru).
*   Idioma de destino predeterminado cambiado al inglés.

## Cambios para 2.5
*   Comando de OCR de archivos nativo (NVDA+Control+Shift+F).
*   Soporte completo de localización (i18n).
*   API de archivos de Gemini para mejor manejo de PDF y audio.

## Cambios para 2.1.1
*   Corrección de la variable [file_ocr] en indicaciones personalizadas.

## Cambios para 2.1
*   Todos los atajos estandarizados con NVDA+Control+Shift.

## Cambios para 2.0
*   Sistema de actualización automática.
*   Caché de traducción inteligente.
*   Memoria de conversación en diálogos de chat.
*   Comando de traducción del portapapeles (NVDA+Control+Shift+Y).

## Cambios para 1.5
*   Soporte para más de 20 nuevos idiomas.
*   Diálogo interactivo de refinado para preguntas de seguimiento.
*   Función de Dictado inteligente nativo.

## Cambios para 1.0
*   Lanzamiento inicial.
