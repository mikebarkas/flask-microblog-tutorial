from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Joe'}
    posts = [
        {
            'author': {'nickname': 'Joe'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Billy'},
            'body': 'The Avengers movie was cool.'
        },
        {
            'author': {'nickname': 'Dave'},
            'body': 'Oh my goodness..'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
