#!/usr/bin/python3
"""
This script starts a Flask web application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """
    flask hello world
    """
    return "Hello HBNB!"
    strict_slashes = False


@app.route('/hbnb')
def hbnb():
    """
    displays HBNB
    """
    return "HBNB"
    strict_slashes = False


@app.route('/c/<text>')
def c_text(text):
    """
    make a simple variable rule
    """
    return "C {}".format(text.replace("_", " "))
    strict_slashes = False


@app.route('/python/')
    strict_slashes = False


@app.route('/python/(<text>)')
def python_text(text='is cool'):
    """
    python followed by a text
    """
    return "Python {}".format(text.replace("_", " "))
    strict_slashes = False


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
