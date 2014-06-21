from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
booklist = Table('booklist', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String),
    Column('user_id', Integer),
)

movielist = Table('movielist', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String),
    Column('user_id', Integer),
)

book_list = Table('book_list', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=60)),
    Column('user_id', Integer),
)

movie_list = Table('movie_list', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=60)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['booklist'].drop()
    pre_meta.tables['movielist'].drop()
    post_meta.tables['book_list'].create()
    post_meta.tables['movie_list'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['booklist'].create()
    pre_meta.tables['movielist'].create()
    post_meta.tables['book_list'].drop()
    post_meta.tables['movie_list'].drop()
