# Phase 4 Code Challenge

## The Goal

- To be able to implement complex problem solving
- To implement routing
- To work with complex data structures

## Instructions

* Fork and clone this repository
* Ensure everything works in flask shell, run `Blog.query.all()` to make sure all of the seeded blogs are there, as well as `Comment.query.all()`. If they aren't you will need to do python3 seed.py.

If this breaks while in a breakout room. Click the 3 dots, or there may be a more button and click on the ask for help button and I will be right there to help.

## The code challenge

Your models and associations should be set up for you for this code challenge. You will have a simple one to many relationship between a blog that has many comments and a comment belongs to a blog. Your goal is to:

Create a get route to `/blogs_comments`. This route should return an array of all of the blogs as json. However formatted in this way:

```
[
    {
        id: 1,
        title_length: 6,
        content_length: 6
        comments: [
            {
                id: 1,
                comment_text_length: 5
            },
            {
                id: 2,
                comment_text_length: 7
            }
            ...etc
        ]
    },
    ...etc
]
```

### Finished?
If you finish before time is complete, then feel free to try this bonus challenge:

Create a route that goes to "/sorted_comments" that would be a get route. This route would return the json of all the Comments, where the content is in alphabetical order.

If done with both, feel free to raise hand and let me know! I will come check on your work!