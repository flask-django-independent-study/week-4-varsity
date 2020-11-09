"""Import libraries."""
from the_bank import db

# By now you should know how to set up a SQLAlchemy Model class. To make
# sure you know what's going on with this app, take a look below to see
# what properties an account has along with what data types it expects.


class Account(db.Model):
    """Account database model class."""

    id = db.Column(db.Integer, primary_key=True)
    holder = db.Column(db.String(100), nullable=False, unique=True)
    balance = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        """Return account holder."""
        return f"Account('{self.holder}')"


# TODO: go to the-bank/__init__.py
