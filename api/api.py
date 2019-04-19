from sanic import Sanic
from sanic.response import json
from marshmallow import Schema, fields
from crawler import crawling

class RequestFieldsSchema(Schema):
    word: str = fields.Str(required=True)
    urls: list = fields.List(fields.Str(), required=True)

def create_app():
    """
        Essa função é responsável por fazer a criação da nossa aplicação e configuração de rotas da API.
    """
    app = Sanic('api-web-crawler')

    @app.post('/v1/crawler')
    async def index(request):
        args: dict = request.json

        # Validação dos dados
        schema: RequestFieldsSchema = RequestFieldsSchema()
        args, erros = schema.load(args)
        if erros != {}:
            return json(
                {
                    "erros": erros
                },
                headers={'Api-Web-Crawler-Served-By':'Sanic'},
                status=400,
            )
        
        # Preparando os dados e fazendo o processo de crawling
        urls: list = args['urls']
        word: str = args['word']
        response_objects: list = await crawling.crawler(urls, word)
        
        return json(
            {
                "crawler_results": response_objects
            },
            headers={'Api-Web-Crawler-Served-By':'Sanic'},
            status=200,
        )
    
    return app