from pymongo import MongoClient
from collections import defaultdict


class PlayerDAO:
    def __init__(self):
        self.client = MongoClient('mongod')
        self.Players = self.client.Players.Players

   PRIMARY_KEY = '_id'

    # Collection of db fields
    KEYS = ['name', 'position', 'team']

    # Converts PyMongo cursor to dict
    @classmethod
    def data_to_collection(cls, data_dict):
        player = dict([data_dict[key] for key in PlayerDAO.KEYS])

        if PRIMARY_KEY in data_dict:
            player[PRIMARY_KEY] = data_dict[PRIMARY_KEY]

        return player


    def get_player_data_by_id(self, player_id):
        cursor = self.Players.find_one({'_id': player_id})

        if not cursor:
            return None

        player = PlayerDAO.data_to_collection(cursor)
        return player

    def get_players(self):
        data = []
        cursors = self.Players.find()

        for cursor in cursors:
            data.append(PlayerDAO.data_to_collection(cursor))

        return data

    def update_player(self, args, id):
        result = self.Players.update_one({'_id': id}, {'$set': args})
        new_player = None

        if result.acknowledged:
            new_player = args

        return new_player

    def insert_player(self, stats):
        player = PlayerDAO.data_to_collection(stats)
        result = self.Players.insert_one(player)
        new_player = None

        if result.acknowledged:
            new_player = stats

        return new_player

    def delete_player(self, id):
        result = self.Players.delete_many({'_id': id})

        # check to see if our write operation succeeds
        return result.acknowledged
