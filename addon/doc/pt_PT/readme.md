# Documentação do Vision Assistant Pro

O **Vision Assistant Pro** é um assistente de IA multimodal avançado para o NVDA. Utiliza motores de IA de classe mundial para fornecer leitura de ecrã inteligente, tradução, ditado por voz e análise de documentos.

_Este extra foi lançado para a comunidade em honra do Dia Internacional das Pessoas com Deficiência._

## 1. Configuração

Aceda ao **Menu NVDA > Preferências > Definições > Vision Assistant Pro**.

### 1.1 Definições de Ligação

- **Fornecedor:** Selecione o seu serviço de IA preferido. Os fornecedores suportados incluem **Google Gemini**, **OpenAI**, **Mistral**, **Groq** e **Personalizado** (servidores compatíveis com OpenAI como Ollama/LM Studio).
- **Nota Importante:** Recomendamos vivamente a utilização do **Google Gemini** para obter o melhor desempenho e precisão (especialmente para análise de imagens/ficheiros).
- **Chave de API (API Key):** Obrigatória. Pode inserir várias chaves (separadas por vírgulas ou novas linhas) para rotação automática.
- **Obter Modelos:** Após inserir a sua chave de API, prima este botão para descarregar a lista mais recente de modelos disponíveis do fornecedor.
- **Modelo de IA:** Selecione o modelo principal utilizado para chat geral e análise.

### 1.2 Encaminhamento Avançado de Modelos

_Disponível para todos os fornecedores, incluindo Gemini, OpenAI, Groq, Mistral e Personalizado._

> **⚠️ Aviso:** Estas definições destinam-se apenas a **utilizadores avançados**. Se não tiver a certeza do que um modelo específico faz, deixe esta opção **desmarcada**. Selecionar um modelo incompatível para uma tarefa (por exemplo, um modelo apenas de texto para Visão) causará erros e interromperá o funcionamento do extra.

Assinale **"Encaminhamento Avançado de Modelos (Específico por tarefa)"** para desbloquear o controlo detalhado. Isto permite selecionar modelos específicos da lista pendente para diferentes tarefas:

- **Modelo de OCR / Visão:** Escolha um modelo especializado para analisar imagens.
- **Fala para Texto (STT):** Escolha um modelo específico para ditado.
- **Texto para Fala (TTS):** Escolha um modelo para gerar áudio.
- **Modelo de Operador de IA:** Selecione um modelo específico para tarefas de operação autónoma do computador.
  _Nota: Funcionalidades não suportadas (ex: TTS para Groq) serão ocultadas automaticamente._

### 1.3 Configuração Avançada de Endpoint (Fornecedor Personalizado)

_Disponível apenas quando "Personalizado" está selecionado._

> **⚠️ Aviso:** Esta secção permite a configuração manual da API e foi concebida para **utilizadores experientes** que executam servidores locais ou proxies. URLs ou nomes de modelos incorretos interromperão a conetividade. Se não sabe exatamente o que são estes endpoints, mantenha isto **desmarcado**.

Assinale **"Configuração Avançada de Endpoint"** para inserir manualmente os detalhes do servidor. Ao contrário dos fornecedores nativos, aqui deve **escrever** os URLs e nomes de modelos específicos:

- **URL da Lista de Modelos:** O endpoint para obter os modelos disponíveis.
- **URL do Endpoint OCR/STT/TTS:** URLs completos para serviços específicos (ex: `http://localhost:11434/v1/audio/speech`).
- **Modelos Personalizados:** Escreva manualmente o nome do modelo (ex: `llama3:8b`) para cada tarefa.

### 1.4 Preferências Gerais

- **Motor de OCR:** Escolha entre **Chrome (Rápido)** para resultados céleres ou **IA (Avançado)** para uma preservação superior do esquema (layout).
  - _Nota:_ Se selecionar "IA (Avançado)", mas o seu fornecedor estiver configurado como OpenAI/Groq, o extra encaminhará inteligentemente a imagem para o modelo de visão do seu fornecedor ativo.
- **Voz do TTS:** Selecione o seu estilo de voz preferido. Esta lista é atualizada dinamicamente com base no seu fornecedor ativo.
- **Criatividade (Temperatura):** Controla a aleatoriedade da IA. Valores mais baixos são melhores para tradução/OCR precisos.
- **URL de Proxy:** Configure isto se os serviços de IA estiverem restritos na sua região (suporta proxies locais como `127.0.0.1` ou URLs de ponte).

## 2. Camada de Comandos e Atalhos

Para evitar conflitos de teclado, este extra utiliza uma **Camada de Comandos**.

1. Prima **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (ouvirá um sinal sonoro).
2. Solte as teclas e prima uma das seguintes teclas individuais:

| Tecla         | Função                        | Descrição                                                                     |
| ------------- | ----------------------------- | ----------------------------------------------------------------------------- |
| **Shift + A** | **Operador de IA**            | **Operação Autónoma:** Diga à IA para realizar uma tarefa no seu ecrã.        |
| **E**         | **Explorador de UI**          | **Clique Interativo:** Identifica e clica em elementos de UI em qualquer app. |
| **T**         | Tradutor Inteligente          | Traduz o texto sob o cursor de navegação ou seleção.                          |
| **Shift + T** | Tradutor da Área de Transf.   | Traduz o conteúdo que está atualmente na área de transferência.               |
| **R**         | Refinador de Texto            | Resumir, Corrigir Gramática, Explicar ou executar **Prompts Personalizados**. |
| **V**         | Visão de Objeto               | Descreve o objeto de navegação atual.                                         |
| **O**         | Visão de Ecrã Inteiro         | Analisa o esquema e o conteúdo de todo o ecrã.                                |
| **Shift + V** | Análise de Vídeo Online       | Analisa vídeos do **YouTube**, **Instagram**, **TikTok** ou **Twitter (X)**.  |
| **D**         | Leitor de Documentos          | Leitor avançado para PDF e imagens com seleção de intervalo de páginas.       |
| **F**         | **Ação de Ficheiro Intelig.** | Reconhecimento contextual de ficheiros de imagem, PDF ou TIFF selecionados.   |
| **A**         | Transcrição de Áudio          | Transcreve ficheiros MP3, WAV ou OGG para texto.                              |
| **C**         | Solucionador de CAPTCHA       | Captura e resolve CAPTCHAs (Suporta portais governamentais).                  |
| **S**         | Ditado Inteligente            | Converte fala em texto. Prima para gravar, novamente para parar/escrever.     |
| **L**         | Relatório de Estado           | Anuncia o progresso atual (ex: "A analisar...", "Inativo").                   |
| **U**         | Verificar Atualização         | Verifica manualmente no GitHub a versão mais recente do extra.                |
| **Espaço**    | Relembrar Último Result.      | Mostra a última resposta da IA num diálogo de chat para revisão.              |
| **H**         | Ajuda de Comandos             | Exibe uma lista de todos os atalhos disponíveis.                              |

### 2.1 Atalhos do Leitor de Documentos (Dentro do Visualizador)

- **Ctrl + PageDown:** Ir para a página seguinte.
- **Ctrl + PageUp:** Ir para a página anterior.
- **Alt + A:** Abrir um diálogo de chat para fazer perguntas sobre o documento.
- **Alt + R:** Forçar um **Re-exame com IA** utilizando o seu fornecedor ativo.
- **Alt + G:** Gerar e guardar um ficheiro de áudio de alta qualidade (WAV/MP3). _Oculto se o fornecedor não suportar TTS._
- **Alt + S / Ctrl + S:** Guardar o texto extraído como um ficheiro TXT ou HTML.

## 3. Prompts Personalizados e Variáveis

Pode gerir os prompts em **Definições > Prompts > Gerir Prompts...**.

### Variáveis Suportadas

- `[selection]`: Texto selecionado no momento.
- `[clipboard]`: Conteúdo da área de transferência.
- `[screen_obj]`: Captura de ecrã do objeto de navegação.
- `[screen_full]`: Captura de ecrã total.
- `[file_ocr]`: Selecionar ficheiro de imagem/PDF para extração de texto.
- `[file_read]`: Selecionar documento para leitura (TXT, Código, PDF).
- `[file_audio]`: Selecionar ficheiro de áudio para análise (MP3, WAV, OGG).

**Nota:** É necessária uma ligação ativa à internet para todas as funcionalidades de IA. Documentos de várias páginas são processados automaticamente.

## 4. Suporte e Comunidade

Mantenha-se atualizado com as últimas notícias, funcionalidades e lançamentos:

- **Canal no Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **GitHub Issues:** Para relatórios de erros e pedidos de novas funcionalidades.

## 5. Apoiantes do Projeto

Um agradecimento sincero aos membros da nossa comunidade que apoiam o desenvolvimento contínuo e a manutenção deste projeto através das suas generosas contribuições financeiras:

- **@Alyabani94**

_Se desejar apoiar o projeto financeiramente e ver o seu nome aqui, pode encontrar a opção **Doar** no menu Ferramentas do NVDA (sub-menu Vision Assistant) ou durante o processo de configuração após a instalação._

## Alterações para a versão 5.6

- **Adicionado Motor de OCR "Nenhum (Extrair Camada de Texto)"**: Os utilizadores podem agora extrair texto diretamente de PDFs pesquisáveis sem utilizar créditos de IA, melhorando significativamente a velocidade e a privacidade para documentos baseados em texto.
- **Refinada a Precisão do Explorador de UI**: Melhorado o prompt do Explorador de UI para identificar melhor os tipos de elementos (como Itens de Lista) e reportar com precisão estados como "(Marcado)", "(Selecionado)" ou "(Expandido)", ignorando componentes do sistema Windows como a Barra de Tarefas e o Relógio.
- **Lembrete de Configuração de Instalação**: Adicionada uma notificação após a instalação para guiar os utilizadores ao menu de definições para configurar as suas chaves de API e preferências.

## Alterações para a versão 5.5.2

- **Corrigido Problema de Escrita do Operador de IA:** Resolvido um erro onde a letra 'v' era escrita em vez de colar o texto em certos sistemas. Esta correção aborda conflitos de tempo que ocorriam durante alta carga do sistema.
- **Estabilidade Melhorada:** Adicionado tratamento robusto de erros para operações de área de transferência para evitar falhas do extra quando a área de transferência do sistema está temporariamente bloqueada por outras aplicações.
- **Otimização de Tempo:** Ajustados os atrasos internos para eventos de teclado para garantir maior fiabilidade em diferentes velocidades de sistema e melhor compatibilidade com gestores de área de transferência de terceiros.

## Alterações para a versão 5.5 (A Atualização de Automação)

- **Operador de IA (Controlo Autónomo - Shift+A):** Esta é a joia da coroa da v5.5. O Vision Assistant Pro deixou de ser um assistente passivo para se tornar o seu **Operador de IA** pessoal. Não se limita a descrever o ecrã — ele assume o comando.
  - _Como funciona:_ Pode agora dar instruções verbais para operar o seu PC. Por exemplo, numa aplicação completamente inacessível onde o seu leitor de ecrã permanece mudo, pode premir **Shift+A** e escrever: _"Clica no botão Definições"_ ou _"Procura o campo de pesquisa, escreve 'Últimas Notícias' e prime enter."_ A IA identifica visualmente os elementos, move o rato e executa a tarefa por si.
  - _Nota de Desempenho:_ Esta funcionalidade está otimizada para o **Gemini 3.0 Flash (Preview)**, fornecendo respostas incrivelmente rápidas e inteligentes que conseguem lidar até com os esquemas de UI mais complexos.
  - **⚠️ Aviso de Utilização de API:** Como o Operador de IA precisa de "ver" exatamente o que está a acontecer para ser preciso, envia uma captura de ecrã de alta resolução a cada passo. Note que a utilização frequente consumirá a sua cota de API muito mais depressa do que tarefas padrão baseadas em texto.
- **Explorador de UI Visual (E):** Cansado de navegar por "botões sem etiqueta"? Prima **E** para ativar o Explorador de UI. A IA analisará toda a janela e gerará uma lista de todos os elementos clicáveis que encontrar — incluindo ícones, gráficos e menus. Basta escolher um item da lista e o Operador de IA clicará nele por si. É como ter uma "camada acessível" sobre qualquer app.
- **Ação de Ficheiro Inteligente Contextual (F):** A tecla "F" foi completamente remodelada. Já não assume que deseja apenas OCR. Ao selecionar uma única imagem, pergunta agora inteligentemente a sua intenção: pode escolher uma **Descrição Visual Detalhada** para compreender a cena ou uma **Extração de Texto Estruturada (OCR)** para leitura. O menu adapta-se dinamicamente com base no tipo de ficheiro e no seu motor de IA ativo.
- **Otimização do Núcleo:** Realizámos uma limpeza profunda na lógica interna do extra, removendo funções legadas não utilizadas e código redundante. Isto resulta numa experiência mais leve, rápida e fiável para todos os utilizadores.

## Alterações para a versão 5.0

- **Arquitetura Multi-Fornecedor**: Adicionado suporte total para **OpenAI**, **Groq** e **Mistral** a par do Google Gemini. Os utilizadores podem agora escolher o seu backend de IA preferido.
- **Encaminhamento Avançado de Modelos**: Utilizadores de fornecedores nativos (Gemini, OpenAI, etc.) podem agora selecionar modelos específicos de uma lista pendente para diferentes tarefas (OCR, STT, TTS).
- **Configuração Avançada de Endpoint**: Utilizadores de fornecedores personalizados podem inserir manualmente URLs e nomes de modelos específicos para controlo granular sobre servidores locais ou de terceiros.
- **Visibilidade Inteligente de Funcionalidades**: O menu de definições e a UI do Leitor de Documentos agora ocultam automaticamente funcionalidades não suportadas (como TTS) com base no fornecedor selecionado.
- **Obtenção Dinâmica de Modelos**: O extra obtém agora a lista de modelos disponíveis diretamente da API do fornecedor, garantindo compatibilidade com novos modelos assim que forem lançados.
- **OCR e Tradução Híbridos**: Otimizada a lógica para utilizar o Google Tradutor para velocidade ao usar o OCR do Chrome, e tradução via IA ao usar os motores Gemini/Groq/OpenAI.
- **"Re-examinar com IA" Universal**: A funcionalidade de re-exame do Leitor de Documentos já não está limitada ao Gemini. Agora utiliza qualquer fornecedor de IA que esteja ativo no momento para re-processar as páginas.

## Alterações para a versão 4.6

- **Recuperação Interativa de Resultados:** Adicionada a tecla **Espaço** à camada de comandos, permitindo que os utilizadores reabram instantaneamente a última resposta da IA numa janela de chat para perguntas de acompanhamento, mesmo quando o modo "Saída Direta" está ativo.
- **Hub da Comunidade no Telegram:** Adicionado um link para o "Canal Oficial no Telegram" no menu Ferramentas do NVDA, fornecendo uma forma rápida de se manter atualizado com as últimas notícias, funcionalidades e lançamentos.
- **Estabilidade de Resposta Melhorada:** Otimizada a lógica central para as funcionalidades de Tradução, OCR e Visão para garantir um desempenho mais fiável e uma experiência mais fluida ao utilizar a saída de fala direta.
- **Orientação de Interface Melhorada:** Atualizadas as descrições de definições e documentação para explicar melhor o novo sistema de recuperação e como funciona em conjunto com as definições de saída direta.

## Alterações para a versão 4.5

- **Gestor de Prompts Avançado:** Introduzido um diálogo de gestão dedicado nas definições para personalizar prompts padrão do sistema e gerir prompts definidos pelo utilizador com suporte total para adicionar, editar, reordenar e pré-visualizar.
- **Suporte Abrangente a Proxy:** Resolvidos problemas de conetividade de rede garantindo que as definições de proxy definidas pelo utilizador sejam aplicadas estritamente a todos os pedidos de API, incluindo tradução, OCR e geração de fala.
- **Migração Automática de Dados:** Integrado um sistema de migração inteligente para atualizar automaticamente as configurações de prompts legadas para um formato JSON v2 robusto na primeira execução, sem perda de dados.
- **Compatibilidade Atualizada (2025.1):** Definida a versão mínima necessária do NVDA como 2025.1 devido a dependências de biblioteca em funcionalidades avançadas como o Leitor de Documentos para garantir um desempenho estável.
- **Interface de Definições Otimizada:** Simplificada a interface de definições reorganizando a gestão de prompts num diálogo separado, proporcionando uma experiência de utilizador mais limpa e acessível.
- **Guia de Variáveis de Prompt:** Adicionado um guia integrado dentro dos diálogos de prompt para ajudar os utilizadores a identificar e utilizar facilmente variáveis dinâmicas como [selection], [clipboard] e [screen_obj].

## Alterações para a versão 4.0.3

- **Resiliência de Rede Melhorada:** Adicionado um mecanismo de repetição automática para lidar melhor com ligações de internet instáveis e erros temporários de servidor, garantindo respostas de IA mais fiáveis.
- **Diálogo de Tradução Visual:** Introduzida uma janela dedicada para resultados de tradução. Os utilizadores podem agora navegar facilmente e ler traduções longas linha a linha, de forma semelhante aos resultados de OCR.
- **Visualização Formatada Agregada:** A funcionalidade "Visualizar Formatado" no Leitor de Documentos apresenta agora todas as páginas processadas numa única janela organizada com cabeçalhos de página claros.
- **Fluxo de Trabalho de OCR Otimizado:** Salta automaticamente a seleção de intervalo de páginas para documentos de página única, tornando o processo de reconhecimento mais rápido e fluido.
- **Estabilidade de API Melhorada:** Mudança para um método de autenticação baseado em cabeçalho mais robusto, resolvendo possíveis erros de "Todas as Chaves de API falharam" causados por conflitos de rotação de chaves.
- **Correções de Erros:** Resolvidos vários bloqueios potenciais, incluindo um problema durante o encerramento do extra e um erro de foco no diálogo de chat.

## Alterações para a versão 4.0.1

- **Leitor de Documentos Avançado:** Um novo e poderoso visualizador para PDF e imagens com seleção de intervalo de páginas, processamento em segundo plano e navegação contínua com `Ctrl+PageUp/Down`.
- **Novo Submenu de Ferramentas:** Adicionado um submenu dedicado "Vision Assistant" sob o menu Ferramentas do NVDA para acesso mais rápido às funcionalidades principais, definições e documentação.
- **Personalização Flexível:** Pode agora escolher o seu motor de OCR preferido e voz de TTS diretamente no painel de definições.
- **Suporte a Múltiplas Chaves de API:** Adicionado suporte para várias chaves de API do Gemini. Pode inserir uma chave por linha ou separá-las por vírgulas nas definições.
- **Motor de OCR Alternativo:** Introduzido um novo motor de OCR para garantir o reconhecimento de texto fiável mesmo ao atingir os limites de cota da API do Gemini.
- **Rotação Inteligente de Chaves de API:** Alterna automaticamente e lembra a chave de API que funciona mais depressa para contornar limites de cota.
- **Documento para MP3/WAV:** Capacidade integrada de gerar e guardar ficheiros de áudio de alta qualidade nos formatos MP3 (128kbps) e WAV diretamente no leitor.
- **Suporte a Stories do Instagram:** Adicionada a capacidade de descrever e analisar Stories do Instagram utilizando os seus URLs.
- **Suporte ao TikTok:** Introduzido suporte para vídeos do TikTok, permitindo descrição visual completa e transcrição de áudio dos clipes.
- **Diálogo de Atualização Redesenhado:** Apresenta uma nova interface acessível com uma caixa de texto rolável para ler claramente as mudanças de versão antes de instalar.
- **Estado e UX Unificados:** Padronização dos diálogos de ficheiros em todo o extra e aprimoramento do comando 'L' para reportar o progresso em tempo real.

## Alterações para a versão 3.6.0

- **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) dentro da Camada de Comandos para fornecer uma lista de fácil acesso de todos os atalhos e respetivas funções.
- **Análise de Vídeo Online:** Suporte expandido para incluir vídeos do **Twitter (X)**. Também melhorada a deteção de URL e estabilidade para uma experiência mais fiável.
- **Contribuição para o Projeto:** Adicionado um diálogo de doação opcional para utilizadores que desejem apoiar as futuras atualizações e o crescimento contínuo do projeto.

## Alterações para a versão 3.5.0

- **Camada de Comandos:** Introduzido um sistema de Camada de Comandos (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestra. Por exemplo, em vez de premir `NVDA+Control+Shift+T` para tradução, agora prime `NVDA+Shift+V` seguido de `T`.
- **Análise de Vídeo Online:** Adicionado um novo recurso para analisar vídeos do YouTube e Instagram diretamente fornecendo um URL.

## Alterações para a versão 3.1.0

- **Modo de Saída Direta:** Adicionada uma opção para saltar o diálogo de chat e ouvir as respostas da IA diretamente via fala para uma experiência mais rápida e integrada.
- **Integração com Área de Transferência:** Adicionada uma nova definição para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações para a versão 3.0

- **Novos Idiomas:** Adicionadas traduções para **Persa** e **Vietnamita**.
- **Modelos de IA Expandidos:** Reorganizada a lista de seleção de modelos com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`) para ajudar os utilizadores a distinguir entre modelos gratuitos e com limite de taxa (pagos). Adicionado suporte para **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
- **Estabilidade de Ditado:** Estabilidade do Ditado Inteligente significativamente melhorada. Adicionada uma verificação de segurança para ignorar clipes de áudio menores que 1 segundo, evitando alucinações da IA e erros vazios.
- **Manuseio de Ficheiros:** Corrigido um problema onde o envio de ficheiros com nomes não em inglês falhava.
- **Otimização de Prompt:** Melhorada a lógica de Tradução e resultados de Visão estruturados.

## Alterações para a versão 2.9

- **Adicionadas traduções para Francês e Turco.**
- **Visualização Formatada:** Adicionado um botão "Visualizar Formatado" nos diálogos de chat para ver a conversa com estilização adequada (Cabeçalhos, Negrito, Código) numa janela de navegação padrão.
- **Configuração de Markdown:** Adicionada uma nova opção "Limpar Markdown no Chat" nas Definições. Desmarcar isto permite que os utilizadores vejam a sintaxe Markdown bruta (ex: `**`, `#`) na janela de chat.
- **Gestão de Diálogos:** Corrigido um problema onde as janelas de "Refinar Texto" ou chat abriam várias vezes ou falhavam ao focar corretamente.
- **Melhorias de UX:** Padronização dos títulos dos diálogos de ficheiro para "Abrir" e remoção de anúncios de voz redundantes (ex: "A abrir menu...") para uma experiência mais fluida.

## Alterações para a versão 2.8

- Adicionada tradução para Italiano.
- **Relatório de Estado:** Adicionado um novo comando (NVDA+Control+Shift+I) para anunciar o estado atual do extra (ex: "A enviar...", "A analisar...").
- **Exportação HTML:** O botão "Guardar Conteúdo" nos diálogos de resultado agora guarda a saída como um ficheiro HTML formatado, preservando estilos como cabeçalhos e negrito.
- **UI de Definições:** Melhorado o esquema do painel de Definições com agrupamento acessível.
- **Novos Modelos:** Adicionado suporte para gemini-flash-latest e gemini-flash-lite-latest.
- **Idiomas:** Adicionado Nepalês aos idiomas suportados.
- **Lógica do Menu Refinar:** Corrigido um erro crítico onde os comandos de "Refinar Texto" falhavam se o idioma da interface do NVDA não fosse Inglês.
- **Ditado:** Melhorada a deteção de silêncio para evitar saída de texto incorreta quando nenhuma fala é introduzida.
- **Definições de Atualização:** "Verificar atualizações ao iniciar" agora está desativado por padrão para cumprir as políticas da Add-on Store.
- Limpeza de código.

## Alterações para a versão 2.7

- Migração da estrutura do projeto para o Modelo de Extra oficial da NV Access para melhor conformidade com os padrões.
- Implementada lógica de repetição automática para erros HTTP 429 (Limite de Taxa) para garantir fiabilidade durante alto tráfego.
- Otimização dos prompts de tradução para maior precisão e melhor manuseio da lógica "Smart Swap".
- Atualização da tradução para Russo.

## Alterações para a versão 2.6

- Adicionado suporte à tradução para Russo (Obrigado ao nvda-ru).
- Atualizadas mensagens de erro para fornecer feedback mais descritivo sobre conetividade.
- Alterado o idioma de destino padrão para Inglês.

## Alterações para a versão 2.5

- Adicionado Comando de OCR Nativo de Ficheiro (NVDA+Control+Shift+F).
- Adicionado botão "Guardar Chat" aos diálogos de resultado.
- Implementado suporte total à localização (i18n).
- Migração do feedback de áudio para o módulo de tons nativos do NVDA.
- Mudança para a API de Ficheiros do Gemini para melhor manuseio de PDF e ficheiros de áudio.
- Correção de erro ao traduzir texto contendo chavetas.

## Alterações para a versão 2.1.1

- Corrigido um problema onde a variável [file_ocr] não funcionava corretamente dentro dos Prompts Personalizados.

## Alterações para a versão 2.1

- Padronização de todos os atalhos para usar NVDA+Control+Shift para eliminar conflitos com o esquema de Portátil do NVDA e teclas de atalho do sistema.

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
- Correção de erros COMError em aplicações específicas como Firefox e Word.
- Adicionado mecanismo de repetição automática para erros de servidor.

## Alterações para a versão 1.0

- Lançamento inicial.
