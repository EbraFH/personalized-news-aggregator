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
