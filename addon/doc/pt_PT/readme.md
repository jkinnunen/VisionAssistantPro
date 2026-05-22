# Documentação do Vision Assistant Pro

**Vision Assistant Pro** é um assistente de IA multimodal avançado para o NVDA. Potencia mecanismos de IA de classe mundial para fornecer leitura de ecrã inteligente, tradução, ditado por voz e análise de documentos.

_Este suplemento foi lançado para a comunidade em homenagem ao Dia Internacional das Pessoas com Deficiência._

## 1. Configuração

Aceda a **Menu do NVDA > Preferências > Definições > Vision Assistant Pro**.

### 1.1 Definições de Conexão

- **Provedor:** Selecione o seu serviço de IA de preferência. Os provedores suportados incluem o **Google Gemini**, **OpenAI**, **Mistral**, **Groq** e **Personalizado** (servidores compatíveis com OpenAI, como Ollama/LM Studio).
- **Nota Importante:** Recomendamos vivamente a utilização do **Google Gemini** para obter o melhor desempenho e precisão (especialmente para análise de imagens/ficheiros).
- **Chave de API:** Obrigatório. Pode introduzir várias chaves (separadas por vírgulas ou quebras de linha) para rotação automática.
- **Procurar Modelos:** Após introduzir a sua chave de API, prima este botão para descarregar a lista mais recente de modelos disponíveis do provedor.
- **Modelo de IA:** Selecione o modelo principal utilizado para chat geral e análise.

### 1.2 Encaminhamento Avançado de Modelos

_Disponível para todos os provedores, incluindo Gemini, OpenAI, Groq, Mistral e Personalizado._

> **⚠️ Aviso:** Estas definições destinam-se **apenas a utilizadores avançados**. Se não tiver a certeza do que um modelo específico faz, por favor, deixe esta opção **desmarcada**. Selecionar um modelo incompatível para uma tarefa (por exemplo, um modelo apenas de texto para Visão) causará erros e fará com que o suplemento deixe de funcionar.

Marque **"Encaminhamento Avançado de Modelos (Específico por tarefa)"** para desbloquear o controlo detalhado. Isto permite-lhe selecionar modelos específicos da lista pendente para diferentes tarefas:

- **Modelo de OCR / Visão:** Escolha um modelo especializado para analisar imagens.
- **Fala para Texto (STT):** Escolha um modelo específico para ditado.
- **Texto para Fala (TTS):** Escolha um modelo para gerar áudio.
- **Modelo do Operador de IA:** Selecione um modelo específico para tarefas de operação autónoma do computador.
  _Nota: Recursos não suportados (por exemplo, TTS para o Groq) serão ocultados automaticamente._

### 1.3 Configuração Avançada de Endpoint (Provedor Personalizado)

_Disponível apenas quando "Personalizado" estiver selecionado._

> **⚠️ Aviso:** Esta secção permite a configuração manual da API e foi concebida para **utilizadores experientes** que executam servidores locais ou proxies. URLs ou nomes de modelos incorretos quebrarão a conectividade. Se não sabe exatamente o que são estes endpoints, mantenha esta opção **desmarcada**.

Marque **"Configuração Avançada de Endpoint"** para introduzir manualmente os detalhes do servidor. Ao contrário dos provedores nativos, aqui deve **escrever** as URLs e os nomes dos modelos específicos:

- **URL da Lista de Modelos:** O endpoint para procurar os modelos disponíveis.
- **URL do Endpoint de OCR/STT/TTS:** URLs completas para serviços específicos (por exemplo, `http://localhost:11434/v1/audio/speech`).
- **Modelos Personalizados:** Escreva manualmente o nome do modelo (por exemplo, `llama3:8b`) para cada tarefa.

### 1.4 Preferências Gerais

- **Mecanismo de OCR:** Escolha entre **Chrome (Rápido)** para resultados rápidos ou **IA (Avançado)** para uma preservação superior do layout.
  - _Nota:_ Se selecionar "IA (Avançado)", mas o seu provedor estiver configurado como OpenAI/Groq, o suplemento encaminhará inteligentemente a imagem para o modelo de visão do seu provedor ativo.
- **Voz do TTS:** Selecione o seu estilo de voz preferido. Esta lista é atualizada dinamicamente com base no seu provedor ativo.
- **Criatividade (Temperatura):** Controla a aleatoriedade da IA. Valores mais baixos são melhores para traduções/OCR precisos.
- **URL do Proxy:** Configure isto se os serviços de IA estiverem restritos na sua região (suporta proxies locais como `127.0.0.1` ou URLs de ponte).

## 2. Camada de Comando e Atalhos

Para evitar conflitos de teclado, este suplemento utiliza uma **Camada de Comando**.

1. Prima **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (ouvirá um sinal sonoro).
2. Solte as teclas e, em seguida, prima uma das seguintes teclas individuais:

| Tecla         | Função                        | Descrição                                                                           |
| ------------- | ----------------------------- | ----------------------------------------------------------------------------------- |
| **Shift + A** | **Operador de IA**            | **Operação Autónoma:** Diga à IA para realizar uma tarefa no seu ecrã.              |
| **E**         | **Explorador de UI**          | **Clique Interativo:** Identifica e clica em elementos de UI em qualquer app.       |
| **T**         | Tradutor Inteligente          | Traduz o texto sob o cursor de navegação ou seleção.                                |
| **Shift + T** | Tradutor de Transferências    | Traduz o conteúdo que está atualmente na área de transferência.                     |
| **R**         | Refinador de Texto            | Resume, corrige gramática, explica ou executa **Prompts Personalizados**.           |
| **V**         | Visão de Objeto               | Descreve o objeto atual do navegador de objetos.                                    |
| **O**         | Visão de Ecrã Inteiro         | Analisa o layout e o conteúdo de todo o ecrã.                                       |
| **Shift + V** | Análise de Vídeo Online       | Analisa vídeos do **YouTube**, **Instagram**, **TikTok** ou **Twitter (X)**.        |
| **D**         | Leitor de Documentos          | Leitor avançado para PDF e imagens com seleção de intervalo de páginas.             |
| **F**         | **Ação Inteligente de Fich.** | Reconhecimento contextual de ficheiros de imagem, PDF ou TIFF selecionados.         |
| **A**         | Transcrição de Áudio          | Transcreve ficheiros MP3, WAV ou OGG em texto.                                      |
| **C**         | Solucionador de CAPTCHA       | Captura e resolve CAPTCHAs (Suporta portais governamentais).                        |
| **S**         | Ditado Inteligente            | Converte fala em texto. Prima para iniciar e novamente para parar/escrever.         |
| **I**         | Relatório de Status           | Anuncia o progresso atual (por exemplo, "A analisar...", "Inativo").                |
| **L**         | **Etiquetar Objeto**          | **Etiquetagem Semântica por IA:** Etiqueta permanentemente o ícone/elemento focado. |
| **Shift + L** | **Gerir/Analisar Etiquetas**  | Abre o Gestor de Etiquetas ou analisa a app por elementos sem nome.                 |
| **U**         | Verificar Atualizações        | Verifica manualmente no GitHub a versão mais recente do suplemento.                 |
| **Espaço**    | Relembrar Último Resultado    | Mostra a última resposta da IA num diálogo de chat para revisão.                    |
| **H**         | Ajuda de Comandos             | Exibe uma lista com todos os atalhos disponíveis.                                   |

### 2.1 Atalhos do Leitor de Documentos (Dentro do Visualizador)

- **Ctrl + PageDown:** Move para a página seguinte.
- **Ctrl + PageUp:** Move para a página anterior.
- **Alt + A:** Abre um diálogo de chat para fazer perguntas sobre o documento.
- **Alt + R:** Força uma **Nova análise com IA** utilizando o seu provedor ativo.
- **Alt + G:** Gera e guarda um ficheiro de áudio de alta qualidade (WAV/MP3). _Oculto se o provedor não suportar TTS._
- **Alt + S / Ctrl + S:** Guarda o texto extraído como um ficheiro TXT ou HTML.

## 3. Prompts Personalizados e Variáveis

Pode gerir os prompts em **Definições > Prompts > Gerir Prompts...**.

### Variáveis Suportadas

- `[selection]`: Texto atualmente selecionado.
- `[clipboard]`: Conteúdo da área de transferência.
- `[screen_obj]`: Captura de ecrã do objeto do navegador.
- `[screen_full]`: Captura de ecrã inteiro.
- `[file_ocr]`: Seleciona ficheiro de imagem/PDF para extração de texto.
- `[file_read]`: Seleciona documento para leitura (TXT, Código, PDF).
- `[file_audio]`: Seleciona ficheiro de áudio para análise (MP3, WAV, OGG).

---

**Nota:** É necessária uma ligação ativa à internet para todos os recursos de IA. Documentos com várias páginas são processados automaticamente.

## 4. Suporte e Comunidade

Mantenha-se atualizado com as últimas notícias, recursos e lançamentos:

- **Canal do Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **GitHub Issues:** For para relatórios de bugs e pedidos de novos recursos.

## 5. Apoiantes do Projeto

Um agradecimento sincero aos membros da nossa comunidade que apoiam o desenvolvimento contínuo e a manutenção deste projeto através das suas generosas contribuições financeiras:

- **@Alyabani94**
- **Ali Alamri**

_Se deseja apoiar o projeto financeiramente e ver o seu nome aqui, pode encontrar a opção **Doar** no menu Ferramentas do NVDA (submenu Vision Assistant) ou durante o processo de configuração após a instalação._

---

## Alterações para a versão 6.0

- **Introdução à Etiquetagem Semântica por IA**: Os utilizadores agora podem etiquetar permanentemente botões e ícones sem nome utilizando IA. Prima **L** para etiquetar o objeto atual do navegador (suportando tanto o foco do Tab como a navegação de objetos) ou **Shift+L** para analisar e etiquetar a aplicação inteira de uma só vez.
- **Gestão Inteligente de Etiquetas**: Adicionado um novo diálogo do Gestor de Etiquetas totalmente acessível (via **Shift+L** se as etiquetas existirem) para visualizar, renomear ou eliminar etiquetas personalizadas em lote.
- **Análise Direta de Ficheiros (Ignorar Diálogo de Ficheiro)**: O suplemento agora é inteligente o suficiente para detetar se está atualmente focado num ficheiro PDF ou de imagem no Explorador de Ficheiros do Windows. Premir **F (Ação Inteligente de Fich.)** ou **D (Leitor de Documentos)** num ficheiro destacado irá processá-lo imediatamente, ignorando completamente o diálogo padrão "Abrir".

## Alterações para a versão 5.6

- **Adicionado Mecanismo de OCR "Nenhum (Extrair Camada de Texto)"**: Os utilizadores agora podem extrair texto diretamente de PDFs pesquisáveis sem gastar créditos de IA, melhorando significativamente a velocidade e a privacidade para documentos baseados em texto.
- **Precisão Refinada do Explorador de UI**: Melhorado o prompt do Explorador de UI para identificar melhor os tipos de elementos (como Itens de Lista) e relatar com precisão estados como "(Marcado)", "(Selecionado)" ou "(Expandido)", enquanto ignora componentes do sistema Windows, como a Barra de Tarefas e o Relógio.
- **Lembrete de Configuração de Instalação**: Adicionada uma notificação após a instalação para guiar os utilizadores ao menu de definições para configurar as suas chaves de API e preferências.

## Alterações para a versão 5.5.2

- **Correção do Problema de Digitação do Operador de IA:** Resolvido um bug onde a letra 'v' era digitada em vez de colar o texto em determinados sistemas. Esta correção aborda conflitos de tempo que ocorriam durante uma alta carga do sistema.
- **Estabilidade Aprimorada:** Adicionado tratamento robusto de erros para operações de área de transferência para evitar bloqueios do suplemento quando a área de transferência do sistema estiver temporariamente bloqueada por outras aplicações.
- **Otimização de Tempo:** Ajustados os atrasos internos para eventos de teclado para garantir maior fiabilidade em diferentes velocidades de sistema e melhor compatibilidade com Gerenciadores de Área de Transferência de terceiros.

## Alterações para a versão 5.5 (A Atualização de Automação)

- **Operador de IA (Controlo Autónomo - Shift+A):** Esta é a joia da coroa da v5.5. O Vision Assistant Pro deixou de ser um assistente passivo para se tornar o seu **Operador de IA** pessoal. Ele não se limita a descrever o ecrã — ele assume o comando.
  - _Como funciona:_ Agora pode dar instruções verbais para operar o seu PC. Por exemplo, numa aplicação completamente inacessível onde o seu leitor de ecrã permanece em silêncio, pode premir **Shift+A** e escrever: _"Clique no botão Definições"_ ou _"Encontre o campo de pesquisa, escreva 'Últimas Notícias' e prima enter."_ A IA identifica visualmente os elementos, move o rato e executa a tarefa por si.
  - _Nota de Desempenho:_ Este recurso é otimizado para o **Gemini 3.0 Flash (Preview)**, entregando respostas incrivelmente rápidas e inteligentes que podem lidar até mesmo com os layouts de UI mais complexos.
  - **⚠️ Aviso de Utilização da API:** Como o Operador de IA precisa de "ver" exatamente o que está a acontecer para ser preciso, ele envia uma captura de ecrã de alta resolução a cada passo. Por favor, note que o uso frequente consumirá a sua cota de API muito mais rápido do que as tarefas padrão baseadas em texto.
- **Explorador Visual de UI (E):** Cansado de navegar por "botões sem etiqueta"? Prima **E** para ativar o Explorador de UI. A IA analisará a janela inteira e gerará uma lista de cada elemento clicável que ela vê — incluindo ícones, gráficos e menus. Basta escolher um item da lista e o Operador de IA clicará nele por si. É como ter uma "camada acessível" no topo de qualquer app.
- **Ação Inteligente de Fich. Sensível ao Contexto (F):** A tecla "F" foi completamente reformulada. Ela já não assume que quer apenas OCR. Quando seleciona uma única imagem, ela agora pergunta inteligentemente qual é a sua intenção: pode escolher uma **Descrição Visual Detalhada** para entender a cena ou uma **Extração de Texto Estruturada (OCR)** para leitura. O menu adapta-se dinamicamente com base no tipo de ficheiro e no seu mecanismo de IA ativo.
- **Otimização do Núcleo:** Realizámos uma limpeza profunda na lógica interna do suplemento, removendo funções legadas não utilizadas e código redundante. Isto resulta numa experiência mais leve, rápida e confiável para todos os utilizadores.

## Alterações para a versão 5.0

- **Arquitetura Multi-Provedor**: Adicionado suporte completo para a **OpenAI**, **Groq** e **Mistral** junto ao Google Gemini. O utilizadores agora podem escolher o seu backend de IA preferido.
- **Roteamento Avançado de Modelos**: Utilizadores de provedores nativos (Gemini, OpenAI, etc.) agora podem selecionar modelos específicos de uma lista pendente para diferentes tarefas (OCR, STT, TTS).
- **Configuração Avançada de Endpoint**: Utilizadores de provedores personalizados podem inserir manualmente URLs e nomes de modelos específicos para um controlo granular sobre servidores locais ou de terceiros.
- **Visibilidade Inteligente de Recursos**: O menu de definições e a UI do Leitor de Documentos agora ocultam automaticamente recursos não suportados (como TTS) com base no provedor selecionado.
- **Procura Dinâmica de Modelos**: O suplemento agora procura a lista de modelos disponíveis diretamente da API do provedor, garantindo compatibilidade com novos modelos assim que forem lançados.
- **OCR Híbrido e Tradução**: Otimizada a lógica para usar o Google Tradutor para maior velocidade ao usar o OCR do Chrome, e tradução baseada em IA ao usar os mecanismos Gemini/Groq/OpenAI.
- **"Nova análise com IA" Universal**: O recurso de nova análise do Leitor de Documentos já não está limitado ao Gemini. Agora ele utiliza qualquer provedor de IA que esteja ativo no momento para reprocessar as páginas.

## Alterações para a versão 4.6

- **Recuperação Interativa de Resultados:** Adicionada a tecla **Espaço** à camada de comando, permitindo que os utilizadores reabram instantaneamente a última resposta da IA numa janela de chat para perguntas de acompanhamento, mesmo quando o modo "Saída Direta" estiver ativo.
- **Hub da Comunidade no Telegram:** Adicionado um link para o "Canal Oficial do Telegram" no menu Ferramentas do NVDA, fornecendo uma maneira rápida de se manter atualizado com as últimas notícias, recursos e lançamentos.
- **Estabilidade de Resposta Aprimorada:** Otimizada a lógica central para os recursos de Tradução, OCR e Visão para garantir um desempenho mais confiável e uma experiência mais suave ao usar a saída de fala direta.
- **Orientação de Interface Melhorada:** Atualizadas as descrições de definições e a documentação para explicar melhor o novo sistema de recuperação e como ele funciona junto com as definições de saída direta.

## Alterações para a versão 4.5

- **Gestor de Prompts Avançado:** Introduzido um diálogo de gestão dedicado nas definições para personalizar os prompts padrão do sistema e gerir prompts definidos pelo utilizador com suporte completo para adicionar, editar, reordenar e pré-visualizar.
- **Suporte Abrangente a Proxy:** Resolvidos os problemas de conectividade de rede garantindo que as definições de proxy configuradas pelo utilizador sejam estritamente aplicadas a todos os pedidos de API, incluindo tradução, OCR e geração de fala.
- **Migração Automatizada de Dados:** Integrado um sistema de migração inteligente para atualizar automaticamente as configurações de prompts legadas para um formato JSON v2 robusto na primeira execução, sem perda de dados.
- **Compatibilidade Atualizada (2025.1):** Definida a versão mínima do NVDA necessária para 2025.1 devido a dependências de biblioteca em recursos avançados como o Leitor de Documentos para garantir um desempenho estável.
- **Interface de Definições Otimizada:** Simplificada a interface de definições reorganizando a gestão de prompts num diálogo separado, proporcionando uma experiência de utilizador mais limpa e acessível.
- **Guia de Variáveis de Prompt:** Adicionado um guia integrado dentro dos diálogos de prompt para ajudar os utilizadores a identificar e usar facilmente variáveis dinâmicas como [selection], [clipboard] e [screen_obj].

## Alterações para a versão 4.0.3

- **Maior Resiliência de Rede:** Adicionado um mecanismo de repetição automática para lidar melhor com ligações instáveis de internet e erros temporários do servidor, garantindo respostas de IA mais confiáveis.
- **Diálogo Visual de Tradução:** Introduzida uma janela dedicada para resultados de tradução. Os utilizadores agora podem navegar e ler facilmente traduções longas linha por linha, de forma semelhante aos resultados de OCR.
- **Visualização Formatada Agregada:** O recurso "Exibir Formatado" no Leitor de Documentos agora exibe todas as páginas processadas numa única janela organizada com cabeçalhos de página claros.
- **Fluxo de Trabalho de OCR Otimizado:** Pula automaticamente a seleção de intervalo de páginas para documentos de página única, tornando o processo de reconhecimento mais rápido e fluido.
- **Estabilidade de API Aprimorada:** Alterado para um método de autenticação baseado em cabeçalho mais robusto, resolvendo possíveis erros de "Todas as chaves de API falharam" causados por conflitos de rotação de chaves.
- **Correções de Bugs:** Resolvidos vários bloqueios potenciais, incluindo um problema durante o encerramento do suplemento e um erro de foco no diálogo de chat.

## Alterações para a versão 4.0.1

- **Leitor de Documentos Avançado:** um novo e poderoso visualizador para PDF e imagens com seleção de intervalo de páginas, processamento em segundo plano e navegação fluida com `Ctrl+PageUp/Down`.
- **Novo Submenu de Ferramentas:** Adicionado um submenu dedicado "Vision Assistant" sob o menu Ferramentas do NVDA para um acesso mais rápido aos recursos principais, definições e documentação.
- **Personalização Flexível:** Agora pode escolher o seu mecanismo de OCR preferido e a voz do TTS diretamente no painel de definições.
- **Suporte a Múltiplas Chaves de API:** Adicionado suporte para várias chaves de API do Gemini. Pode inserir uma chave por linha ou separá-las com vírgulas nas definições.
- **Mecanismo de OCR Alternativo:** Introduzido um novo mecanismo de OCR para garantir o reconhecimento confiável de texto mesmo ao atingir os limites de cota da API do Gemini.
- **Rotação Inteligente de Chaves de API:** Alterna automaticamente para a chave de API em funcionamento mais rápida e a memoriza para contornar os limites de cota.
- **Documento para MP3/WAV:** Capacidade integrada de gerar e guardar ficheiros de áudio de alta qualidade nos formatos MP3 (128kbps) e WAV diretamente dentro do leitor.
- **Suporte a Stories do Instagram:** Adicionada a capacidade de descrever e analisar Stories do Instagram usando as suas URLs.
- **Suporte ao TikTok:** Introduzido suporte para vídeos do TikTok, permitindo a descrição visual completa e a transcrição de áudio dos clipes.
- **Diálogo de Atualização Redesenhado:** Apresenta uma nova interface acessível com uma caixa de texto rolável para ler claramente as alterações da versão antes de instalar.
- **Status Unificado e UX:** Padronizados os diálogos de ficheiros em todo o suplemento e aprimorado o comando 'L' para relatar o progresso em tempo real.

## Alterações para a versão 3.6.0

- **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) dentro da Camada de Comando para fornecer uma lista de fácil acesso com todos os atalhos e as suas funções.
- **Análise de Vídeo Online:** Suporte expandido para incluir vídeos do **Twitter (X)**. Também foi melhorada a detecção de URL e a estabilidade para uma experiência mais confiável.
- **Contribuição com o Projeto:** Adicionado um diálogo opcional de doação para utilizadores que desejam apoiar as futuras atualizações e o crescimento contínuo do projeto.

## Alterações para a versão 3.5.0

- **Camada de Comando:** Introduzido um sistema de Camada de Comando (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestra. Por exemplo, em vez de premir `NVDA+Control+Shift+T` para tradução, agora prime `NVDA+Shift+V` seguido por `T`.
- **Análise de Vídeo Online:** Adicionado um novo recurso para analisar vídeos do YouTube e Instagram diretamente fornecendo uma URL.

## Alterações para a versão 3.1.0

- **Modo de Saída Direta:** Adicionada uma opção para ignorar o diálogo de chat e ouvir as respostas da IA diretamente via fala para uma experiência mais rápida e fluida.
- **Integração com a Área de Transferência:** Adicionada uma nova configuração para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações para a versão 3.0

- **Novos Idiomas:** Adicionadas traduções para **Persa** e **Vietnamita**.
- **Modelos de IA Expandidos:** Reorganizada a lista de seleção de modelos com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`) para ajudar os utilizadores a distinguir entre modelos gratuitos e com limite de taxa (pagos). Adicionado suporte para o **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
- **Estabilidade de Ditado:** Melhorada significativamente a estabilidade do Ditado Inteligente. Adicionada uma verificação de segurança para ignorar clipes de áudio com menos de 1 segundo, evitando alucinações da IA e erros vazios.
- **Manipulação de Ficheiros:** Corrigido um problema onde o envio de ficheiros com nomes que não estavam em inglês falhava.
- **Otimização de Prompts:** Melhorada a lógica de Tradução e estruturados os resultados de Visão.

## Alterações para a versão 2.9

- **Adicionadas traduções para Francês e Turco.**
- **Visualização Formatada:** Adicionado um botão "Exibir Formatado" nos diálogos de chat para visualizar a conversa com a estilização adequada (Títulos, Negrito, Código) numa janela de navegação padrão.
- **Configuração de Markdown:** Adicionada uma nova opção "Limpar Markdown no Chat" nas Definições. Desmarcar isso permite que os utilizadores vejam a sintaxe bruta do Markdown (por exemplo, `**`, `#`) na janela de chat.
- **Gerenciamento de Diálogos:** Corrigido um problema onde as janelas de "Refinar Texto" ou de chat abriam várias vezes ou falhavam em obter o foco corretamente.
- **Melhorias de UX:** Padronizados os títulos dos diálogos de ficheiro para "Abrir" e removidos os anúncios de fala redundantes (por exemplo, "A abrir menu...") para uma experiência mais suave.

## Alterações para a versão 2.8

- Adicionada tradução para o Italiano.
- **Relatório de Status:** Adicionado um novo comando (NVDA+Control+Shift+I) para anunciar o status atual do suplemento (por exemplo, "A enviar...", "A analisar...").
- **Exportação em HTML:** O botão "Guardar Conteúdo" nos diálogos de resultado agora guarda a saída como um ficheiro HTML formatado, preservando estilos como títulos e texto em negrito.
- **UI de Definições:** Melhorado o layout do painel de Definições com agrupamento acessível.
- **Novos Modelos:** Adicionado suporte para gemini-flash-latest e gemini-flash-lite-latest.
- **Idiomas:** Adicionado Nepalês aos idiomas suportados.
- **Lógica do Menu Refinar:** Corrigido um bug crítico onde os comandos de "Refinar Texto" falhavam se o idioma da interface do NVDA não fosse o Inglês.
- **Ditado:** Melhorada a detecção de silêncio para evitar saídas de texto incorretas quando nenhuma fala é inserida.
- **Configurações de Atualização:** "Verificar atualizações na inicialização" agora está desativado por certas políticas da Add-on Store.
- Limpeza de Código.

## Alterações para a versão 2.7

- Migrada a estrutura do projeto para o Modelo de Suplemento oficial da NV Access para melhor conformidade com os padrões.
- Implementada lógica de repetição automática para erros HTTP 429 (Limite de Taxa) para garantir fiabilidade durante tráfego alto.
- Otimizados os prompts de tradução para maior precisão e melhor manipulação da lógica de "Troca Inteligente".
- Atualizada a tradução para o Russo.

## Alterações para a versão 2.6

- Adicionado suporte de tradução para o Russo (Obrigado ao nvda-ru).
- Atualizadas as mensagens de erro para fornecer um feedback mais descritivo em relação à conectividade.
- Alterado o idioma de destino padrão para o Inglês.

## Alterações para a versão 2.5

- Adicionado Comando de OCR de Ficheiro Nativo (NVDA+Control+Shift+F).
- Adicionado botão "Guardar Chat" aos diálogos de resultado.
- Implementado suporte completo de localização (i18n).
- Migrado o feedback de áudio para o módulo de tons nativo do NVDA.
- Alterado para a API de Ficheiros do Gemini para melhor manipulação de ficheiros PDF e de áudio.
- Corrigido bloqueio ao traduzir textos que continham chavetas.

## Alterações para a versão 2.1.1

- Corrigido um problema onde a variável [file_ocr] não funcionava corretamente dentro de Prompts Personalizados.

## Alterações para a versão 2.1

- Padronizados todos os atalhos para usar NVDA+Control+Shift para eliminar conflitos com o layout de Portátil do NVDA e teclas de atalho do sistema.

## Alterações para a versão 2.0

- Implementado sistema integrado de Atualização Automática.
- Adicionado Cache de Tradução Inteligente para recuperação instantânea de textos traduzidos anteriormente.
- Adicionada Memória de Conversa para refinar os resultados contextualmente em diálogos de chat.
- Adicionado comando Dedicado de Tradução da Área de Transferência (NVDA+Control+Shift+Y).
- Otimizados os prompts de IA para impor estritamente a saída no idioma de destino.
- Corrigido bloqueio causado por caracteres especiais no texto de entrada.

## Alterações para a versão 1.5

- Adicionado suporte para mais de 20 novos idiomas.
- Implementado Diálogo Interativo de Refinamento para perguntas de acompanhamento.
- Adicionado recurso de Ditado Inteligente Nativo.
- Adicionada a categoria "Vision Assistant" ao diálogo de Definir Comandos do NVDA.
- Corrigidos bloqueios de COMError em aplicações específicas como o Firefox e Word.
- Adicionado mecanismo de repetição automática para erros do servidor.

## Alterações para a versão 1.0

- Lançamento inicial.
