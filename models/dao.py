from pymongo import MongoClient
from collections import defaultdict

class PlayerDAO:
    def __init__(self):
        self.client = MongoClient('mongod')
        self.Players = self.client.Players.Players

    # Collection of db fields
    KEYS = ['_id', 'name', 'position', 'team']

    # Converts PyMongo cursor to dict
    @classmethod
    def data_to_collection(cls, data_dict):
        player = defaultdict(str)

        for key in cls.KEYS:
            player[key] = data_dict[key]

        return player

    def get_player_data_by_id(self, player_id):
        cursor = self.Players.find_one({'_id': player_id})

        if not cursor:
            return False

        player = PlayerDAO.data_to_collection(cursor)
        return player

    def get_players(self):
        data = []
        cursors = self.Players.find()

        for cursor in cursors:
            data.append(PlayerDAO.data_to_collection(cursor))

        return data

    def update_player(self, args, id):
        result = self.Players.update({'_id': id}, {'$set': args})
        return result

    def insert_player(self, stats):
        player = PlayerDAO.data_to_collection(stats)
        self.Players.insert_one(player)

    def delete_player(self, id):
        result = self.Players.delete_many({'_id': id})

        # check to see if our write operation succeeds
        return result.acknowledged
