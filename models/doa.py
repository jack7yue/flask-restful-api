from pymongo import MongoClient
from flask import jsonify


client = MongoClient('mongodb://localhost:27017/')
db = client.Players


def get_player(id):
    cursor = db.Players.find_one({'id': id})
    player = {'id': cursor['id'], 'name': cursor['name'], 'position': cursor['position']}
    return player


def get_players():
    data = []
    cursor = db.Players.find()

    for player in cursor:
        data.append(player)

    return jsonify(data)


def update_player(id, stats):
    db.Players.update({'id': id}, {'$set': stats})


def insert_player(stats):
    player = {'id': stats['id'], 'name': stats['name'], 'position': stats['position']}
    db.Players.insert_one(player)


def delete_player(id):
    db.Players.delete({'id': id})
