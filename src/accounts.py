# --- accounts.py --
# Contains code for managing your account

accounts = {}  # dictionary where key is the  password and value is User

# Write a function adds user details to accounts


def add_account(name, password):
    """
    Adds the key value pair to the accounts dictionary
    """
    accounts.update(name=password)


def login(name, password):
    """
    returns true if the password and corresponding name exist in the
    accounts dicitionary
    """
    if name in accounts and password in accounts:
        return True

