#!flask/bin/python
from migrate.versioning import api
from papylus.config import SQLALCHEMY_DATABASE_URI
from papylus.config import SQLALCHEMY_MIGRATE_REPO
from papylus.core import db
import os.path
db.create_all()
print 'DB Successfully Created!'
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
