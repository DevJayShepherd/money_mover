from models.core_models import User


class UserManagement:
    """
    A simple class to store user management methods
    """

    @staticmethod
    def get_current_user(email):
        user = User.query.filter(User.email == email).first()
        return user
