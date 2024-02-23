#!/usr/bin/python3
"""
script starts Flask web app
listen on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """display text"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """
    display custom text given
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def text_if_int(n):
    """display text only if int given"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>")
def html_if_int(n):
    """display html page only if int given
    place given int into html template
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
