from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User resource model."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    preferences = db.relationship('Preferences', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def to_dict(self):
        """Convert User object to dictionary."""
        return {
            'id': self.id,
            'email': self.email,
            'preferences': [pref.to_dict() for pref in self.preferences]
        }

class Preferences(db.Model):
    """Preferences resource model."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    frequency = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert Preferences object to dictionary."""
        return {
            'id': self.id,
            'category': self.category,
            'frequency': self.frequency
        }