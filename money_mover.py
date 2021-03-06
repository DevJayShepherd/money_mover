from flask import render_template, request, jsonify, url_for, redirect, session
from app import app
from webapp.models.core_models import User, Transaction
from webapp.utility.user_management import UserManagement


@app.route('/')
def homepage():
    try:
        # Retrieve the current user
        user = UserManagement.get_current_user(session['email'])
        if user:
            return render_template('home_page.html')
    except KeyError:
        # Happens when no session has been created
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check user exists first
        if User.query.filter_by(email=email).first():
            user = User.query.filter_by(email=email).first()
        else:
            return jsonify(message='User or password incorrect'), 400
            # Frontend will do something here like flash message or on API I would raise exception
            # TODO Raise exception or flash message

        # Check user password is correct
        if user.check_password(password=password):
            # Begin the users session
            session['email'] = request.form['email']
            return redirect(url_for('homepage'))
        else:
            return jsonify(message='User or password incorrect'), 400
            # Frontend will do something here like flash message or on API I would raise exception
            # TODO Raise exception or flash message

    return render_template('login.html')


@app.route('/activity')
def transactions():
    try:
        # Retrieve the current user
        user = UserManagement.get_current_user(session['email'])
        # Retrieve a list of transactions for current user
        list_transactions = Transaction.query.filter_by(user_id=user.id)
        return render_template('transactions.html', transactions=list_transactions)
    except KeyError:
        # Happens when no session has been created
        return redirect(url_for('login'))


@app.route('/activity/details/<transaction_id>')
def transaction_details(transaction_id):
    try:
        # Retrieve the current user
        if UserManagement.get_current_user(session['email']):
            # Retrieve a list of transactions for current user
            the_transaction = Transaction.query.filter_by(id=transaction_id).first()
            return render_template('transaction_details.html', transaction=the_transaction)
    except KeyError:
        # Happens when no session has been created
        return redirect(url_for('login'))
