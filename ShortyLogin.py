from flask import Flask, request, redirect, render_template
import validators
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

app = Flask('ShortyLogin')

USERS = {

}

SECRET = "DABESTTEAM"


if __name__ == "__main__":
    from waitress import serve
    debug = True
    if debug:
        app.run(debug=True)
    else:
        serve(app, host="0.0.0.0", port=8081)
