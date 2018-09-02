#!/usr/bin/env python3
import scraper
import os
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/grades', methods=['POST'])
def grades():
    username = request.form['username']
    password = request.form['password']
    return scraper.getData(username, password)


#if __name__ == '__main__':
#    # this is just for testing
#    scraper.getData(os.environ['HUSERNAME'], os.environ['HPASSWORD'])
