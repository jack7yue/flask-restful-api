from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Resource, Api


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'flask_learning'
app.config['MONGO_URI'] = 'mongodb://user1:asd123@ds161823.mlab.com:61823/flask_learning'

api = Api(app)
db = PyMongo(app)

players = [
    {
        'id': 1,
        'name': 'Stephen Curry',
        'position': 'PG'
    },
    {
        'id': 2,
        'name': 'Lebron James',
        'position': 'SF/PF',
    },
    {
        'id': 3,
        'name': 'Kevin Durant',
        'position': 'SF',
    }
    ]


class PlayerAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(PlayerAPI, '/players/<int:id>')




