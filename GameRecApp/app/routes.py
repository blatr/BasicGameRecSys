from app import app
from flask import render_template, redirect, session, request
from app.forms import LoginForm
import requests


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        session['steamid'] = request.form['steamid'];
        return redirect('/rec')
    return render_template('front.html', form=login_form)


@app.route('/rec')
def rec():
    header = 'https://steamcdn-a.akamaihd.net/steam/apps/' + session['steamid'] + '/header.jpg'
    payload = {'key': '7304F7A4EA044CC7038ABAEC2973C0DF', 'appid': session['steamid']}
    game_data = requests.get("http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2", params=payload)
    game_title = game_data.json()['game']['gameName']

    return render_template('rec.html', header=header, game_title=game_title)
