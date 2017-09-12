from flask import abort, jsonify
from flask_restful import Resource, reqparse
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
            abort(404)

        return jsonify(player.fields())

    def put(self, player_id):
        args = self.reqparse.parse_args()
        result = self.data.update_player(player_id, args)

        if not result:
            abort(404)

        return 200

    def delete(self, player_id):
        result = self.data.delete_player(player_id)

        if not result:
            abort(404)

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
        return_data = [player_data.fields() for player_data in players]
        return jsonify(return_data)

    def post(self):
        args = self.reqparse.parse_args()
        PlayerData.insert_player(args)
        return 201, "New player with id: $d was inserted" % args['_id']

    def put(self):
        return 405

    def delete(self):
        return 405
