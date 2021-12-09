from flask import render_template, request, jsonify, url_for, redirect
from app import app
from models.core_models import User


@app.route('/')
def homepage():
    return render_template('home_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check user exists first
        if User.query.filter_by(email=email).first():
            user = User.query.filter_by(email=email).first()
        else:
            return jsonify(message="User or password incorrect"), 400
            # Frontend will do something here like flash message or on API I would raise exception
            # TODO Raise exception or flash message

        # Check user password is correct
        if user.check_password(password=password):
            return redirect(url_for('homepage'))
        else:
            return jsonify(message="User or password incorrect"), 400
            # Frontend will do something here like flash message or on API I would raise exception
            # TODO Raise exception or flash message

    return render_template('login.html')
