from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Alexandr'}
    posts = [{
    'author':{'username':'John'},
    'body': 'Beautiful day in Portland'
    },
    {
        'author':{'username':'Susan'},
        'body': 'The Avengers movie was so cool'
    },
    {
        'author':{'username':'Igor'},
        'body': 'I hate fish!!!'
    }]
    return render_template('index.html', user=user, title='Home', posts=posts)