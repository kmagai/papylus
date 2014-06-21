import os

CSRF_ENABLED = True
SECRET_KEY = 'jsadasdsasafsjafsajkfsfjksz'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


###

from authomatic.providers import oauth2, oauth1

CONFIG = {
    'tw': { # Your internal provider name
        # Provider class
        'class_': oauth1.Twitter,
        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': 'INSQ9JymGGIxpBbCL1P1Q',
        'consumer_secret': '6nPYPBR5F23uOCFj9TehfRILf8SOX4q0QTnyit5cRI',
    },
    'fb': {
        'class_': oauth2.Facebook,
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '1420558231533819',
        'consumer_secret': '1f5b8fa55948c20de200379b35964730',
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    }
}
AWS = {
        'ACCESS_KEY': 'AKIAIMAW3FVHF2C4LAXA',
        'SECRET_KEY': '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',
    }
