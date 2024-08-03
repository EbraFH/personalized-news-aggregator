from app.accessor import UserAccessor

class UserEngine:
    """Engine class for user business logic."""

    def __init__(self, db):
        self.user_accessor = UserAccessor(db)

    def create_user(self, email, preferences):
        """Create a new user."""
        return self.user_accessor.create_user(email, preferences)

    def get_user_by_email(self, email):
        """Get a user by email."""
        return self.user_accessor.get_user_by_email(email)

    def update_preferences(self, user_id, preferences):
        """Update user preferences."""
        return self.user_accessor.update_preferences(user_id, preferences)