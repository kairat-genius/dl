from app import db
from app.database.models import Users
from . import api_bp
from flask import jsonify, request
from app.auxiliary import create_token, redis_token_save


@api_bp.route('/user/register/', methods=['POST'])
def user_register():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400

    if Users.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email is already in use'}), 400

    token = create_token(data.get('email'))
    redis_token_save[data.get('email')] = token

    new_user = Users(email=data['email'])
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully', 'token': token}), 201




@api_bp.route('/user/login', methods=['POST'])
def user_login():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400

    user = Users.query.filter_by(email=data['email']).first()

    if user is None or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid email or password'}), 401

    token = create_token(data.get('email'))
    redis_token_save[data.get('email')] = token

    return jsonify({'message': 'Login successful', 'token': token}), 200


@api_bp.route('/user/', methods=['GET'])
def user_get():
    users = Users.query.all()
    return jsonify([{'id': user.id, 'email': user.email,} for user in users])