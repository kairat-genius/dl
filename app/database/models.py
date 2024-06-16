from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(200))
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    profession = db.Column(db.String(200))
    img = db.Column(db.LargeBinary)

    def __repr__(self):
        return f"<Users {self.id}>"