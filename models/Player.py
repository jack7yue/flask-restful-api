from flask import abort
from flask_restful import Resource, reqparse
from models.doa import db
from models import doa


reqparse = reqparse.RequestParser()
reqparse.add_argument('id', type=int, location='json')
reqparse.add_argument('name', type=str, location='json')
reqparse.add_argument('is_active', type=bool, location='json')


class PlayerAPI(Resource):
    def get(self, id):
        player = doa.get_player(id)

        if not player:
            abort(404)

        return player


    def put(self, id):
        args = reqparse.parse_args()
        db.Players.update({'id': id}, {'$set': args})


    def delete(self, id):
        doa.delete_player(id)
        return 200


class PlayersAPI(Resource):
    def get(self):
        players = doa.get_players()
        return players

    def post(self):
        args = reqparse.parse_args()
        doa.insert_player(args)





