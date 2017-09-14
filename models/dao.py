from pymongo import MongoClient
from pymongo import ReturnDocument
import settings


class PlayerDAO:
    def __init__(self):
        self.client = MongoClient(settings.MONGO_SERVICE_NAME)
        self.Players = self.client.Players.Players
        self.Counters = self.client.Players.Counters

    # Increment the id counter to get the next id value from mongo, Counters collection gets created if it doesn't exist
    def get_next_id(self):
        new_id = self.Counters.find_one_and_update(
            {settings.MONGO_PRIMARY_KEY: settings.MONGO_COUNTER_NAME},
            {settings.MONGO_INCREMENT: {settings.MONGO_SEQ: 1}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return new_id['seq']

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

    def update_player(self, args):
        """Returns a dictionary representation of a player or None"""
        result = self.Players.update_one(
            {settings.MONGO_PRIMARY_KEY: args[settings.MONGO_PRIMARY_KEY]},
            {settings.MONGO_SET: args}
        )
        new_player = None

        if result.acknowledged:
            new_player = args

        return new_player

    def insert_player(self, stats):
        """Returns a dictionary representation of a player or None"""
        player = stats
        player[settings.MONGO_PRIMARY_KEY] = self.get_next_id()
        result = self.Players.insert_one(player)
        new_player = None

        if result.acknowledged:
            new_player = stats

        return new_player

    def delete_player(self, id):
        """Returns a boolean on successful delete"""
        result = self.Players.delete_many({settings.MONGO_PRIMARY_KEY: id})

        # check to see if our write operation succeeds
        return result.acknowledged
