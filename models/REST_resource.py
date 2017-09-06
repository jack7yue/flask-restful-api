from flask import abort
from flask_restful import Resource, reqparse
from models import doa


reqparse = reqparse.RequestParser()
reqparse.add_argument('id', type=int, location='json', required=True)
reqparse.add_argument('name', type=str, location='json', required=True)
reqparse.add_argument('position', type=str, location='json', required=True)


class PlayerAPI(Resource):
    def get(self, id):
        player = doa.get_player(id)

        if not player:
            abort(400, "No player with id %d exists" % id)

        return player

    def put(self, id):
        args = reqparse.parse_args()
        doa.update_player(id, args)
        return args

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
        return args
