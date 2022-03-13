# Accounts Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)


class Accounts(Resource):
    def get(self):
        return {
            'Accounts': [
                {"id": "account_1", "name": "Account-holder-fname-1", "user_id": "user_1"},
                {"id": "account_2", "name": "Account-holder-fname-2", "user_id": "user_2"},
                {"id": "account_3", "name": "Account-holder-fname-3", "user_id": "user_3"}
            ]
        }


# Create routes
api.add_resource(Accounts, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
