from flask import render_template
from app import app


# first view function
@app.route('/')
@app.route('/index')
def index():
    users = {'username': 'Aswin Setiadi'}
    posts = [
        {
            'author': {'username': 'Patricia'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Hina'},
            'body': 'Feed me.'
        }

    ]
    return render_template('index.html', title='Home', users=users, posts=posts)
