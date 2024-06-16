from flask import jsonify, request
from app import db
from app.database.models import Users
from . import api_bp

@api_bp.route('/users/', methods=['GET'])
def get_users():
    users = Users.query.all()
    return jsonify([{'id': user.id, 'email': user.email, 'name': user.name, 'age': user.age,
                     'description': user.description, 'profession': user.profession} for user in users])

@api_bp.route('/users/', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = Users(
        email=data['email'],
        name=data['name'],
        age=data['age'],
        description=data['description'],
        profession=data['profession']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201


