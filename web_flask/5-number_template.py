#!/usr/bin/python3
"""Simple Flask Server Script."""


from flask import Flask, render_template

app = Flask(__name__)

app.url_map.strict_slashes = False


def greeting():
    """
    Greeting to return a greeting message.

    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"


@app.route('/')
def index():
    """
    Route decorator for the root URL.

    Returns:
        str: A greeting message.
    """
    return greeting()


@app.route('/hbnb')
def hbnb():
    """
    Route decorator for the /hbnb URL.

    Returns:
        str: A  message.
    """
    return "HBNB"


@app.route('/c/<text>')
def String(text):
    """
    Route decorator for the /c/ with dynamique URL.

    Returns:
        str: A  message.
    """
    dynurl = text.replace("_", " ")
    return "C %s" % dynurl


@app.route('/python/')
@app.route('/python/<text>')
def dyUrl(text="is_cool"):
    """
    Route decorator for the /c/ with dynamique URL.

    Returns:
        str: A  message.
    """
    dynurl = text.replace("_", " ")
    return "Python %s" % dynurl


@app.route('/number/<int:n>')
def intUrl(n):
    """
    Route decorator for the number with dynamique URL.

    Returns:
        str: A  message.
    """
    return "%i is a number" % n


@app.route('/number_template/<int:n>')
def intTmplUrl(n):
    """
    Route decorator for the number with dynamique URL.

    Returns:
        str: A  message.
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
