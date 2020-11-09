"""Import libraries."""
from flask import Blueprint, request, jsonify
from the_bank import db
from the_bank.models import Account

api = Blueprint("api", __name__)

# Okay so with all of that explaination out of the way, let's start creating
# API endpoints.

# Here you can see I already set one up for you. This is a route that will
# print out all of the open accounts to the terminal. This endpoint will not
# be used by our front-end. It is instead here for development.


@api.route("/account", methods=["GET"])
def get_all_accounts():
    """Get all open accounts."""
    accounts = Account.query.all()
    print(accounts)
    return ""


# Before we get started try running the app to see where it is currently at.
# Try accessing the get_all_accounts route.
# HINT: remember we will need to access the route by "/api/account" since
# we specified a url prefix in the __init__.py file when we defined the
# blueprint.


# I will walk you throught this next endpoint but after that you're on your own
# TODO: create an endpoint "/account" that accepts only POST requests.
# This endpoint will be able to create or open a new account.
# With APIs instead of serving html files we receive and return json data.
# We have a "holder" that we can get by accessing request.json.get("holder")
# and assigning that to a holder variable.
# Next we want to look up the account to see if it already exists.
# TODO: query Account by the holder and assign it to a variable account.
# If this account does exist, we want to return an error message saying
# "Account already exists"
# TODO: in the if statement return jsonify({"error": "Account already exists"})
# jsonify is a function built into flask. It takes a python dictionary {} and
# converts the data into json so that the front end can understand it.
# Then, if we don't make it into the if check we want to create a new account
# and assign the holder as the holder variable from the request.
# TODO: create the account, add it to the db, commit it to the db.
# Lastly, we want to return some json data to tell the front-end this was
# successful.
# TODO: return jsonify({"message": f"An account for {account.holder} has been created"}), 201
# We are returning a message with the newly created account holder.
# Notice the , 201 after jsonify. This is an http status code. Although we
# didn't do this on the first return statement it is good practice to send
# status codes to the front end. The let the client know what happened with the
# request.


# We can test our newly created enpoint in Postman. If you don't already have
# it I highly recommend downloading it:
# https://www.postman.com/downloads/
# Postman will allow us to make requests to the back-end without needing a
# fully-functioning front-end or without any front-end at all. For more on
# how to use Postman, check out the resources


# TODO: create an endpoint that allows client to GET or view a single account.
# This endpoint will take an account holder from the url, look up the account,
# and return "holder" and "balance" as associated with the account.
# TODO: make sure you check if the account exists and even if the account does
# not exists, still return json data.


# TODO: create an endpoint that allows the client to DELETE or close an account


# TODO: create an endpoint that allows the client to deposit to a given account


# TODO: create an endpoint that allows the client to withdraw from a given account


# TODO: make sure all these routes are tested and working before moving on. It
# will make the next stage, when we move to the front-end much easier

# TODO: go to the-bank/static/js/main.js
