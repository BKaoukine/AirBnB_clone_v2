#!/usr/bin/python3
"""A script that starts a Flask application."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list')
def states_list_page():
    """Route decorator for displaying a list of states."""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_database(arg):
    """Close the current database."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
