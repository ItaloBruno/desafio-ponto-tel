# Desafio Ponto Tel

Este projeto foi criado para a participação no processo seletivo da Empresa Ponto Tel. O Desafio consiste na criação de uma API, escrita em python 3.7, que receba os seguintes parâmetros:

+ Uma lista de URLs
+ Uma palavra qualquer

A API deve ser capaz de fazer um crawler no site informado e retornar uma resposta contendo um json com a quantidade de ocorrências da palavra informada, por site.

---
## Dependências

Para este desafio foram utilizadas as seguintes dependências:

+ [Python 3.7](https://www.python.org/)
    - É uma das versões mais novas desta linguagem.
+ [Framework Web Sanic](https://sanic.readthedocs.io/en/latest/index.html)
    - Muito semelhante ao Flask e que suporta manipuladores de solicitação assíncrona, além de ter uma boa documentação.
+ [AIOHTTP](https://github.com/aio-libs/aiohttp)
    - Fazer a coleta do HTML de uma determinada url de forma assíncrona, assim aumentando a performance da API.
+ [Html2text](https://github.com/Alir3z4/html2text)
    - Possibilita fazer a coleta dos dados que estão contidos nas tags HTML de um determinado site.
+ [Validators](https://validators.readthedocs.io/en/latest/)
    - Realizar a validação das urls recebidas pela API.
<!-- + [Pytest](https://docs.pytest.org/en/latest/)
    - Realização dos testes de nossa API.
+ [Swagger Editor](https://swagger.io/)
    - Software que possibilita projetar, descrever e documentar  APIs. -->

---
## Criação do ambiente e Execução

Tem duas maneiras possíveis para a execução deste projeto:

### 1.  Utilizando Python 3.7 instalado em seu computador

Primeiramente verifique se o Python 3.7 está instalado em seu sistema. Caso não esteja, procure mais informações de como realizar a sua instalação entrando no site oficial do [Python](https://www.python.org/).

Após feita a verificação, é preciso fazer a instalação das dependências do projeto. Para isso, abra uma instância do seu terminal favorito e execute o comando abaixo:

` pip3 install -r requirements/dev.txt `

Isso fará com que o ambiente de desenvolvimento da aplicação seja instalado em seu computador.

Para a execução do projeto, execute o seguinte comando:

` python3 run.py `

---
## Dificuldades encontradas

+ Encontrar uma maneira de fazer a coleta dos dados presentes entre as tags HTML, fazendo isso de um modo em que fosse independente de como a página é estruturada.

+ Entender o funcionamento da biblioteca Asyncio do python, pois nunca estudei/trabalhei com alguma aplicação que usasse o conceito de programação assíncrona.

+ Encontrar um Framework Web Python que fosse assíncrono e tivesse uma documentação simples, além de ser fácil de utilizar.
