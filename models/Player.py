from models.dao import PlayerDAO


class PlayerData:
    def __init__(self, data=None):
        self._id = ""
        self.name = ""
        self.position = ""
        self.team = ""

        if data:
            self._id = data['_id']
            self.name = data['name']
            self.position = data['position']
            self.team = data['team']

    def fields(self):
        return self.__dict__

    @classmethod
    def find_by_id(cls, player_id):
        dao = PlayerDAO()
        data = dao.get_player_data_by_id(player_id)
        player_data = PlayerData(data)
        return player_data

    @classmethod
    def find_all_players(cls):
        dao = PlayerDAO()
        data = dao.get_players()
        player_data = [PlayerData(player_dict) for player_dict in data]
        return player_data

    @classmethod
    def update_player(cls, player_args, player_id=None):
        dao = PlayerDAO()
        return dao.update_player(player_id if player_id else player_args['_id'], player_args)

    @classmethod
    def insert_player(cls, player_args):
        dao = PlayerDAO()
        return dao.insert_player(player_args)

    @classmethod
    def delete_player(cls, player_id):
        dao = PlayerDAO()
        return dao.delete_player(player_id)
