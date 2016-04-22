from loader import app_instance, db
from flask import send_file, make_response, url_for, jsonify, abort, \
                    make_response, request, redirect
from models import Game, Company, Person
from sqlalchemy_searchable import parse_search_query
from sqlalchemy_searchable import search
import requests
import os, time


@app_instance.route('/', methods=['GET'])
def index():
    return send_file('index.html')

@app_instance.route('/run_unittests')
def run_tests():
    os.system('python tests.py > myTest.out 2>&1')
    f = open('myTest.out', encoding='utf-8')
    output = f.read()
    f.close()
    return jsonify({'output': str(output)})

@app_instance.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)
