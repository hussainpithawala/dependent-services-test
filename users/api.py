# Accounts Service

# Import framework
import requests
import json
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        return {
            'Users': [
                {"id": "user_1", "user-name": "user-fname-1"},
                {"id": "user_2", "user-name": "user-fname-2"},
                {"id": "user_3", "user-name": "user-fname-3"}
            ]
        }


class UserswithDetails(Resource):
    def get(self):
        accounts = requests.get("http://accounts/").json()
        print(json.dumps(accounts))
        cards = requests.get("http://cards/").json()
        print(json.dumps(cards))
        account_list = accounts.get('Accounts')
        card_list = cards.get('Cards')
        return {
            'Users': [
                {
                    "id": "user_1", "user-name": "user-fname-1",
                    "accounts": list(filter(lambda account: account['user_id'] == 'user_1', account_list)),
                    "cards": list(filter(lambda card: card['user_id'] == 'user_1', card_list))
                },
                {
                    "id": "user_2", "user-name": "user-fname-2",
                    "accounts": list(filter(lambda account: account['user_id'] == 'user_2', account_list)),
                    "cards": list(filter(lambda card: card['user_id'] == 'user_2', card_list))
                },
                {
                    "id": "user_3", "user-name": "user-fname-3",
                    "accounts": list(filter(lambda account: account['user_id'] == 'user_3', account_list)),
                    "cards": list(filter(lambda card: card['user_id'] == 'user_3', card_list))
                }
            ]
        }


# Create routes
api.add_resource(Users, '/')
api.add_resource(UserswithDetails, '/details')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
