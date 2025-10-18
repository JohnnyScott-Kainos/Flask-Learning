from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route("/")
def home():
    return render_template('base.html')

@app.route("/index")
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/thoughts')
def thoughts():
    thoughts = [
        "I wonder what the future holds.",
        "Is technology advancing too quickly?",
        "How can we make the world a better place?"
    ]
    return render_template('thoughts.html', title='Thoughts', thoughts=thoughts)
