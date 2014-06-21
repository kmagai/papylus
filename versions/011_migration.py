from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
book = Table('book', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=60)),
    Column('capture_url', String(length=60)),
    Column('comment', String(length=60)),
    Column('list_id', Integer),
)

booklist = Table('booklist', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=60)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['book'].create()
    post_meta.tables['booklist'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['book'].drop()
    post_meta.tables['booklist'].drop()
