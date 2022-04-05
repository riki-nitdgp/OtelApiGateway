
class User:

    def __init__(self, username: str, phone_number: int, email: str):
        self.username = username
        self.phone_number = phone_number
        self.email = email



    @classmethod
    def user_info(cls, user: dict):
        if user:
            return User(
                user.get("username"),
                user.get("phone_number"),
                user.get("email")
            )
        else:
            return None
