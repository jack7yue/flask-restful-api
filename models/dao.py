from pymongo import MongoClient
from pymongo import ReturnDocument
import json
from bson import json_util


class PlayerDAO:
    def __init__(self):
        self.client = MongoClient('mongod')
        self.Players = self.client.Players.Players
        self.Counters = self.client.Players.Counters

    PRIMARY_KEY = '_id'

    # Increment the id counter to get the next id value from mongo, Counters collection gets created if it doesn't exist
    def get_next_id(self):
        new_id = self.Counters.find_one_and_update(
            {'_id': 'userid'},
            {'$inc': {'seq': 1}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return new_id['seq']

    # Pulls a new id for new player insertion, only used for db insertions
    def data_to_collection(self, data_dict):
        player = json.dumps(data_dict, default=json_util.default)
        player[PlayerDAO.PRIMARY_KEY] = self.get_next_id()
        return player

    def get_player_data_by_id(self, player_id):
        """Returns a single document or None"""
        player = self.Players.find_one({'_id': player_id})
        return player

    def get_players(self):
        """Returns a collection of documents or None"""
        data = []
        cursors = self.Players.find()

        for cursor in cursors:
            data.append(cursor)

        return data

    def update_player(self, args, id):
        """Returns a dictionary representation of a player or None"""
        result = self.Players.update_one({'_id': id}, {'$set': args})
        new_player = None

        if result.acknowledged:
            new_player = args

        return new_player

    def insert_player(self, stats):
        """Returns a dictionary representation of a player or None"""
        player = self.data_to_collection(stats)
        result = self.Players.insert_one(player)
        new_player = None

        if result.acknowledged:
            new_player = stats

        return new_player

    def delete_player(self, id):
        """Returns a boolean on successful delete"""
        result = self.Players.delete_many({'_id': id})

        # check to see if our write operation succeeds
        return result.acknowledged
