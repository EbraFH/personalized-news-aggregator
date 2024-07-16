from app import db
from app.resource import User

class UserAccessor:
    """
    Accessor class for user database operations.
    """

    def create_user(self, email, preferences):
        """
        Create a new user.
        """
        user = User(email=email, preferences=preferences)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_email(self, email):
        """
        Get a user by email.
        """
        return User.query.filter_by(email=email).first()

    def update_preferences(self, email, preferences):
        """
        Update user preferences.
        """
        user = self.get_user_by_email(email)
        if user:
            user.preferences = preferences
            db.session.commit()
            return user
        else:
            raise ValueError("User not found")
