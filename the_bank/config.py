"""Import os and dotenv."""
import os
from dotenv import load_dotenv


# TODO: create a .env file with the SECRET_KEY and SQLALCHEMY_DATABASE_URI
# HINT: if you get a "drivername" error try exporting to the terminal
# as well as having them in your .env file. i.e.
# export SECRET_KEY=secret


class Config:
    """Config class."""

    ENV = "development"
    DEBUG = True
    # TODO: add SECRET_KEY to .env
    SECRET_KEY = os.getenv("SECRET_KEY")
    # TODO: add SQLALCHEMY_DATABASE_URI to .env
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


# TODO: go to the_bank/models.py
