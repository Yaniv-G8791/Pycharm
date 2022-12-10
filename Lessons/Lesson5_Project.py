from flask import Flask, redirect, url_for, render_template, request
import json
import pymysql
from selenium import webdriver

@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        add_user(user_id, user_name)
        return {'user id': user_id , 'user name': user_name, 'status': 'saved'}, 200 # status code
    elif request.method == 'GET':
    elif request.method == 'DELETE':
    elif request.method == 'PUT':
    else:

  # todo elif for get put and delete