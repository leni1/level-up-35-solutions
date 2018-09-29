"""Helper class"""
import re

from .user_class import User

class Helper:

    user_db = []

    def check_password(self, password):

        digit = re.search(r"\d", password)
        uppercase = re.search(r"[A-Z]", password)
        lowercase = re.search(r"[a-z]", password)
        symbol = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]',
                                 password)

        if len(password) < 4:
            return 'Password too short.'
        if not digit:
            return 'Password has no digit.'
        if not uppercase:
            return 'Password has no capital letter.'
        if not lowercase:
            return 'Password has no lowercase letter.'
        if not symbol:
            return 'Password has no special character.'
        return True

    def check_email(self, email):
        correct_email = re.search(
            r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email)
        if not correct_email:
            return 'Invalid e-mail.'
        return True

    def register_user(self, name, username, email, password, age):
        if len(username) < 4 or len(name) < 4:
            return 'Username or name too short.'

        if not isinstance(age, int) or age <= 0:
            return 'Invalid age.'

        if name.lower() == username.lower():
            return 'Name and username cannot be the same.'

        valid_email = self.check_email(email)
        valid_password = self.check_password(password)

        if isinstance(valid_email, bool) and isinstance(valid_password, bool):
            new_user = User(name, age, email, password, username)
            self.user_db.append(new_user)
            return True
        return False

    def login_user(self, email, password):
        for user in self.user_db:
            if user.email == email and user.password == password:
                user.logged_in = True
                return True
        return False

    def reset_password(self, new_password):
        for user in self.user_db:
            if user.logged_in:
                user.password = new_password
            return True

    def return_info(self):
        for user in self.user_db:
            if user.logged_in:
                return vars(user)
        return False

