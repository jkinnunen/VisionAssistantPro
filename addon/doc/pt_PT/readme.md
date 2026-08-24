# Documentação do Vision Assistant Pro

<!-- DOWNLOAD_COUNT_START --> Total Downloads: 62,863 <!-- DOWNLOAD_COUNT_END -->

O **Vision Assistant Pro** é um assistente de IA avançado e multimodal para o NVDA. Ele utiliza motores de IA de classe mundial para fornecer leitura inteligente de ecrãs, tradução, ditado por voz e análise de documentos.

_Este suplemento foi lançado para a comunidade em honra do Dia Internacional das Pessoas com Deficiência._

## 1. Configuração

Aceda a **Menu do NVDA > Preferências > Configurações > Vision Assistant Pro**. A caixa de diálogo de configurações está organizada em 9 separadores acessíveis: **Conexão**, **Assistente em Direto**, **Comportamento da IA**, **Idiomas de Tradução**, **Leitor de Documentos**, **Vídeo**, **CAPTCHA**, **Prompts** e **Avançado**.

### 1.1 Separador Conexão

* **Fornecedor:** Selecione o seu serviço de IA preferido. Os fornecedores suportados incluem **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** e **Personalizado** (servidores compatíveis com a OpenAI, como Ollama, LM Studio, Jan.ai ou KoboldCPP).
* **Chave de API:** Introduza uma ou múltiplas chaves de API (separadas por vírgulas ou quebras de linha) para rotação automática.
* **Obter Modelos:** Prima este botão após introduzir a sua chave de API para descarregar a lista mais recente de modelos disponíveis do fornecedor.
* **Modelo de IA:** Selecione o modelo principal utilizado para chat geral e análise.
* **Configurações de Fornecedor Personalizado:** Configure pontos de extremidade (endpoints) locais ou personalizados. Inclui **Configurar IA Local** (configuração com um clique para Ollama, LM Studio, Jan.ai ou KoboldCPP) e **Configuração Avançada de Ponto de Extremidade**.
* **Encaminhamento Avançado de Modelos (Específico por Tarefa):** Opcionalmente, selecione modelos dedicados através de caixas combinadas para tarefas de OCR, STT, TTS, Operador de IA, Vídeo e Assistente em Direto.
* **Opções de Conexão e Saída:** Configure o URL de Proxy, verificações de atualizações no arranque, limpar Markdown no chat, copiar respostas da IA para a área de transferência e Saída Direta (Sem Janela de Chat).

### 1.2 Separador Assistente em Direto

* **Assistente em Direto: Saída Direta (Sem Janela):** Inicia o Assistente em Direto sem a sua janela de conversação; abra-a mais tarde com a tecla de Chamar Último Resultado (`Espaço`).
* **Pressionar para Falar (Push to Talk):** Alterna o modo de pressionar para falar. Quando ativado, o seu microfone apenas envia áudio enquanto mantém premida a tecla atribuída.
* **Tecla Pressionar para Falar:** Prima as teclas para gravar o atalho (por exemplo, `F12` ou `Ctrl+F12`) - pode até atribuir apenas uma tecla modificadora como `Ctrl Esquerdo`. Mantenha a tecla premida para falar e largue-a para terminar; um breve sinal sonoro confirma cada pressão e libertação.

Nota: Este separador aparece apenas quando o **Google Gemini** (ou um fornecedor personalizado compatível com o Gemini) é o seu fornecedor ativo.

### 1.3 Separador Comportamento da IA

* **Criatividade (Temperatura):** Controla a aleatoriedade e criatividade da IA (de 0.0 a 2.0). Valores mais baixos produzem resultados de tradução/OCR mais determinísticos e precisos.

### 1.4 Separador Idiomas de Tradução

* **Idioma de Origem:** Selecione o seu idioma de entrada predefinido.
* **Idioma de Destino:** Selecione o seu idioma principal de tradução de destino.
* **Idioma de Resposta da IA:** Selecione o idioma para as respostas gerais da IA.
* **Troca Inteligente:** Troca automaticamente os idiomas de origem e destino com base na entrada detetada.

### 1.5 Separador Leitor de Documentos

* **Motor de OCR:** Escolha entre **Chrome (Rápido)** para resultados rápidos ou **AI (Avançado)** para uma preservação superior do layout.
* **Tamanho do Lote de OCR:** Especifique as páginas por pedido (defina como 0 para processamento num único pedido).
* **Descrever Imagens Inline:** Alterna descrições de imagens inline durante a extração de texto de documentos.
* **Exportar Números de Página:** Alterna números de página e separadores em saídas de documentos de várias páginas.
* **Voz TTS:** Selecione o estilo de voz predefinido para a geração de áudio.

### 1.6 Separador Vídeo

* **Tamanho do Bloco de Vídeo:** Duração do segmento em minutos para a geração de Audiodescrição (defina como 0 para processar o ficheiro inteiro).
* **Adicionar Lista de Personagens:** Opção para adicionar o dicionário de personagens como a primeira entrada de legendas.
* **Adicionar Aviso de IA:** Opção para inserir um aviso de IA no início das legendas SRT de vídeo.

### 1.7 Separador CAPTCHA

* **Ativar Resolvedor de CAPTCHA Visual:** Alterna a resolução automatizada de desafios visuais (hCaptcha, reCAPTCHA).
* **Método de CAPTCHA de Texto:** Escolha entre capturar o **Objeto Navegador** ou o **Ecrã Completo**.

### 1.8 Separador Prompts

* **Gerir Prompts:** Abre uma caixa de diálogo dedicada para personalizar prompts de sistema predefinidos ou criar, editar, reordenar e pré-visualizar prompts personalizados definidos pelo utilizador com variáveis dinâmicas (por exemplo, `[selection]`, `[screen_fg_obj]`).
* **Atalhos de Prompts Personalizados:** Atribua uma tecla de atalho dedicada a qualquer prompt personalizado diretamente no Gestor de Prompts. Prima as teclas para as gravar - teclas individuais executam-se dentro da Camada de Comandos (e globalmente como `NVDA + Shift + tecla`), enquanto combinações como `Control + Shift + 1` executam-se globalmente por si só.

### 1.9 Separador Avançado e Registos Globais

Aceda ao separador **Avançado** para configurar o registo global do suplemento:

* **Ativar ficheiro de registo dedicado:** Alterna o registo de todos os eventos operacionais, tráfego de API e erros em todos os módulos do suplemento num ficheiro separado (`vision_assistant.log`).
* **Nível de Registo:** Selecione o nível de detalhe entre **Depuração (Todos os Detalhes)**, **Informação (Informação Geral)**, **Aviso (Apenas Avisos)** e **Erro (Apenas Erros)**.
* **Manter Registos Durante:** Define períodos de retenção automáticos para limpar automaticamente entradas de registo mais antigas (variando de 1 hora a 90 dias).
* **Controlos de Gestão de Registos:** Utilize **Abrir Ficheiro de Registo**, **Abrir Pasta de Registos** ou **Limpar Ficheiro de Registo** para inspecionar ou limpar dados de registo diretamente sem reiniciar o NVDA ou interferir com os registos padrão do NVDA.

### 1.10 Cópia de Segurança e Restauro de Configurações

O separador **Avançado** também inclui uma secção de **Cópia de Segurança e Restauro**:

* **Cópia de Segurança:** Guarda a sua configuração num único ficheiro JSON. Quando clica nele, escolhe o que incluir: **Tudo** (definições, rótulos personalizados, progresso de OCR e histórico) ou **Apenas Definições**.
* **Restauro:** Carrega uma cópia de segurança guardada anteriormente para restaurar a sua configuração e dados a qualquer momento, em qualquer máquina, ou após reinstalar o NVDA. Ser-lhe-á pedido que confirme primeiro, uma vez que o restauro substitui todas as suas definições e dados atuais.

## 2. Camada de Comandos e Atalhos

Para evitar conflitos de teclado, este suplemento utiliza uma **Camada de Comandos**.

1. Prima **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (ouvirá um sinal sonoro).
2. Largue as teclas e, em seguida, prima uma das seguintes teclas individuais:

| Tecla | Função | Descrição |
| --- | --- | --- |
| **Shift + A** | **Operador de IA** | **Operação Autónoma:** Diz à IA para executar uma tarefa no seu ecrã. Premir novamente cancela instantaneamente as operações ativas. |
| **E** | **Explorador de UI** | **Clique Interativo:** Identifica e clica em elementos de UI em qualquer aplicação. |
| **T** | Tradutor Inteligente | Traduz o texto sob o cursor do navegador ou a seleção. |
| **Shift + T** | Tradutor da Área de Transferência | Traduz o conteúdo atualmente presente na área de transferência. |
| **R** | Refinador de Texto | Resume, corrige gramática, explica ou executa **Prompts Personalizados**. |
| **V** | Visão de Objeto | Descreve o objeto navegador atual. |
| **O** | Visão de Ecrã Completo | Analisa todo o layout e conteúdo do ecrã. |
| **Shift + V** | Análise de Vídeo | Analisa ficheiros de vídeo locais ou vídeos online do **YouTube**, **Instagram**, **TikTok** ou **Twitter (X)**. |
| **Control + V** | Gravação de Vídeo Local | Grava um vídeo silencioso do seu ecrã e analisa as ações e o layout. |
| **D** | Leitor de Documentos | Leitor avançado para PDF, imagens e ficheiros de texto simples/HTML com seleção de intervalo de páginas. |
| **F** | **Ação Inteligente em Ficheiros** | Reconhecimento consciente do contexto a partir de imagens, PDFs ou ficheiros TIFF selecionados. |
| **M** | Transcrição e Dobragem de Média | Transcreve ou dobra ficheiros de áudio/vídeo (MP3, WAV, MP4, etc.) para o seu idioma de destino. |
| **C** | Resolvedor de CAPTCHA | Captura e resolve CAPTCHAs. |
| **Shift + C** | Chat Direto | Abre uma interface de chat baseada em texto diretamente com a IA. |
| **S** | Ditado Inteligente | Converte fala em texto. Prima para iniciar a gravação, prima novamente para parar/escrever. |
| **Control+T** | Tradução por Voz | Transcreve, traduz e escreve o resultado com base nas suas definições de idioma. |
| **Control+L** | **Assistente em Direto** | **Copilot em Tempo Real (apenas Gemini):** Inicia ou termina uma conversação de voz e ecrã em direto com o assistente de IA. |
| **I** | Relatório de Estado | Anuncia o progresso atual (por exemplo, "A analisar...", "Inativo"). |
| **L** | **Rotular Objeto** | **Rotulagem Semântica por IA:** Rotula permanentemente o elemento/ícone atualmente em foco. |
| **Shift + L** | **Gerir/Escanear Rótulos** | Abre o Gestor de Rótulos (se existirem rótulos) ou examina a aplicação em busca de elementos sem nome. |
| **U** | Verificação de Atualizações | Verifica manualmente no GitHub a versão mais recente do suplemento. |
| **Espaço** | Chamar Último Resultado | Mostra a última resposta da IA numa caixa de diálogo de chat para revisão ou seguimento. |
| **H** | Ajuda de Comandos | Exibe uma lista de todos os atalhos disponíveis. |
| **Control + H** | **Histórico** | Abre a caixa de diálogo de Histórico listando os seus chats e documentos passados, com filtros de tipo e opções de Eliminar/Limpar. |
| **Alt + S** | Configurações | Abre a caixa de diálogo de configurações do Vision Assistant Pro. |
| **Alt + Q** | Relatório de Chaves com Quota Esgotada | Informa o número de chaves da API do Gemini que excederam a sua quota diária e o respetivo tempo de reinicialização. |
| **Alt + M** | Auditoria de Encaminhamento | Informa os modelos de IA atualmente selecionados no encaminhamento avançado. |
| **Para cima / Para baixo** | Navegação Rápida nas Configurações | Navega entre categorias de configurações rápidas (Fornecedor, Modelo, etc.) na camada. |
| **Esquerda / Direita** | Alterar Configuração Rápida | Altera o valor da configuração rápida atualmente selecionada. |

## 3. Chat e Histórico

As janelas de chat e a caixa de diálogo de Histórico funcionam em todas as funcionalidades, para que possa rever conversas e continuar exatamente de onde parou.

### 3.1 Atalhos da Janela de Chat

Quando uma janela de chat está aberta (Chat Direto, chat de documentos, refinamento e semelhantes), pode rever a conversação com:

* **Alt + Para baixo:** Ler a mensagem seguinte.
* **Alt + Para cima:** Ler a mensagem anterior.
* **Alt + C:** Copiar a mensagem atual.

### 3.2 Histórico (Control + H)

Prima **Control + H** na Camada de Comandos para abrir a caixa de diálogo **Histórico** com os seus chats e documentos anteriores, filtráveis por tipo (Todos / Chats / Documentos). Abra um chat para continuar a conversação - incluindo os seus ficheiros anexados, que são reanexados automaticamente - ou abra um documento e continue a ler. Prima **Delete** em qualquer item para o remover, ou **Limpar Tudo** para esvaziar a lista.

## 4. Operador de IA - Controlo Autónomo do Computador

O **Operador de IA** transforma o Vision Assistant Pro de um leitor passivo num assistente ativo que pode interagir com o seu computador em seu nome. Pode pedir-lhe para descrever o ecrã, responder a perguntas sobre o que vê ou até assumir o controlo - clicando em botões, arrastando itens, escrevendo texto e navegando por aplicações utilizando comandos em linguagem natural.

A maior vantagem? Funciona perfeitamente em softwares completamente inacessíveis. Se estiver preso numa aplicação personalizada, num ambiente de trabalho remoto (Remote Desktop) ou num site onde o seu leitor de ecrã fica totalmente em silêncio, o operador não se importa. Como "vê" o ecrã visualmente, consegue encontrar, ler e interagir com elementos que têm zero rótulos de acessibilidade.

### Como Funciona

1. Prima **NVDA + Shift + V** e, em seguida, prima **Shift + A** (ou utilize o atalho direto) para abrir a caixa de diálogo do Operador de IA.
2. Escreva o que pretende fazer em linguagem simples (por exemplo, "Clica no botão Guardar", "O que diz a mensagem de erro?" ou "Muda o nome do ficheiro para final.pdf").
3. A IA analisará o seu ecrã, identificará os elementos relevantes e executará a ação ou fornecerá a resposta. Se uma tarefa exigir vários passos, o operador continuará a trabalhar até que esteja concluída.
4. Prima **Shift + A** novamente a qualquer momento para abortar instantaneamente uma operação em curso.

### Ações Suportadas

O operador compreende uma vasta gama de comandos:

* **Descrever e Responder**: "Descreve o layout do ecrã" ou "O que diz a mensagem de erro?"
* **Clicar**: "Clica no botão Guardar"
* **Clique Direito**: "Clica com o botão direito no ficheiro"
* **Duplo Clique**: "Faz duplo clique no documento"
* **Arrastar e Soltar**: "Arrasta o documento para a pasta Arquivo"
* **Escrever**: "Escreve 'Olá Mundo' na caixa de pesquisa"
* **Deslocar (Scroll)**: "Faz scroll para baixo três vezes"
* **Premir Tecla**: "Prima Enter", "Prima Tab", "Prima Escape"
* **Tarefas de Vários Passos**: "Abre o Explorador de Ficheiros, encontra o relatório e muda o nome para final.pdf"

### Notas Importantes

* **⚠️ Aviso de Utilização da API**: Como o operador precisa de "ver" exatamente o que está a acontecer no ecrã, envia uma captura de ecrã de alta resolução a cada passo. A utilização frequente consumirá a sua quota de API muito mais rapidamente do que as funcionalidades padrão baseadas em texto.
* **Aplicações de Administrador**: Se o NVDA não estiver a ser executado com privilégios de Administrador, o operador poderá não conseguir interagir com janelas que exijam permissões elevadas. Esta é uma limitação de segurança do Windows, não um erro do suplemento.
* **Boas Práticas**: Para obter os melhores resultados, dê comandos claros e específicos. "Clica no botão azul Enviar na parte inferior do formulário" funcionará quase sempre melhor do que apenas "Clica no botão".

## 5. Análise de Vídeo e Audiodescrição

> **Nota:** As funcionalidades de Análise de Vídeo e Audiodescrição são estritamente alimentadas pelo fornecedor **Google Gemini**. Certifique-se de que o seu fornecedor ativo nas definições do suplemento está definido como Google Gemini.

O Vision Assistant Pro introduz poderosas capacidades de processamento de vídeo concebidas especificamente para utilizadores cegos. Consegue analisar tanto vídeos online como gravações de ecrã locais para fornecer descrições visuais altamente detalhadas e gerar scripts de Audiodescrição profissionais (SRT).

### 5.1 Gravação de Ecrã Local (Control + V)

Se encontrar um vídeo silencioso, uma animação ou um tutorial no seu ecrã, pode capturá-lo diretamente:

1. Prima **NVDA + Shift + V** para entrar na Camada de Comandos e, em seguida, prima **Control + V**.
2. O suplemento gravará o seu ecrã silenciosamente em segundo plano.
3. Prima **Control + V** novamente para parar a gravação.
4. A IA analisará o segmento de vídeo gravado e fornecerá uma descrição altamente detalhada da cena, personagens e ações.

### 5.2 Análise de Vídeo (Shift + V)

Pode analisar tanto ficheiros de vídeo locais como vídeos online. Basta selecionar um ficheiro de vídeo local no Explorador do Windows ou copiar uma hiperligação (URL) de vídeo online para a sua área de transferência. Também pode premir **Shift + V** em qualquer lugar (como dentro de um leitor multimédia) para abrir uma caixa de diálogo onde pode procurar um ficheiro de vídeo ou colar um URL manualmente.

* **Plataformas Online Suportadas:** YouTube, Instagram, TikTok e Twitter (X).
* A IA detetará automaticamente o ficheiro local ou o URL, processará o vídeo e fornecerá uma descrição visual abrangente e um resumo em áudio.

### 5.3 Geração de Audiodescrição (SRT)

Para uma experiência mais estruturada, o suplemento pode gerar scripts de Audiodescrição profissionais no formato padrão SubRip (SRT).

* **Sincronização Inteligente de Intervalos:** A IA ouve a faixa de áudio e ancora especificamente as suas descrições visuais a pausas naturais e intervalos silenciosos para minimizar de forma inteligente a sobreposição de diálogos.
* **Acompanhamento de Personagens:** O motor efetua uma passagem prévia para extrair personagens distintas com base em caraterísticas faciais imutáveis. Constrói um dicionário global para acompanhar e rotular com precisão personagens em diferentes cenas sem confusão.
* **OCR de Texto Literal:** Qualquer texto que apareça no ecrã (sinais, telemóveis, créditos) é estritamente citado de forma literal.
* **Como Utilizar:** Para ouvir a legenda gerada, basta colocar o ficheiro `.srt` na mesma pasta do seu ficheiro de vídeo e dar-lhe exatamente o mesmo nome. Em seguida, configure o seu leitor multimédia (por exemplo, VLC ou PotPlayer) para encaminhar o texto da legenda diretamente para o seu leitor de ecrã ou motor TTS durante a reprodução.

### 5.4 Narração de Áudio Sincronizada (Exportação MP3)

Para além de criar apenas ficheiros SRT baseados em texto, o suplemento funciona como uma ferramenta completa de produção de Audiodescrição, sintetizando as descrições em voz e misturando-as com o vídeo. Pode agora escolher **Gemini Live TTS** como o motor de voz, que utiliza a API Gemini Live para gerar narração de voz altamente realista e ilimitada. Ao gerar um MP3 para ficheiros de vídeo locais, tem múltiplos modos de mistura:

* **AD Padrão (Misturar Voz):** A narração é sobreposta diretamente por cima do áudio do vídeo. Será questionado se pretende aplicar **Atenuação de Áudio (Audio Ducking)** (baixar o volume de fundo durante as descrições) para garantir que a narração é clara.
* **AD Estendida (Pausar Áudio):** O motor pausa o áudio original do vídeo durante as descrições, garantindo que nunca perde uma única palavra do diálogo original ou da narração da IA.
* **Vídeos do YouTube:** Para fontes do YouTube (que não são descarregadas localmente), a exportação MP3 conterá estritamente a faixa de voz da IA sincronizada, sem o áudio de fundo do vídeo.

## 6. Transcrição e Dobragem de Média (M)

O Transcritor de Áudio foi completamente reestruturado para suportar ficheiros de áudio e vídeo (MP3, WAV, MP4, MKV, etc.). Prima **M** na Camada de Comandos para selecionar um ficheiro multimédia e escolher um de 3 modos de operação distintos:

1. **Transcrever (Idioma Original)**: Transcreve com precisão a fala no seu idioma original.
2. **Transcrever e Traduzir (Idioma de Destino)**: Transcreve a fala e traduz-a para o seu idioma de destino configurado.
3. **Dobrar e Traduzir (Idioma de Destino)** _(Apenas Gemini)_: Uma nova funcionalidade poderosa que transcreve a fala, traduz-a para o seu idioma de destino e sintetiza uma dobragem de áudio falada utilizando o motor TTS do suplemento.

## 7. Leitor Avançado de Documentos e Imagens

O **Leitor de Documentos** transforma os seus documentos em texto limpo e legível - para que possa ler, traduzir e ouvir qualquer coisa, desde um livro digitalizado até uma pilha de fotografias. Lida com PDFs de várias páginas, imagens complexas, formatos HEIC do iPhone e até ficheiros de texto simples (`.txt`) e HTML (`.html`, `.htm`), que são abertos instantaneamente sem OCR ou processamento por IA. Selecione vários ficheiros de uma vez e estes são unidos num único documento contínuo na ordem das páginas. Estão disponíveis três motores de OCR - **Chrome (Rápido)**, **AI (Avançado)** para uma preservação superior do layout e **Nenhum (Extrair Camada de Texto)** para PDFs pesquisáveis -, selecionados em Definições → Leitor de Documentos.

### Como Funciona

1. Prima **NVDA + Shift + V**, depois **D** para abrir o Leitor de Documentos — ou realce primeiro um ficheiro no Explorador de Ficheiros e prima **D** / **F** para ignorar totalmente a caixa de diálogo de ficheiros.
2. Escolha um ou mais PDFs ou imagens. O suplemento examina-os e anuncia a contagem total de páginas.
3. Na caixa de diálogo de **Opções**, escolha o intervalo de páginas (De/Para). Também pode marcar **Traduzir Saída** e escolher o idioma de destino, ou alternar **Descrever imagens inline durante o OCR**.
4. A extração de texto começa em segundo plano por lotes. Pode fechar a janela a qualquer momento e continuar mais tarde — nada é perdido.
5. Assim que as páginas estiverem prontas, leia-as no visualizador: navegue entre páginas, salte para qualquer página, faça perguntas à IA, guarde o texto ou gere uma narração em áudio.

### 7.1 Processamento em Lote e Retoma

Não precisa de ler um documento massivo de uma só vez. Escolha um intervalo de páginas (por exemplo, `1-20`) ou mantenha os valores predefinidos para processar tudo, e a IA extrai todas as páginas em segundo plano. Se o NVDA crashar ou interromper o exame, o suplemento lembra-se do seu progresso e oferece a opção de **Retomar** exatamente onde ficou — mesmo após reinicializações. Os documentos concluídos também ficam em cache, pelo que reabri-los (a partir de Documentos Recentes ou através de **D**) carrega o texto instantaneamente sem voltar a executar o OCR, a menos que os ficheiros de origem tenham sido alterados.

### 7.2 Ação Inteligente em Ficheiros

Não precisa de abrir sempre o documento primeiro. No Explorador de Ficheiros do Windows, basta realçar um PDF, imagem ou ficheiro de texto/HTML e premir **D** (Leitor de Documentos) — ou realçar um PDF ou imagem e premir **F** (Ação Inteligente em Ficheiros) — dentro da Camada de Comandos. O suplemento ignora instantaneamente a caixa de diálogo de ficheiros e começa a processar o ficheiro realçado. Selecionar vários ficheiros de uma vez processa-os em conjunto como um único documento.

### 7.3 Controlos e Atalhos do Visualizador de Documentos

Quando a janela do Leitor de Documentos está aberta, pode utilizar o seguinte:

#### Atalhos de Teclado

* **Ctrl + PageDown / Ctrl + PageUp:** Avança para a página seguinte / anterior.
* **Seta Para baixo / Para cima:** Quando o cursor atingir a última linha de uma página, prima **Para baixo** para saltar para a página seguinte; prima **Para cima** no topo de uma página para regressar à anterior.
* **Alt + A:** Abre uma caixa de diálogo de chat para fazer perguntas sobre o documento.
* **Alt + R:** Força um **Reexaminar com IA** utilizando o seu fornecedor ativo.
* **Alt + G:** Gera e guarda um ficheiro de áudio de alta qualidade (WAV/MP3). _(Oculto se o fornecedor não suportar TTS)._
* **Alt + S / Ctrl + S:** Guarda o texto extraído como um ficheiro TXT ou HTML.

#### Botões e Controlos

* **Ir para:** Escolha qualquer página a partir do seletor de páginas.
* **Ver Formatado:** Vê o documento inteiro combinado como texto formatado.
* **Tentar Novamente Páginas com Falha:** Tenta novamente apenas os lotes que falharam devido a um erro temporário do servidor (por exemplo, alta procura). Este botão aparece automaticamente quando necessário.
* **Voz TTS / Motor TTS:** Escolha a voz e, no Gemini, escolha entre **TTS Padrão** e **Gemini Live** em streaming.
* **Anterior / Seguinte:** Navega entre páginas (o mesmo que os atalhos Ctrl+PageUp/Down).

### 7.4 Documentos Recentes (D)

Premir **D** na Camada de Comandos lista primeiro os seus documentos lidos recentemente. Escolha um para continuar a partir da página em que estava — mesmo que o OCR já tenha terminado — ou prima **Abrir Ficheiro...** (`Ctrl + O`) para procurar um ficheiro como habitualmente.

## 8. Rotulagem Semântica por IA e Explorador de UI

Apanhado numa aplicação com "botão sem rótulo" em todo o lado? O motor de Rotulagem Semântica por IA resolve isto permanentemente.

### 8.1 Rotulagem Permanente de Objetos (L)

Foque o seu leitor de ecrã num gráfico ou botão sem rótulo e prima **L** na Camada de Comandos. A IA examinará o botão visualmente, determinará a sua função e aplicará um rótulo permanente.
_Ao contrário das ferramentas de rotulagem de leitores de ecrã mais antigas, este suplemento utiliza um sistema híbrido avançado de "Assinatura de Objeto" (AutomationId/ControlID). Os seus rótulos personalizados sobreviverão a redimensionamentos de janelas, trocas de monitores e atualizações de aplicações!_

### 8.2 Exame Completo da Aplicação (Shift + L)

Prima **Shift + L** para examinar toda a janela ativa de uma só vez. A IA encontrará todos os elementos sem rótulo e nomeá-los-á de forma inteligente de uma só vez. Posteriormente, pode gerir, mudar o nome ou eliminar em lote estes rótulos a partir do Gestor de Rótulos integrado.

### 8.3 Explorador de UI (E)

Precisa de interagir com um elemento sem navegar até ele manualmente? Prima **E** para ativar o Explorador de UI. A IA examinará o ecrã e gerará uma lista acessível de cada elemento clicável (ignorando ruído do sistema como barras de tarefas). Escolha um item da lista e o suplemento clicará instantaneamente nele por si.

## 9. Assistente de Voz em Direto

O Assistente em Direto transforma o Vision Assistant Pro num copiloto interativo em tempo real.
_(Nota: Esta funcionalidade é exclusiva do Google Gemini e de fornecedores Personalizados compatíveis com o Gemini)._

* **Ativação:** Prima **Control + L** na Camada de Comandos para abrir a caixa de diálogo do Assistente em Direto.
* **Interação em Tempo Real:** Fale naturalmente através do seu microfone. A IA ouvirá simultaneamente a sua voz e observará o seu ecrã ativo. Pode fazer perguntas como "O que estou a ver?" ou "Lê-me o terceiro parágrafo."
* **Pressionar para Falar:** Ative o **Pressionar para Falar** no separador de definições do Assistente em Direto (ou alterne-o diretamente dentro da janela do Assistente em Direto), depois mantenha premida a tecla atribuída para falar e largue-a quando terminar. Isto mantém o microfone sem som até premir a tecla — perfeito para ambientes ruidosos.
* **Personalização:** Dentro da caixa de diálogo, pode alterar o Estilo de Voz da IA (por exemplo, Profissional, Amigável, Animado) e ajustar a respetiva "Profundidade de Pensamento" para controlar o nível de raciocínio antes de responder.

## 10. Prompts Personalizados e Variáveis

Pode gerir prompts em **Definições > Prompts > Gerir Prompts...**.

### Atalhos de Prompts Personalizados

Atribua a qualquer prompt personalizado a sua própria tecla de atalho diretamente no Gestor de Prompts e execute-o instantaneamente com a sua seleção ou contexto atual:

* **Tecla individual** (por exemplo, `1`, `p` ou `F3`): Funciona dentro da Camada de Comandos e também globalmente como `NVDA + Shift + tecla`.
* **Combinação de teclas** (por exemplo, `Control + Shift + 1`, `Alt + P` ou `Insert + 1`): Funciona globalmente por si só.

### Variáveis Suportadas

* `[selection]`: Texto atualmente selecionado.
* `[clipboard]`: Conteúdo da área de transferência.
* `[clipboard_image]`: Imagem atualmente na área de transferência.
* `[screen_obj]`: Captura de ecrã do objeto navegador.
* `[screen_fg_obj]`: Captura de ecrã da janela em primeiro plano ativa.
* `[screen_full]`: Captura de ecrã completo.
* `[file_ocr]`: Selecionar imagem/ficheiro PDF para extração de texto.
* `[file_read]`: Selecionar documento para leitura (TXT, Code, PDF).
* `[file_audio]`: Selecionar ficheiro de áudio para análise (MP3, WAV, OGG).
* `{target_lang}`: Idioma de destino atual.
* `{source_lang}`: Idioma de origem atual.
* `{response_lang}`: Idioma de resposta atual da IA.
* `{swap_target}`: Idioma de recurso para tradução de troca inteligente.
* `{swap_instruction}`: Bloco de instruções de tradução de troca inteligente.

## 11. Casos de Uso no Mundo Real (Que funcionalidade devo utilizar?)

O Vision Assistant Pro está repleto de ferramentas avançadas. Eis alguns cenários comuns para o ajudar a escolher a correta:

* **Cenário: Pretende compreender o layout completo de uma janela complicada ou de uma aplicação inacessível.**
_Solução:_ Prima **O** (Visão de Ecrã Completo). A IA analisará todo o ecrã e descreverá exatamente onde os elementos, textos e botões estão posicionados.
* **Cenário: Encontrou uma imagem numa página web ou um gráfico sem rótulo num documento.**
_Solução:_ Mova o seu objeto navegador para o gráfico e prima **V** (Visão de Objeto). A IA descreverá especificamente o que essa imagem contém.
* **Cenário: Quer ver um filme ou clipe de vídeo com audiodescrições.**
_Solução:_ Prima **Shift + V** no seu vídeo e escolha **"Gerir Audiodescrição (Ficheiro SRT)"**. Quando terminar, clique em **"Gerir Narração Sincronizada (MP3)"** e selecione **"AD Estendida"**. O suplemento criará uma faixa de áudio que pausa inteligentemente o diálogo do filme para descrever as cenas visuais.
* **Cenário: Deparou-se com uma aplicação cheia de "botões sem rótulo".**
_Solução:_ Prima **L** para rotular permanentemente o botão específico utilizando IA. Em alternativa, prima **Shift + L** para examinar e rotular toda a janela de uma vez. Se apenas quiser clicar em algo rapidamente, prima **E** (Explorador de UI) para obter uma lista de todos os itens clicáveis.
* **Cenário: Precisa de contornar um CAPTCHA inacessível.**
_Solução:_ Prima **C** (Resolvedor de CAPTCHA). A IA capturará automaticamente o CAPTCHA, resolvê-lo-á e injetará a resposta no campo correto.
* **Cenário: Pretende ler um documento PDF longo de 50 páginas.**
_Solução:_ Prima **D** (Leitor de Documentos), defina o seu fornecedor como Google Gemini e introduza o intervalo de páginas `1-50`. O suplemento extrairá o texto com precisão em segundo plano.
* **Cenário: Está a ver um tutorial em vídeo silencioso ou uma animação no seu ecrã.**
_Solução:_ Prima **Control + V** para iniciar a gravação do ecrã. Deixe o tutorial reproduzir-se e, em seguida, prima **Control + V** novamente. A IA explicará exatamente o que foi demonstrado.
* **Cenário: Ocorre um erro inesperado, falha de ligação à API ou quer diagnosticar problemas com servidores locais personalizados.**
_Solução:_ Aceda a **Definições > Avançado**, selecione **"Ativar ficheiro de registo dedicado"** e defina o **Nível de Registo** como **"Depuração"**. Execute a ação novamente e clique em **"Abrir Ficheiro de Registo"** para inspecionar os detalhes técnicos ou anexar o `vision_assistant.log` a um pedido de suporte.

---

**Nota:** É necessária uma ligação ativa à internet para todas as funcionalidades de IA. Os documentos de várias páginas são processados automaticamente.

## 12. Suporte e Comunidade

Mantenha-se atualizado com as últimas notícias, funcionalidades e lançamentos:

* **Canal do Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
* **GitHub Issues:** Para relatórios de erros e pedidos de novas funcionalidades.

### Relatar Erros e Registos

Ao abrir uma issue no GitHub ou pedir suporte, inclua detalhes sobre o seu fornecedor de IA ativo, modelo e versão do NVDA. Se estiver a experienciar problemas de ligação ou crashes inesperados, ative o ficheiro de registo dedicado em **Definições > Avançado**, recrie o problema e anexe o seu ficheiro `vision_assistant.log` para nos ajudar a resolver o problema mais rapidamente.

## 13. Apoiantes do Projeto

Um agradecimento sincero aos membros da nossa comunidade que apoiam o desenvolvimento contínuo e a manutenção deste projeto através das suas generosas contribuições financeiras:

* **@Alyabani94**
* **Ali Alamri**
* **Ilya**
* **Apoiante Anónimo** (`UQDd...CnMY`)
* **leonardo0216**
* **Sergei Fleytin**
* **Suman Gayen**

_Se desejar apoiar o projeto financeiramente e ver o seu nome aqui, pode encontrar a opção **Doar** no menu Ferramentas do NVDA (subdiretório Vision Assistant) ou durante o processo de configuração após a instalação._

---

## Alterações para 2026.09.01

* **Histórico (Control + H)**: A Camada de Comandos inclui agora uma caixa de diálogo de **Histórico** (`Control + H`) que lista os seus chats e documentos anteriores com filtros para Todos, Chats e Documentos. Reabra qualquer chat com a respetiva conversação completa — os ficheiros anexados são reanexados automaticamente — ou reabra um documento e continue a ler. Prima **Delete** em qualquer item para o remover, ou limpe tudo de uma vez.
* **Documentos Recentes no Leitor**: Premir **D** na Camada de Comandos mostra agora primeiro os seus documentos lidos recentemente. Escolha um para continuar a partir da página em que estava — mesmo quando o OCR já terminou — ou prima **Abrir Ficheiro...** (`Ctrl + O`) para procurar como habitualmente.
* **Pressionar para Falar para o Assistente em Direto**: Assuma o controlo total das suas conversas em direto! Ative o **Pressionar para Falar** no novo separador de definições do Assistente em Direto e atribua qualquer tecla — ou até mesmo apenas uma tecla modificadora como `Ctrl Esquerdo` — para falar. Mantenha a tecla premida para falar e largue-a quando terminar, com um breve sinal sonoro em cada pressão e libertação. Um botão correspondente também aparece diretamente na janela do Assistente em Direto, para que possa alternar entre o modo de pressionar para falar e microfone aberto sem sair da conversa.
* **Áudio Nativo Gemini 2.5 Flash**: O Assistente em Direto suporta agora o modelo de áudio nativo do Gemini 2.5 Flash (`gemini-2.5-flash-native-audio-preview-12-2025`) para conversas de voz naturais e de baixa latência. Pode mudar para ele em **Definições → Encaminhamento Avançado de Modelos → Modelo do Assistente em Direto (Apenas Gemini)**, ou manter "Automático" para permanecer no modelo recomendado.
* **Cópia de Segurança e Restauro de Configurações**: Foi adicionado um poderoso sistema de cópia de segurança e restauro no separador **Avançado**! Pode agora guardar todas as definições do seu suplemento — incluindo chaves de API, modelos, prompts personalizados e preferências — num único ficheiro JSON e restaurá-las perfeitamente a qualquer momento, em qualquer máquina, ou após reinstalar o NVDA.
* **Leitura Direta de Texto e HTML**: O Leitor de Documentos pode agora abrir diretamente ficheiros de texto simples (`.txt`) e HTML (`.html`, `.htm`)! Deteta automaticamente a codificação do ficheiro, remove scripts e elementos de formatação desnecessários, e divide inteligentemente o conteúdo em páginas legíveis — reimportando inclusivamente os seus próprios ficheiros exportados mantendo a estrutura de páginas —, para que possa lê-los instantaneamente sem OCR ou processamento por IA!
* **Gemini Live TTS para o Leitor de Documentos**: O botão "Gerir Áudio" suporta agora o Gemini Live — um motor de conversão de texto em áudio em streaming, de alta qualidade e ritmo natural! Quando o Gemini é o seu fornecedor ativo, pode escolher entre o TTS Padrão e o Gemini Live diretamente no leitor, e a sua seleção fica guardada para a próxima vez!
* **Atalhos de Prompts Personalizados**: Pode agora atribuir uma tecla de atalho a qualquer um dos seus prompts personalizados diretamente a partir do Gestor de Prompts! Atribua a cada prompt a sua própria tecla dedicada ou combinação de teclas para o executar instantaneamente, capturando automaticamente a sua seleção ou contexto atual sem passos extra!
* **Navegação de Mensagens de Chat**: Reveja qualquer conversação sem usar as mãos! Dentro de qualquer janela de chat (Chat Direto, chat de documentos, refinamento e mais), prima `Alt + Para baixo` para ouvir a mensagem seguinte e `Alt + Para cima` para ouvir a anterior — com prefixos claros "Tu" / "IA" e limites de "Primeira mensagem" / "Última mensagem" anunciados à medida que avança.
* **Copiar Mensagem de Chat (Alt + C)**: Enquanto revê uma conversação com `Alt + Para cima/Para baixo`, prima `Alt + C` para copiar a mensagem em que se encontra atualmente para a área de transferência — respeitando a sua configuração de limpeza de Markdown — com uma confirmação falada.
* **Prompt de Sistema do Chat Direto**: O Chat Direto (`Shift+C`) tem agora o seu próprio prompt de sistema editável — "Instrução de Chat Direto" — que define a persona do assistente e o idioma de resposta para cada conversação. Pode personalizá-lo a partir do separador Prompts Predefinidos do Gestor de Prompts.
* **Navegação de Página por Cursor no Leitor de Documentos**: Ler documentos de várias páginas ficou ainda mais fluído! No Visualizador de Documentos, quando o seu cursor atinge a última linha de uma página e prime `Para baixo`, o leitor salta automaticamente para a página seguinte. Premir `Para cima` no início de uma página leva-o de volta à anterior sem interrupções — sem necessidade de mudar de página manualmente durante a leitura!
* **Novos Botões de Definições Rápidas**: Copiar respostas da IA para a área de transferência, Saída Direta (sem janela de chat), Limpar Markdown no Chat e Troca Inteligente podem agora ser ativados e desativados instantaneamente a partir das Definições Rápidas da camada de comandos!
* **Separador de Definições do Assistente em Direto**: O Assistente em Direto tem agora o seu próprio separador de definições dedicado! A opção "Assistente em Direto: Saída Direta (Sem Janela)" foi movida para aqui a partir do separador Conexão, e o separador aparece apenas quando o Google Gemini (ou um fornecedor Personalizado compatível com o Gemini) é o seu fornecedor ativo.

## Alterações para 2026.08.06

* **Rotulagem do Explorador de UI**: Pode agora adicionar rótulos diretamente aos elementos encontrados dentro do Explorador de UI! Foi adicionado um novo botão "Adicionar Rótulo" e a interface mantém-se inteligentemente aberta e preserva o foco para que possa rotular rapidamente vários objetos sem interrupção.
* **Melhoria da Camada de Definições Rápidas**: A camada do Vision Assistant (`Insert+Shift+V`) é agora persistente e altamente interativa! Pode utilizar as setas `Para cima/Para baixo` para navegar entre definições rápidas (Fornecedor, Modelo, Idioma de Resposta da IA, Modelo TTS) e as setas `Esquerda/Direita` para alterar instantaneamente os seus valores com feedback de voz inteligente e conciso. As suas seleções entram em vigor imediatamente (incluindo a ativação automática de encaminhamento avançado quando necessário), e a camada permanece ativa enquanto configura.
* **Chat Direto (`Shift+C`)**: Adicionado um novo comando à camada! Prima `Shift+C` para abrir instantaneamente uma janela de "Chat Direto". Isto fornece uma interface conversacional limpa e baseada em texto com a IA de imediato, sem necessidade de uma imagem ou documento como ponto de partida.
* **Recuperação Perfeita do Histórico de Chat**: Corrigido um erro importante em que premir `Espaço` para chamar o último resultado fazia perder o histórico de chat subsequente. Agora, o suplemento rastreia globalmente a sua conversação. Se conversar, fechar a diálogo e premir `Espaço` para o chamar, todo o seu histórico de ida e volta é perfeitamente restaurado! Funciona para Chat Direto, Análise de Visão, Chat de Documentos e Tradução.
* **Descrições de Imagem Inline no OCR**: Adicionada uma funcionalidade opcional para descrever imagens inline durante o OCR de documentos. Pode alternar esta definição nas definições de OCR do suplemento, dentro das opções do Leitor de Documentos antes da extração, e rapidamente em tempo real através da camada de Definições Rápidas.
* **Tradução por Voz (`Control+T`)**: Adicionada uma nova e poderosa funcionalidade! Dite fala e traduza-a e escreva-a instantaneamente utilizando a IA com base nos seus idiomas de origem e destino configurados.
* **Melhorias no Descarregador de Atualizações**: A caixa de diálogo de descarregador de atualizações exibe agora corretamente o progresso do descarregamento em percentagens, e foi corrigido um erro em que aparecia uma mensagem fantasma "A descarregar atualização" ao cancelar a instalação.
* **Melhorias no Descarregador do eSk-NG**: Adicionado o acompanhamento de progresso em percentagem para os descarregamentos do eSpeak-NG.
* **Resiliência de OCR em Lote**: Corrigido um problema no OCR de PDFs em lote em que o processo parava se a chave de API ativa atingisse a respetiva quota a meio; agora, muda automaticamente para a próxima chave disponível e retoma o processo.
* **Suporte para Captcha Visual**: Adicionado suporte robusto para a resolução de captchas visuais. Tenta resolver automaticamente desafios de imagem complexos como hCaptcha e reCAPTCHA, melhorando significativamente a acessibilidade em formulários web desafiantes.
* **Reformulação do Transcritor de Áudio**: O módulo Transcritor de Áudio foi completamente reestruturado e suporta agora ficheiros de áudio e vídeo. Apresenta 3 modos de operação distintos: "Transcrever (Idioma Original)", "Transcrever e Traduzir (Idioma de Destino)" e uma nova e poderosa opção "Dobrar e Traduzir (Idioma de Destino)" (exclusiva do Gemini) que gera uma dobragem de áudio traduzida da fala original.
* **Números de Página Opcionais no Leitor de Documentos**: Adicionada uma nova definição para alternar a inclusão de números de página e separadores em saídas de documentos de várias páginas. Pode gerir facilmente esta opção a partir das definições principais ou ativá-la/desativá-la em tempo real através da camada de Definições Rápidas. Esta funcionalidade aplica-se tanto às exportações de ficheiros de texto/HTML como à janela inline "Ver Formatado", permitindo-lhe ler documentos combinados sem interrupções.
* **TTS Gemini Live Ilimitado para Descrições de Vídeo**: Pode agora selecionar "Gemini Live TTS" como o motor de voz ao gerar Narração de Áudio Sincronizada (MP3) para vídeos. Isto utiliza a API Gemini Live para sintetizar audiodescrições de alta qualidade sem quaisquer limites de carateres ou restrições de comprimento.
* **Modularização da Base de Código**: A estrutura do suplemento foi refatorada de um único ficheiro para uma arquitetura modular de múltiplos ficheiros para melhorar a manutenibilidade.
* **Redesign da UI de Definições**: A caixa de diálogo de Definições foi completamente redesenhada para utilizar uma interface moderna baseada em separadores em vez de um layout agrupado, proporcionando uma melhor organização e navegação mais fácil, mantendo todas as opções existentes.
* **Registo de Ficheiro Global e Dedicado**: Adicionado um sistema de registo de ficheiro global opcional sob o novo separador de definições "Avançado". Captura automaticamente eventos operacionais, tráfego de API e erros em todos os módulos do suplemento num ficheiro dedicado (`vision_assistant.log`). Suporta níveis de detalhe de registo configuráveis (Depuração, Informação, Aviso, Erro), períodos de retenção automatizados (1 hora a 90 dias) e abertura ou limpeza direta de registos a partir das definições, sem impacto no desempenho ou interferência com os registos do NVDA.
* **Acompanhamento de Progresso de Carregamento do Gemini**: Adicionados anúncios de progresso em percentagem em tempo real ao carregar ficheiros grandes (vídeo, áudio, documentos) para a API do Google Gemini.

## Alterações para 2026.07.15

* **Filtragem Inteligente de Modelos de API**: Reformulação completa do sistema de filtragem de modelos para utilizar uma abordagem de lista negra pura em vez de listas brancas. Foram adicionadas palavras-chave de filtragem mais fortes (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`) para garantir que a lista pendente principal do modelo de chat permaneça perfeitamente limpa e preparada para o futuro, mantendo todos os modelos especializados acessíveis na secção de Encaminhamento Avançado.
* **Pesquisa de Encaminhamento Avançado**: Todas as listas pendentes de Encaminhamento Avançado de Modelos (OCR, STT, TTS, Operador, Vídeo, Em Direto) e o seletor de Variante eSpeak são agora totalmente pesquisáveis. Pode escrever rapidamente para filtrar e encontrar o modelo ou variante pretendidos.
* **Novos Atalhos da Camada de Comandos**:
* **Definições (`Alt + S`)**: Abre instantaneamente a caixa de diálogo de definições do Vision Assistant Pro.
* **Relatório de Chaves com Quota Esgotada (`Alt + Q`)**: Informa o número exato de chaves da API do Gemini que excederam a sua quota diária, identificando em que modelo específico estão esgotadas e anunciando o seu tempo exato de reinicialização.
* **Auditoria de Encaminhamento (`Alt + M`)**: Audita e anuncia a sua configuração atual de Encaminhamento Avançado, lendo quais os modelos selecionados ativamente para tarefas especializadas (ignorando as definições predefinidas).

* **Reformulação Completa do Analisador de Vídeo**: O Analisador de Vídeo foi completamente transformado! Anteriormente, fornecia apenas uma descrição básica de vídeos online. Agora, é um pacote abrangente de processamento de vídeo adaptado para utilizadores cegos:
* **Gravação de Ecrã Local (`Control+V`)**: Pode agora gravar vídeos silenciosos diretamente a partir do seu ecrã. A IA analisará o segmento gravado e fornecerá uma descrição altamente detalhada da cena, layout e ações.
* **Geração de Audiodescrição (SRT)**: O suplemento pode agora gerar scripts de Audiodescrição altamente detalhados (no formato SRT padrão) para vídeos, completos com temporização de intervalos inteligente para ancorar inteligentemente as descrições a pausas naturais na faixa de áudio, e OCR literal para qualquer texto no ecrã.
* **Narração de Áudio Sincronizada (Exportação MP3)**: Para além de legendas baseadas em texto, o suplemento pode sintetizar a Audiodescrição em fala, misturá-la automaticamente com a faixa de áudio original do vídeo, aplicar atenuação de áudio (baixar o volume de fundo durante as descrições) e exportar o resultado final sincronizado como um ficheiro MP3!
* **Ação Inteligente em Ficheiros de Vídeo**: Se focar um ficheiro de vídeo local e premir o atalho de vídeo, o suplemento detetá-lo-á automaticamente e processará o ficheiro diretamente.
* **Acompanhamento Avançado de Personagens**: A IA efetua agora uma passagem prévia de extração de personagens. Constrói um dicionário global de personagens e acompanha as mesmas com precisão, segmento a segmento, sem confundir identidades.
* **Configuração de Análise de Vídeo**: Adicionadas novas definições para controlar tamanhos de blocos SRT, legendagem de personagens e avisos de isenção de responsabilidade.
* **Encaminhamento Avançado de Modelos**: Pode agora selecionar explicitamente modelos de vídeo especializados (`gemini_video_model`, `custom_video_model`) nas definições de Encaminhamento Avançado de Modelos.

* **Gestão Inteligente de Quotas de API**: Tratamento melhorado de erros 429 (Limite Diário) através do acompanhamento de quotas por modelo. Se uma chave atinge o seu limite diário num modelo, é colocada em quarentena de forma inteligente apenas para esse modelo específico, mantendo a chave disponível para utilização com outros modelos.

## Alterações para 7.0.0

* **Retoma de Exames Não Concluídos**: Adicionada uma funcionalidade de retoma tanto para o Leitor de Documentos como para as Ações Inteligentes em Ficheiros. Se um exame for interrompido, pode agora continuar a partir de onde parou em vez de recomeçar do zero.
* **Nova Variável `[screen_fg_obj]**`: Adicionada uma variável de prompt personalizada para capturar uma captura de ecrã apenas da janela em primeiro plano ativa, em vez de todo o ecrã.
* **Tentativas Inteligentes e Rotação de Chaves**: O suplemento tenta agora silenciosamente até 5 vezes na mesma chave quando ocorrem sobrecargas temporárias do servidor (como "alta procura" ou respostas malformadas). Se as tentativas falharem, muda automaticamente para a próxima chave de API na sua lista.
* **Deteção de Cortina de Ecrã (Screen Curtain)**: Adicionada uma verificação para evitar tirar capturas de ecrã quando a Cortina de Ecrã está ativa (esteja ativada permanentemente ou alternada temporariamente com a tecla de atalho). Irá avisá-lo e parar, evitando o envio de imagens pretas e o desperdício de tokens de API.
* **Ajustes no Leitor de Documentos**: A caixa de diálogo de intervalos de PDF pré-seleciona agora automaticamente o idioma de destino predefinido a partir das definições do seu suplemento. Também foi melhorada a gestão de threads para garantir que as tarefas em segundo plano param de forma limpa quando o leitor é fechado.
* **Integração Nativa de OCR da Mistral**: Integrada a API de OCR de Documentos nativa da Mistral. Os documentos de várias páginas são automaticamente unidos, carregados e processados em lotes utilizando o ponto de extremidade especializado `/v1/ocr` da Mistral, enquanto as imagens de uma única página são processadas diretamente sem conversões desnecessárias de PDF [1].
* **Gestores de URLs Personalizados Dinâmicos**: A modificação do URL da API Personalizada limpa agora instantaneamente a lista de modelos em cache e restaura a caixa de texto de introdução manual de modelos. Isto garante total compatibilidade com pontos de extremidade personalizados (como o Cloudflare AI Gateway) que não suportam o ponto de extremidade de listagem padrão `/v1/models`.
* **Motor de Entrada do Operador de IA Reformulado**: O sistema de simulação de rato e teclado subjacente para o Operador de IA foi totalmente reescrito. A API legada `mouse_event` foi substituída pela API moderna do Windows `SendInput`, trazendo uma compatibilidade significativamente superior com aplicações modernas, janelas protegidas pelo UAC e ecrãs de alto DPI.
* **Correção de Operações de Arrastar e Soltar (Drag & Drop)**: As ações de arrastar e soltar no Operador de IA são agora totalmente estáveis e fiáveis. O novo motor utiliza curvas de "suavização" naturais, posicionamento preciso do cursor, temporização otimizada e uma técnica inteligente de "impulso" para garantir que o Windows e as aplicações reconhecem e executam corretamente os gestos de arrastar e soltar sem falhar a meio.
* **Suporte para Vários Monitores**: O Operador de IA suporta agora totalmente configurações com vários monitores. Os movimentos do rato e cliques funcionam corretamente em todos os monitores utilizando a flag `MOUSEEVENTF_VIRTUALDESK`, garantindo um posicionalamento preciso independentemente do monitor em que a aplicação de destino se encontra.
* **Simulação de Teclado Melhorada**: A injeção de teclas foi melhorada para suportar totalmente "Teclas Estendidas" (como as setas, Home, End, Page Up/Down, Insert, Delete e F1-F12). Isto garante que os comandos de navegação e atalhos enviados pelo Operador de IA funcionam sem falhas em todas as aplicações.
* **Suporte para Imagens HEIC/HEIF**: Adicionado suporte nativo para formatos de fotografia do iPhone. Pode agora selecionar diretamente ficheiros `.heic` e `.heif` para descrição por IA, OCR ou Leitura de Documentos sem necessidade de conversão prévia.

## Alterações para 6.5.0

* **Assistente em Direto**: Adicionada uma funcionalidade de assistente de voz e ecrã em tempo real, disponível exclusivamente para o fornecedor Google Gemini (ou fornecedores personalizados compatíveis com o Gemini). Inclui personalização interativa de voz e profundidade de pensamento diretamente dentro da caixa de diálogo, com reconexão automática ao alterar as definições.
* **Fornecedor de IA MiniMax**: Integrado o MiniMax como fornecedor integrado com suporte multimodal completo (chat, visão, OCR), TTS personalizado utilizando mais de 300+ vozes dinâmicas e remoção automática de blocos de raciocínio (por exemplo, `<think>...</think>`) das respostas.
* **Tradução do Visualizador de Documentos**: Corrigida uma falha de tradução silenciosa para utilizadores do NVDA que não usam o inglês, garantindo que o código de idioma padrão de 2 letras é enviado para o Google Translate em vez do nome do idioma localizado.
* **Tentativa Repetida de OCR em Lote de PDF**: Implementada uma lógica de tentativa repetida altamente otimizada, separada e silenciosa para o exame em lote de documentos PDF, para evitar carregamentos redundantes e pop-ups de erro disruptivos durante as tentativas.
* **Estado do Visualizador de Documentos**: Corrigido um erro em que o estado geral do suplemento (verificado através de `I`) ficava preso em "Processamento em Lote Iniciado" durante exames longos de documentos.
* **Resolução de Crash por Threading**: Corrigido um erro grave de asserção de thread `IsMain() failed in wxTimerImpl` ao abrir documentos a partir de uma thread em segundo plano, efetuando a transição da fila de callbacks da GUI para `wx.CallAfter`.

## Alterações para 6.1.2

* **Pré-verificação de Rótulos Duplicados**: Corrigido um problema na rotulagem individual em que a verificação de duplicados utilizava chaves de coordenadas antigas, fazendo com que o NVDA fizesse pedidos de IA duplicados para objetos já rotulados em vez de anunciar o rótulo existente.
* **Chat de Documentos para Fornecedores Não-Gemini**: Corrigida uma verificação estrita de chave de API no Chat de Documentos (`on_ask`) para garantir que os utilizadores na OpenAI, Groq ou fornecedores personalizados locais (como o Ollama) conseguem conversar com documentos com sucesso sem serem bloqueados.
* **OCR Rápido do Chrome**: Restaurada a API de tradução gratuita e sem chave para o OCR do Chrome. Traduzir texto extraído ignora agora a Gemini AI, poupando quotas de API e acelerando o processo de tradução.
* **Filtro Alfanumérico de CAPTCHA**: Corrigida a lógica de filtragem no resolvedor de CAPTCHA para garantir que os caracteres não alfanuméricos são devidamente limpos em todas as situações.
* **Atualização da Ajuda da Camada de Comandos**: Corrigido o atalho de anúncio de estado no menu de ajuda de `L` para `I` e adicionados ambos os comandos de rotulagem (`L` e `Shift+L`) à lista.

## Alterações para 6.1.1

* **Correção de Saída de Pensamento do Gemma 4**: Corrigido um problema com modelos Gemma 4 em que todo o processo de pensamento interno era exibido como a resposta final, ou em que a desativação do pensamento resultava em respostas vazias. O suplemento isola e extrai agora corretamente apenas a resposta de texto limpa final.
* **OCR em Lote a partir do Explorador de Ficheiros**: Pode agora selecionar várias fotografias ou PDFs diretamente no Explorador de Ficheiros do Windows e extrair texto ou analisá-los em lote. O suplemento filtrará e processará automaticamente apenas os formatos de ficheiro suportados.

## Alterações para 6.1.0

* **Integração Universal de IA Local (Configurar IA Local)**: Adicionado um novo botão **"Configurar IA Local"** nas Definições de Fornecedor Personalizado. Os utilizadores podem agora configurar automaticamente motores de IA local, incluindo **Ollama**, **LM Studio**, **Jan.ai** e **KoboldCPP**, instantaneamente.
* **Contornamento Inteligente de Proxy Local**: A lógica de ligação foi reconstruída com um mecanismo avançado de contornamento de proxy. O suplemento é agora suficientemente inteligente para contornar totalmente os proxies de sistema do Windows para ligações de loopback locais, garantindo ligações de IA local estáveis mesmo quando a sua VPN em modo TUN está ativa.
* **Rotulagem de IA Ultra-Estável (v2)**: As chaves de coordenadas absolutas do ecrã foram substituídas por um sistema híbrido avançado de "Assinatura de Objeto". Os rótulos baseiam-se agora em identificadores programáticos (UIA **AutomationId** ou Win32 **ControlID**) e coordenadas relativas à janela, tornando os seus rótulos personalizados totalmente resistentes a redimensionamentos de janelas, deslocamentos, trocas de monitores ou escala.
* **Migração Automática e Transparente de Rótulos**: A atualização é totalmente transparente. O suplemento migrará automaticamente os seus rótulos baseados em coordenadas legadas mais antigos para o novo formato de impressão digital estável em segundo plano aquando da primeira focagem, sem perda de dados.

## Alterações para 6.0

* **Introdução da Rotulagem Semântica por IA**: Os utilizadores podem agora rotular permanentemente botões e ícones sem rótulo utilizando IA. Prima **L** para rotular o objeto navegador atual (suportando tanto o foco por Tab como a navegação por objetos) ou **Shift+L** para examinar e rotular toda a aplicação de uma só vez.
* **Gestão Inteligente de Rótulos**: Adicionada uma nova caixa de diálogo de Gestor de Rótulos totalmente acessível (através de **Shift+L** se existirem rótulos) para ver, mudar o nome ou eliminar em lote rótulos personalizados.
* **Análise Direta de Ficheiros (Ignorar Caixa de Diálogo de Ficheiros)**: O suplemento é agora suficientemente inteligente para detetar se está atualmente a focar um ficheiro PDF ou de imagem no Explorador de Ficheiros do Windows. Premir **F (Ação Inteligente em Ficheiros)** ou **D (Leitor de Documentos)** num ficheiro realçado irá processá-lo imediatamente, ignorando por completo a caixa de diálogo "Abrir" padrão.

## Alterações para 5.6

* **Adicionado o Motor de OCR "Nenhum (Extrair Camada de Texto)"**: Os utilizadores podem agora extrair texto diretamente de PDFs pesquisáveis sem utilizar créditos de IA, melhorando significativamente a velocidade e a privacidade para documentos baseados em texto.
* **Precisão Refinada do Explorador de UI**: O prompt do Explorador de UI foi melhorado para identificar melhor os tipos de elementos (como Itens de Lista) e relatar com precisão estados como "(Marcado)", "(Selecionado)" ou "(Expandido)", ignorando componentes de sistema do Windows como a Barra de Tarefas e o Relógio.
* **Lembrete de Configuração de Instalação**: Adicionada uma notificação após a instalação para guiar os utilizadores até ao menu de definições para configurarem as suas chaves de API e preferências.

## Alterações para 5.5.2

* **Correção de Problema de Escrita do Operador de IA:** Resolvido um erro em que a letra 'v' era escrita em vez de colar texto em determinados sistemas. Esta correção aborda conflitos de temporização que ocorriam durante uma carga elevada do sistema.
* **Estabilidade Melhorada:** Adicionada uma gestão robusta de erros para operações da área de transferência, para evitar crashes do suplemento quando a área de transferência do sistema é bloqueada temporariamente por outras aplicações.
* **Otimização de Temporização:** Ajustados os atrasos internos para eventos de teclado para garantir maior fiabilidade em diferentes velocidades de sistema e melhor compatibilidade com Gestores de Área de Transferência de terceiros.

## Alterações para 5.5 (A Atualização de Automação)

* **Operador de IA (Controlo Autónomo - Shift+A):** Esta é a joia da coroa da v5.5. O Vision Assistant Pro evoluiu de um assistente passivo para se tornar no seu **Operador de IA** pessoal. Não se limita a descrever o ecrã — assume o comando.
* _Como funciona:_ Pode agora dar instruções verbais para operar o seu PC. Por exemplo, numa aplicação completamente inacessível onde o seu leitor de ecrã fica em silêncio, pode premir **Shift+A** e escrever: _"Clica no botão Definições"_ ou _"Encontra o campo de pesquisa, escreve 'Últimas Notícias' e prime enter."_ A IA identifica visualmente os elementos, move o rato e executa a tarefa por si.
* _Nota de Desempenho:_ Esta funcionalidade está otimizada para **Gemini 3.0 Flash (Pré-visualização)**, proporcionando respostas incrivelmente rápidas e inteligentes que conseguem lidar até com os layouts de UI mais complexos.
* _⚠️ Aviso de Utilização da API:_ Como o Operador de IA precisa de "ver" exatamente o que está a acontecer para ser preciso, envia uma captura de ecrã de alta resolução a cada passo. Note que a utilização frequente consumirá a sua quota de API muito mais rapidamente do que as tarefas padrão baseadas em texto.

* **Explorador de UI Visual (E):** Cansado de navegar através de "botões sem rótulo"? Prima **E** para ativar o Explorador de UI. A IA examinará toda a janela e gerará uma lista de cada elemento clicável que vê — incluindo ícones, gráficos e menus. Basta escolher um item da lista e o Operador de IA clicará nele por si. É como ter uma "camada acessível" por cima de qualquer aplicação.
* **Ação Inteligente em Ficheiros Consciente do Contexto (F):** A tecla "F" foi completamente reestruturada. Deixa de assumir que quer apenas OCR. Quando seleciona uma única imagem, pede agora inteligentemente qual a sua intenção: pode escolher uma **Descrição Visual Detalhada** para compreender a cena ou uma **Extração de Texto Estruturada (OCR)** para leitura. O menu adapta-se dinamicamente com base no formato do ficheiro e no seu motor de IA ativo.
* **Otimização do Núcleo:** Efetuámos uma limpeza profunda da lógica interna do suplemento, removendo funções legadas não utilizadas e código redundante. Isto resulta numa experiência mais leve, rápida e fiável para todos os utilizadores.

## Alterações para 5.0

* **Arquitetura Multi-Fornecedor**: Adicionado suporte completo para **OpenAI**, **Groq** e **Mistral** a par do Google Gemini. Os utilizadores podem agora escolher o seu backend de IA preferido.
* **Encaminhamento Avançado de Modelos**: Os utilizadores de fornecedores nativos (Gemini, OpenAI, etc.) podem agora selecionar modelos específicos a partir de uma lista pendente para diferentes tarefas (OCR, STT, TTS).
* **Configuração Avançada de Ponto de Extremidade**: Os utilizadores de fornecedores personalizados podem introduzir manualmente URLs específicos e nomes de modelos para um controlo granular sobre servidores locais ou de terceiros.
* **Visibilidade Inteligente de Funcionalidades**: O menu de definições e a UI do Leitor de Documentos ocultam automaticamente funcionalidades não suportadas (como o TTS) com base no fornecedor selecionado.
* **Obtenção Dinâmica de Modelos**: O suplemento obtém agora a lista de modelos disponíveis diretamente a partir da API do fornecedor, garantindo compatibilidade com novos modelos assim que são lançados.
* **OCR Híbrido e Tradução**: Otimizada a lógica para utilizar o Google Translate para velocidade ao utilizar o OCR do Chrome, e tradução potenciada por IA ao utilizar os motores Gemini/Groq/OpenAI.
* **"Reexaminar com IA" Universal**: A funcionalidade de reexame do Leitor de Documentos deixa de estar limitada ao Gemini. Utiliza agora qualquer fornecedor de IA que esteja ativo no momento para reprocessar as páginas.

## Alterações para 4.6

* **Recuperação Interativa de Resultados:** Adicionada a tecla **Espaço** à camada de comandos, permitindo aos utilizadores reabrir instantaneamente a última resposta da IA numa janela de chat para perguntas de seguimento, mesmo quando o modo "Saída Direta" está ativo.
* **Centro da Comunidade do Telegram:** Adicionada uma hiperligação para o "Canal Oficial do Telegram" ao menu Ferramentas do NVDA, proporcionando uma forma rápida de se manter atualizado com as últimas notícias, funcionalidades e lançamentos.
* **Estabilidade de Resposta Melhorada:** Otimizada a lógica principal para as funcionalidades de Tradução, OCR e Visão para garantir um desempenho mais fiável e uma experiência mais fluída ao utilizar a saída de fala direta.
* **Orientação de Interface Melhorada:** Atualizadas as descrições das definições e a documentação para explicar melhor o novo sistema de recuperação e como funciona juntamente com as definições de saída direta.

## Alterações para 4.5

* **Gestor Avançado de Prompts:** Introduzida uma caixa de diálogo de gestão dedicada nas definições para personalizar prompts de sistema predefinidos e gerir prompts definidos pelo utilizador com suporte total para adicionar, editar, reordenar e pré-visualizar.
* **Suporte Abrangente para Proxy:** Resolvidos problemas de conectividade de rede ao garantir que as definições de proxy configuradas pelo utilizador são estritamente aplicadas a todos os pedidos de API, incluindo tradução, OCR e geração de fala.
* **Migração Automatizada de Dados:** Integrado um sistema de migração inteligente para atualizar automaticamente as configurações de prompts legadas para um formato JSON v2 robusto aquando da primeira execução sem perda de dados.
* **Compatibilidade Atualizada (2025.1):** Definida a versão mínima exigida do NVDA para 2025.1 devido a dependências de bibliotecas em funcionalidades avançadas como o Leitor de Documentos, para garantir um desempenho estável.
* **Interface de Definições Otimizada:** Simplificada a interface de definições reorganizando a gestão de prompts numa caixa de diálogo separada, proporcionando uma experiência de utilizador mais limpa e acessível.
* **Guia de Variáveis de Prompts:** Adicionado um guia integrado dentro das caixas de diálogo de prompts para ajudar os utilizadores a identificar e utilizar facilmente variáveis dinâmicas como [selection], [clipboard] e [screen_obj].

## Alterações para 4.0.3

* **Resiliência de Rede Melhorada:** Adicionado um mecanismo de tentativa automática para melhor lidar com ligações de internet instáveis e erros temporários de servidor, garantindo respostas de IA mais fiáveis.
* **Caixa de Diálogo de Tradução Visual:** Introduzida uma janela dedicada para resultados de tradução. Os utilizadores podem agora navegar e ler facilmente traduções longas linha a linha, de forma semelhante aos resultados de OCR.
* **Vista Formatada Agregada:** A funcionalidade "Ver Formatado" no Leitor de Documentos exibe agora todas as páginas processadas numa única janela organizada com cabeçalhos de página claros.
* **Fluxo de Trabalho de OCR Otimizado:** Ignora automaticamente a seleção de intervalos de páginas para documentos de uma única página, tornando o processo de reconhecimento mais rápido e fluido.
* **Estabilidade de API Melhorada:** Mudança para um método de autenticação baseado em cabeçalhos mais robusto, resolvendo potenciais erros de "Todas as chaves de API falharam" causados por conflitos de rotação de chaves.
* **Correções de Erros:** Resolvidos vários crashes potenciais, incluindo um problema durante a terminação do suplemento e um erro de foco na caixa de diálogo de chat.

## Alterações para 4.0.1

* **Leitor de Documentos Avançado:** Um novo e poderoso visualizador para PDF e imagens com seleção de intervalos de páginas, processamento em segundo plano e navegação fluida `Ctrl+PageUp/Down`.
* **Novo Submenu de Ferramentas:** Adicionado um submenu dedicado "Vision Assistant" sob o menu Ferramentas do NVDA para um acesso mais rápido a funcionalidades principais, definições e documentação.
* **Personalização Flexível:** Pode agora escolher o seu motor de OCR preferido e voz TTS diretamente a partir do painel de definições.
* **Suporte para Múltiplas Chaves de API:** Adicionado suporte para múltiplas chaves da API do Gemini. Pode introduzir uma chave por linha ou separá-las com vírgulas nas definições.
* **Motor de OCR Alternativo:** Introduzido um novo motor de OCR para garantir um reconhecimento de texto fiável mesmo quando atinge os limites de quota da API do Gemini.
* **Rotação Inteligente de Chaves de API:** Muda automaticamente para a chave de API a funcionar mais rapidamente e memoriza-a para contornar os limites de quota.
* **Documento para MP3/WAV:** Capacidade integrada para gerar e guardar ficheiros de áudio de alta qualidade em formatos MP3 (128kbps) e WAV diretamente dentro do leitor.
* **Suporte para Instagram Stories:** Adicionada a capacidade de descrever e analisar Stories do Instagram utilizando os respetivos URLs.
* **Suporte para TikTok:** Introduzido suporte para vídeos do TikTok, permitindo a descrição visual completa e transcrição de áudio de clipes.
* **Caixa de Diálogo de Atualização Redesenhada:** Apresenta uma nova interface acessível com uma caixa de texto deslocável para ler claramente as alterações de versão antes de instalar.
* **Estado Unificado e UX:** Padronizadas as caixas de diálogo de ficheiros em todo o suplemento e melhorado o comando 'L' para relatar o progresso em tempo real.

## Alterações para 3.6.0

* **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) na Camada de Comandos para fornecer uma lista de fácil acesso de todos os atalhos e respetivas funções.
* **Análise de Vídeo Online:** Expandido o suporte para incluir vídeos do **Twitter (X)**. Também foi melhorada a deteção de URLs e a estabilidade para uma experiência mais fiável.
* **Contribuição para o Projeto:** Adicionada uma caixa de diálogo de doação opcional para utilizadores que desejem apoiar as futuras atualizações e o crescimento contínuo do projeto.

## Alterações para 3.5.0

* **Camada de Comandos:** Introduzido um sistema de Camada de Comandos (predefinição: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestra. Por exemplo, em vez de premir `NVDA+Control+Shift+T` para tradução, prime agora `NVDA+Shift+V` seguido de `T`.
* **Análise de Vídeo Online:** Adicionada uma nova funcionalidade para analisar vídeos do YouTube e Instagram diretamente fornecendo um URL.

## Alterações para 3.1.0

* **Modo de Saída Direta:** Adicionada uma opção para ignorar a caixa de diálogo de chat e ouvir as respostas da IA diretamente através de fala para uma experiência mais rápida e fluida.
* **Integração com a Área de Transferência:** Adicionada uma nova definição para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações para 3.0

* **Novos Idiomas:** Adicionadas traduções em **Persa** e **Vietnamita**.
* **Modelos de IA Expandidos:** Reorganizada a lista de seleção de modelos com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`) para ajudar os utilizadores a distinguir entre modelos gratuitos e limitados por taxa (pagos). Adicionado suporte para **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
* **Estabilidade de Ditado:** Significativamente melhorada a estabilidade do Ditado Inteligente. Adicionada uma verificação de segurança para ignorar clipes de áudio com menos de 1 segundo, prevenindo alucinações da IA e erros de conteúdo vazio.
* **Gestão de Ficheiros:** Corrigido um problema em que o carregamento de ficheiros com nomes não ingleses falhava.
* **Otimização de Prompts:** Melhorada a lógica de Tradução e resultados estruturados de Visão.

## Alterações para 2.9

* **Adicionadas traduções em Francês e Turco.**
* **Vista Formatada:** Adicionado um botão "Ver Formatado" nas caixas de diálogo de chat para ver a conversação com formatação adequada (Cabeçalhos, Negrito, Código) numa janela padrão navegável.
* **Definição de Markdown:** Adicionada uma nova opção "Limpar Markdown no Chat" nas Definições. Desmarcar esta opção permite aos utilizadores ver a sintaxe de Markdown em bruto (por exemplo, `**`, `#`) na janela de chat.
* **Gestão de Caixas de Diálogo:** Corrigido um problema em que as janelas "Refinar Texto" ou de chat abriam várias vezes ou falhavam ao focar corretamente.
* **Melhorias de UX:** Padronizados os títulos das caixas de diálogo de ficheiros para "Abrir" e removidos anúncios de fala redundantes (por exemplo, "A abrir menu...") para uma experiência mais fluida.

## Alterações para 2.8

* Adicionada tradução em Italiano.
* **Relatório de Estado:** Adicionado um novo comando (NVDA+Control+Shift+I) para anunciar o estado atual do suplemento (por exemplo, "A carregar...", "A analisar...").
* **Exportação HTML:** O botão "Guardar Conteúdo" nas caixas de diálogo de resultados guarda agora a saída como um ficheiro HTML formatado, preservando estilos como cabeçalhos e texto em negrito.
* **UI de Definições:** Melhorado o layout do painel de Definições com agrupamento acessível.
* **Novos Modelos:** Adicionado suporte para gemini-flash-latest e gemini-flash-lite-latest.
* **Idiomas:** Adicionado o Nepali aos idiomas suportados.
* **Lógica do Menu Refinar:** Corrigido um erro crítico em que os comandos "Refinar Texto" falhavam se o idioma da interface do NVDA não fosse o inglês.
* **Ditado:** Melhorada a deteção de silêncio para evitar saídas de texto incorretas quando não é introduzida fala.
* **Definições de Atualização:** "Verificar atualizações no arranque" está agora desativado por predefinição para cumprir as políticas da Loja de Suplementos.
* Limpeza de código.

## Alterações para 2.7

* Migração da estrutura do projeto para o Modelo Oficial de Suplementos da NV Access para uma melhor conformidade com as normas.
* Implementação de lógica de tentativa repetida automática para erros HTTP 429 (Limite de Taxa) para garantir a fiabilidade durante tráfego elevado.
* Otimização dos prompts de tradução para maior precisão e melhor tratamento da lógica de "Troca Inteligente" (Smart Swap).
* Atualização da tradução em Russo.

## Alterações para 2.6

* Adicionado suporte para tradução em Russo (Agradecimentos a nvda-ru).
* Atualização das mensagens de erro para fornecer feedback mais descritivo relativamente à conectividade.
* Alteração do idioma de destino predefinido para Inglês.

## Alterações para 2.5

* Adicionado o Comando de OCR de Ficheiro Nativo (NVDA+Control+Shift+F).
* Adicionado o botão "Guardar Chat" às caixas de diálogo de resultados.
* Implementação de suporte de localização completo (i18n).
* Migração do feedback de áudio para o módulo de tons nativo do NVDA.
* Mudança para a API de Ficheiros do Gemini para um melhor tratamento de ficheiros PDF e de áudio.
* Correção de um crash ao traduzir texto contendo chavetas.

## Alterações para 2.1.1

* Corrigido um problema em que a variável `[file_ocr]` não funcionava corretamente dentro de Prompts Personalizados.

## Alterações para 2.1

* Padronização de todos os atalhos para utilizar NVDA+Control+Shift de modo a eliminar conflitos com o esquema Portátil do NVDA e teclas de atalho do sistema.

## Alterações para 2.0

* Implementação de um sistema integrado de Atualização Automática.
* Adicionada Cache de Tradução Inteligente para a recuperação instantânea de texto traduzido anteriormente.
* Adicionada Memória de Conversação para refinar contextualmente os resultados em caixas de diálogo de chat.
* Adicionado Comando Dedicado de Tradução da Área de Transferência (NVDA+Control+Shift+Y).
* Otimização dos prompts de IA para impor estritamente a saída no idioma de destino.
* Correção de um crash causado por caracteres especiais no texto de entrada.

## Alterações para 1.5

* Adicionado suporte para mais de 20 novos idiomas.
* Implementação de Caixa de Diálogo de Refinamento Interativa para perguntas de seguimento.
* Adicionada funcionalidade de Ditado Inteligente Nativo.
* Adicionada a categoria "Vision Assistant" à caixa de diálogo de Gestos de Entrada do NVDA.
* Corrigidos crashes de COMError em aplicações específicas como o Firefox e o Word.
* Adicionado mecanismo de tentativa repetida automática para erros de servidor.

## Alterações para 1.0

* Lançamento inicial.
