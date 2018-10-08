from flask import render_template
from app import app
from app.forms import LoginForm
from flask import flash, redirect
from flask import url_for
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


"""
-Methods is provided to override accepted default method which is only GET

-One problem with writing links directly in templates and source files is that if one day you decide to reorganize your 
links, then you are going to have to search and replace these links in your entire application.
"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {} with password {} , remember_me={}'.format(
            form.username.data, form.password.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
