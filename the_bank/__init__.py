"""Import libraries."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from the_bank.config import Config

db = SQLAlchemy()

# This file layout should look familiar to you as well. Notice the api route.
# We prefix the blueprint with "/api". All our routes that will be created
# in the api package will have to be accessed on the front-end in that same way


def create_app(config_class=Config):
    """Create an instance of the bank app."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from the_bank.main.routes import main
    from the_bank.api.routes import api

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app


# TODO: go to the-bank/main/routes.py
