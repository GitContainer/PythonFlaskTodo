import os
basedir = os.path.dirname(__file__)

# sqlite database file path
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../../todo.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, '../../repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False