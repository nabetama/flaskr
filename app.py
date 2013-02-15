# coding: utf-8
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index nginx gunicorn'

@app.route('/hello')
def hello():
    return 'hello nginx gunicorn'

if __name__ == "__main__":
    app.run()