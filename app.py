from flask import Flask
from flask_restful import Api
from API_Resources.REST_resource import PlayerAPI, PlayersAPI


app = Flask(__name__)
api = Api(app)

api.add_resource(PlayerAPI, '/api/<int:player_id>')
api.add_resource(PlayersAPI, '/api/')

if __name__ == '__main__':
    app.run(debug=True)
