#!/usr/bin/env python3
import scraper
import os
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# returns grades as JSON
@app.route('/api/grades', methods=['POST'])
def grades():
    username = request.form['username']
    password = request.form['password']
    return scraper.getData(username, password)