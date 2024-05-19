#!/usr/bin/python3
"""
This module starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space)
/python/(<text>): display “Python ” followed by the value of the text variable
(replace underscore _ symbols with a space).
The default value of text is “is cool”.
/number/<n>: display “n is a number” only if n is an integer
The route definitions use the option strict_slashes=False.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Displays a simple greeting.

    This function handles the root route and returns the string
    "Hello HBNB!" when accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays a simple message.

    This function handles the /hbnb route and returns the string
    "HBNB" when accessed.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays a message with a variable.

    This function handles the /c/<text> route and returns the string
    "C " followed by the value of the text variable, with underscores
    replaced by spaces.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Displays a message with a variable or a default value.

    This function handles the /python/(<text>) route and returns the string
    "Python " followed by the value of the text variable, with underscores
    replaced by spaces. If no text is provided, it defaults to "is cool".
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays a message indicating that n is a number.

    This function handles the /number/<n> route and returns the string
    "n is a number" only if n is an integer.
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
