from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    number_of_transactions = db.Column(db.Integer, nullable=False, default=0)
    transactions = db.relationship('Transaction', backref='users')


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    destination_wallet = db.Column(db.String(120), nullable=False)
    date_sent = db.Column(db.DateTime, onupdate=datetime.now(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

