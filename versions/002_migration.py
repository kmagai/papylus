from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String),
    Column('body', String),
    Column('img_url', String),
    Column('comment', String),
    Column('user_id', Integer),
    Column('option', String),
    Column('price', String),
)

list = Table('list', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=60)),
    Column('user_id', Integer),
)

movie = Table('movie', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=60)),
    Column('capture_url', String(length=60)),
    Column('trailer_url', String(length=60)),
    Column('comment', String(length=60)),
    Column('list_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].drop()
    post_meta.tables['list'].create()
    post_meta.tables['movie'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].create()
    post_meta.tables['list'].drop()
    post_meta.tables['movie'].drop()
