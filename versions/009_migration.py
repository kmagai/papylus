from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=60)),
    Column('tw_id', String(length=200)),
    Column('fb_id', String(length=200)),
    Column('fb_oauth_token', String(length=200)),
    Column('fb_oauth_secret', String(length=200)),
    Column('tw_oauth_token', String(length=200)),
    Column('tw_oauth_secret', String(length=200)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['fb_id'].create()
    post_meta.tables['user'].columns['tw_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['fb_id'].drop()
    post_meta.tables['user'].columns['tw_id'].drop()
