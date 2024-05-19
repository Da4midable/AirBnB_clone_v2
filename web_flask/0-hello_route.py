#!/usr/bin/python3
"""
This module starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
Routes:
/: display “Hello HBNB!”
The route definition uses the option strict_slashes=False.
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
