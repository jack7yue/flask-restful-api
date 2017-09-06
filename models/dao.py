from pymongo import MongoClient


class PlayerDAO:
    def __init__(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017/')
        self.Players = self.client.Players.Players

    def get_player_data_by_id(self, player_id):
        cursor = self.Players.find_one({'_id': player_id})

        if not cursor:
            return False

        player = {'_id': cursor['_id'], 'name': cursor['name'], 'position': cursor['position'], 'team': cursor['team']}
        return player

    def get_players(self):
        data = []
        cursor = self.Players.find()
        for player in cursor:
            data.append({'_id': player['_id'], 'name': player['name'], 'position': player['position'],
                         'team': player['team']})
        return data

    def update_player(self, id, args):
        self.Players.update({'_id': id}, {'$set': args})

    def insert_player(self, stats):
        player = {'name': stats['name'], 'position': stats['position'], 'team': stats['team']}
        if '_id' in stats:
            player['_id'] = stats['_id']
        self.Players.insert_one(player)

    def delete_player(self, id):
        self.Players.delete({'_id': id})
