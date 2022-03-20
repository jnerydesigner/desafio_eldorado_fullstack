# Desafio - Criar uma Aplicação Web para gerenciar a execução de atividades

Você deve utilizar React para criação do front-end, Python+Flask para a criação da API do back-end, 
e banco de dados MySql para a persistência dos dados.

## Descrição do projeto

Todos os dias clientes de uma oficina deixam seus carros para fazer diversos tipos de manutenção.
As manutenções podem levar algumas horas ou até meses para serem concluídas de acordo com a gravidade do problema.

Por ter uma rotatividade muito grande os funcionários do atendimento não conseguem responder aos clientes de uma forma rápida qual a previsão de quando o automóvel estará pronto.

Por isso os donos da oficina decidiram investir em um sistema em que os mecânicos pudessem informar a equipe de atendimento que tipos de serviços serão necessários para realizar a manutenção completa 
do veículo e qual a tempo previsto para cada uma dessas atividades.

Assim a equipe de atendimento poderia dizer ao cliente o estado atual da manutenção, quais serviços já foram concluídos e quanto tempo mais precisa para ser finalizado.


## Requisitos:

- Uma manutenção pode ser um serviço (ex.: troca de óleo) ou pode ter uma lista de serviços (ex.: Revisão de 60 mil Km: - Troca de óleo, Troca da correia, alinhamento e balanceamento) 
- É necessário que um funcionário possa cadastrar, editar e excluir uma manutenção
- É necessário que um funcionário possa alterar o estado de um serviço (não iniciado, em andamento e
 concluído)
- É necessário que a aplicação mostre todos os serviço que não foram concluídos e o tempo 
estimado em dias, horas e minutos, para a conclusão de cada serviço.
- É importante que um funcionário possa filtrar os serviços por seu estado, concluído, em andamento ou 
não iniciado.
- É interessante que um funcionário possa filtrar os serviços de uma manutenção pela placa de um veículo
- É interessante que os serviços possam ser exibidos no painel agrupados pelo tempo previsto de conclusão (nesta semana, semana que vem, neste mês, próximos meses)


Abaixo estão os requisitos de tecnologias a serem utilizadas. Observe que apenas alguns itens são obrigatórios. Tenha isso em mente ao decidir quais itens irá implementar com o tempo que terá para entregar o desafio.

* Front-end:
    * React (Obrigatório)
    * Se preferir, pode utilizar libs UI, como material-ui por exemplo.
    * Implementação de testes unitários é opcional mas será bem visto.
    * Usar Typescript é opcional.

* Back-end:
    * Flask para a criação dos endpoints (Obrigatório)
    * Se preferir, pode utilizar libs ORM, como SQLAlchemy por exemplo.
    * Implementação de testes unitários é opcional mas será bem visto.

* Banco de dados:
    * MySQL (Obrigatório, apenas por questões de compatibilidade e facilidade de avaliação).
    * Configurar as stacks utilizando docker-compose é opcional mas será muito bem visto.


## O que deve ser entregue:

Ao final do prazo deve ser entregue um link para um repositório no github, para que possamos ver seu progresso no desenvolvimento do desafio, o nome do branch (caso use mais de um) com o código totalmente funcional a ser avaliado, e instruções de como inicializar e acessar a aplicação. Para reduzir as chances de incompatibilidade, recomendamos que fixe as versões das libs e ferramentas usadas nos seus respectivos arquivos de dependências, e também informe as versões das linguagens, ferramentas, libs e serviços utilizados no arquivo de documentação.

Nesse repositório deve conter:

* Os códigos do front-end.
* Os códigos do back-end.
* Arquivo de documentação contendo instruções para build e execução do código:
    * Por exemplo: passo a passo com os comandos para instalação de dependências, compilação do front-end e back-end, configuração do banco, configurações de acesso, criação das tabelas, comando para a execução dos serviços, etc.
* `docker-compose.yml` se utilizado.

## Como será avaliado:

O código enviado será avaliado de acordo com os seguintes critérios. (A ordem não necessariamente implica grau de importância, mas vale observar que para testarmos as funcionalidades, o código precisa ser funcional):

* Código funcional (configuração, build e execução).
* Atende os requisitos do desafio.
* Qualidade do código e do repositório (clareza, limpeza, organização, comentários de código, boas práticas).
* Documentação.
* Usabilidade (Facilidade de encontrar e utilizar as funcionalidades).

## Considerações finais:
Sinta-se livre para escolher a IDE e as ferramentas que irá utilizar no desenvolvimento. O mesmo vale para a escolha do layout e cores do front-end, e também para a organização dos arquivos e códigos dos projetos.

_Bom desafio!_