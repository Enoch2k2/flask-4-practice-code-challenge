#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import Blog, Comment

# Views go here!


class Home(Resource):
    def get(self):
        return {"message": "This works!"}, 200


api.add_resource(Home, "/")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
