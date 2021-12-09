from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI


db = SQLAlchemy(app)

@app.route('/')
def homepage():
    return render_template('home_page.html')
