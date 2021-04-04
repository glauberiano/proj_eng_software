# Resumo sobre o sistema

Vamos desenvolver um sistema de E-mail Marketing. Ela deve ser capaz de:

- Pré-campanha:
    * Gerenciar informações sobre lista de contatos:
    * Gerenciar acessos a ferramenta
- Realizar campanhas: 
    * Enviar um conteúdo de marketing via de e-mail para um público-alvo;
    * Capturar métricas;
    * Manter histórico
- Pós-campanha;
    * Gerenciar relatórios;

## 1. Requisitos

O coleta de requisitos foi realizada a partir de entrevistas com os principais stakeholdes do projeto: dono do sistema. equipe de marketing, equipe de relacionamento com o cliente, equipe de modelagem, equipe de desenvolvimento e equipe de segurança.

Neste primeiro levantamento falaram: dono do sistema. equipe de marketing e equipe de segurança.

### 1.1 Dono do sistema

__Pergunta: porque você nos procurou? Qual problema deseja resolver?__

Tivemos um problema a última empresa que nos fornecia serviços de e-mail marketing. O sistema deles sofreu uma falha de segurança que resultou no vazamento de dados pessoais de inúmeros clientes da nossa empresa. Estamos preocupados com possíveis processos que podem chegar, porque a empresa não tratava corretamente os dados sensíveis dos clientes. Decidimos por encerrar o contrato vigente e procurar pelos meios legais para nos proteger e proteger os nossos clientes. Precisamos de outro sistema de E-mail Marketing para a nossa empresa, que nos proteja dos problemas que tivemos com o software anterior.

__Pergunta: que funcionalidades você deseja?__

- O sistema deve ser capaz de enviar um conteúdo de marketing via e-mail para a lista de e-mails selecionados do público-alvo. O retorno deve ser uma lista de métricas que são usadas pela equipe de marketing para avaliação e desenvolvimento de novas campanhas, com o intuito de melhorar o engajamento dos nossos clientes;
- O sistema deve ser capaz de enviar a campanha para diferentes segmentações da lista de contatos;
- É de extrema importância que os problemas que tivemos não voltem a ocorrem, portanto o sistema deve ser seguro contra invasões. E caso elas ocorram, o sistema deve se precaver de que quaisquer dados sensíveis existentes não serão expostos;

__Pergunta: quantas pessoas terão acesso ao sistema?__

Atualmente, quatro equipes trabalham neste tipo de sistema:

- Equipe de Marketing: responsável por captar informações dos clientes, definir estratégias de marketing, gerar conteúdo e avaliação das campanhas de marketing;
- Equipe de Relacionamento com o Cliente: responsável por captar informações sobre o processo de compra e manter o cliente ativo;
- Equipe de Modelagem: responsável por definir estratégias de marketing, geração de lista de contatos, captação de clientes e avaliação das campanhas de marketing;

Cada equipe é composta por uma gestora e cinco analistas.

### 1.2 Equipe de Marketing

__Pergunta: quais dados são necessários para enviar uma campanha de marketing?__

- Lista de contatos do público-alvo;
- Conteúdo de Marketing;
- ID funcionário criador;
- Funcionários responsáveis;

__Pergunta: quais métricas vocês utilizam para avaliar uma campanha de marketing?__

Para saber a qualidade das campanhas realizadas, necessitamos das seguintes métricas:
- Taxa de abertura de e-mail;
- Taxa de crescimento da lista de contatos;
- Taxa de inativação da lista de contatos;
- Taxa de cliques;
- Taxa de cliques por abertura;
- Leads gerados;
- Taxa de conversão;
- Eficácia da campanha no funil:
    * Taxa de Leads que se tornaram Leads qualificados;
    * Taxa de Leads que viraram oportunidades de vendas;
    * Número de clientes;
- Taxa de descadastro e marcação de spam;
- Taxa de hard bounce;

__Pergunta: a partir de quais dados vocês geram essas métricas?__

- Tamanho do público-alvo;
- Período de coleta;
- Assunto do conteúdo de marketing;
- ID do conteúdo de marketing;
- Metadados do email:
    * Abertura
    * Cliques
    * Descadastros
    * Spam

__Pergunta: quais resultados vocês esperam obter a partir dessas métricas?__

Com essas métricas conseguimos:
- Definir o melhor assunto em um teste A/B;
- Saber qual o melhor horário para iniciar uma campanha;
- Identificar o potencial atratativo da campanha.

__Pergunta: qual deve ser o formato de entrada dos dados?__

O sistema deve estar conectado com a base de contatos da empresa, e sempre que possível, estar atualizado com a mesma. O sistema deve ser capaz download/upload

### 1.3 Equipe de Segurança

__Pergunta: quantas pessoas terão acesso ao sistema?__

Inicialmente, os coordenadores das equipes de marketing, relacionamento com o cliente e modelagem. Eles adicionaram novos usuários conforma a necessidade.

__Pergunta: quais são os perfis de acesso?__

Devem existir dois tipos de usuários no sistema: ADMIN e NORMAL. Coordenadores ter permissões de ADMIN, enquanto analistas tem permissões um perfil NORMAL.

Um usuário "NORMAL" pode:
- Editar informações pessoais;
- Iniciar campanhas;
- Avaliar métricas de campanhas;

Um "ADMIN" pode:
- Adicionar, remover ou editar contas de usuários ADMIN e NORMAL
    * O sistema deve pedir por uma nova digitação da senha para confirmar EDIÇÕES e REMOÇÕES do sistema;
    * Caso o "ADMIN" sejá o único restante, ele não pode ser excluído;
- Além das mesmas funções que um usuário "NORMAL";

__Pergunta: vocês tem alguma lista inicial de quais dados sensíveis devemos nos preocupar?__

- Nome completo
- CPF, RG, CNPJ