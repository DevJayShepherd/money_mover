from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from webapp.config import settings

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.secret_key = settings.SECRET_KEY
db = SQLAlchemy(app)
