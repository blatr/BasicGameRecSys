from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    login_form = LoginForm()
    return render_template('front.html', form=login_form)