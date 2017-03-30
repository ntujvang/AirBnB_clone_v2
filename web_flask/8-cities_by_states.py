#!/usr/bin/python3
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def cities_by_states():
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')