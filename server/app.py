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


class BlogComments(Resource):
    def get(self):
        blogs = [{
            "id": blog.id,
            "title_length": len(blog.title),
            "content_length": len(blog.content),
            "comments": [{
                "id": comment.id,
                "content_length": len(comment.content)
            } for comment in blog.comments]
        } for blog in Blog.query.all()]

        return blogs, 200


class Alphabetical(Resource):
    def get(self):
        # dict_comments = [comment.to_dict() for comment in Comment.query.all()]
        sorted_comments = sorted(
            Comment.query.all(), key=lambda x: x.content, reverse=False)
        serialized = [comment.to_dict() for comment in sorted_comments]
        return serialized, 200


api.add_resource(Home, "/")
api.add_resource(BlogComments, "/blog_comments")
api.add_resource(Alphabetical, "/sorted_comments")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
