from flask import jsonify, request
from app import db
from app.database.models import Personnel
from . import api_bp

@api_bp.route('/personnel/', methods=['GET'])
def get_personnel():
    users = Personnel.query.all()
    return jsonify([{'id': user.id, 'email': user.email, 'name': user.name, 'age': user.age,
                     'description': user.description, 'profession': user.profession} for user in users])

@api_bp.route('/personnel/', methods=['POST'])
def add_personnel():
    data = request.get_json()
    new_user = Personnel(
        email=data['email'],
        name=data['name'],
        age=data['age'],
        description=data['description'],
        profession=data['profession']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Personnel added successfully'}), 201


