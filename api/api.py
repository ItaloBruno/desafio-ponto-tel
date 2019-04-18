from sanic import Sanic
from sanic.response import json
from crawler import crawling

def create_app():
    app = Sanic('api-web-crawler')

    @app.get('/v1')
    async def index(request):
        args: dict = request.json
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