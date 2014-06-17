import os

from flask import (Flask, request, Response, g, flash,
                render_template, url_for, redirect, send_from_directory,
                send_file, make_response, abort, session)
from papylus import app
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic

# routing for API endpoints (generated from the models designated as API_MODELS)
from papylus.core import api_manager
from papylus.models import List, Item, User, db
from config import CONFIG
from functools import wraps
import json

api_manager.create_api(app.config['API_MODELS']['user'], methods=['GET', 'PUT'], results_per_page=None)
api_manager.create_api(app.config['API_MODELS']['list'], methods=['GET', 'POST', 'DELETE', 'PUT'], results_per_page=None)
api_manager.create_api(app.config['API_MODELS']['item'], methods=['GET', 'POST', 'DELETE', 'PUT'], results_per_page=None)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    response = make_response(open('papylus/templates/index.html').read())
    return response

@app.route('/search/item')
def search_item():
    query = request.args.get('q')
    category = request.args.get('c')
    ## replace confidencial to secret file and put it in gitignore
    from amazon.api import AmazonAPI
    amazon = AmazonAPI('AKIAITMCHY2NAIZNCQGA','rXqFN4ytnf9//0ILqsdCMqlYi24xLdnSI+Py95xP','papylus-22', region="JP")

    if not category:
        category = 'All'

    try:
        products = amazon.search_n(5, Keywords=query, SearchIndex=category)
    except:
        # in case 503 Error occurs without any reason
        import time
        for i in range(3):
            print '503 Error'
            time.sleep(1)
            products = amazon.search_n(5, Keywords=query, SearchIndex=category)
            if products:
                break

    items = []
    for i in products:
        items.append({'name': i.title, 'url': i.offer_url, 'img': i.medium_image_url})
    return json.dumps(items)

'''
Login
'''

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=True)

@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    """
    Login handler, must accept both GET and POST to be able to use OpenID.
    """
    
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)
    
    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()

            if result.provider.name == 'tw':

                username = result.user.username
                credentials = result.user.credentials
                user = User.query.filter_by(tw_oauth_token=credentials.token).first()

                if user == None or user.tw_oauth_secret != credentials.token_secret:
                    url = 'https://api.twitter.com/1.1/users/show/' + username + '.json'
                    response = result.provider.access(url)
                    icon_img = response.data['profile_image_url_https'].replace('normal', 'bigger')
                    user = User()
                    user.tw_id = result.user.id
                    user.name = result.user.name
                    user.tw_oauth_token = credentials.token
                    user.tw_oauth_secret = credentials.token_secret
                    user.icon = icon_img
                    db.session.add(user)
                    db.session.commit()
                    user = User.query.filter_by(tw_oauth_token=credentials.token).first()

            ### not being tested
            if result.provider.name == 'fb':
                credentials = result.user.credentials
                user = User.query.filter_by(fb_oauth_token=credentials.token).first()
                if user == None or user.tw_oauth_secret != credentials.token_secret:
                    user = User()
                    user.fb_id = result.user.id
                    user.name = result.user.name
                    user.description = result.user.description
                    user.fb_oauth_token = credentials.token
                    user.fb_oauth_secret = credentials.token_secret
                    db.session.add(user)
                    db.session.commit()

            userpath = os.path.join('user', str(user.id))

            next_url = request.args.get('next') or url_for('index', path=userpath)
            redirect_to_next = make_response(redirect(next_url))
            redirect_to_next.set_cookie('token', credentials.token)
            redirect_to_next.set_cookie('userId', str(user.id))
            return redirect_to_next

    return response


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
							   'img/favicon.ico')

