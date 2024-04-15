from app import app 
from flask import render_template,flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    """Index URL"""
    return render_template('index.html' , title="Home page")

@app.route('/about-me')
def about_me():
    """ About-me URL"""
    return render_template('about_me.html', title="About me")

@app.route('/login' , methods=['GET','POST'])
def login():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You are requesting to log in {form.username.data}')
        return redirect(url_for('/index'))
    return render_template('login.html' , title="login", form=form)





