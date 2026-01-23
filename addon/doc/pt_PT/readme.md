# Documentação do Vision Assistant Pro

**Vision Assistant Pro** é um assistente de IA avançado e multimodal para o NVDA. Ele utiliza os modelos Gemini do Google para fornecer leitura inteligente de tela, tradução, ditado por voz e recursos de análise de documentos.

_Este complemento foi lançado para a comunidade em homenagem ao Dia Internacional das Pessoas com Deficiência._

## 1. Instalação e Configuração

Acesse **Menu do NVDA > Preferências > Configurações > Vision Assistant Pro**.

- **Chave de API:** Obrigatória. Você pode inserir várias chaves (separadas por vírgulas ou por novas linhas). O assistente alternará automaticamente entre elas se um limite de cota for atingido.
- **Modelo de IA:** Escolha entre os modelos **Flash** (Mais rápido/Gratuito), **Lite** ou **Pro** (Alta Inteligência).
- **URL de Proxy:** Opcional. Use isto se o Google estiver bloqueado na sua região. Deve ser um endereço web que atue como ponte para a API do Gemini.
- **Motor de OCR:** Escolha entre **Chrome (Rápido)** para resultados rápidos ou **Gemini (Formatado)** para melhor preservação de layout e reconhecimento de tabelas.
- **Voz TTS:** Selecione o estilo de voz preferido para gerar arquivos de áudio a partir das páginas de documentos.
- **Troca Inteligente:** Alterna automaticamente os idiomas se o texto de origem corresponder ao idioma de destino.
- **Saída Direta:** Ignora a janela de chat e anuncia a resposta da IA diretamente por fala.
- **Integração com a Área de Transferência:** Copia automaticamente a resposta da IA para a área de transferência.

## 2. Camada de Comandos e Atalhos

Para evitar conflitos de teclado, este complemento utiliza uma **Camada de Comandos**.

1. Pressione **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (você ouvirá um bip).
2. Solte as teclas e, em seguida, pressione uma das seguintes teclas únicas:

| Tecla         | Função                            | Descrição                                                                                 |
| ------------- | --------------------------------- | ----------------------------------------------------------------------------------------- |
| **T**         | Tradutor Inteligente              | Traduz o texto sob o cursor de navegação ou a seleção.                                    |
| **Shift + T** | Tradutor da Área de Transferência | Traduz o conteúdo atualmente na área de transferência.                                    |
| **R**         | Refinador de Texto                | Resumir, corrigir gramática, explicar ou executar **Prompts Personalizados**.             |
| **V**         | Visão de Objetos                  | Descreve o objeto atual do navegador.                                                     |
| **O**         | Visão de Tela Inteira             | Analisa todo o layout e conteúdo da tela.                                                 |
| **Shift + V** | Análise de Vídeo Online           | Analisa vídeos do **YouTube**, **Instagram** ou **Twitter (X)** via URL.                  |
| **D**         | Leitor de Documentos              | Leitor avançado para PDF e imagens com seleção de intervalo de páginas.                   |
| **F**         | OCR de Arquivo                    | Reconhecimento direto de texto a partir de imagens, PDFs ou arquivos TIFF selecionados.   |
| **A**         | Transcrição de Áudio              | Transcreve arquivos MP3, WAV ou OGG para texto.                                           |
| **C**         | Solucionador de CAPTCHA           | Captura e resolve CAPTCHAs na tela ou no objeto do navegador.                             |
| **S**         | Ditado Inteligente                | Converte fala em texto. Pressione para iniciar a gravação e novamente para parar/digitar. |
| **L**         | Relatório de Status               | Anuncia o progresso atual (ex.: "Escaneando...", "Ocioso").                               |
| **U**         | Verificação de Atualizações       | Verifica manualmente no GitHub a versão mais recente do complemento.                      |
| **H**         | Ajuda de Comandos                 | Exibe uma lista de todos os atalhos disponíveis dentro da camada de comandos.             |

### 2.1 Atalhos do Leitor de Documentos (Dentro do Visualizador)

Depois que um documento é aberto pelo comando **D**:

- **Ctrl + PageDown:** Ir para a próxima página (anuncia o número da página).
- **Ctrl + PageUp:** Ir para a página anterior (anuncia o número da página).
- **Alt + A:** Abrir um diálogo de chat para fazer perguntas sobre o documento.
- **Alt + R:** Forçar uma nova varredura da página atual ou de todas as páginas usando o motor Gemini.
- **Alt + G:** Gerar e salvar um arquivo de áudio de alta qualidade (WAV) a partir do conteúdo.
- **Alt + S / Ctrl + S:** Salvar o texto extraído como um arquivo TXT ou HTML.

## 3. Prompts Personalizados e Variáveis

Você pode criar comandos personalizados poderosos de IA nas Configurações usando o formato: `Nome:Texto do Prompt` (separe vários comandos com `|` ou novas linhas).

### Variáveis Disponíveis

| Variável        | Descrição                                    | Tipo de Entrada   |
| --------------- | -------------------------------------------- | ----------------- |
| `[selection]`   | Texto atualmente selecionado                 | Texto             |
| `[clipboard]`   | Conteúdo da área de transferência            | Texto             |
| `[screen_obj]`  | Captura de tela do objeto do navegador       | Imagem            |
| `[screen_full]` | Captura de tela da tela inteira              | Imagem            |
| `[file_ocr]`    | Selecionar imagem/PDF para extração de texto | Imagem, PDF, TIFF |
| `[file_read]`   | Selecionar documento para leitura            | TXT, Código, PDF  |
| `[file_audio]`  | Selecionar arquivo de áudio para análise     | MP3, WAV, OGG     |

### Exemplos de Prompts Personalizados

- **OCR Rápido:** `Meu OCR:[file_ocr]`
- **Traduzir Imagem:** `Traduzir Img:Extraia o texto desta imagem e traduza para o inglês. [file_ocr]`
- **Analisar Áudio:** `Resumir Áudio:Ouça esta gravação e resuma os pontos principais. [file_audio]`
- **Depurador de Código:** `Depurar:Encontre erros neste código e explique-os: [selection]`

---

**Nota:** É necessária uma conexão ativa com a internet para todos os recursos de IA. Documentos com várias páginas e arquivos TIFF são processados automaticamente.

## Alterações na versão 4.0

- **Leitor Avançado de Documentos:** Novo visualizador poderoso para PDFs e imagens, com seleção de intervalo de páginas, processamento em segundo plano e navegação fluida com `Ctrl+PageUp/Down`.

- **Novo Submenu de Ferramentas:** Adicionado um submenu dedicado "Vision Assistant" no menu Ferramentas do NVDA para acesso mais rápido aos recursos principais, configurações e documentação.
- **Personalização Flexível:** Agora é possível escolher o motor de OCR e a voz TTS preferidos diretamente no painel de configurações.
- **Suporte a Múltiplas Chaves de API:** Adicionado suporte a várias chaves de API do Gemini para garantir serviço contínuo.
- **Motor OCR Alternativo:** Introduzido um novo motor de OCR para garantir reconhecimento confiável mesmo ao atingir limites de cota da API Gemini.
- **Rotação Inteligente de Chaves de API:** Alterna automaticamente para a chave de API mais rápida disponível.
- **Documento para Áudio:** Capacidade integrada de gerar e salvar arquivos de áudio (WAV) de alta qualidade a partir de páginas de documentos.
- **Diálogo de Atualização Redesenhado:** Nova interface acessível com caixa de texto rolável para leitura clara das alterações.
- **Status Unificado e UX:** Padronização dos diálogos de arquivo e melhoria do comando `L` para relatar progresso em tempo real.

## Alterações na versão 3.6.0

- **Sistema de Ajuda:** Adicionado comando de ajuda (`H`) dentro da Camada de Comandos.

- **Análise de Vídeo Online:** Suporte expandido para vídeos do **Twitter (X)**.
- **Contribuição para o Projeto:** Adicionado diálogo opcional de doação.

## Alterações na versão 3.5.0

- **Camada de Comandos:** Introdução do sistema de Camada de Comandos (padrão: `NVDA+Shift+V`).

- **Análise de Vídeo Online:** Novo recurso para analisar vídeos do YouTube e Instagram via URL.

## Alterações na versão 3.1.0

- **Modo de Saída Direta:** Opção para ouvir respostas da IA diretamente por fala.

- **Integração com a Área de Transferência:** Cópia automática das respostas da IA.

## Alterações na versão 3.0

- **Novos Idiomas:** Adicionadas traduções para **Persa** e **Vietnamita**.

- **Modelos de IA Expandidos:** Reorganização da lista de modelos e suporte ao **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
- **Estabilidade do Ditado:** Melhorias significativas no Ditado Inteligente.
- **Manipulação de Arquivos:** Correção de falhas ao enviar arquivos com nomes não ingleses.
- **Otimização de Prompts:** Melhorias na lógica de tradução e nos resultados de visão.

## Alterações na versão 2.9

- **Adicionadas traduções em Francês e Turco.**

- **Visualização Formatada:** Botão "Ver Formatado" nos diálogos de chat.
- **Configuração de Markdown:** Opção "Limpar Markdown no Chat".
- **Gerenciamento de Diálogos:** Correções de foco e abertura múltipla.
- **Melhorias de UX:** Padronização de títulos de diálogos e remoção de anúncios redundantes.

## Alterações na versão 2.8

- Tradução para Italiano adicionada.

- **Relatório de Status:** Novo comando para anunciar o status atual.
- **Exportação HTML:** Salvamento de conteúdo formatado em HTML.
- **Interface de Configurações:** Layout melhorado com agrupamentos acessíveis.
- **Novos Modelos:** Suporte a gemini-flash-latest e gemini-flash-lite-latest.
- **Idiomas:** Adicionado Nepali.
- **Lógica do Menu Refinar:** Correção de erro crítico.
- **Ditado:** Melhoria na detecção de silêncio.
- **Configurações de Atualização:** Verificação automática desativada por padrão.
- Limpeza de código.

## Alterações na versão 2.7

- Migração da estrutura do projeto para o modelo oficial de complementos da NV Access.

- Implementação de nova lógica de repetição automática para erros HTTP 429.
- Otimização dos prompts de tradução.
- Tradução russa atualizada.

## Alterações na versão 2.6

- Adicionado suporte à tradução russa.

- Mensagens de erro mais descritivas.
- Idioma de destino padrão alterado para inglês.

## Alterações na versão 2.5

- Adicionado comando nativo de OCR de arquivos.

- Botão "Salvar Chat" nos diálogos de resultado.
- Suporte completo à localização (i18n).
- Migração do feedback de áudio para o módulo nativo de tons do NVDA.
- Uso da API de arquivos do Gemini.
- Correção de falha ao traduzir texto com chaves.

## Alterações na versão 2.1.1

- Correção de falha na variável [file_ocr] em Prompts Personalizados.

## Alterações na versão 2.1

- Padronização de todos os atalhos para NVDA+Control+Shift.

## Alterações na versão 2.0

- Sistema de atualização automática integrado.

- Cache inteligente de tradução.
- Memória de conversas.
- Comando dedicado de tradução da área de transferência.
- Otimização rigorosa dos prompts de idioma.
- Correção de falhas com caracteres especiais.

## Alterações na versão 1.5

- Suporte a mais de 20 novos idiomas.

- Diálogo interativo de refinamento.
- Ditado inteligente nativo.
- Categoria "Vision Assistant" nos gestos de entrada do NVDA.
- Correção de falhas COMError.
- Mecanismo automático de repetição para erros de servidor.

## Alterações na versão 1.0

- Lançamento inicial.
