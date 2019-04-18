from sanic import Sanic
from sanic.response import json
from crawler import crawling

def configure_app():
    app = Sanic('api-web-crawler')

    @app.get('/v1')
    async def index(request):
        args: dict = request.json
        urls: list = args['urls']
        word: str = args['word']

        response_objects = []
        for url in urls:
            response_object: dict = crawling.crawler(url, word)
            response_objects.append(response_object)
        
        return json(
            {
                "crawler_results": response_objects
            },
            headers={'Api-Web-Crawler-Served-By':'Sanic'},
            status=200,
        )
    
    return app