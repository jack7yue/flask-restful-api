from pymongo import MongoClient



class PlayerDAO:
    def __init__(self):
        self.client = MongoClient('mongod')
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

    def update_player(self, args, id):
        result = self.Players.update({'_id': id}, {'$set': args})
        return result

    def insert_player(self, stats):
        player = {'name': stats['name'], 'position': stats['position'], 'team': stats['team']}
        if '_id' in stats:
            player['_id'] = stats['_id']
        self.Players.insert_one(player)

    def delete_player(self, id):
        result = self.Players.delete_many({'_id': id})

        # check to see if our write operation succeeds
        return result.acknowledged
