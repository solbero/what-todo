import flask

from what_todo import config
from what_todo.views import admin, home, user


def create(testing=False) -> flask.Flask:
    """Flask app factory. Makes testing easier."""
    app = flask.Flask(__name__)
    flask_env = app.config["ENV"]

    if testing:
        app.config.from_object(config.TestingConfig())
    elif flask_env == ("development" or "dev"):
        app.config.from_object(config.DevelopmentConfig())
    elif flask_env == ("testing" or "test"):
        app.config.from_object(config.TestingConfig())
    else:
        app.config.from_object(config.ProductionConfig())

    app.register_blueprint(home.route)
    app.register_blueprint(admin.route)
    app.register_blueprint(user.route)

    return app
