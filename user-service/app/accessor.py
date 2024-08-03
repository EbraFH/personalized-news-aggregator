from app.resource import User, Preferences

class UserAccessor:
    """Accessor class for user database operations."""

    def __init__(self, db):
        self.db = db

    def create_user(self, email, preferences):
        """Create a new user."""
        user = User(email=email)
        self.db.session.add(user)
        self.db.session.commit()
        self.add_preferences(user.id, preferences)
        return user

    def get_user_by_email(self, email):
        """Get a user by email."""
        return User.query.filter_by(email=email).first()

    def add_preferences(self, user_id, preferences):
        """Add user preferences."""
        for category, frequency in preferences.items():
            pref = Preferences(user_id=user_id, category=category, frequency=frequency)
            self.db.session.add(pref)
        self.db.session.commit()

    def update_preferences(self, user_id, preferences):
        """Update user preferences."""
        Preferences.query.filter_by(user_id=user_id).delete()
        self.add_preferences(user_id, preferences)