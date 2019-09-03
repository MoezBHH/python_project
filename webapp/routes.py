from flask import render_template
from webapp import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Guest'}
    return render_template('index.html', title="Page d'accueil", user=user)