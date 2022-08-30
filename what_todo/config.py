import os


class Config:
    # Flask
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    # Flask
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    # Flask
    TESTING = True
    SESSION_COOKIE_SECURE = False
