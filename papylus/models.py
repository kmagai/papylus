from datetime import datetime

from papylus.core import db
from papylus import app

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    
    def __init__(self, title, body, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
    
    def __repr__(self):
        return '<List %r>' % self.title

# models for which we want to create API endpoints
app.config['API_MODELS'] = { 'list': List }
