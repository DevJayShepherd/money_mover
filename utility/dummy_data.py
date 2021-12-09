from app import db
from models.core_models import User, Transaction

# Create the tables based on the imported models
db.create_all()
db.session.commit()

# Create some dummy data
user = User(name='user', email='user@example.com', balance=1500, number_of_transactions=0)
transaction_one = Transaction(amount=25, destination_wallet='12hggftt862h', user_id=1)

db.session.add(user)
db.session.add(transaction_one)
db.session.commit()
