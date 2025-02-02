from app.engine import UserEngine

class UserManager:
    """Manager class for user operations."""

    def __init__(self, db):
        self.user_engine = UserEngine(db)

    def create_user(self, email, preferences):
        """Create a new user."""
        return self.user_engine.create_user(email, preferences)

    def get_user_by_email(self, email):
        """Get a user by email."""
        return self.user_engine.get_user_by_email(email)

    def update_preferences(self, user_id, preferences):
        """Update user preferences."""
        return self.user_engine.update_preferences(user_id, preferences)