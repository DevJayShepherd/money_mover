from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128))
    balance = db.Column(db.Integer, nullable=False)
    number_of_transactions = db.Column(db.Integer, nullable=False, default=0)
    transactions = db.relationship('Transaction', backref='users')

    # Password hashing methods
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    destination_wallet = db.Column(db.String(120), nullable=False)
    date_sent = db.Column(db.DateTime, onupdate=datetime.now(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
