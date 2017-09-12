from models.dao import PlayerDAO


class PlayerData:
    def __init__(self, data=None):
        self._id = None
        self.name = None
        self.team = None
        self.position = None
        self.fill_fields(data)

    def fields(self):
        return self.__dict__

    def fill_fields(self, data):
        self._id = data['_id'] if data and '_id' in data else ""
        self.name = data['name'] if data and 'name' in data else ""
        self.team = data['team'] if data and 'team' in data else ""
        self.position = data['position'] if data and 'position' in data else ""

    @classmethod
    def find_by_id(self, player_id):
        dao = PlayerDAO()
        data = dao.get_player_data_by_id(player_id)
        player_data = PlayerData(data)
        return player_data

    @classmethod
    def find_all_players(self):
        dao = PlayerDAO()
        data = dao.get_players()
        player_data = [PlayerData(player_dict) for player_dict in data]
        return player_data

    def update_player(cls, player_args, player_id=None):
        dao = PlayerDAO()
        new_player = dao.update_player(player_id if player_id else player_args['_id'], player_args)
        cls.fill_fields()

    @classmethod
    def insert_player(cls, player_args):
        dao = PlayerDAO()
        return dao.insert_player(player_args)

    @classmethod
    def delete_player(cls, player_id):
        dao = PlayerDAO()
        return dao.delete_player(player_id)
