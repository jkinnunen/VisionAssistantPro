# Documentação do Vision Assistant Pro

O **Vision Assistant Pro** é um assistente de IA multimodal avançado para o NVDA. Ele utiliza mecanismos de IA de classe mundial para fornecer leitura de tela inteligente, tradução, ditado por voz e análise de documentos.

_Este complemento foi lançado para a comunidade em homenagem ao Dia Internacional das Pessoas com Deficiência._

## 1. Configuração

Vá para **Menu NVDA > Preferências > Configurações > Vision Assistant Pro**.

### 1.1 Configurações de Conexão

- **Provedor:** Selecione seu serviço de IA preferido. Os provedores suportados incluem **Google Gemini**, **OpenAI**, **Mistral**, **Groq** e **Personalizado** (servidores compatíveis com OpenAI como Ollama/LM Studio).
- **Nota Importante:** Recomendamos fortemente o uso do **Google Gemini** para obter o melhor desempenho e precisão (especialmente para análise de imagens/arquivos).
- **Chave de API (API Key):** Obrigatória. Você pode inserir várias chaves (separadas por vírgulas ou novas linhas) para rotação automática.
- **Buscar Modelos:** Após inserir sua chave de API, pressione este botão para baixar a lista mais recente de modelos disponíveis do provedor.
- **Modelo de IA:** Selecione o modelo principal usado para chat geral e análise.

### 1.2 Roteamento Avançado de Modelos

_Disponível para todos os provedores, incluindo Gemini, OpenAI, Groq, Mistral e Personalizado._

> **⚠️ Aviso:** Estas configurações são destinadas apenas a **usuários avançados**. Se você não tiver certeza do que um modelo específico faz, deixe esta opção **desmarcada**. Selecionar um modelo incompatível para uma tarefa (por exemplo, um modelo apenas de texto para Visão) causará erros e interromperá o funcionamento do complemento.

Marque **"Roteamento Avançado de Modelos (Específico por tarefa)"** para desbloquear o controle detalhado. Isso permite selecionar modelos específicos da lista suspensa para diferentes tarefas:

- **Modelo de OCR / Visão:** Escolha um modelo especializado para analisar imagens.
- **Fala para Texto (STT):** Escolha um modelo específico para ditado.
- **Texto para Fala (TTS):** Escolha um modelo para gerar áudio.
- **Modelo de Operador de IA:** Selecione um modelo específico para tarefas de operação autônoma do computador.
  _Nota: Recursos não suportados (ex: TTS para Groq) serão ocultados automaticamente._

### 1.3 Configuração Avançada de Endpoint (Provedor Personalizado)

_Disponível apenas quando "Personalizado" está selecionado._

> **⚠️ Aviso:** Esta seção permite a configuração manual da API e foi projetada para **usuários experientes** que executam servidores locais ou proxies. URLs ou nomes de modelos incorretos interromperão a conectividade. Se você não sabe exatamente o que são esses endpoints, mantenha isso **desmarcado**.

Marque **"Configuração Avançada de Endpoint"** para inserir manualmente os detalhes do servidor. Ao contrário dos provedores nativos, aqui você deve **digitar** as URLs e nomes de modelos específicos:

- **URL da Lista de Modelos:** O endpoint para buscar os modelos disponíveis.
- **URL do Endpoint OCR/STT/TTS:** URLs completas para serviços específicos (ex: `http://localhost:11434/v1/audio/speech`).
- **Modelos Personalizados:** Digite manualmente o nome do modelo (ex: `llama3:8b`) para cada tarefa.

### 1.4 Preferências Gerais

- **Mecanismo de OCR:** Escolha entre **Chrome (Rápido)** para resultados ágeis ou **IA (Avançado)** para preservação superior do layout.
  - _Nota:_ Se você selecionar "IA (Avançado)", mas seu provedor estiver configurado como OpenAI/Groq, o complemento roteará inteligentemente a imagem para o modelo de visão do seu provedor ativo.
- **Voz do TTS:** Selecione seu estilo de voz preferido. Esta lista é atualizada dinamicamente com base no seu provedor ativo.
- **Criatividade (Temperatura):** Controla a aleatoriedade da IA. Valores mais baixos são melhores para tradução/OCR precisos.
- **URL de Proxy:** Configure isto se os serviços de IA estiverem restritos em sua região (suporta proxies locais como `127.0.0.1` ou URLs de ponte).

## 2. Camada de Comandos e Atalhos

Para evitar conflitos de teclado, este complemento utiliza uma **Camada de Comandos**.

1. Pressione **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (você ouvirá um bipe).
2. Solte as teclas e pressione uma das seguintes teclas individuais:

| Tecla         | Função                       | Descrição                                                                     |
| ------------- | ---------------------------- | ----------------------------------------------------------------------------- |
| **Shift + A** | **Operador de IA**           | **Operação Autônoma:** Diga à IA para realizar uma tarefa na sua tela.        |
| **E**         | **Explorador de UI**         | **Clique Interativo:** Identifica e clica em elementos de UI em qualquer app. |
| **T**         | Tradutor Inteligente         | Traduz o texto sob o cursor de navegação ou seleção.                          |
| **Shift + T** | Tradutor de Área de Transf.  | Traduz o conteúdo que está atualmente na área de transferência.               |
| **R**         | Refinador de Texto           | Resumir, Corrigir Gramática, Explicar ou executar **Prompts Personalizados**. |
| **V**         | Visão de Objeto              | Descreve o objeto de navegação atual.                                         |
| **O**         | Visão de Tela Cheia          | Analisa o layout e o conteúdo de toda a tela.                                 |
| **Shift + V** | Análise de Vídeo Online      | Analisa vídeos do **YouTube**, **Instagram**, **TikTok** ou **Twitter (X)**.  |
| **D**         | Leitor de Documentos         | Leitor avançado para PDF e imagens com seleção de intervalo de páginas.       |
| **F**         | **Ação de Arquivo Intelig.** | Reconhecimento contextual de arquivos de imagem, PDF ou TIFF selecionados.    |
| **A**         | Transcrição de Áudio         | Transcreve arquivos MP3, WAV ou OGG para texto.                               |
| **C**         | Solucionador de CAPTCHA      | Captura e resolve CAPTCHAs (Suporta portais governamentais).                  |
| **S**         | Ditado Inteligente           | Converte fala em texto. Pressione para gravar, novamente para parar/digitar.  |
| **L**         | Relatório de Status          | Anuncia o progresso atual (ex: "Escaneando...", "Inativo").                   |
| **U**         | Verificar Atualização        | Verifica manualmente no GitHub a versão mais recente do complemento.          |
| **Espaço**    | Relembrar Último Result.     | Mostra a última resposta da IA em um diálogo de chat para revisão.            |
| **H**         | Ajuda de Comandos            | Exibe uma lista de todos os atalhos disponíveis.                              |

### 2.1 Atalhos do Leitor de Documentos (Dentro do Visualizador)

- **Ctrl + PageDown:** Ir para a próxima página.
- **Ctrl + PageUp:** Ir para a página anterior.
- **Alt + A:** Abrir um diálogo de chat para fazer perguntas sobre o documento.
- **Alt + R:** Forçar um **Re-escaneamento com IA** usando seu provedor ativo.
- **Alt + G:** Gerar e salvar um arquivo de áudio de alta qualidade (WAV/MP3). _Oculto se o provedor não suportar TTS._
- **Alt + S / Ctrl + S:** Salvar o texto extraído como um arquivo TXT ou HTML.

## 3. Prompts Personalizados e Variáveis

Você pode gerenciar os prompts em **Configurações > Prompts > Gerenciar Prompts...**.

### Variáveis Suportadas

- `[selection]`: Texto selecionado no momento.
- `[clipboard]`: Conteúdo da área de transferência.
- `[screen_obj]`: Captura de tela do objeto de navegação.
- `[screen_full]`: Captura de tela inteira.
- `[file_ocr]`: Selecionar arquivo de imagem/PDF para extração de texto.
- `[file_read]`: Selecionar documento para leitura (TXT, Código, PDF).
- `[file_audio]`: Selecionar arquivo de áudio para análise (MP3, WAV, OGG).

**Nota:** Uma conexão ativa com a internet é necessária para todos os recursos de IA. Documentos de várias páginas são processados automaticamente.

## 4. Suporte e Comunidade

Fique atualizado com as últimas notícias, recursos e lançamentos:

- **Canal no Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **GitHub Issues:** Para relatórios de bugs e solicitações de recursos.

## 5. Apoiadores do Projeto

Um agradecimento sincero aos membros da nossa comunidade que apoiam o desenvolvimento contínuo e a manutenção deste projeto através de suas generosas contribuições financeiras:

- **@Alyabani94**

_Se você deseja apoiar o projeto financeiramente e ver seu nome aqui, você pode encontrar a opção **Doar** no menu Ferramentas do NVDA (sub-menu Vision Assistant) ou durante o processo de configuração após a instalação._

## Alterações para a versão 5.6

- **Adicionado Mecanismo de OCR "Nenhum (Extrair Camada de Texto)"**: Os usuários agora podem extrair texto diretamente de PDFs pesquisáveis sem usar créditos de IA, melhorando significativamente a velocidade e a privacidade para documentos baseados em texto.
- **Refinada a Precisão do Explorador de UI**: Melhorado o prompt do Explorador de UI para identificar melhor os tipos de elementos (como Itens de Lista) e relatar com precisão estados como "(Marcado)", "(Selecionado)" ou "(Expandido)", ignorando componentes do sistema Windows como a Barra de Tarefas e o Relógio.
- **Lembrete de Configuração de Instalação**: Adicionada uma notificação após a instalação para guiar os usuários ao menu de configurações para configurar suas chaves de API e preferências.

## Alterações para a versão 5.5.2

- **Corrigido Problema de Digitação do Operador de IA:** Resolvido um bug onde a letra 'v' era digitada em vez de colar o texto em certos sistemas. Esta correção aborda conflitos de tempo que ocorriam durante alta carga do sistema.
- **Estabilidade Aprimorada:** Adicionado tratamento robusto de erros para operações de área de transferência para evitar travamentos do complemento quando a área de transferência do sistema está temporariamente bloqueada por outros aplicativos.
- **Otimização de Tempo:** Ajustados os atrasos internos para eventos de teclado para garantir maior confiabilidade em diferentes velocidades de sistema e melhor compatibilidade com gerenciadores de área de transferência de terceiros.

## Alterações para a versão 5.5 (A Atualização de Automação)

- **Operador de IA (Controle Autônomo - Shift+A):** Esta é a joia da coroa da v5.5. O Vision Assistant Pro deixou de ser um assistente passivo para se tornar seu **Operador de IA** pessoal. Ele não apenas descreve a tela — ele assume o comando.
  - _Como funciona:_ Agora você pode dar instruções verbais para operar seu PC. Por exemplo, em um aplicativo completamente inacessível onde seu leitor de tela permanece mudo, você pode pressionar **Shift+A** e digitar: _"Clique no botão Configurações"_ ou _"Encontre o campo de busca, digite 'Últimas Notícias' e pressione enter."_ A IA identifica visualmente os elementos, move o mouse e executa a tarefa para você.
  - _Nota de Desempenho:_ Este recurso é otimizado para o **Gemini 3.0 Flash (Preview)**, fornecendo respostas incrivelmente rápidas e inteligentes que podem lidar até com os layouts de UI mais complexos.
  - **⚠️ Aviso de Uso de API:** Como o Operador de IA precisa "ver" exatamente o que está acontecendo para ser preciso, ele envia uma captura de tela de alta resolução a cada passo. Observe que o uso frequente consumirá sua cota de API muito mais rápido do que tarefas padrão baseadas em texto.
- **Explorador de UI Visual (E):** Cansado de navegar por "botões sem etiqueta"? Pressione **E** para ativar o Explorador de UI. A IA escaneará toda a janela e gerará uma lista de todos os elementos clicáveis que encontrar — incluindo ícones, gráficos e menus. Basta escolher um item da lista e o Operador de IA clicará nele para você. É como ter uma "camada acessível" sobre qualquer app.
- **Ação de Arquivo Inteligente Contextual (F):** A tecla "F" foi completamente reformulada. Ela não assume mais que você deseja apenas OCR. Ao selecionar uma única imagem, ela agora pergunta inteligentemente sua intenção: você pode escolher uma **Descrição Visual Detalhada** para entender a cena ou uma **Extração de Texto Estruturada (OCR)** para leitura. O menu se adapta dinamicamente com base no tipo de arquivo e no seu mecanismo de IA ativo.
- **Otimização de Núcleo:** Realizamos uma limpeza profunda na lógica interna do complemento, removendo funções legadas não utilizadas e código redundante. Isso resulta em uma experiência mais enxuta, rápida e confiável para todos os usuários.

## Alterações para a versão 5.0

- **Arquitetura Multi-Provedor**: Adicionado suporte total para **OpenAI**, **Groq** e **Mistral** junto ao Google Gemini. Os usuários agora podem escolher seu backend de IA preferido.
- **Roteamento Avançado de Modelos**: Usuários de provedores nativos (Gemini, OpenAI, etc.) agora podem selecionar modelos específicos de uma lista suspensa para diferentes tarefas (OCR, STT, TTS).
- **Configuração Avançada de Endpoint**: Usuários de provedores personalizados podem inserir manualmente URLs e nomes de modelos específicos para controle granular sobre servidores locais ou de terceiros.
- **Visibilidade Inteligente de Recursos**: O menu de configurações e a UI do Leitor de Documentos agora ocultam automaticamente recursos não suportados (como TTS) com base no provedor selecionado.
- **Busca Dinâmica de Modelos**: O complemento agora busca a lista de modelos disponíveis diretamente da API do provedor, garantindo compatibilidade com novos modelos assim que forem lançados.
- **OCR e Tradução Híbridos**: Otimizada a lógica para usar o Google Tradutor para velocidade ao usar o OCR do Chrome, e tradução via IA ao usar os mecanismos Gemini/Groq/OpenAI.
- **"Re-escanear com IA" Universal**: O recurso de re-escanear do Leitor de Documentos não está mais limitado ao Gemini. Agora ele utiliza qualquer provedor de IA que estiver ativo no momento para re-processar as páginas.

## Alterações para a versão 4.6

- **Recuperação Interativa de Resultados:** Adicionada a tecla **Espaço** à camada de comandos, permitindo que os usuários reabram instantaneamente a última resposta da IA em uma janela de chat para perguntas de acompanhamento, mesmo quando o modo "Saída Direta" está ativo.
- **Hub da Comunidade no Telegram:** Adicionado um link para o "Canal Oficial no Telegram" no menu Ferramentas do NVDA, fornecendo uma maneira rápida de se manter atualizado com as últimas notícias, recursos e lançamentos.
- **Estabilidade de Resposta Aprimorada:** Otimizada a lógica central para os recursos de Tradução, OCR e Visão para garantir um desempenho mais confiável e uma experiência mais suave ao usar a saída de fala direta.
- **Orientação de Interface Melhorada:** Atualizadas as descrições de configurações e documentação para explicar melhor o novo sistema de recuperação e como ele funciona junto com as configurações de saída direta.

## Alterações para a versão 4.5

- **Gerenciador de Prompts Avançado:** Introduzido um diálogo de gerenciamento dedicado nas configurações para personalizar prompts padrão do sistema e gerenciar prompts definidos pelo usuário com suporte total para adicionar, editar, reordenar e visualizar.
- **Suporte Abrangente a Proxy:** Resolvidos problemas de conectividade de rede garantindo que as configurações de proxy definidas pelo usuário sejam aplicadas estritamente a todas as solicitações de API, incluindo tradução, OCR e geração de fala.
- **Migração Automática de Dados:** Integrado um sistema de migração inteligente para atualizar automaticamente as configurações de prompts legadas para um formato JSON v2 robusto na primeira execução, sem perda de dados.
- **Compatibilidade Atualizada (2025.1):** Definida a versão mínima necessária do NVDA como 2025.1 devido a dependências de biblioteca em recursos avançados como o Leitor de Documentos para garantir um desempenho estável.
- **Interface de Configurações Otimizada:** Simplificada a interface de configurações reorganizando o gerenciamento de prompts em um diálogo separado, proporcionando uma experiência de usuário mais limpa e acessível.
- **Guia de Variáveis de Prompt:** Adicionado um guia integrado dentro dos diálogos de prompt para ajudar os usuários a identificar e usar facilmente variáveis dinâmicas como [selection], [clipboard] e [screen_obj].

## Alterações para a versão 4.0.3

- **Resiliência de Rede Aprimorada:** Adicionado um mecanismo de repetição automática para lidar melhor com conexões de internet instáveis e erros temporários de servidor, garantindo respostas de IA mais confiáveis.
- **Diálogo de Tradução Visual:** Introduzida uma janela dedicada para resultados de tradução. Os usuários agora podem navegar facilmente e ler traduções longas linha por linha, de forma semelhante aos resultados de OCR.
- **Visualização Formatada Agregada:** O recurso "Visualizar Formatado" no Leitor de Documentos agora exibe todas as páginas processadas em uma única janela organizada com cabeçalhos de página claros.
- **Fluxo de Trabalho de OCR Otimizado:** Pula automaticamente a seleção de intervalo de páginas para documentos de página única, tornando o processo de reconhecimento mais rápido e fluido.
- **Estabilidade de API Melhorada:** Mudança para um método de autenticação baseado em cabeçalho mais robusto, resolvendo possíveis erros de "Todas as Chaves de API falharam" causados por conflitos de rotação de chaves.
- **Correções de Bugs:** Resolvidos vários travamentos potenciais, incluindo um problema durante o encerramento do complemento e um erro de foco no diálogo de chat.

## Alterações para a versão 4.0.1

- **Leitor de Documentos Avançado:** Um novo e poderoso visualizador para PDF e imagens com seleção de intervalo de páginas, processamento em segundo plano e navegação contínua com `Ctrl+PageUp/Down`.
- **Novo Submenu de Ferramentas:** Adicionado um submenu dedicado "Vision Assistant" sob o menu Ferramentas do NVDA para acesso mais rápido aos recursos principais, configurações e documentação.
- **Personalização Flexível:** Agora você pode escolher seu mecanismo de OCR preferido e voz de TTS diretamente no painel de configurações.
- **Suporte a Múltiplas Chaves de API:** Adicionado suporte para várias chaves de API do Gemini. Você pode inserir uma chave por linha ou separá-las por vírgulas nas configurações.
- **Mecanismo de OCR Alternativo:** Introduzido um novo mecanismo de OCR para garantir o reconhecimento de texto confiável mesmo ao atingir os limites de cota da API do Gemini.
- **Rotação Inteligente de Chaves de API:** Alterna automaticamente e lembra a chave de API que funciona mais rápido para contornar limites de cota.
- **Documento para MP3/WAV:** Capacidade integrada de gerar e salvar arquivos de áudio de alta qualidade nos formatos MP3 (128kbps) e WAV diretamente no leitor.
- **Suporte a Stories do Instagram:** Adicionada a capacidade de descrever e analisar Stories do Instagram usando suas URLs.
- **Suporte ao TikTok:** Introduzido suporte para vídeos do TikTok, permitindo descrição visual completa e transcrição de áudio dos clipes.
- **Diálogo de Atualização Redesenhado:** Apresenta uma nova interface acessível com uma caixa de texto rolável para ler claramente as mudanças de versão antes de instalar.
- **Status e UX Unificados:** Padronização dos diálogos de arquivos em todo o complemento e aprimoramento do comando 'L' para relatar o progresso em tempo real.

## Alterações para a versão 3.6.0

- **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) dentro da Camada de Comandos para fornecer uma lista de fácil acesso de todos os atalhos e suas funções.
- **Análise de Vídeo Online:** Suporte expandido para incluir vídeos do **Twitter (X)**. Também melhorada a detecção de URL e estabilidade para uma experiência mais confiável.
- **Contribuição ao Projeto:** Adicionado um diálogo de doação opcional para usuários que desejam apoiar as futuras atualizações e o crescimento contínuo do projeto.

## Alterações para a versão 3.5.0

- **Camada de Comandos:** Introduzido um sistema de Camada de Comandos (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestra. Por exemplo, em vez de pressionar `NVDA+Control+Shift+T` para tradução, agora você pressiona `NVDA+Shift+V` seguido de `T`.
- **Análise de Vídeo Online:** Adicionado um novo recurso para analisar vídeos do YouTube e Instagram diretamente fornecendo uma URL.

## Alterações para a versão 3.1.0

- **Modo de Saída Direta:** Adicionada uma opção para pular o diálogo de chat e ouvir as respostas da IA diretamente via fala para uma experiência mais rápida e integrada.
- **Integração com Área de Transferência:** Adicionada uma nova configuração para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações para a versão 3.0

- **Novos Idiomas:** Adicionadas traduções para **Persa** e **Vietnamita**.
- **Modelos de IA Expandidos:** Reorganizada a lista de seleção de modelos com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`) para ajudar os usuários a distinguir entre modelos gratuitos e com limite de taxa (pagos). Adicionado suporte para **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
- **Estabilidade de Ditado:** Estabilidade do Ditado Inteligente significativamente aprimorada. Adicionada uma verificação de segurança para ignorar clipes de áudio menores que 1 segundo, evitando alucinações da IA e erros vazios.
- **Manuseio de Arquivos:** Corrigido um problema onde o upload de arquivos com nomes não em inglês falhava.
- **Otimização de Prompt:** Melhorada a lógica de Tradução e resultados de Visão estruturados.

## Alterações para a versão 2.9

- **Adicionadas traduções para Francês e Turco.**
- **Visualização Formatada:** Adicionado um botão "Visualizar Formatado" nos diálogos de chat para ver a conversa com estilização adequada (Cabeçalhos, Negrito, Código) em uma janela de navegação padrão.
- **Configuração de Markdown:** Adicionada uma nova opção "Limpar Markdown no Chat" nas Configurações. Desmarcar isso permite que os usuários vejam a sintaxe Markdown bruta (ex: `**`, `#`) na janela de chat.
- **Gerenciamento de Diálogos:** Corrigido um problema onde as janelas de "Refinar Texto" ou chat abriam várias vezes ou falhavam ao focar corretamente.
- **Melhorias de UX:** Padronização dos títulos dos diálogos de arquivo para "Abrir" e remoção de anúncios de voz redundantes (ex: "Abrindo menu...") para uma experiência mais fluida.

## Alterações para a versão 2.8

- Adicionada tradução para Italiano.
- **Relatório de Status:** Adicionado um novo comando (NVDA+Control+Shift+I) para anunciar o status atual do complemento (ex: "Fazendo upload...", "Analisando...").
- **Exportação HTML:** O botão "Salvar Conteúdo" nos diálogos de resultado agora salva a saída como um arquivo HTML formatado, preservando estilos como cabeçalhos e negrito.
- **UI de Configurações:** Melhorado o layout do painel de Configurações com agrupamento acessível.
- **Novos Modelos:** Adicionado suporte para gemini-flash-latest e gemini-flash-lite-latest.
- **Idiomas:** Adicionado Nepalês aos idiomas suportados.
- **Lógica do Menu Refinar:** Corrigido um bug crítico onde os comandos de "Refinar Texto" falhavam se o idioma da interface do NVDA não fosse Inglês.
- **Ditado:** Melhorada a detecção de silêncio para evitar saída de texto incorreta quando nenhuma fala é inserida.
- **Configurações de Atualização:** "Verificar atualizações ao iniciar" agora está desativado por padrão para cumprir as políticas da Add-on Store.
- Limpeza de código.

## Alterações para a versão 2.7

- Migração da estrutura do projeto para o Modelo de Complemento oficial da NV Access para melhor conformidade com os padrões.
- Implementada lógica de repetição automática para erros HTTP 429 (Limite de Taxa) para garantir confiabilidade durante alto tráfego.
- Otimização dos prompts de tradução para maior precisão e melhor manuseio da lógica "Smart Swap".
- Atualização da tradução para Russo.

## Alterações para a versão 2.6

- Adicionado suporte à tradução para Russo (Obrigado ao nvda-ru).
- Atualizadas mensagens de erro para fornecer feedback mais descritivo sobre conectividade.
- Alterado o idioma de destino padrão para Inglês.

## Alterações para a versão 2.5

- Adicionado Comando de OCR Nativo de Arquivo (NVDA+Control+Shift+F).
- Adicionado botão "Salvar Chat" aos diálogos de resultado.
- Implementado suporte total à localização (i18n).
- Migração do feedback de áudio para o módulo de tons nativos do NVDA.
- Mudança para a API de Arquivos do Gemini para melhor manuseio de PDF e arquivos de áudio.
- Correção de erro ao traduzir texto contendo chaves.

## Alterações para a versão 2.1.1

- Corrigido um problema onde a variável [file_ocr] não funcionava corretamente dentro dos Prompts Personalizados.

## Alterações para a versão 2.1

- Padronização de todos os atalhos para usar NVDA+Control+Shift para eliminar conflitos com o layout de Laptop do NVDA e teclas de atalho do sistema.

## Alterações para a versão 2.0

- Implementado sistema de Atualização Automática embutido.
- Adicionado Cache de Tradução Inteligente para recuperação instantânea de textos traduzidos anteriormente.
- Adicionada Memória de Conversa para refinar resultados contextualmente em diálogos de chat.
- Adicionado comando dedicado de Tradução de Área de Transf. (NVDA+Control+Shift+Y).
- Otimização dos prompts de IA para reforçar estritamente a saída no idioma de destino.
- Correção de erro causado por caracteres especiais no texto de entrada.

## Alterações para a versão 1.5

- Adicionado suporte para mais de 20 novos idiomas.
- Implementado Diálogo de Refinamento Interativo para perguntas de acompanhamento.
- Adicionado recurso de Ditado Inteligente Nativo.
- Adicionada categoria "Vision Assistant" ao diálogo de Gestos de Entrada do NVDA.
- Correção de erros COMError em aplicativos específicos como Firefox e Word.
- Adicionado mecanismo de repetição automática para erros de servidor.

## Alterações para a versão 1.0

- Lançamento inicial.
