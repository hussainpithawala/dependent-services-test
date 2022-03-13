---
# Assignment for automation testing
---

### How to run:
> The assignment is self contained in a local github repository within this folder.

```shell
git branch
* dev-1
  dev-2
```

Checkout to branch dev-1 using following command
```shell
git checkout dev-1
```

```shell
git checkout dev-1
```

Do a docker-compose up to build the images and run the services
```shell
docker compose up

Starting testing-assignment_accounts_1 ... done
Starting testing-assignment_cards_1    ... done
Starting testing-assignment_users_1    ... done
Attaching to testing-assignment_cards_1, testing-assignment_accounts_1, testing-assignment_users_1
cards_1     |  * Running on all addresses.
cards_1     |    WARNING: This is a development server. Do not use it in a production deployment.
accounts_1  |  * Running on all addresses.
accounts_1  |    WARNING: This is a development server. Do not use it in a production deployment.
accounts_1  |  * Running on http://172.18.0.3:80/ (Press CTRL+C to quit)
accounts_1  |  * Restarting with stat
cards_1     |  * Running on http://172.18.0.2:80/ (Press CTRL+C to quit)
cards_1     |  * Restarting with stat
cards_1     |  * Debugger is active!
cards_1     |  * Debugger PIN: 406-820-174
accounts_1  |  * Debugger is active!
accounts_1  |  * Debugger PIN: 135-698-799
users_1     |  * Running on all addresses.
users_1     |    WARNING: This is a development server. Do not use it in a production deployment.
users_1     |  * Running on http://172.18.0.4:80/ (Press CTRL+C to quit)
users_1     |  * Restarting with stat
users_1     |  * Debugger is active!
users_1     |  * Debugger PIN: 106-444-521
```

### APIs and other details
There are 3 different API(s) present in the following assignment

Accounts-API: This Api is available at [Accounts](http://localhost:5001/) http://localhost:5001/
```json
{
    "Accounts": [
        {
            "id": "account_1",
            "name": "Account-holder-fname-1",
            "user_id": "user_1"
        },
        {
            "id": "account_2",
            "name": "Account-holder-fname-2",
            "user_id": "user_2"
        },
        {
            "id": "account_3",
            "name": "Account-holder-fname-3",
            "user_id": "user_3"
        }
    ]
}
```
Cards-API: This Api is available at [Cards](http://localhost:5002/) http://localhost:5002/
```json
{
    "Cards": [
        {
            "card-holder-name": "Card-holder-fname-1",
            "id": "card_1",
            "user_id": "user_1"
        },
        {
            "card-holder-name": "Card-holder-fname-2",
            "id": "card_2",
            "user_id": "user_2"
        },
        {
            "card-holder-name": "Card-holder-fname-3",
            "id": "card_3",
            "user_id": "user_3"
        }
    ]
}
```
Users-API: This Api is available at [Users](http://localhost:5003/) http://localhost:5003/
```json
{
    "Users": [
        {
            "id": "user_1",
            "user-name": "user-fname-1"
        },
        {
            "id": "user_2",
            "user-name": "user-fname-2"
        },
        {
            "id": "user_3",
            "user-name": "user-fname-3"
        }
    ]
}
```
Users-Detail-API: This Api is available at [Users-details](http://localhost:5003/details) http://localhost:5003/details
```json
{
    "Users": [
        {
            "accounts": [
                {
                    "id": "account_1",
                    "name": "Account-holder-fname-1",
                    "user_id": "user_1"
                }
            ],
            "cards": [
                {
                    "card-holder-name": "Card-holder-fname-1",
                    "id": "card_1",
                    "user_id": "user_1"
                }
            ],
            "id": "user_1",
            "user-name": "user-fname-1"
        },
        {
            "accounts": [
                {
                    "id": "account_2",
                    "name": "Account-holder-fname-2",
                    "user_id": "user_2"
                }
            ],
            "cards": [
                {
                    "card-holder-name": "Card-holder-fname-2",
                    "id": "card_2",
                    "user_id": "user_2"
                }
            ],
            "id": "user_2",
            "user-name": "user-fname-2"
        },
        {
            "accounts": [
                {
                    "id": "account_3",
                    "name": "Account-holder-fname-3",
                    "user_id": "user_3"
                }
            ],
            "cards": [
                {
                    "card-holder-name": "Card-holder-fname-3",
                    "id": "card_3",
                    "user_id": "user_3"
                }
            ],
            "id": "user_3",
            "user-name": "user-fname-3"
        }
    ]
}
```
## What to test?

### Part-1: 
Write down test suite for accounts, cards and users
### Expectation:
This is general case and integration suites for the all API endpoints in 3 services are expected.

### Part-2: 
dependent test-suites to kick off when a dependency API has made any changes 

Here, User service is dependent on accounts and cards service to fulfil the `details` API contract.

So Api endpoint http://localhost:5003/details is internally dependent on 
http://localhost:5001/ and http://localhost:5002

However, if Account API and Cards API change their contract subsequently the User-API for details will
be affected.

To visualize this thing.
```shell
git checkout dev-2
```
and
```shell
docker-compose up
```
Now when we invoke 

Accounts-API: available at [Accounts](http://localhost:5001/) http://localhost:5001/
```json
[
    {
        "id": "account_1",
        "name": "Account-holder-fname-1",
        "user_id": "user_1"
    },
    {
        "id": "account_2",
        "name": "Account-holder-fname-2",
        "user_id": "user_2"
    },
    {
        "id": "account_3",
        "name": "Account-holder-fname-3",
        "user_id": "user_3"
    }
]
```
Cards-API:  available at [Cards](http://localhost:5002/) http://localhost:5002/
```json
[
    {
        "card-holder-name": "Card-holder-fname-1",
        "id": "card_1",
        "user_id": "user_1"
    },
    {
        "card-holder-name": "Card-holder-fname-2",
        "id": "card_2",
        "user_id": "user_2"
    },
    {
        "card-holder-name": "Card-holder-fname-3",
        "id": "card_3",
        "user_id": "user_3"
    }
]
```
This change in the API contract will lead to breaking the `user-details` Api

Users-Detail-API: available at [Users-details](http://localhost:5003/details) http://localhost:5003/details

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1994, in __call__
    return self.wsgi_app(environ, start_response)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1985, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/local/lib/python3.6/site-packages/flask_restful/__init__.py", line 271, in error_router
    return original_handler(e)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1540, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/site-packages/flask/_compat.py", line 32, in reraise
    raise value.with_traceback(tb)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1982, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1614, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/site-packages/flask_restful/__init__.py", line 271, in error_router
    return original_handler(e)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1517, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/site-packages/flask/_compat.py", line 32, in reraise
    raise value.with_traceback(tb)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1612, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1598, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/usr/local/lib/python3.6/site-packages/flask_restful/__init__.py", line 477, in wrapper
    resp = resource(*args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/flask/views.py", line 84, in view
    return self.dispatch_request(*args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/flask_restful/__init__.py", line 587, in dispatch_request
    resp = meth(*args, **kwargs)
  File "/usr/src/app/api.py", line 31, in get
    account_list = accounts.get('Accounts')
AttributeError: 'list' object has no attribute 'get'
```
### Expectation
Dependent test suites should kick off to make sure that any changes in the dependency API endpoints don't go unnoticeable.
> @author: Hussain Pithawala for Incred Financial Services