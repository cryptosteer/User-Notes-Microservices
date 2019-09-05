
import os
import sys
import requests
from flask import Flask, jsonify, request, make_response, render_template, send_from_directory

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    """ error handler """
    return send_from_directory('static', '404.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
