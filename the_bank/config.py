"""Import os and dotenv."""
import os
from dotenv import load_dotenv


# TODO: create a .env file
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
