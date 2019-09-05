import os
import json
import datetime
from bson.objectid import ObjectId
from flask import Flask, jsonify, request, make_response, send_from_directory
from flask_pymongo import PyMongo
from flask_cors import CORS


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
CORS(app)
# app.config['MONGO_URI'] = os.environ.get('DB')
app.config['MONGO_URI'] = 'mongodb://users_db:27017/users'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/users'
mongo = PyMongo(app)

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder

@app.errorhandler(404)
def not_found(error):
    """ error handler """
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/v1/users', methods=['GET'])
def users():
    query = request.args.to_dict()
    if 'query' in query:
        query.pop('query')
    cursor = mongo.db.users.find(query)
    return jsonify(list(cursor)), 200


@app.route('/v1/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def user():
    if request.method == 'GET':
        query = request.args
        data = mongo.db.users.find_one(query)
        return jsonify(data), 200

    data = request.get_json()
    if request.method == 'POST':
        email = data.get('email', None)
        if email is not None:
            queryset = mongo.db.users.find_one({'email': email})
            if queryset is None:
                cleaned = {}
                cleaned['name'] = data.get('name', '')
                cleaned['lastname'] = data.get('lastname', '')
                cleaned['age'] = data.get('age', '')
                cleaned['email'] = email
                cleaned['gender'] = data.get('gender', '')
                cleaned['timestamp'] = datetime.datetime.now()
                mongo.db.users.insert_one(cleaned)
                return jsonify({'ok': True, 'message': 'User created successfully!'}), 200
            else:
                return jsonify({'ok': False, 'message': 'Email address already exists!'}), 400
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'DELETE':
        if data.get('email', None) is not None:
            db_response = mongo.db.users.delete_one({'email': data['email']})
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'record deleted'}
            else:
                response = {'ok': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'PATCH':
        if data.get('query', {}) != {}:
            mongo.db.users.update_one(
                data['query'], {'$set': data.get('payload', {})})
            return jsonify({'ok': True, 'message': 'record updated'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001)
