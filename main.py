from flask import Flask, jsonify, request
from model.twit import Twit
from model.user import User
import json

twits = []

app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj, Twit):
            return {'id': obj.id, 'body': obj.body, 'author': obj.author.username}
        elif isinstance(obj, User):
            return {'username': obj.username}
        else:
            return super().default(obj)



@app.route('/twit', methods=['POST'])
def create_twit():
    '''{"id": 1, body": "Hello World", "author": "@Sam"}'''

    twit_json = request.get_json()
    author = User(twit_json['author'])
    twit = Twit(twit_json['id'], twit_json['body'], author)
    twits.append(twit)
    return jsonify({'status': 'success'})

@app.route('/twit', methods=['GET'])
def read_twit():
    return jsonify({'twits': [json.dumps(twit, cls=CustomJSONEncoder) for twit in twits]})

@app.route('/twit', methods=['PUT'])
def update_twit():
    twit_json = request.get_json()
    author = User(twit_json['author'])
    twit = Twit(twit_json['id'],twit_json['body'], author)
    for t in twits:
        if twit.id == t.id:
            t.body = twit.body
    return jsonify({'status': 'success'})

@app.route('/twit', methods=['DELETE'])
def delete_twit():
    twit_json = request.get_json()
    author = User(twit_json['author'])
    twit = Twit(twit_json['id'],twit_json['body'], author)
    for t in twits:
        if twit.id == t.id:
            twits.remove(t)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run()
