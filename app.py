from flask import Flask, jsonify
from flask_pymongo import MongoClient
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

client = MongoClient('localhost', 27017)
db = client['Players']

class PlayerAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('is_active', type=bool, location='json')

    def post(self):
        args = self.reqparse.parse_args()
        db.Players.insert(args)

    def get(self, id):
        cursor = db.Players.find_one({'id': id})
        player = {'name': cursor['name'], 'position': cursor['position']}
        return player

    def put(self, id):
        args = self.reqparse.parse_args()
        db.Players.update({'id': id}, {'$set': args})

    def delete(self, id):
        db.Players.delete_many({'id': id})

api.add_resource(PlayerAPI, '/api/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)