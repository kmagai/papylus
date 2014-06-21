from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
item = Table('item', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('type', String),
    Column('title', String),
    Column('img_url', String),
    Column('comment', String),
    Column('tmdb_id', String),
    Column('video_url', String),
    Column('list_id', Integer),
)

item = Table('item', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('item_type', String(length=60)),
    Column('title', String(length=60)),
    Column('img_url', String(length=60)),
    Column('comment', String(length=60)),
    Column('tmdb_id', String(length=60)),
    Column('video_url', String(length=60)),
    Column('list_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['item'].columns['type'].drop()
    post_meta.tables['item'].columns['item_type'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['item'].columns['type'].create()
    post_meta.tables['item'].columns['item_type'].drop()
