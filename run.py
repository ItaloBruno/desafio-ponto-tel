from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        data = {
            'teste':'passou'
        }
        return jsonify(data)

api.add_resource(Home, '/')