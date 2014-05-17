import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from papylus import app

# routing for API endpoints (generated from the models designated as API_MODELS)
from papylus.core import api_manager
from papylus.models import List, db

for model_name in app.config['API_MODELS']:
    model_class = app.config['API_MODELS'][model_name]
    api_manager.create_api(model_class, methods=['GET', 'POST', 'DELETE', 'PUT'], results_per_page=None)


session = api_manager.session

@app.route('/')
def landing():
    return make_response(open('papylus/templates/landing.html').read())

@app.route('/search/item')
def search_item():
    return 'hoge'

@app.route('/<path>')
def index(path):
    return make_response(open('papylus/templates/index.html').read())

# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
							   'img/favicon.ico')

