import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):

    APPLICATION_ROOT = "/"
    SESSION_COOKIE_NAME = "session"
    SESSION_COOKIE_SECURE = True
    SECRET_KEY = "4f8a3ffcf409d63c2501e01da98de6c615414f812dc1abc66105c62b5bf5d510"
    DEBUG = False
    DATABASE = ""
    TESTING = False
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "root"

class ProductionConfig(Config):

    DATABASE_URI = "./app/db/flaskdb-db.db"
    DATABASE_INIT = "./db/init.sql"
    DB_NAME = "auth_service-db"
    DB_USERNAME = None
    DB_PASSWORD = None

class DevelopmentConfig(Config):

    DEBUG = True
    DATABASE_URI = "./app/db/flaskdb-db.db"
    DATABASE_INIT = "./db/init.sql"
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "root"

class TestConfig(Config):

    DATABASE_URI = "./app/db/testing-db.db"
    DATABASE_INIT = "./db/init.sql"
    TESTING = True
    DB_NAME = "testing-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    SESSION_COOKIE_SECURE = False