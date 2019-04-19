# Desafio Ponto Tel

Este projeto foi criado para a participação no processo seletivo da Empresa Ponto Tel. O Desafio consiste na criação de uma API, escrita em python 3.7, que receba os seguintes parâmetros:

+ Uma lista de URLs
+ Uma palavra qualquer

A API deve ser capaz de fazer um crawler no site informado e retornar uma resposta contendo um json com a quantidade de ocorrências da palavra informada, por site.

---
**Endpoint API: localhost:8000/v1/crawler - Método POST**

Para mais informações acerca da documentação da API, acesse o site do [Swagger Editor](https://editor.swagger.io/) e importe o arquivo [doc_api_crawler.yaml](https://github.com/ItaloBruno/desafio-ponto-tel/blob/master/doc_api_crawler) (**Na barra superior: File -> Import File**).

---
## Dependências Utilizadas

Para este desafio foram utilizadas as seguintes dependências:

+ [Python 3.7](https://www.python.org/)
    - É uma das versões mais novas desta linguagem.
+ [Framework Web Sanic](https://sanic.readthedocs.io/en/latest/index.html)
    - Muito semelhante ao Flask e que suporta manipuladores de solicitação assíncrona, além de ter uma boa documentação.
+ [AIOHTTP](https://github.com/aio-libs/aiohttp)
    - Fazer a coleta do HTML de uma determinada url de forma assíncrona, assim aumentando a performance da API.
+ [Html2text](https://github.com/Alir3z4/html2text)
    - Possibilita fazer a coleta dos dados que estão contidos nas tags HTML de um determinado site.
+ [Marshmallow](https://github.com/marshmallow-code/marshmallow)
    - Realizar a validação do tipo dos dados vindos na requisição.
+ [Validators](https://validators.readthedocs.io/en/latest/)
    - Verificar se as urls recebidas pela API são válidas ou não.
+ [Swagger Editor](https://swagger.io/)
    - Software que possibilita projetar, descrever e documentar  APIs.
<!-- + [Pytest](https://docs.pytest.org/en/latest/)
    - Realização dos testes de nossa API. -->

---
## Criação do ambiente e Execução

Tem duas maneiras possíveis para a execução deste projeto:

### 1.  Utilizando Python 3.7 instalado em seu computador

Primeiramente verifique se o Python 3.7 está instalado em seu sistema. Caso não esteja, procure mais informações de como realizar a sua instalação entrando no site oficial do [Python](https://www.python.org/).

Com a versão correta instalada, é preciso fazer a instalação das dependências do projeto. Para isso, abra uma instância do seu terminal e execute o comando abaixo:

` pip3 install -r requirements/requiremenst.txt `

Isso fará com que o ambiente da aplicação seja instalado em seu computador.

Para a execução do projeto, execute o seguinte comando:

` python3 run.py `

Isso fará com que o servidor seja inicializado na porta **8000**, possibilitando com que a API seja acessada. Para a verificação dos resultados de resposta da API, foi utilizado o software [Postman](https://www.getpostman.com/). Segue abaixo um json de exemplo para que verificação da resposta:

```
    {
        "urls":["https://www.getpostman.com/", "https://www.python.org/", "https://swagger.io/"],
        "word": "Python"
    }
```

Utlizando o JSON exemplificado acima e o enviando no corpo da requisição HTTP para o endpoint **/v1/crawler**, usando o método **POST**, a API retorna o seguinte resultado:
```
{
    "crawler_results": [
        {
            "url": "https://www.getpostman.com/",
            "number_of_repititions": 0,
            "status": true
        },
        {
            "url": "https://www.python.org/",
            "number_of_repititions": 66,
            "status": true
        },
        {
            "url": "https://swagger.io/",
            "number_of_repititions": 0,
            "status": true
        }
    ]
}
```

### 2. Utilizando Docker

Para a execução usando docker, primeiramente verifique se está instalado em seu computador. Caso não esteja, entre no [site oficial do Docker](https://www.docker.com/) e siga as instruções para a sua instalação.

Com o docker instalado, abra o terminal e execute o seguinte comando:

` docker build -t api-crawler .`

Isso fará com que a imagem docker da aplicação seja criada, possibilitando a criação do container para execução do projeto. Para isso, execute o comando abaixo:

` docker run -d -p 8000:8000 api-crawler`

Após isso, faça os mesmos passos descritos no item anterior para efetuar o acesso a API.

Caso você tenha o [docker-compose](https://docs.docker.com/compose/) instalado em sua máquina, execute o comando a seguir e ele fará o mesmo processo descrito nos dois passos anteriores. Para isso execute:

` docker-compose up `

---
## Dificuldades encontradas

+ Encontrar uma maneira de fazer a coleta dos dados presentes entre as tags HTML, fazendo isso de um modo em que fosse independente de como a página é estruturada;

+ Entender o funcionamento da biblioteca Asyncio do python, pois nunca estudei/trabalhei com alguma aplicação que usasse o conceito de programação assíncrona;

+ Encontrar um Framework Web Python que fosse assíncrono e tivesse uma documentação boa e simples, além de ser fácil de utilizar;

+ Realizar a integração entre o módulo que realizava a operação de crawler e a API;

+ Encontrar alguma biblioteca que fizesse o processo de coleta do HTML de forma assíncrona, para aumentar o desempenho da aplicação.
