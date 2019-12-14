from flask import Flask, escape, request
import json

app = Flask(__name__)

users = dict()

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/users', methods=['GET'])
def hello_name():
    global users
    return users

@app.route('/user/<name>', methods=['GET'])
def hello_name_get(name):
    global users
    return users[name]

@app.route('/user/<name>', methods=['POST'])
def hello_name_post(name):
    user = request.json
    global users
    users[user['name']] = user
    return 'You entered %s name and %s surname' % (user['name'], user['surname'])

if __name__ == '__main__':
    app.run(port=8080)

