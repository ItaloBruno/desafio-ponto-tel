from api import api
import json

app = api.create_app()

def test_post_response():
    data: dict = {
        'urls':['https://www.getpostman.com/', 'https://www.python.org/', 'https://swagger.io/'],
	    'word': 'Python'
        }
    request, response = app.test_client.post('/v1/crawler', data=json.dumps(data))
    res: dict = response.json

    response_mock: dict = {
        'crawler_results': [
            {
                'url': 'https://www.getpostman.com/',
                'number_of_repititions': 0,
                'status': True,
            },
            {
                'url': 'https://www.python.org/',
                'number_of_repititions': 66,
                'status': True,
            },
            {
                'url': 'https://swagger.io/',
                'number_of_repititions': 0,
                'status': True,
            }
        ]
    }

    assert res['crawler_results'] == response_mock['crawler_results']

def test_post_status_code_200():
    data: dict = {
        'urls':['https://www.getpostman.com/', 'https://www.python.org/', 'https://swagger.io/'],
	    'word': 'Python'
        }
    request, response = app.test_client.post('/v1/crawler', data=json.dumps(data))
    
    assert response.status == 200

def test_post_status_code_400():
    data: dict = {
        'urls':[100, 'https://www.python.org/', 10],
	    'word': 'Python'
        }
    request, response = app.test_client.post('/v1/crawler', data=json.dumps(data))
    
    assert response.status == 400

def test_post_data_validation():
    data: dict = {
        'urls':['https://www.getpostman.com/', 10, 10],
	    'word': True
        }
    request, response = app.test_client.post('/v1/crawler', data=json.dumps(data))
    res: dict = response.json

    response_mock: dict = {
        "erros": {
            "word": [
                "Not a valid string."
            ],
            "urls": {
                "1": [
                    "Not a valid string."
                ],
                "2": [
                    "Not a valid string."
                ]
            }
        }
    }

    assert res['erros'] == response_mock['erros']
