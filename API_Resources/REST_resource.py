from flask import abort
from flask_restful import Resource, reqparse
from models import dao
from models.Player import PlayerData


class PlayerAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('_id', type=int, location='json', required=False)
        self.reqparse.add_argument('team', type=str, location='json', required=True)
        self.reqparse.add_argument('name', type=str, location='json', required=True)
        self.reqparse.add_argument('position', type=str, location='json', required=True)

        self.data = PlayerData()

    def get(self, player_id):
        player = self.data.find_by_id(player_id)

        if not player:
            abort(404, "No player with id %d exists" % id)

        return player.json()

    def put(self, player_id):
        args = self.reqparse.parse_args()
        self.data.update(player_id, args)
        return 200

    def delete(self, player_id):
        result = dao.delete_player(player_id)

        if not result:
            abort(404, "No player with id %d exists" % id)

        return 200


class PlayersAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('_id', type=int, location='json', required=False)
        self.reqparse.add_argument('team', type=str, location='json', required=True)
        self.reqparse.add_argument('name', type=str, location='json', required=True)
        self.reqparse.add_argument('position', type=str, location='json', required=True)

    def get(self):
        players = PlayerData.find_all_players()
        return [player_data.json() for player_data in players]

    def post(self):
        args = self.reqparse.parse_args()
        PlayerData.update_player(args)
        return 201
