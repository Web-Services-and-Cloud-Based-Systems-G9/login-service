from datetime import datetime, timedelta
from flask import Flask, request, redirect, render_template
import validators
import os
import jwt
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

app = Flask('ShortyLogin')
USERS = { }

SECRET = "DABESTTEAM"


@app.route('/users', methods=['POST'])
def create_one_user():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username, password)
    try:
        if username in USERS:
            return f'Username already existed', 401
        else:
            USERS[username] = {}
            USERS[username]['password'] = password
            print(USERS)
            return f'Success', 200
    except Exception as e:
        print(e)
        return f'Unexpected error', 500


@app.route('/users/login', methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    stamp = datetime.now() + timedelta(days=1)
    try:
        if username in USERS.keys() and password == USERS[username]['password']:
            return "{encoded_jwt}".format(encoded_jwt=jwt.encode({"username": "{name}".format(name = username), "exp": stamp}, "DABESTTEAM", algorithm="HS256")), 200
        else:
            return f"check the username and password", 404
    except Exception as e:
        print(e)
        return f'Unexpected error', 500


if __name__ == "__main__":
    from waitress import serve
    debug = True
    if debug:
        app.run(debug=True)
    else:
        serve(app, host="0.0.0.0", port=8081)
