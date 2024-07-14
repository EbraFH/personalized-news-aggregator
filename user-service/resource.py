from app import db

class User(db.Model):
    """
    User resource model.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    preferences = db.Column(db.String(120))

    def __repr__(self):
        return f'<User {self.email}>'
