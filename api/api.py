from sanic import Sanic
from sanic.response import json

app = Sanic('api-web-crawler')

@app.get('/v1')
async def index(request):
    args: dict = request.json
    urls: list = args['urls']
    word: str = args['word']
    
    response_object = {
        'urls': '',
        'number_of_repetitions':''
    }

    return json(
        {
            "received": True,
            "message": response_object
        },
        headers={'Api-Web-Crawler-Served-By':'Sanic'},
        status=200,
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)