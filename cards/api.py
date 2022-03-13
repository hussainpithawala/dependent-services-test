# Accounts Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)


class Cards(Resource):
    def get(self):
        return {
            'Cards': [
                {"id": "card_1", "card-holder-name": "Card-holder-fname-1", "user_id": "user_1"},
                {"id": "card_2", "card-holder-name": "Card-holder-fname-2", "user_id": "user_2"},
                {"id": "card_3", "card-holder-name": "Card-holder-fname-3", "user_id": "user_3"}
            ]
        }


# Create routes
api.add_resource(Cards, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
