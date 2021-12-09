from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import settings

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
