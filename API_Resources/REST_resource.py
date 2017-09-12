from flask import abort
from flask_restful import Resource, request
from models.Player import PlayerData
from validation import Validator
from voluptuous.error import MultipleInvalid


class PlayerAPI(Resource):
    def get(self, player_id):
        player = self.data.find_by_id(player_id)

        if not player:
            abort(404)

        return player.fields()

    def put(self, player_id):
        payload = request.get_json()

        try:
            Validator.validate(payload)
        except MultipleInvalid as e:
            return 404, str(e)

        result = PlayerData.update_player(player_id, payload)

        if not result:
            abort(404)

        return result.fields()

    def delete(self, player_id):
        result = PlayerData.delete_player(player_id)

        if not result:
            abort(404)

        return 200


class PlayersAPI(Resource):
    def get(self):
        players = PlayerData.find_all_players()
        return_data = [player_data.fields() for player_data in players]
        return return_data

    def post(self):
        payload = request.get_json()

        try:
            Validator.validate_post(payload)
        except MultipleInvalid as e:
            return 404, str(e)

        new_player = PlayerData.insert_player(payload)
        return 201, new_player

    def put(self):
        return 405

    def delete(self):
        return 405
