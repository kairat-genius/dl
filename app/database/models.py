from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Personnel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(200))
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    profession = db.Column(db.String(200))
    img = db.Column(db.LargeBinary)

    def __repr__(self):
        return f"<Personnel {self.id}>"



class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Users {self.email}>"
