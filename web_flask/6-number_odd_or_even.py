#!/usr/bin/python3

"""a script that starts a Flask web application:
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    returns hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns HBNB!
    """
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    display “C ” followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    display “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space
    """
    text = text.replace("_", " ")
    return "python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
     display a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
     display
     a HTML page only if n is an integer
    """
    if not (n % 2):
        text = "is even"
        return render_template("6-number_odd_or_even.html", n=n, text=text)
    else:
        text = "is odd"
        return render_template("6-number_odd_or_even.html", n=n, text=text)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
