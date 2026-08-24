# Documentação do Vision Assistant Pro

<!-- DOWNLOAD_COUNT_START --> Total Downloads: 62,863 <!-- DOWNLOAD_COUNT_END -->

O **Vision Assistant Pro** é um assistente de IA multimodal avançado para o NVDA. Ele utiliza motores de IA de classe mundial para oferecer leitura de tela inteligente, tradução, ditado por voz e análise de documentos.

_Este complemento foi disponibilizado à comunidade em homenagem ao Dia Internacional das Pessoas com Deficiência._

## 1. Configuração e Instalação

Acesse o **Menu do NVDA > Preferências > Configurações > Vision Assistant Pro**. A caixa de diálogo de configurações está organizada em 9 abas acessíveis: **Conexão**, **Assistente ao Vivo**, **Comportamento da IA**, **Idiomas de Tradução**, **Leitor de Documentos**, **Vídeo**, **CAPTCHA**, **Prompts** e **Avançado**.

### 1.1 Aba Conexão

- **Provedor:** Selecione o seu serviço de IA preferido. Os provedores suportados incluem **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** e **Personalizado** (servidores compatíveis com a OpenAI, como Ollama, LM Studio, Jan.ai ou KoboldCPP).
- **Chave da API:** Insira uma ou mais chaves de API (separadas por vírgulas ou quebras de linha) para rotação automática.
- **Obter Modelos:** Pressione este botão após inserir sua chave de API para baixar a lista de modelos mais recente disponível no provedor.
- **Modelo de IA:** Selecione o modelo principal utilizado para bate-papo geral e análise.
- **Configurações de Provedor Personalizado:** Configure pontos de extremidade (endpoints) locais ou personalizados. Inclui **Configurar IA Local** (configuração com um clique para Ollama, LM Studio, Jan.ai ou KoboldCPP) e **Configuração Avançada de Endpoint**.
- **Roteamento Avançado de Modelos (Específico por tarefa):** Opcionalmente, selecione modelos dedicados nas caixas de seleção para tarefas de OCR, STT, TTS, Operador de IA, Vídeo e Assistente ao Vivo.
- **Opções de Conexão e Saída:** Configure a URL do Proxy, verificação de atualizações ao iniciar, Limpar Markdown no Bate-Papo, Copiar respostas da IA para a área de transferência e Saída Direta (Sem Janela de Bate-Papo).

### 1.2 Aba Assistente ao Vivo

- **Assistente ao Vivo: Saída Direta (Sem Janela):** Inicia o Assistente ao Vivo sem a janela de conversa; abra-a mais tarde com a tecla de Chamar Último Resultado (`Espaço`).
- **Pressionar para Falar:** Alterna o modo pressionar para falar. Quando ativado, o microfone envia áudio apenas enquanto você mantém a tecla atribuída pressionada.
- **Tecla Pressionar para Falar:** Pressione as teclas para gravar o atalho (por exemplo `F12` ou `Ctrl+F12`) - você pode até atribuir uma tecla modificadora isolada, como `Ctrl Esquerdo`. Mantenha a tecla pressionada para falar e solte-a para finalizar; um sinal sonoro curto confirma cada toque e liberação.

Nota: Esta aba aparece apenas quando o **Google Gemini** (ou um provedor Personalizado compatível com o Gemini) estiver ativo.

### 1.3 Aba Comportamento da IA

- **Criatividade (Temperatura):** Controla a aleatoriedade e criatividade da IA (de 0,0 a 2,0). Valores mais baixos produzem resultados de tradução e OCR mais determinísticos e precisos.

### 1.4 Aba Idiomas de Tradução

- **Idioma de Origem:** Selecione seu idioma de entrada padrão.
- **Idioma de Destino:** Selecione seu idioma principal de tradução.
- **Idioma de Resposta da IA:** Selecione o idioma para as respostas gerais da IA.
- **Troca Inteligente:** Alterna automaticamente os idiomas de origem e destino com base no texto detectado.

### 1.5 Aba Leitor de Documentos

- **Mecanismo de OCR:** Escolha entre **Chrome (Rápido)** para resultados rápidos ou **IA (Avançado)** para superior preservação de layout.
- **Tamanho do Lote do OCR:** Especifique o número de páginas por solicitação (defina como 0 para processamento em uma única solicitação).
- **Descrever Imagens Inline:** Alterna as descrições de imagens no próprio texto durante a extração do documento.
- **Exportar Números de Página:** Alterna a inclusão de números de página e separadores na saída de documentos com várias páginas.
- **Voz TTS:** Selecione o estilo de voz padrão para a geração de áudio.

### 1.6 Aba Vídeo

- **Tamanho do Bloco de Vídeo:** Duração dos segmentos em minutos para a geração de Audiodescrição (defina como 0 para processar o arquivo inteiro).
- **Adicionar Lista de Personagens:** Opção para adicionar um dicionário de personagens como a primeira entrada de legenda.
- **Adicionar Aviso de IA:** Opção para inserir um aviso sobre o uso de IA no início das legendas SRT do vídeo.

### 1.7 Aba CAPTCHA

- **Ativar Resolução Visual de CAPTCHA:** Alterna a resolução automática de desafios visuais (hCaptcha, reCAPTCHA).
- **Método de CAPTCHA de Texto:** Escolha entre capturar o **Objeto do Navegador** ou a **Tela Inteira**.

### 1.8 Aba Prompts

- **Gerenciar Prompts:** Abre uma caixa de diálogo dedicada para personalizar os prompts padrão do sistema ou criar, editar, reordenar e pré-visualizar prompts personalizados do usuário com variáveis dinâmicas (ex.: `[selection]`, `[screen_fg_obj]`).
- **Atalhos de Prompts Personalizados:** Atribua uma tecla de atalho dedicada a qualquer prompt personalizado diretamente no Gerenciador de Prompts. Pressione as teclas para gravá-las - teclas únicas são executadas dentro da Camada de Comandos (e globalmente como `NVDA + Shift + tecla`), enquanto combinações como `Control + Shift + 1` são executadas globalmente de forma independente.

### 1.9 Aba Avançado e Log Global

Navegue até a aba **Avançado** para configurar o log global de eventos do complemento:

- **Ativar arquivo de log dedicado:** Alterna o registro de todos os eventos operacionais, tráfego da API e erros de todos os módulos do complemento em um arquivo separado (`vision_assistant.log`).
- **Nível do Log:** Selecione o nível de detalhe entre **Depuração (Todos os Detalhes)**, **Informação (Informação Geral)**, **Aviso (Apenas Avisos)** e **Erro (Apenas Erros)**.
- **Manter Logs Durante:** Defina períodos de retenção automática para limpar registros antigos automaticamente (variando de 1 hora a 90 dias).
- **Controles de Gerenciamento de Logs:** Use **Abrir Arquivo de Log**, **Abrir Pasta de Logs** ou **Limpar Arquivo de Log** para inspecionar ou apagar dados de log diretamente, sem reiniciar o NVDA ou interferir com os logs padrão do NVDA.

### 1.10 Backup e Restauração de Configurações

A aba **Avançado** também inclui uma seção de **Backup e Restauração**:

- **Backup:** Salva sua configuração em um único arquivo JSON. Ao clicar, você escolhe o que incluir: **Tudo** (configurações, etiquetas personalizadas, progresso do OCR e histórico) ou **Apenas Configurações**.
- **Restaurar:** Carrega um backup salvo anteriormente para restaurar sua configuração e dados a qualquer momento, em qualquer máquina ou após reinstalar o NVDA. Você deverá confirmar primeiro, pois a restauração substitui todas as suas configurações e dados atuais.

## 2. Camada de Comandos e Atalhos

Para evitar conflitos de teclado, este complemento utiliza uma **Camada de Comandos**.

1. Pressione **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (você ouvirá um sinal sonoro).
2. Solte as teclas e, em seguida, pressione uma das seguintes teclas individuais:

| Tecla                  | Função                                 | Descrição                                                                                                                               |
| ---------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Shift + A**          | **Operador de IA**                     | **Operação Autônoma:** Peça à IA para realizar uma tarefa na tela. Pressionar novamente aborta instantaneamente as operações ativas.    |
| **E**                  | **Explorador de UI**                   | **Clique Interativo:** Identifica e clica em elementos da interface em qualquer aplicativo.                                             |
| **T**                  | Tradutor Inteligente                   | Traduz o texto sob o cursor de navegação ou seleção.                                                                                    |
| **Shift + T**          | Tradutor da Área de Transferência      | Traduz o conteúdo atualmente na área de transferência.                                                                                  |
| **R**                  | Refinador de Texto                     | Resumir, Corrigir Gramática, Explicar ou executar **Prompts Personalizados**.                                                           |
| **V**                  | Visão do Objeto                        | Descreve o objeto de navegação atual.                                                                                                   |
| **O**                  | Visão de Tela Inteira                  | Analisa o layout e o conteúdo de toda a tela.                                                                                           |
| **Shift + V**          | Análise de Vídeo                       | Analisa arquivos de vídeo locais ou vídeos online do **YouTube**, **Instagram**, **TikTok** ou **Twitter (X)**.                         |
| **Control + V**        | Gravação de Vídeo Local                | Grava um vídeo silencioso da sua tela e analisa as ações e o layout.                                                                    |
| **D**                  | Leitor de Documentos                   | Leitor avançado para PDF, imagens e arquivos de texto simples/HTML com seleção de intervalo de páginas.                                 |
| **F**                  | **Ação de Arquivo Inteligente**        | Reconhecimento sensível ao contexto de arquivos de imagem, PDF ou TIFF selecionados.                                                    |
| **M**                  | Transcrição e Dublagem de Mídia        | Transcreve ou dubla arquivos de áudio/vídeo (MP3, WAV, MP4, etc.) para o seu idioma de destino.                                         |
| **C**                  | Solucionador de CAPTCHA                | Captura e resolve CAPTCHAs.                                                                                                             |
| **Shift + C**          | Bate-Papo Direto                       | Abre uma interface de bate-papo por texto direta com a IA.                                                                              |
| **S**                  | Ditado Inteligente                     | Converte voz em texto. Pressione para iniciar a gravação e novamente para parar/digitar.                                                |
| **Control+T**          | Tradução por Voz                       | Transcreve, traduz e digita o resultado com base nas suas configurações de idioma.                                                      |
| **Control+L**          | **Assistente ao Vivo**                 | **Copiloto em Tempo Real (Apenas Gemini):** Inicia ou encerra uma conversa de voz e tela ao vivo com o assistente de IA.                |
| **I**                  | Relatório de Status                    | Anuncia o progresso atual (ex.: "Analisando...", "Inativo").                                                                            |
| **L**                  | **Etiquetar Objeto**                   | **Rotulagem Semântica por IA:** Etiqueta permanentemente o elemento/ícone focado.                                                       |
| **Shift + L**          | **Gerenciar/Escanear Etiquetas**       | Abre o Gerenciador de Etiquetas (se existirem) ou escaneia o aplicativo em busca de elementos sem nome.                                 |
| **U**                  | Verificar Atualizações                 | Verifica manualmente no GitHub a existência da versão mais recente do complemento.                                                      |
| **Espaço**             | Chamar Último Resultado                | Mostra a última resposta da IA em uma janela de bate-papo para revisão ou acompanhamento.                                               |
| **H**                  | Ajuda de Comandos                      | Exibe uma lista de todos os atalhos disponíveis.                                                                                        |
| **Control + H**        | **Histórico**                          | Abre a caixa de diálogo do Histórico listando seus bate-papos e documentos anteriores, com filtros por tipo e opções de Excluir/Limpar. |
| **Alt + S**            | Configurações                          | Abre a caixa de diálogo de configurações do Vision Assistant Pro.                                                                       |
| **Alt + Q**            | Relatório de Chaves com Quota Esgotada | Informa o número de chaves de API do Gemini que excederam a cota diária e a respectiva hora de reinício.                                |
| **Alt + M**            | Auditoria de Roteamento                | Informa os modelos de IA atualmente selecionados no roteamento avançado.                                                                |
| **Cima / Baixo**       | Navegação nas Configurações Rápidas    | Navega entre as categorias de configurações rápidas (Provedor, Modelo, etc.) na camada.                                                 |
| **Esquerda / Direita** | Alterar Configuração Rápida            | Altera o valor da configuração rápida atualmente selecionada.                                                                           |

## 3. Bate-Papo e Histórico

As janelas de bate-papo e a caixa de diálogo do Histórico funcionam em todos os recursos, permitindo que você revise conversas e continue exatamente de onde parou.

### 3.1 Atalhos da Janela de Bate-Papo

Quando uma janela de bate-papo estiver aberta (Bate-Papo Direto, bate-papo de documento, refinamento e similares), você poderá revisar a conversa com:

- **Alt + Seta para Baixo:** Lê a próxima mensagem.
- **Alt + Seta para Cima:** Lê a mensagem anterior.
- **Alt + C:** Copia a mensagem atual.

### 3.2 Histórico (Control + H)

Pressione **Control + H** na Camada de Comandos para abrir a caixa de diálogo do **Histórico** com seus bate-papos e documentos anteriores, filtráveis por tipo (Tudo / Bate-papos / Documentos). Abra um bate-papo para continuar a conversa - incluindo seus arquivos anexados, que são reanexados automaticamente - ou abra um documento e continue a leitura. Pressione **Delete** em qualquer item para removê-lo, ou **Limpar Tudo** para esvaziar a lista.

## 4. Operador de IA - Controle Autônomo do Computador

O **Operador de IA** transforma o Vision Assistant Pro de um leitor passivo em um assistente ativo capaz de interagir com o seu computador em seu nome. Você pode pedir a ele para descrever a tela, responder a perguntas sobre o que vê ou até mesmo assumir o controle - clicando em botões, arrastando itens, digitando textos e navegando pelos aplicativos usando comandos em linguagem natural.

A maior vantagem? Funciona perfeitamente em softwares completamente inacessíveis. Se você estiver preso em um aplicativo personalizado, em uma área de trabalho remota ou em um site onde o seu leitor de tela fica totalmente silencioso, o operador não se importa. Como ele "vê" a tela visualmente, consegue encontrar, ler e interagir com elementos que não possuem nenhuma etiqueta de acessibilidade.

### Como Funciona

1. Pressione **NVDA + Shift + V** e, em seguida, pressione **Shift + A** (ou use o atalho direto) para abrir a caixa de diálogo do Operador de IA.
2. Digite o que deseja fazer em linguagem simples (ex.: "Clique no botão Salvar", "O que diz a mensagem de erro?" ou "Renomeie o arquivo para final.pdf").
3. A IA analisará sua tela, identificará os elementos relevantes e executará a ação ou fornecerá a resposta. Se uma tarefa exigir várias etapas, o operador continuará trabalhando até que esteja concluída.
4. Pressione **Shift + A** novamente a qualquer momento para abortar instantaneamente uma operação em andamento.

### Ações Suportadas

O operador compreende uma ampla variedade de comandos:

- **Descrever e Responder**: "Descreva o layout da tela" ou "O que diz a mensagem de erro?"
- **Clique**: "Clique no botão Salvar"
- **Clique com Botão Direito**: "Clique com o botão direito no arquivo"
- **Duplo Clique**: "Dê um duplo clique no documento"
- **Arrastar e Soltar**: "Arraste o documento para a pasta Arquivo"
- **Digitar**: "Digite 'Olá Mundo' na caixa de pesquisa"
- **Rolar (Scroll)**: "Role para baixo três vezes"
- **Pressionar Tecla**: "Pressione Enter", "Pressione Tab", "Pressione Esc"
- **Tarefas de Múltiplas Etapas**: "Abra o Explorador de Arquivos, encontre o relatório e renomeie-o para final.pdf"

### Notas Importantes

- **⚠️ Aviso de Uso da API**: Como o operador precisa "ver" exatamente o que está acontecendo na tela, ele envia uma captura de tela em alta resolução a cada etapa. O uso frequente consumirá sua cota de API muito mais rápido do que os recursos padrão baseados em texto.
- **Aplicativos com Privilégios de Administrador**: Se o NVDA não estiver sendo executado com privilégios de Administrador, o operador pode não conseguir interagir com janelas que exijam permissões elevadas. Essa é uma limitação de segurança do Windows e não um erro do complemento.
- **Melhores Práticas**: Para obter os melhores resultados, dê comandos claros e específicos. "Clique no botão azul Enviar na parte inferior do formulário" quase sempre funcionará melhor do que apenas "Clique no botão".

## 5. Análise de Vídeo e Audiodescrição

> **Nota:** Os recursos de Análise de Vídeo e Audiodescrição são executados estritamente pelo provedor **Google Gemini**. Certifique-se de que o seu provedor ativo nas configurações do complemento esteja definido como Google Gemini.

O Vision Assistant Pro introduz recursos poderosos de processamento de vídeo projetados especificamente para usuários cegos. Ele pode analisar tanto vídeos online quanto gravações de tela locais para fornecer descrições visuais altamente detalhadas e gerar roteiros profissionais de Audiodescrição (SRT).

### 5.1 Gravação de Tela Local (Control + V)

Se você encontrar um vídeo silencioso, uma animação ou um tutorial em sua tela, pode capturá-lo diretamente:

1. Pressione **NVDA + Shift + V** para entrar na Camada de Comandos e, em seguida, pressione **Control + V**.
2. O complemento gravará sua tela silenciosamente em segundo plano.
3. Pressione **Control + V** novamente para parar a gravação.
4. A IA analisará o segmento de vídeo gravado e fornecerá uma descrição altamente detalhada da cena, dos personagens e das ações.

### 5.2 Análise de Vídeo (Shift + V)

Você pode analisar tanto arquivos de vídeo locais quanto vídeos online. Basta selecionar um arquivo de vídeo local no Explorador de Arquivos do Windows ou copiar um link de vídeo online para a área de transferência. Você também pode pressionar **Shift + V** em qualquer lugar (como dentro de um reprodutor de mídia) para abrir uma caixa de diálogo onde pode procurar por um arquivo de vídeo ou colar uma URL manualmente.

- **Plataformas Online Suportadas:** YouTube, Instagram, TikTok e Twitter (X).
- A IA detectará automaticamente o arquivo local ou a URL, processará o vídeo e fornecerá uma descrição visual abrangente e um resumo em áudio.

### 5.3 Geração de Audiodescrição (SRT)

Para uma experiência mais estruturada, o complemento pode gerar roteiros profissionais de Audiodescrição no formato padrão SubRip (SRT).

- **Sincronização Inteligente por Pausas:** A IA escuta a faixa de áudio e ancora especificamente suas descrições visuais em pausas naturais e intervalos silenciosos para minimizar inteligentemente a sobreposição com os diálogos.
- **Rastreamento de Personagens:** O motor realiza uma análise prévia para extrair personagens distintas com base em características faciais imutáveis. Ele constrói um dicionário global para rastrear e etiquetar com precisão as personagens ao longo das diferentes cenas, sem confusões.
- **OCR de Texto Literal:** Qualquer texto que apareça na tela (placas, celulares, créditos) é rigorosamente citado de forma literal.
- **Como Usar:** Para ouvir a legenda gerada, basta colocar o arquivo `.srt` na mesma pasta do seu arquivo de vídeo e dar a ele exatamente o mesmo nome. Depois, configure seu reprodutor de mídia (ex.: VLC ou PotPlayer) para encaminhar o texto das legendas diretamente para o seu leitor de tela ou motor TTS durante a reprodução.

### 5.4 Narração de Áudio Sincronizada (Exportação MP3)

Além de criar arquivos SRT em texto, o complemento funciona como uma ferramenta completa de produção de Audiodescrição, sintetizando as descrições em voz e misturando-as com o vídeo. Você agora pode escolher o **Gemini Live TTS** como motor de voz, o qual utiliza a API do Gemini Live para gerar narrações de voz altamente realistas e ilimitadas. Ao gerar um MP3 para arquivos de vídeo locais, você dispõe de vários modos de mixagem:

- **AD Padrão (Misturar Voz):** A narração é sobreposta diretamente sobre o áudio do vídeo. Será perguntado se você deseja aplicar **Atenuação de Áudio (Ducking)** (reduzir o volume de fundo durante as descrições) para garantir que a narração fique clara.
- **AD Estendida (Pausar Áudio):** O motor pausa o áudio original do vídeo durante as descrições, garantindo que você nunca perca uma única palavra do diálogo original ou da narração da IA.
- **Vídeos do YouTube:** Para fontes do YouTube (que não são baixadas localmente), a exportação MP3 conterá estritamente a faixa de voz da IA sincronizada, sem o áudio de fundo do vídeo.

## 6. Transcrição e Dublagem de Mídia (M)

O Transcritor de Áudio foi completamente reconstruído para suportar arquivos de áudio e vídeo (MP3, WAV, MP4, MKV, etc.). Pressione **M** na Camada de Comandos para selecionar um arquivo de mídia e escolha um dos 3 modos de operação distintos:

1. **Transcrever (Idioma Original)**: Transcreve com precisão a fala em seu idioma original.
2. **Transcrever e Traduzir (Idioma de Destino)**: Transcreve a fala e a traduz para o seu idioma de destino configurado.
3. **Dublar e Traduzir (Idioma de Destino)** _(Apenas Gemini)_: Um novo recurso poderoso que transcreve a fala, traduz para o seu idioma de destino e sintetiza uma dublagem em áudio falado utilizando o motor TTS do complemento.

## 7. Leitor Avançado de Documentos e Imagens

O **Leitor de Documentos** transforma seus documentos em texto limpo e legível - para que você possa ler, traduzir e ouvir qualquer coisa, desde um livro escaneado até uma pilha de fotos. Ele manipula PDFs de várias páginas, imagens complexas, formatos HEIC do iPhone e até arquivos de texto simples (`.txt`) e HTML (`.html`, `.htm`), que são abertos instantaneamente sem OCR ou processamento de IA. Selecione vários arquivos de uma vez e eles serão mesclados em um único documento contínuo na ordem das páginas. Três motores de OCR estão disponíveis - **Chrome (Rápido)**, **IA (Avançado)** para preservação superior de layout e **Nenhum (Extrair Camada de Texto)** para PDFs pesquisáveis - selecionados em Configurações → Leitor de Documentos.

### Como Funciona

1. Pressione **NVDA + Shift + V** e, em seguida, **D** para abrir o Leitor de Documentos - ou selecione um arquivo no Explorador de Arquivos primeiro e pressione **D** / **F** para ignorar completamente a caixa de seleção de arquivos.
2. Escolha um ou mais PDFs ou imagens. O complemento os analisará e anunciará a contagem total de páginas.
3. Na caixa de diálogo **Opções**, escolha o intervalo de páginas (De/Para). Você também pode marcar **Traduzir Resultado** e escolher o idioma de destino, ou alternar **Descrever imagens embutidas durante o OCR**.
4. A extração de texto começa em segundo plano em lotes. Você pode fechar a janela a qualquer momento e continuar mais tarde - nada é perdido.
5. Assim que as páginas estiverem prontas, leia-as no visualizador: mova-se entre as páginas, vá para qualquer página, faça perguntas à IA, salve o texto ou gere uma narração em áudio.

### 7.1 Processamento em Lote e Retomada

Você não precisa ler um documento enorme de uma só vez. Escolha um intervalo de páginas (ex.: `1-20`) ou mantenha os padrões para processar tudo, e a IA extrairá todas as páginas em segundo plano. Se o NVDA travar ou se você interromper a análise, o complemento se lembrará do seu progresso e oferecerá a opção de **Retomar** exatamente de onde parou - mesmo após reiniciar. Documentos concluídos também são mantidos em cache, portanto, reabri-los (a partir dos Documentos Recentes ou via **D**) carrega o texto instantaneamente sem executar o OCR novamente, a menos que os arquivos de origem tenham sido alterados.

### 7.2 Ação de Arquivo Inteligente

Você nem sempre precisa abrir o documento primeiro. No Explorador de Arquivos do Windows, basta selecionar um arquivo PDF, imagem ou texto/HTML e pressionar **D** (Leitor de Documentos) - ou selecionar um PDF ou imagem e pressionar **F** (Ação de Arquivo Inteligente) - dentro da Camada de Comandos. O complemento ignora instantaneamente a caixa de seleção de arquivos e começa a processar o arquivo selecionado. Selecionar vários arquivos de uma vez os processa juntos como um único documento.

### 7.3 Controles e Atalhos do Visualizador de Documentos

Quando a janela do Leitor de Documentos estiver aberta, você poderá usar os seguintes recursos:

#### Atalhos de Teclado

- **Ctrl + PageDown / Ctrl + PageUp:** Move para a próxima página / página anterior.
- **Seta para Baixo / Seta para Cima:** Quando o cursor atingir a última linha de uma página, pressione **Seta para Baixo** para ir para a próxima página; pressione **Seta para Cima** no topo de uma página para voltar à anterior.
- **Alt + A:** Abre uma caixa de diálogo de bate-papo para fazer perguntas sobre o documento.
- **Alt + R:** Força uma **Nova Análise com IA** utilizando o seu provedor ativo.
- **Alt + G:** Gera e salva um arquivo de áudio de alta qualidade (WAV/MP3). _(Oculto se o provedor não suportar TTS)._
- **Alt + S / Ctrl + S:** Salva o texto extraído como um arquivo TXT ou HTML.

#### Botões e Controles

- **Ir para:** Escolha qualquer página no seletor de páginas.
- **Ver Formatado:** Veja o documento inteiro combinado como texto formatado.
- **Tentar Novamente Páginas com Falha:** Tenta novamente apenas os lotes que falharam devido a um erro temporário do servidor (ex.: alta demanda). Este botão aparece automaticamente quando necessário.
- **Voz do TTS / Motor de TTS:** Escolha a voz e, no Gemini, escolha entre **TTS Padrão** e transmissão em tempo real via **Gemini Live**.
- **Anterior / Próxima:** Alterna entre as páginas (mesmo funcionamento dos atalhos Ctrl+PageUp/PageDown).

### 7.4 Documentos Recentes (D)

Pressionar **D** na Camada de Comandos lista primeiramente os seus documentos lidos recentemente. Escolha um para continuar a partir da página em que parou - mesmo que o OCR já tenha sido concluído - ou pressione **Abrir Arquivo...** (`Ctrl + O`) para procurar por um arquivo normalmente.

## 8. Rotulagem Semântica por IA e Explorador de Interface

Preso em um aplicativo cheio de "botão sem rótulo" por toda parte? O motor de Rotulagem Semântica por IA resolve isso definitivamente.

### 8.1 Rotulagem Permanente de Objetos (L)

Foque o seu leitor de tela em um gráfico ou botão sem rótulo e pressione **L** na Camada de Comandos. A IA analisará o botão visualmente, determinará sua função e aplicará um rótulo permanente.
_Ao contrário das ferramentas de rotulagem mais antigas dos leitores de tela, este complemento utiliza um sistema híbrido avançado de "Assinatura de Objeto" (AutomationId/ControlID). Seus rótulos personalizados resistirão ao redimensionamento de janelas, à troca de monitores e às atualizações dos aplicativos!_

### 8.2 Varredura Completa do Aplicativo (Shift + L)

Pressione **Shift + L** para analisar toda a janela ativa de uma só vez. A IA encontrará todos os elementos sem rótulo e os nomeará inteligentemente de uma só vez. Mais tarde, você poderá gerenciar, renomear ou excluir em lote esses rótulos no Gerenciador de Rótulos integrado.

### 8.3 Explorador de Interface (E)

Precisa interagir com um elemento sem navegar até ele manualmente? Pressione **E** para ativar o Explorador de Interface. A IA analisará a tela e gerará uma lista acessível de todos os elementos clicáveis (ignorando ruídos do sistema como as barras de tarefas). Escolha um item da lista e o complemento clicará nele instantaneamente para você.

## 9. Assistente de Voz em Tempo Real

O Assistente em Tempo Real transforma o Vision Assistant Pro em um copiloto interativo em tempo real.
_(Nota: Este recurso é exclusivo do Google Gemini e de provedores Personalizados compatíveis com o Gemini)._

- **Ativação:** Pressione **Control + L** na Camada de Comandos para abrir a caixa de diálogo do Assistente em Tempo Real.
- **Interação em Tempo Real:** Fale naturalmente através do seu microfone. A IA ouvirá sua voz e analisará sua tela ativa simultaneamente. Você pode fazer perguntas como "O que estou vendo?" ou "Leia o terceiro parágrafo para mim."
- **Pressionar para Falar (Push to Talk):** Ative o **Pressionar para Falar** na aba de configurações do Assistente em Tempo Real (ou alterne diretamente dentro da janela do Assistente em Tempo Real), depois segure a tecla atribuída para falar e solte-a para finalizar. Isso mantém o microfone mudo até que você pressione a tecla - perfeito para ambientes barulhentos.
- **Personalização:** Dentro da caixa de diálogo, você pode alterar o Estilo de Voz da IA (ex.: Profissional, Amigável, Animado) e ajustar sua "Profundidade de Raciocínio" para controlar o nível de análise antes de responder.

## 10. Prompts Personalizados e Variáveis

Você pode gerenciar os prompts em **Configurações > Prompts > Gerenciar Prompts...**.

### Atalhos de Prompts Personalizados

Atribua a qualquer prompt personalizado sua própria tecla de atalho diretamente no Gerenciador de Prompts e execute-o instantaneamente com sua seleção ou contexto atual:

- **Tecla única** (ex.: `1`, `p` ou `F3`): Funciona dentro da Camada de Comandos e também globalmente como `NVDA + Shift + tecla`.
- **Combinação de teclas** (ex.: `Control + Shift + 1`, `Alt + P` ou `Insert + 1`): Funciona de forma global e independente.

### Variáveis Suportadas

- `[selection]`: Texto atualmente selecionado.
- `[clipboard]`: Conteúdo da área de transferência.
- `[clipboard_image]`: Imagem atualmente na área de transferência.
- `[screen_obj]`: Captura de tela do objeto de navegação.
- `[screen_fg_obj]`: Captura de tela da janela ativa em primeiro plano.
- `[screen_full]`: Captura da tela inteira.
- `[file_ocr]`: Selecionar arquivo de imagem/PDF para extração de texto.
- `[file_read]`: Selecionar documento para leitura (TXT, Code, PDF).
- `[file_audio]`: Selecionar arquivo de áudio para análise (MP3, WAV, OGG).
- `{target_lang}`: Idioma de destino atual.
- `{source_lang}`: Idioma de origem atual.
- `{response_lang}`: Idioma atual de resposta da IA.
- `{swap_target}`: Idioma alternativo para a tradução com troca inteligente.
- `{swap_instruction}`: Bloco de instruções para tradução com troca inteligente.

## 11. Casos de Uso Reais (Qual recurso devo utilizar?)

O Vision Assistant Pro está repleto de ferramentas avançadas. Aqui estão alguns cenários comuns para ajudar você a escolher a opção certa:

- **Cenário:** Você deseja entender o layout completo de uma janela complexa ou de um aplicativo inacessível.
_Solução:_ Pressione **O** (Visão de Tela Inteira). A IA analisará toda a tela e descreverá exatamente onde os elementos, textos e botões estão posicionados.

- **Cenário:** Você encontrou uma imagem em uma página da web ou um gráfico sem rótulo em um documento.
_Solução:_ Mova seu objeto de navegação para o gráfico e pressione **V** (Visão de Objeto). A IA descreverá especificamente o que aquela imagem contém.

- **Cenário:** Você quer assistir a um filme ou clipe de vídeo com audiodescrição.
  _Solução:_ Pressione **Shift + V** no seu vídeo e escolha **"Gerar Audiodescrição (Arquivo SRT)"**. Quando terminar, clique em **"Gerar Narração Sincronizada (MP3)"** e selecione **"AD Estendida"**. O complemento criará uma faixa de áudio que pausa inteligentemente os diálogos do filme para descrever as cenas visuais.

- **Cenário:** Você encontrou um aplicativo cheio de "botões sem rótulo".
  _Solução:_ Pressione **L** para rotular permanentemente o botão específico usando IA. Ou pressione **Shift + L** para escanear e rotular a janela inteira de uma só vez. Se você apenas quiser clicar em algo rapidamente, pressione **E** (Explorador de Interface) para obter uma lista de todos os itens clicáveis.

- **Cenário:** Você precisa contornar um CAPTCHA inacessível.
  _Solução:_ Pressione **C** (Resolvedor de CAPTCHA). A IA capturará automaticamente o CAPTCHA, o resolverá e inserirá a resposta no campo correto.

- **Cenário:** Você quer ler um documento PDF longo de 50 páginas.
  _Solução:_ Pressione **D** (Leitor de Documentos), defina seu provedor como Google Gemini e insira o intervalo de páginas `1-50`. O complemento extrairá o texto com precisão em segundo plano.

- **Cenário:** Você está assistindo a um tutorial em vídeo silencioso ou a uma animação na sua tela.
  _Solução:_ Pressione **Control + V** para iniciar a gravação da tela. Deixe o tutorial ser reproduzido e, em seguida, pressione **Control + V** novamente. A IA explicará exatamente o que foi demonstrado.

- **Cenário:** Você encontra um erro inesperado, uma falha de conexão de API ou deseja diagnosticar problemas com servidores locais personalizados.
  _Solução:_ Vá em **Configurações > Avançado**, marque **"Ativar arquivo de log dedicado"** e defina o **Nível de Log** como **"Depuração"** (Debug). Execute a ação novamente e clique em **"Abrir arquivo de log"** para inspecionar os detalhes técnicos ou anexar o arquivo `vision_assistant.log` a um chamado de suporte.

***

**Nota:** É necessária uma conexão ativa com a internet para todos os recursos de IA. Documentos de várias páginas são processados automaticamente.

## 12. Suporte e Comunidade

Mantenha-se atualizado com as últimas notícias, recursos e lançamentos:

- **Canal no Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **Issues no GitHub:** Para relatórios de erros e solicitações de recursos.

### Relatando Erros e Logs

Ao abrir um chamado (issue) no GitHub ou solicitar suporte, inclua detalhes sobre seu provedor de IA ativo, modelo e versão do NVDA. Se estiver enfrentando problemas de conexão ou fechamentos inesperados, habilite o arquivo de log dedicado em **Configurações > Avançado**, reproduza o problema e anexe seu arquivo `vision_assistant.log` para nos ajudar a resolver o problema mais rapidamente.

## 13. Apoiadores do Projeto

Um agradecimento do fundo do coração aos membros da nossa comunidade que apoiam o desenvolvimento contínuo e a manutenção deste projeto por meio de suas generosas contribuições financeiras:

- **@Alyabani94**
- **Ali Alamri**
- **Ilya**
- **Apoiador Anônimo** (`UQDd...CnMY`)
- **leonardo0216**
- **Sergei Fleytin**
- **Suman Gayen**

_Se você deseja apoiar o projeto financeiramente e ver seu nome aqui, poderá encontrar a opção **Doar** no menu Ferramentas do NVDA (submenù Vision Assistant) ou durante o processo de configuração após a instalação._

***

## Alterações para 2026.09.01

- **Histórico (Control + H)**: A Camada de Comandos agora inclui uma caixa de diálogo de **Histórico** (`Control + H`) que lista seus bate-papos e documentos anteriores com filtros para Todos, Bate-papos e Documentos. Reabra qualquer bate-papo com sua conversa completa - os arquivos anexados são reanexados automaticamente - ou reabra um documento e continue a leitura. Pressione **Delete** em qualquer item para removê-lo ou limpe tudo de uma só vez.
- **Documentos Recentes no Leitor**: Pressionar **D** na Camada de Comandos agora exibe primeiramente seus documentos lidos recentemente. Escolha um para continuar a partir da página em que parou - mesmo quando o OCR já tiver sido concluído - ou pressione **Abrir Arquivo...** (`Ctrl + O`) para procurar normalmente.
- **Pressionar para Falar no Assistente em Tempo Real**: Tenha controle total de suas conversas ao vivo! Habilite o **Pressionar para Falar (Push to Talk)** na nova aba de configurações do Assistente em Tempo Real e atribua qualquer tecla - ou até mesmo uma tecla modificadora isolada como `Ctrl Esquerdo` - para falar. Mantenha a tecla pressionada para falar e solte-a quando terminar, com um curto sinal sonoro a cada pressionamento e liberação. Uma opção correspondente também aparece diretamente na janela do Assistente em Tempo Real, permitindo alternar entre o modo pressionar para falar e o microfone aberto sem sair da conversa.
- **Áudio Nativo do Gemini 2.5 Flash**: O Assistente em Tempo Real agora suporta o modelo de áudio nativo do Gemini 2.5 Flash (`gemini-2.5-flash-native-audio-preview-12-2025`) para conversas de voz naturais e com baixa latência. Você pode alternar para ele em **Configurações → Roteamento Avançado de Modelos → Modelo do Assistente em Tempo Real (somente Gemini)**, ou manter em "Auto" para permanecer no modelo recomendado.
- **Backup e Restauração de Configurações**: Adicionado um poderoso sistema de backup e restauração na aba **Avançado**! Agora você pode salvar todas as configurações do seu complemento - incluindo chaves de API, modelos, prompts personalizados e preferências - em um único arquivo JSON e restaurá-las perfeitamente a qualquer momento, em qualquer máquina ou após reinstalar o NVDA.
- **Leitura Direta de Texto e HTML**: O Leitor de Documentos agora pode abrir arquivos de texto puro (`.txt`) e HTML (`.html`, `.htm`) diretamente! Ele detecta automaticamente a codificação do arquivo, remove scripts e sujeiras de formatação, e divide o conteúdo de forma inteligente em páginas legíveis - inclusive reimportando seus próprios arquivos exportados mantendo a estrutura das páginas -, para que você possa lê-los instantaneamente sem necessidade de OCR ou processamento por IA!
- **TTS do Gemini Live para o Leitor de Documentos**: O botão "Gerar Áudio" agora suporta o Gemini Live - um motor de síntese de voz via transmissão de alta qualidade e ritmo natural! Quando o Gemini for seu provedor ativo, você pode escolher entre o TTS Padrão e o Gemini Live diretamente no leitor, e sua seleção será lembrada para a próxima vez!
- **Atalhos de Prompts Personalizados**: You can now assign a shortcut key to any of your custom prompts right from the Prompt Manager! Give every prompt its own dedicated key or key combination to run it instantly, automatically capturing your current selection or context with zero extra steps!
- **Navegação pelas Mensagens do Bate-Papo**: Revise qualquer conversa sem usar as mãos! Dentro de qualquer janela de bate-papo (Bate-Papo Direto, bate-papo de documento, refinamento e mais), pressione `Alt + Seta para Baixo` para ouvir a próxima mensagem e `Alt + Seta para Cima` para ouvir a anterior - com prefixos claros de "Você" / "IA" e anúncios de limites de "Primeira mensagem" / "Última mensagem" à medida que navega.
- **Copiar Mensagem do Bate-Papo (Alt + C)**: Ao revisar uma conversa com `Alt + Seta para Cima/Baixo`, pressione `Alt + C` para copiar a mensagem em que você está atualmente para a área de transferência - respeitando sua configuração de Markdown Limpo - com uma confirmação falada.
- **Prompt de Sistema do Bate-Papo Direto**: O Bate-Papo Direto (`Shift+C`) agora tem seu próprio prompt de sistema editável - "Instrução do Bate-Papo Direto" - que define a persona do assistente e o idioma de resposta para cada conversa. Você pode personalizá-lo na aba Prompts Padrão do Gerenciador de Prompts.
- **Navegação de Página pelo Cursor no Leitor de Documentos**: Ler documentos de várias páginas ficou ainda mais fluido! No Visualizador de Documentos, quando seu cursor atinge a última linha de uma página e você pressiona `Seta para Baixo`, o leitor pula automaticamente para a próxima página. Pressionar `Seta para Cima` no início de uma página retorna sem interrupções para a anterior - sem necessidade de alternar páginas manualmente durante a leitura!
- **Novas Alternâncias nas Configurações Rápidas**: Copiar respostas da IA para a área de transferência, Saída Direta (sem janela de bate-papo), Markdown Limpo no Bate-Papo e Troca Inteligente agora podem ser ativados e desativados instantaneamente nas Configurações Rápidas da camada de comandos!
- **Aba de Configurações do Assistente em Tempo Real**: O Assistente em Tempo Real agora possui sua própria aba de configurações dedicada! A opção "Assistente em Tempo Real: Saída Direta (Sem Janela)" foi movida da aba Conexão para cá, e a aba é exibida apenas quando o Google Gemini (ou um provedor Personalizado compatível com Gemini) for o seu provedor ativo.

## Alterações para 2026.08.06

- **Rotulagem no Explorador de Interface**: Agora você pode adicionar rótulos diretamente aos elementos encontrados dentro do Explorador de Interface! Foi adicionado um novo botão "Adicionar Rótulo", e a interface permanece aberta de forma inteligente mantendo o foco para que você possa rotular rapidamente vários objetos sem interrupções.
- **Melhoria na Camada de Configurações Rápidas**: A camada do Vision Assistant (`Insert+Shift+V`) agora é persistente e altamente interativa! Você pode utilizar as setas para `Cima/Baixo` para navegar entre as configurações rápidas (Provedor, Modelo, Idioma de Resposta da IA, Modelo de TTS) e as setas para `Esquerda/Direita` para alterar instantaneamente seus valores com um retorno de voz inteligente e conciso. Suas seleções entram em vigor imediatamente (incluindo a ativação automática do roteamento avançado, quando necessário) e a camada permanece ativa enquanto você configura.
- **Bate-Papo Direto (`Shift+C`)**: Adicionado um novo comando à camada! Pressione `Shift+C` para abrir instantaneamente uma janela de "Bate-Papo Direto". Isso fornece de imediato uma interface de conversa limpa e baseada em texto com a IA, sem necessitar de uma imagem ou documento como ponto de partida.
- **Restauração Perfeita do Histórico do Bate-Papo**: Corrigido um erro grave onde pressionar a tecla `Espaço` para restaurar o último resultado perdia o histórico da conversa subsequente. Agora, o complemento rastreia globalmente sua conversa. Se você conversar, fechar a caixa de diálogo e pressionar `Espaço` para restaurá-la, todo o seu histórico de trocas de mensagens será perfeitamente restaurado! Funciona para Bate-Papo Direto, Análise de Visão, Bate-Papo sobre Documentos e Tradução.
- **Descrições de Imagens no Texto (Inline) no OCR**: Adicionado um recurso opcional para descrever imagens no próprio texto durante o OCR de documentos. Você pode ativar ou desativar esta configuração nas configurações de OCR do complemento, nas opções do Leitor de Documentos antes da extração ou rapidamente na camada de Configurações Rápidas.
- **Tradução por Voz (`Control+T`)**: Adicionado um novo e poderoso recurso! Dite sua fala e ela será traduzida e digitada instantaneamente via IA com base nos seus idiomas de origem e destino configurados.
- **Melhorias no Gerenciador de Download de Atualizações**: A caixa de diálogo de download de atualizações agora exibe corretamente o progresso em porcentagens, e foi corrigido um erro em que uma mensagem fantasma "Baixando atualização" aparecia ao cancelar a instalação.
- **Melhorias no Gerenciador de Download do eSpeak-NG**: Adicionado o acompanhamento do progresso em porcentagem para os downloads do eSpeak-NG.
- **Resiliência no OCR em Lote**: Corrigido um problema no OCR em lote de arquivos PDF onde o processo parava se a chave de API ativa atingisse a cota na metade; agora o sistema alterna automaticamente para a próxima chave disponível e retoma o processo.
- **Suporte a CAPTCHA Visual**: Adicionado suporte robusto para resolução de CAPTCHAs visuais. O sistema tenta resolver automaticamente desafios complexos de imagem, como hCaptcha e reCAPTCHA, melhorando significativamente a acessibilidade em formulários web desafiadores.
- **Reformulação do Transcritor de Áudio**: O módulo Transcritor de Áudio foi completamente reconstruído e agora suporta arquivos de áudio e vídeo. Ele possui 3 modos de operação distintos: "Transcrever (Idioma Original)", "Transcrever e Traduzir (Idioma de Destino)" e uma nova e poderosa opção "Dublar e Traduzir (Idioma de Destino)" (exclusiva do Gemini) que gera uma dublagem de áudio traduzida da fala original.
- **Números de Página Opcionais no Leitor de Documentos**: Adicionada uma nova configuração para alternar a inclusão de números de página e separadores na saída de documentos com várias páginas. Você pode gerenciar facilmente essa opção nas configurações principais ou alterná-la na camada de Configurações Rápidas. Este recurso se aplica tanto à exportação de arquivos de texto/HTML quanto à janela "Ver Formatado", permitindo ler documentos combinados de forma contínua.
- **Gemini Live TTS Ilimitado para Descrições de Vídeo**: Agora você pode selecionar o "Gemini Live TTS" como motor de voz ao gerar Narração de Áudio Sincronizada (MP3) para vídeos. Isso utiliza a API do Gemini Live para sintetizar audiodescrições de alta qualidade sem limites de caracteres ou restrições de duração.
- **Modularização do Código-Fonte**: A estrutura do complemento foi refatorada de um único arquivo para uma arquitetura modular de múltiplos arquivos, melhorando sua manutenibilidade.
- **Redesign da Interface de Configurações**: A caixa de diálogo de Configurações foi completamente redesenhada para usar uma interface moderna baseada em abas em vez de um layout agrupado, proporcionando melhor organização e navegação mais fácil, mantendo todas as opções existentes.
- **Registro de Log Global e em Arquivo Dedicado**: Adicionado um sistema opcional de registro global em arquivo na nova aba de configurações "Avançado". Captura automaticamente eventos operacionais, tráfego de API e erros em todos os módulos do complemento em um arquivo dedicado (`vision_assistant.log`). Suporta níveis configuráveis de detalhamento do log (Depuração, Informação, Aviso, Erro), períodos de retenção automatizados (1 hora a 90 dias) e abertura ou limpeza direta do log a partir das configurações, sem nenhum impacto no desempenho ou interferência nos logs do NVDA.
- **Acompanhamento do Progresso de Envio no Gemini**: Adicionados anúncios de progresso em porcentagem e em tempo real ao enviar arquivos grandes (vídeo, áudio, documentos) para a API do Google Gemini.

## Alterações para 2026.07.15

- **Filtragem Inteligente de Modelos de API**: Reformulação completa do sistema de filtragem de modelos para utilizar uma abordagem de lista negra pura em vez de listas brancas. Adicionadas palavras-chave de filtragem mais fortes (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`) para garantir que o menu suspenso do modelo de bate-papo principal permaneça limpo e preparado para o futuro, mantendo todos os modelos especializados acessíveis na seção de Roteamento Avançado.
- **Pesquisa no Roteamento Avançado**: Todos os menus suspensos do Roteamento Avançado de Modelos (OCR, STT, TTS, Operador, Vídeo, Tempo Real) e o seletor de Variantes do eSpeak agora são totalmente pesquisáveis. Você pode digitar rapidamente para filtrar e encontrar o modelo ou variante desejado.
- **Novos Atalhos na Camada de Comandos**:
  - **Configurações (`Alt + S`)**: Abre instantaneamente a caixa de diálogo de configurações do Vision Assistant Pro.
  - **Relatório de Chaves com Cota Esgotada (`Alt + Q`)**: Informa o número exato de chaves de API do Gemini que excederam sua cota diária, identificando em qual modelo específico esgotaram, e anuncia o horário exato da sua reinicialização.
  - **Auditoria de Roteamento (`Alt + M`)**: Audita e anuncia sua configuração atual do Roteamento Avançado, lendo quais modelos estão ativamente selecionados para tarefas especializadas (ignorando as configurações padrão).
- **Reformulação Completa do Analisador de Vídeo**: O Analisador de Vídeo foi completamente transformado! Anteriormente, ele fornecia apenas uma descrição básica de vídeos online. Agora, é um pacote completo de processamento de vídeo sob medida para usuários cegos:
  - **Gravação de Tela Local (`Control+V`)**: Agora você pode gravar vídeos silenciosos diretamente da sua tela. A IA analisará o segmento gravado e fornecerá uma descrição altamente detalhada da cena, estrutura e ações.
  - **Geração de Audiodescrição (SRT)**: O complemento agora pode gerar roteiros de Audiodescrição altamente detalhados (no formato padrão SRT) para vídeos, com sincronização inteligente de pausas para ancorar as descrições nas pausas naturais da faixa de áudio, e OCR literal para qualquer texto na tela.
  - **Narração de Áudio Sincronizada (Exportação em MP3)**: Além das legendas em texto, o complemento pode sintetizar a Audiodescrição em voz, misturá-la automaticamente com a faixa de áudio original do vídeo, aplicar atenuador de áudio (reduzindo o volume de fundo durante as descrições) e exportar o resultado sincronizado final como um arquivo MP3!
  - **Ação Inteligente de Arquivo de Vídeo**: Se você focar em um arquivo de vídeo local e pressionar o atalho de vídeo, o complemento irá detectá-lo automaticamente e processará o arquivo diretamente.
  - **Rastreamento Avançado de Personagens**: A IA agora realiza uma análise prévia para extração de personagens. Ela constrói um dicionário global de personagens e rastreia cada um com precisão, segmento por segmento, sem confundir identidades.
  - **Configuração da Análise de Vídeo**: Adicionadas novas configurações para controlar o tamanho dos blocos SRT, legendagem de personagens e avisos de responsabilidade.
  - **Roteamento Expandido de Modelos**: Agora você pode selecionar explicitamente modelos de vídeo especializados (`gemini_video_model`, `custom_video_model`) nas configurações de Roteamento Avançado de Modelos.
- **Gerenciamento Inteligente de Cotas de API**: Tratamento aprimorado para erros 429 (Limite Diário Excedido) ao rastrear cotas por modelo. Se uma chave atingir seu limite diário em um modelo, ela entra inteligentemente em quarentena apenas para aquele modelo específico, mantendo a chave disponível para uso com outros modelos.

## Alterações para 7.0.0

- **Retomada de Análises Incompletas**: Adicionado um recurso de retomada tanto para o Leitor de Documentos quanto para as Ações Inteligentes de Arquivos. Se uma análise for interrompida, agora você pode continuar de onde parou em vez de recomeçar do zero.
- **Nova Variável `[screen_fg_obj]`**: Adicionada uma variável de prompt personalizada para capturar uma imagem apenas da janela ativa em primeiro plano, em vez da tela inteira.
- **Tentativas Inteligentes e Rotação de Chaves**: O complemento agora tenta novamente de forma silenciosa até 5 vezes na mesma chave ao encontrar sobrecargas temporárias no servidor (como "alta demanda" ou respostas malformadas). Se as tentativas falharem, ele alterna automaticamente para a próxima chave de API da sua lista.
- **Detecção de Cortina de Tela**: Adicionada uma verificação para evitar tirar capturas de tela quando a Cortina de Tela estiver ativa (seja ativada permanentemente ou alternada temporariamente pelo atalho). O complemento emitirá um aviso e interromperá a ação, evitando o envio de imagens pretas e o desperdício de tokens de API.
- **Ajustes no Leitor de Documentos**: A caixa de diálogo de intervalo de páginas de PDF agora pré-seleciona automaticamente o idioma de destino padrão das configurações do complemento. Também foi aprimorado o gerenciamento de threads para garantir que as tarefas em segundo plano sejam encerradas de forma limpa quando o leitor for fechado.
- **Integração Nativa do OCR da Mistral**: Integrada a API nativa de OCR de Documentos da Mistral. Os documentos de várias páginas são mesclados, enviados e processados em lotes automaticamente utilizando o endpoint especializado `/v1/ocr` da Mistral, enquanto imagens de página única são processadas diretamente, sem conversões desnecessárias para PDF [1].
- **Manipuladores Dinâmicos de URL Personalizada**: A alteração da URL de API personalizada agora limpa instantaneamente a lista de modelos em cache e restaura a caixa de texto para entrada manual do modelo. Isso garante total compatibilidade com endpoints personalizados (como o Cloudflare AI Gateway) que não suportam o endpoint de listagem padrão `/v1/models`.
- **Reformulação do Motor de Entrada do Operador de IA**: Reescrita completa do sistema subjacente de simulação de mouse e teclado para o Operador de IA. Substituída a API legada `mouse_event` pela moderna API `SendInput` do Windows, trazendo uma compatibilidade significativamente superior com aplicativos modernos, janelas protegidas por UAC e telas de alta densidade de pixels (High-DPI).
- **Correção nas Operações de Arrastar e Soltar**: As ações de arrastar e soltar no Operador de IA agora são totalmente estáveis e confiáveis. O novo motor utiliza curvas de atenuação suaves e naturais, posicionamento preciso do cursor, temporização otimizada e uma técnica inteligente de toque para garantir que o Windows e os aplicativos reconheçam e executem corretamente os gestos de arrastar e soltar sem falhar no meio do caminho.
- **Suporte a Múltiplos Monitores**: O Operador de IA agora suporta totalmente configurações de múltiplos monitores. Os movimentos do mouse e cliques funcionam corretamente em todos os monitores através da flag `MOUSEEVENTF_VIRTUALDESK`, garantindo um posicionamento preciso independentemente do monitor em que o aplicativo de destino esteja.
- **Simulação de Teclado Aprimorada**: Aprimorada a injeção de teclas para suportar totalmente as "Teclas Estendidas" (como teclas de Seta, Home, End, Page Up/Down, Insert, Delete e F1-F12). Isso garante que os comandos de navegação e atalhos enviados pelo Operador de IA funcionem sem falhas em todos os aplicativos.
- **Suporte a Imagens HEIC/HEIF**: Adicionado suporte nativo para os formatos de foto do iPhone. Agora você pode selecionar diretamente arquivos `.heic` e `.heif` para descrição por IA, OCR ou Leitura de Documentos sem necessidade de conversão prévia.

## Alterações para 6.5.0

- **Assistente em Tempo Real**: Adicionado um recurso de assistente de tela e voz em tempo real, disponível exclusivamente para o provedor Google Gemini (ou provedores personalizados compatíveis com o Gemini). Inclui personalização interativa de voz e de profundidade de pensamento diretamente na caixa de diálogo, com reconexão automática ao alterar as configurações.
- **Provedor de IA MiniMax**: Integrado o MiniMax como um provedor equivalente com suporte multimodal completo (bate-papo, visão, OCR), TTS personalizado utilizando mais de 300 vozes dinâmicas e remoção automática de blocos de raciocínio (ex.: `<think>...</think>`) das saídas.
- **Tradução no Visualizador de Documentos**: Corrigida uma falha silenciosa de tradução para usuários do NVDA que não usam inglês, garantindo que o código de idioma padrão de 2 letras seja enviado para o Google Tradutor em vez do nome do idioma localizado.
- **Nova Tentativa na Análise de PDF em Lote**: Implementada uma lógica de nova tentativa separada, silenciosa e altamente otimizada para a análise em lote de documentos PDF, evitando envios redundantes e janelas de erro incômodas durante as novas tentativas.
- **Status do Visualizador de Documentos**: Corrigido um erro onde o status geral do complemento (verificado via `I`) permanecia travado em "Processamento em Lote Iniciado" durante análises longas de documentos.
- **Resolução de Falha de Threads**: Corrigida uma falha grave de asserção de threads `IsMain() failed in wxTimerImpl` ao abrir documentos a partir de uma thread em segundo plano, através da transição da fila de retorno da interface gráfica para `wx.CallAfter`.

## Alterações para 6.1.2

- **Pré-Verificação de Rótulos Duplicados**: Corrigido um problema na rotulagem individual onde a verificação de duplicados utilizava chaves de coordenadas antigas, fazendo com que o NVDA fizesse solicitações de IA duplicadas para objetos já rotulados em vez de anunciar o rótulo existente.
- **Bate-Papo de Documentos para Provedores não-Gemini**: Corrigida uma verificação rigorosa da chave de API no Bate-Papo de Documentos (`on_ask`) para garantir que usuários do OpenAI, Groq ou provedores Personalizados locais (como o Ollama) possam conversar com documentos com sucesso sem serem bloqueados.
- **Tradução Rápida de OCR do Chrome**: Restaurada a API de tradução gratuita e sem necessidade de chave para o OCR do Chrome. A tradução do texto extraído agora ignora a IA do Gemini, economizando cotas de API e acelerando o processo de tradução.
- **Filtro Alfanumérico do CAPTCHA**: Corrigida a lógica de filtragem no resolutor de CAPTCHA para garantir que os caracteres não alfanuméricos sejam devidamente limpos em todas as situações.
- **Atualização da Ajuda da Camada de Comandos**: Corrigido o atalho do anúncio de status no menu de ajuda de `L` para `I` e adicionados ambos os comandos de rotulagem (`L` e `Shift+L`) à lista.

## Alterações para 6.1.1

- **Correção do Raciocínio dos Modelos Gemma 4**: Corrigido um problema com os modelos Gemma 4 onde todo o processo de pensamento interno era exibido como resposta final, ou onde desativar o raciocínio resultava em respostas em branco. O complemento agora isola e extrai corretamente apenas a resposta de texto limpa final.
- **OCR em Lote no Explorador de Arquivos**: Agora você pode selecionar várias fotos ou PDFs diretamente no Explorador de Arquivos do Windows e extrair texto ou analisá-los em lote. O complemento filtrará e processará automaticamente apenas os formatos de arquivo suportados.

## Alterações para 6.1.0

- **Integração Universal de IA Local (Configurar IA Local)**: Adicionado um novo botão **"Configurar IA Local"** nas Configurações do Provedor Personalizado. Os usuários agora podem configurar automaticamente motores de IA locais, incluindo **Ollama**, **LM Studio**, **Jan.ai** e **KoboldCPP** de forma instantânea.
- **Bypass Inteligente de Proxy Local**: Reconstruída a lógica de conexão com um mecanismo avançado de bypass de proxy. O complemento agora é inteligente o suficiente para ignorar completamente os proxies do sistema Windows para conexões de loopback locais, garantindo conexões estáveis com a IA local mesmo quando sua VPN ou modo TUN estiver ativo.
- **Rotulagem por IA Ultraestável (v2)**: Substituição das chaves de coordenadas absolutas de tela por um sistema híbrido e avançado de **Assinatura de Objeto**. Os rótulos dependem agora de identificadores programáticos (UIA **AutomationId** ou Win32 **ControlID**) e de coordenadas relativas à janela, tornando seus rótulos personalizados completamente resistentes ao redimensionamento de janelas, à movimentação, à alteração de monitor ou de escala.
- **Migração Automática e Transparente de Rótulos**: A atualização é totalmente transparente. O complemento migrará automaticamente seus rótulos antigos baseados em coordenadas para o novo formato estável de impressão digital em segundo plano assim que você focar o objeto pela primeira vez, com zero perda de dados.

## Alterações para 6.0

- **Apresentando a Rotulagem Semântica por IA**: Os usuários agora podem rotular permanentemente botões e ícones sem nome utilizando a IA. Pressione **L** para rotular o objeto de navegação atual (suportando tanto o foco do Tab quanto a navegação por objetos) ou **Shift+L** para analisar e rotular todo o aplicativo de uma só vez.
- **Gerenciamento Inteligente de Rótulos**: Adicionada uma nova caixa de diálogo do Gerenciador de Rótulos totalmente acessível (através de **Shift+L** se existirem rótulos) para ver, renomear ou excluir rótulos personalizados em lote.
- **Análise Direta de Arquivos (Bypass da Caixa de Diálogo de Arquivos)**: O complemento agora é inteligente o suficiente para detectar se você está focado em um arquivo PDF ou de imagem no Explorador de Arquivos do Windows. Pressionar **F (Ação Inteligente de Arquivo)** ou **D (Leitor de Documentos)** em um arquivo selecionado irá processá-lo imediatamente, ignorando completamente a caixa de diálogo padrão "Abrir".

## Alterações para 5.6

- **Adicionado Motor OCR "Nenhum (Extrair Camada de Texto)"**: Os usuários podem agora extrair texto diretamente de PDFs pesquisáveis sem utilizar créditos de IA, melhorando significativamente a velocidade e a privacidade para documentos baseados em texto.
- **Precisão Refinada do Explorador de UI**: Aprimorado o prompt do Explorador de UI para identificar melhor os tipos de elementos (como Itens de Lista) e relatar com precisão estados como "(Marcado)", "(Selecionado)" ou "(Expandido)", ignorando os componentes do sistema Windows como a Barra de Tarefas e o Relógio.
- **Lembrete de Configuração de Instalação**: Adicionada uma notificação após a instalação para guiar os usuários ao menu de configurações para configurarem suas chaves de API e preferências.

## Alterações para 5.5.2

- **Correção na Digitação do Operador de IA:** Corrigido um erro onde a letra 'v' era digitada em vez de colar o texto em determinados sistemas. Esta correção resolve conflitos de temporização que ocorriam durante uma carga elevada do sistema.
- **Estabilidade Aprimorada:** Adicionado um tratamento de erros robusto para operações na área de transferência para evitar falhas do complemento quando a área de transferência do sistema estiver temporariamente bloqueada por outros aplicativos.
- **Otimização de Temporização:** Ajustados os atrasos internos para eventos de teclado de modo a garantir maior confiabilidade em diferentes velocidades do sistema e melhor compatibilidade com Gerenciadores da Área de Transferência de terceiros.

## Alterações para 5.5 (A Atualização de Automação)

- **Operador de IA (Controle Autônomo - Shift+A):** Esta é a joia da coroa da v5.5. O Vision Assistant Pro deixou de ser um assistente passivo para se tornar seu **Operador de IA** pessoal. Ele não se limita a descrever a tela - ele assume o comando.
  - _Como funciona:_ Você agora pode dar instruções por texto ou voz para operar seu PC. Por exemplo, em um aplicativo completamente inacessível onde seu leitor de tela permanece em silêncio, você pode pressionar **Shift+A** e digitar: _"Clique no botão Configurações"_ ou _"Encontre o campo de pesquisa, digite 'Últimas Notícias' e pressione Enter."_ A IA identifica visualmente os elementos, move o mouse e executa a tarefa por você.
  - _Nota de Desempenho:_ Este recurso está otimizado para o **Gemini 3.0 Flash (Preview)**, oferecendo respostas incrivelmente rápidas e inteligentes que conseguem lidar até com os layouts de interface de usuário mais complexos.
  - **⚠️ Aviso de Uso da API:** Como o Operador de IA precisa "ver" exatamente o que está acontecendo para ser preciso, ele envia uma captura de tela de alta resolução a cada passo. Observe que o uso frequente consumirá sua cota de API muito mais rapidamente do que as tarefas normais de texto.
- **Explorador Visual de UI (E):** Cansado de navegar por "botões sem rótulo"? Pressione **E** para ativar o Explorador de UI. A IA analisará toda a janela e gerará uma lista de cada elemento clicável que encontrar - incluindo ícones, gráficos e menus. Basta escolher um item da lista e o Operador de IA clicará nele para você. É como ter uma "camada acessível" sobre qualquer aplicativo.
- **Ação Inteligente de Arquivo com Sensibilidade ao Contexto (F):** A tecla "F" foi completamente reformulada. Ela não assume mais que você quer apenas OCR. Ao selecionar uma única imagem, agora pergunta inteligentemente qual é a sua intenção: você pode escolher uma **Descrição Visual Detalhada** para entender a cena ou uma **Extração de Texto Estruturada (OCR)** para leitura. O menu adapta-se dinamicamente com base no tipo de arquivo e no seu motor de IA ativo.
- **Otimização Principal:** Realizamos uma limpeza profunda da lógica interna do complemento, removendo funções legadas não utilizadas e código redundante. Isso resulta em uma experiência mais leve, rápida e confiável para todos os usuários.

## Alterações para 5.0

- **Arquitetura Multiprovedor**: Adicionado suporte total para **OpenAI**, **Groq** e **Mistral**, em conjunto com o Google Gemini. Os usuários agora podem escolher sua plataforma de IA preferida.
- **Roteamento Avançado de Modelos**: Os usuários de provedores nativos (Gemini, OpenAI, etc.) podem agora selecionar modelos específicos em um menu suspenso para diferentes tarefas (OCR, STT, TTS).
- **Configuração Avançada de Endpoints**: Os usuários de provedores personalizados podem inserir manualmente URLs específicas e nomes de modelos para um controle detalhado sobre servidores locais ou de terceiros.
- **Visibilidade Inteligente de Recursos**: O menu de configurações e a interface do Leitor de Documentos agora ocultam automaticamente os recursos não suportados (como o TTS) com base no provedor selecionado.
- **Busca Dinâmica de Modelos**: O complemento obtém agora a lista de modelos disponíveis diretamente da API do provedor, garantindo compatibilidade com novos modelos assim que são lançados.
- **OCR e Tradução Híbridos**: Otimizada a lógica para utilizar o Google Tradutor para maior velocidade ao usar o OCR do Chrome, e tradução baseada em IA ao utilizar os motores Gemini/Groq/OpenAI.
- **"Analisar Novamente com IA" Universal**: O recurso de reanalisar do Leitor de Documentos não está mais limitado ao Gemini. Ele agora utiliza qualquer provedor de IA que estiver ativo no momento para reprocessar as páginas.

## Alterações para 4.6

- **Recuperação Interativa de Resultados:** Adicionada a tecla **Espaço** à camada de comandos, permitindo aos usuários reabrir instantaneamente a última resposta da IA em uma janela de bate-papo para perguntas adicionais, mesmo quando o modo "Saída Direta" estiver ativo.
- **Central da Comunidade no Telegram:** Adicionado um link para o "Canal Oficial no Telegram" no menu Ferramentas do NVDA, proporcionando uma forma rápida de se manter atualizado com as últimas notícias, recursos e lançamentos.
- **Estabilidade de Resposta Aprimorada:** Otimizada a lógica principal para os recursos de Tradução, OCR e Visão para garantir um desempenho mais confiável e uma experiência mais fluida ao utilizar a saída direta de voz.
- **Orientação de Interface Aprimorada:** Atualizadas as descrições das configurações e a documentação para explicar melhor o novo sistema de recuperação de histórico e como ele funciona junto com as configurações de saída direta.

## Alterações para 4.5

- **Gerenciador Avançado de Prompts:** Introduzida uma caixa de diálogo de gerenciamento dedicada nas configurações para personalizar os prompts padrão do sistema e gerenciar prompts definidos pelo usuário, com suporte total para adicionar, editar, reordenar e pré-visualizar.
- **Suporte Abrangente a Proxy:** Resolvidos problemas de conexão de rede garantindo que as configurações de proxy definidas pelo usuário sejam rigorosamente aplicadas a todas as requisições de API, incluindo tradução, OCR e geração de voz.
- **Migração Automática de Dados:** Integrado um sistema de migração inteligente para atualizar automaticamente configurações de prompts antigas para um formato JSON v2 robusto na primeira execução, sem perda de dados.
- **Compatibilidade Atualizada (2025.1):** Definida a versão mínima do NVDA necessária para 2025.1 devido a dependências de bibliotecas em recursos avançados como o Leitor de Documentos, garantindo um desempenho estável.
- **Interface de Configurações Otimizada:** Simplificada a interface de configurações ao reorganizar o gerenciamento de prompts em uma caixa de diálogo separada, proporcionando uma experiência de uso mais limpa e acessível.
- **Guia de Variáveis de Prompt:** Adicionado um guia integrado nas caixas de diálogo de prompt para ajudar os usuários a identificar e utilizar facilmente variáveis dinâmicas como [selection], [clipboard] e [screen_obj].

## Alterações para 4.0.3

- **Resiliência de Rede Aprimorada:** Adicionado um mecanismo de nova tentativa automática para lidar melhor com conexões de internet instáveis e erros temporários do servidor, garantindo respostas de IA mais confiáveis.
- **Janela de Tradução Visual:** Introduzida uma janela dedicada para os resultados de tradução. Os usuários podem agora navegar facilmente e ler traduções longas linha por linha, de forma semelhante aos resultados de OCR.
- **Visualização Formatada Agregada:** O recurso "Ver Formatado" no Leitor de Documentos exibe agora todas as páginas processadas em uma única janela organizada, com cabeçalhos de página claros.
- **Fluxo de Trabalho de OCR Otimizado:** Ignora automaticamente a seleção de intervalo de páginas para documentos de página única, tornando o processo de reconhecimento mais rápido e fluido.
- **Estabilidade da API Aprimorada:** Alterado para um método de autenticação baseado em cabeçalho mais robusto, resolvendo potenciais erros de "Todas as chaves de API falharam" causados por conflitos na rotação de chaves.
- **Correções de Erros:** Resolvidas várias falhas potenciais, incluindo um problema durante o encerramento do complemento e um erro de foco na caixa de diálogo de bate-papo.

## Alterações para 4.0.1

- **Leitor Avançado de Documentos:** Um novo e potente visualizador de PDF e imagens com seleção de intervalo de páginas, processamento em segundo plano e navegação fluida com `Ctrl+PageUp/PageDown`.
- **Novo Submenu de Ferramentas:** Adicionado um submenu dedicado "Vision Assistant" no menu Ferramentas do NVDA para um acesso mais rápido aos recursos principais, configurações e documentação.
- **Personalização Flexível:** Você pode agora escolher seu motor de OCR e voz TTS preferidos diretamente no painel de configurações.
- **Suporte a Múltiplas Chaves de API:** Adicionado suporte para várias chaves de API do Gemini. Você pode inserir uma chave por linha ou separá-las por vírgulas nas configurações.
- **Motor OCR Alternativo:** Introduzido um novo motor de OCR para garantir um reconhecimento de texto confiável mesmo ao atingir os limites de cota da API do Gemini.
- **Rotação Inteligente de Chaves de API:** Alterna automaticamente para a chave de API funcional mais rápida e memoriza-a para ultrapassar os limites de cota.
- **Documento para MP3/WAV:** Recurso integrado para gerar e salvar arquivos de áudio de alta qualidade nos formatos MP3 (128kbps) e WAV diretamente no leitor.
- **Suporte a Stories do Instagram:** Adicionada a capacidade de descrever e analisar Stories do Instagram utilizando suas URLs.
- **Suporte ao TikTok:** Introduzido suporte para vídeos do TikTok, permitindo uma descrição visual completa e transcrição de áudio dos vídeos.
- **Janela de Atualização Redesenhada:** Apresenta uma nova interface acessível com uma caixa de texto rolável para ler claramente as alterações de versão antes de instalar.
- **Status e UX Unificados:** Caixas de diálogo de arquivo padronizadas em todo o complemento e aprimoramento do comando 'L' para relatar o progresso em tempo real.

## Alterações para 3.6.0

- **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) na Camada de Comandos para fornecer uma lista de fácil acesso com todos os atalhos e suas respectivas funções.
- **Análise de Vídeos Online:** Expandido o suporte para incluir vídeos do **Twitter (X)**. Também foram melhoradas a detecção de URLs e a estabilidade para uma experiência mais confiável.
- **Contribuição para o Projeto:** Adicionada uma caixa de diálogo opcional de doação para usuários que desejem apoiar as futuras atualizações e o crescimento contínuo do projeto.

## Alterações para 3.5.0

\*   \*\*Camada de Comandos:\*\* Introduzido um sistema de Camada de Comandos (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla principal. Por exemplo, em vez de pressionar `NVDA+Control+Shift+T` para traduzir, você agora pressiona `NVDA+Shift+V` seguido de `T`.
\*   \*\*Análise de Vídeos Online:\*\* Adicionado um novo recurso para analisar vídeos do YouTube e Instagram diretamente fornecendo uma URL.

## Alterações para 3.1.0

- **Modo de Saída Direta:** Adicionada uma opção para ignorar a caixa de diálogo de bate-papo e ouvir as respostas da IA diretamente por voz, proporcionando uma experiência mais rápida e fluida.
- **Integração com a Área de Transferência:** Adicionada uma nova configuração para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações para 3.0

- **Novos Idiomas:** Adicionadas traduções para **Persa** e **Vietnamita**.
- **Modelos de IA Expandidos:** Reorganizada a lista de seleção de modelos com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`) para ajudar os usuários a distinguir entre modelos gratuitos e modelos com limite de taxa (pagos). Adicionado suporte para o **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
- **Estabilidade do Ditado:** Melhoria significativa na estabilidade do Ditado Inteligente. Adicionada uma verificação de segurança para ignorar clipes de áudio com menos de 1 segundo, evitando alucinações da IA e erros de resposta em branco.
- **Gerenciamento de Arquivos:** Corrigido um problema em que o envio de arquivos com nomes em caracteres não-ingleses falhava.
- **Otimização de Prompts:** Melhorada a lógica de Tradução e a estrutura dos resultados de Visão.

## Alterações para 2.9

- **Adicionadas traduções para Francês e Turco.**
- **Visualização Formatada:** Adicionado o botão "Ver Formatado" nas caixas de diálogo de bate-papo para visualizar a conversa com a devida formatação (Cabeçalhos, Negrito, Código) em uma janela navegável padrão.
- **Configuração de Markdown:** Adicionada a nova opção "Limpar Markdown no Bate-Papo" nas Configurações. Desmarcar esta opção permite aos usuários verem a sintaxe Markdown pura (ex.: `**`, `#`) na janela de bate-papo.
- **Gerenciamento de Janelas:** Corrigido um problema em que as janelas de "Refinar Texto" ou de bate-papo abriam múltiplas vezes ou falhavam ao colocar o foco corretamente.
- **Melhorias na Experiência do Usuário:** Padronizados os títulos das caixas de diálogo de arquivos para "Abrir" e removidos anúncios de voz redundantes (ex.: "Abrindo menu...") para uma navegação mais fluida.

## Alterações para 2.8

- Adicionada tradução para Italiano.
- **Relatório de Status:** Adicionado um novo comando (NVDA+Control+Shift+I) para anunciar o status atual do complemento (ex.: "Enviando...", "Analisando...").
- **Exportação em HTML:** O botão "Salvar Conteúdo" nas caixas de diálogo de resultados salva agora a saída como um arquivo HTML formatado, preservando estilos como cabeçalhos e texto em negrito.
- **Interface de Configurações:** Melhorada a disposição do painel de Configurações com agrupamentos acessíveis.
- **Novos Modelos:** Adicionado suporte para gemini-flash-latest e gemini-flash-lite-latest.
- **Idiomas:** Adicionado o Nepalês à lista de idiomas suportados.
- **Lógica do Menu de Refinamento:** Corrigido um erro crítico em que os comandos de "Refinar Texto" falhavam se o idioma da interface do NVDA não fosse o Inglês.
- **Ditado:** Melhorada a detecção de silêncio para evitar a geração de texto incorreto quando não há entrada de voz.
- **Configurações de Atualização:** A opção "Procurar atualizações ao iniciar" está agora desativada por padrão para cumprir as políticas da Loja de Complementos do NVDA.
- Limpeza de Código.

## Alterações para 2.7

- Migrada a estrutura do projeto para o modelo oficial de complementos da NV Access para melhor conformidade com os padrões.
- Implementada lógica de nova tentativa automática para erros HTTP 429 (Limite de Taxa Excedido) para garantir a confiabilidade durante períodos de tráfego elevado.
- Otimizadas as prompts de tradução para maior precisão e melhor gerenciamento da lógica de "Troca Inteligente".
- Atualizada a tradução para Russo.

## Alterações para 2.6

- Adicionado suporte à tradução em Russo (Agradecimentos a nvda-ru).
- Atualizadas as mensagens de erro para fornecer informações mais descritivas relativamente à conectividade.
- Alterado o idioma de destino padrão para Inglês.

## Alterações para 2.5

- Adicionado o Comando de OCR de Arquivo Nativo (NVDA+Control+Shift+F).
- Adicionado o botão "Salvar Bate-Papo" às caixas de diálogo de resultados.
- Implementado suporte completo de internacionalização (i18n).
- Migrado o retorno sonoro para o módulo nativo de tons do NVDA.
- Alterado para a API de Arquivos do Gemini para um melhor manuseio de arquivos PDF e de áudio.
- Corrigida uma falha no sistema ao traduzir texto que contivesse chaves.

## Alterações para 2.1.1

- Corrigido um problema em que a variável [file_ocr] não funcionava corretamente dentro das Prompts Personalizadas.

## Alterações para 2.1

- Padronizados todos os atalhos para utilizar NVDA+Control+Shift de modo a eliminar conflitos com o layout para Notebook do NVDA e teclas de atalho do sistema.

## Alterações para 2.0

- Implementado um sistema integrado de Atualização Automática.
- Adicionada a Cache de Tradução Inteligente para recuperação instantânea de texto traduzido anteriormente.
- Adicionada Memória de Conversa para refinar contextualmente os resultados nas caixas de diálogo de bate-papo.
- Adicionado comando dedicado para Tradução da Área de Transferência (NVDA+Control+Shift+Y).
- Otimizadas as prompts da IA para impor rigorosamente a saída no idioma de destino.
- Corrigida uma falha causada por caracteres especiais no texto de entrada.

## Alterações para 1.5

- Adicionado suporte para mais de 20 novos idiomas.
- Implementada a Caixa de Diálogo Interativa de Refinamento para perguntas adicionais.
- Adicionado o recurso nativo de Ditado Inteligente.
- Adicionada a categoria "Vision Assistant" à caixa de diálogo de Gestos de Entrada do NVDA.
- Corrigidas falhas por COMError em aplicativos específicos como o Firefox e o Word.
- Adicionado mecanismo de nova tentativa automática para erros do servidor.

## Alterações para 1.0

- Lançamento inicial.
