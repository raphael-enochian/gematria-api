# -*- coding: utf-8 -*-

from flask import Flask, request, make_response, abort
from random import randint

app = Flask(__name__)


@app.route('/cart/<item>')
def cart(item):
    items = ['hat', 'book', 'computer']
    if not item in items:
        abort(404)
    return make_response('<h1>You bought a {}!</h1>'.format(item))


@app.route('/user/<name>')
def user(name):
    response = make_response(
        '<h1>Hola {}!</h1>'.format(name) +
        '<p>You\'re using {}</p>'.format(request.headers.get('User-Agent')) +
        '<p>We have given you a cookie with a magic number.</p>'
    )
    response.set_cookie('magic_number', str(randint(-1000, 9999)))
    return response


@app.route('/')
def index():
    return '<h1>Welcome to the Index.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
