from sanic import Sanic
from sanic.response import json

def configure_app():
    app = Sanic('api-web-crawler')

    @app.get('/v1')
    async def index(request):
        args: dict = request.json
        urls: list = args['urls']
        word: str = args['word']
        
        response_object: dict = {
            'url': '',
            'number_of_repetitions':''
        }

        return json(
            {
                "crawler_results": response_object
            },
            headers={'Api-Web-Crawler-Served-By':'Sanic'},
            status=200,
        )
    
    return app