# Prototipação de tela

__Objetivo:__ criar versao 1.0 dos protótipos de tela do produto. Essas telas devem colaborar para a construção da arquitetura (modelos UML) de diferentes requisitos do software.

A arquitetura pode ser construída seguindo alguns destes exemplos:

- Modelos de classes (diagramas de classes, diagramas de colaboração)
- Modelos baseados em cenários (casos de uso, histórias de usuários)
- Modelos comportamentais (diagramas de estados, diagramas de sequência)
- Modelos de fluxo (DFDs, modelos de dados)


## 1. Requisitos de tela

A prototipação deve ser feita seguindo os requisitos e cenários descritos pelos Stakeholders (cliente principal, equipe de desenvolvimento, equipe de marketing e equipe de segurança), tornando a implementação destes mais intuitiva no que seja possível.

### 1.1 Tela Inicial / Página do produto

Visando a expansão do sistema para novos clientes, uma página web dedicada a ter informações sobre o sistema de E-mail Marketing deve ser criada. Esta página será a principal fonte de informação que potenciais clientes. Porém, para direcionar os esforços na implementação do produto do cliente atual, a página inicial será redirecionada diretamente para uma página de login.

### 1.2. Tela de login

Está tela redireciona o usuário para a tela principal de usuário cadastrados.

### 1.3. Tela principal para usuários cadastrados

Está tela deve ter acesso facilitado a todas as funcionalidades permitidas a um usuário.

No menu principal haverá links para as seguintes páginas:
- Campanhas
- Conteúdo de marketing
- Relatórios
- Lista de contatos
- Configurações
- Ajuda

### 1.4 Campanhas

Menu lateral:
* Ver Campanhas
* Nova Campanha
* Campanhas Realizadas
* Campanhas em Andamento

Está página começa na Tela "Ver Campanhas". Está função permite enxergar uma tabela com informações de todas as campanhas existentes na empresa, por ordem de "Data Início". A tabela mostra vinte linhas por vez. Se possível, a página deve aceitar filtros no formato de Query.

Ao dar um duplo clique em alguma linha da tabela, uma janela (_pop-up_) deve aparecer com informações especificas sobre a campanha. Deve ser possível:

1. Enviar campanha para uma nova lista de contatos;
    - Esse passo redireciona a página para a Tela "Nova Campanha", preenchendo automaticamente alguns dados do formulário.
2. Encerrar ou Pausar / Reiniciar coleta de dados da campanha;
3. Alterar lista de usuários com permissão de edição

Em "Nova Campanha", é possível inserir os dados necessários para iniciar uma nova campanha. "Campanhas Realizadas" e "Campanhas em Andamento" são atalhos para as respectivos filtros.

### 1.5 Conteúdo de Marketing

Menu lateral:
* Ver conteúdos
* Adicionar novo conteúdo

Nesta página deve ser possível visualizar todos os conteúdos de marketing gerados e adicionar novos. Deve ser possível segmentar os conteúdos de acordo com o assunto.

### 1.6 Relatórios

Menu lateral:
* Ver relatórios
* Novo relatório
    * Gerar gráficos a partir de métricas e informações
    * Upload / download de arquivo

Nesta página deve ser possível acessar relatórios criados, gerar novos ou fazer upload de material externo. Relatórios podem ser marcados com "LOCK", indicando que ele não deve mais ser editado até que alguém com permissão desmarque esta opção.

Relatório são compostos por:
- Metadados de uma ou mais campanhas;
- Métricas de uma ou mais campanhas;
- Comentários dos responsáveis.

Deve ser possível dar avaliar relatórios com comentários. Estes, devem ser mostrados via _pop-up_.

### 1.7 Lista de contatos

Menu lateral:
- Ver Lista
- Métricas da Lista
- Gerenciar Lista

Nesta página deve ser possível ver a lista de contatos, métricas e gerencimento da lista. Ações de "Adição/Exclusão/Edição" de contatos pode ser feita por qualquer usuário por meio de uma solicitação. Entretanto, apenas usuários ADMIN podem aceitar essas solicitações. O mesmo usuário ADMIN não podem enviar e aceitar uma solicitação.

Adição deve ser feita a partir de um arquivo .csv, o sistema deve verificar se o arquivo contém todos os dados necessários para que a solicitação possa ser enviada.

### 1.8 Configurações

Menu lateral:
- Perfil do usuário
- Gerenciar acessos

Nesta página o usuário tem acesso a suas informações pessoais cadastradas. Edições são enviadas por meio de solicitações, que devem ser avaliadas por um usuário ADMIN. O mesmo usuário ADMIN não podem enviar e aceitar uma solicitação.

A opção "Gerenciar Acessos" só é visível para usuários ADMIN

### 1.9 Ajuda

Menu lateral:
- Sobre a ferramenta
- Guia sobre Campanhas
- Guia sobre Conteúdos de Marketing
- Guia sobre Relatórios
- Guia sobre Lista de Contatos
- Guia sobre Configurações

Nesta página deve estar a documentação da ferramenta, assim como guias de boas práticas ensinando como utilizar cada uma das funcionalidades do sistema.

## 2. Considerações Finais

Esta material foi criado para auxiliar na criação do sistema. Qualquer atualização no layout do sistema deve ser mantida aqui, como forma de auxiliar os profissionais que venham a utilizar a ferramenta.

A seguir, estaram algumas explicações sobre os motivos do padrão atual do layout:

- Edições só podem ser autorizadas por usuários ADMIN: isso foi criado para dificultar que ações indevidas aconteçam. Usuários ADMIN são responsabilizados diretamente por qualquer danificação proposital ou não que venha a acontecer com os dados da empresa, seus funcionários e seus clientes.