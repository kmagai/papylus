from datetime import datetime

from papylus.core import db
from papylus import app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    icon = db.Column(db.String)
    description = db.Column(db.String)
    tw_id = db.Column(db.String(200))
    fb_id = db.Column(db.String(200))
    tw_oauth_token = db.Column(db.String(200))
    fb_oauth_token = db.Column(db.String(200))
    lists = db.relationship('List', backref='user', lazy='dynamic')
    associates_id = db.Column(db.String)

    def __init__(self, name=None, tw_id=None, fb_id=None,
                 tw_oauth_token=None, fb_oauth_token=None, associates_id=None):
        self.name = name
        self.tw_id = tw_id
        self.fb_id = fb_id
        self.tw_oauth_token = tw_oauth_token
        self.fb_oauth_token = fb_oauth_token
        if associates_id is None:
            associates_id = 'papylus-22'
        self.associates_id = associates_id

    def __repr__(self):
        return 'user: %r, id: %r' % (self.name, self.id)


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80))
    pub_date = db.Column(db.DateTime)
    items = db.relationship('Item', backref='list', lazy='dynamic')
    
    def __init__(self, user_id, title, pub_date=None):
        self.user_id = user_id
        self.title = title
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
    
    def __repr__(self):
        return '<List %r>' % self.title

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    publisher = db.Column(db.String)
    pub_date = db.Column(db.String)
    url = db.Column(db.String)
    img = db.Column(db.String)
    body = db.Column(db.Text)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))
    
    def __init__(self, name, url, img, list_id, pub_date=None, publisher=None, body=None):
        self.name = name
        self.url = url
        self.img = img
        self.list_id = list_id
        self.pub_date = pub_date
        self.publisher = publisher
        self.body = body
    
    def __repr__(self):
        return '<Item %r>' % self.name

# models for which we want to create API endpoints
app.config['API_MODELS'] = { 'list': List, 'item': Item , 'user': User}
