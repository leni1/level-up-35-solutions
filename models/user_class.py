"""User class"""
class User:
    """Instance variable for log in status"""
    logged_in = False

    def __init__(self, name, age, email, password, user_name):
        self.name = name
        self.user_name = user_name
        self.age = age
        self.email = email
        self.password = password
