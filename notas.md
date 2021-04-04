## Tarefas dia 22

### Leituras

Definir arquitetura e camadas do sistema

- Estrutura de implementação
- Estilo orientado a objetos
- Genero: comunicações

diagrama de contexto arquitetural

-------------------------------------------------

Estrutura de implementação: nessa estrutura, os componentes se referem a elementos para “empacotar” funcionalidades em vários níveis de abstração, como classes, funções, métodos, objetos, etc. Os conectores se referem a como esses elementos vão se comunicar dentro do sistema, transmitindo dados de controle e instâncias de objetos e compartilhando dados. As propriedades se referem a elementos de qualidades como manutenibilidade e reusabilidade

 Arquiteturas orientadas a objetos: são sistemas baseados em classes e objetos com certo grau de encapsulamento, em que a comunicação e a coordenação ocorrem entre os objetos por meio de mensagens.

No âmbito dos estilos de arquitetura, Sommerville (2007) ainda acres-centa a arquitetura cliente-servidor, que consiste em uma arquitetura baseada em serviços, ou seja, cada cliente acessa o servidor para ter acesso aos dados e funcionalidades específicas. Muitos sistemas possuem esse tipo de arquitetura; em especial, esse tipo de arquitetura privilegia sistemas distribuído

Entre as camadas comuns em um software, temos:
 interface;  camada de negócios;  camada central


## Requisitos ## 

1. Requisitos de Campanha
	- Pegar um modelo de campanha (conteúdo de markting)
	- Lista de contatos
    - Lista de métricas
    - Data início
    - Data fim
    - Anonimizador de dados

2. Requisitos Conteúdo de Marketing
    - Documento (formato ainda não definido) em que seja possível adicionar metadados de maneira automatizada.
    - Metadados: 
        * dados do cliente (nome e outros)
        * dados da campanha

3. Requisito de Relatórios
    - Lista quais serão os formato de relatório
        * Acesso as métricas das campanhas

4. Requisitos Lista de Contatos
    - Dados do cliente
        * Nome, idade, email

5. Requisitos da Front-end
    - API
    - Programar a prototipação de telas

6. Requisitos de Banco de Dados
    - Mongodb e Sql
    - Tabela 1: Campanhas
        * Guarda informações de uma campanha em andamento
        * 

    - Tabela 2: Lista de Contatos
        * Guarda informações dos contatos
            ** Nome
            ** Telefone
            ** E-mail
            ** Campanhas que participou

    - Tabela 3: Relatórios
        * Guarda relatórios criados

    - Tabela 4: Conteúdo de Marketing
        * Guarda padrões de conteúdos de marketing
