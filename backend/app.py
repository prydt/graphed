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
    return scraper.getDataWithLogin(username, password)

@app.route('/api/grades_with_token', methods=['POST'])
def grades_with_token():
    session_id = request.form['session_id']
    auth_cookie = request.form['auth_cookie']
    return scraper.getDataWithToken(session_id, auth_cookie)
