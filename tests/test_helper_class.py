import unittest

from models.helper_class import Helper

class UserTest(unittest.TestCase):

    def setUp(self):
        self.helper = Helper()
        self.helper.user_db = []

    def tearDown(self):
        self.helper.user_db = []

    def test_attributes_of_helper(self):
        attrs = {'check_password', 'check_email', 'register_user',
                 'login_user', 'reset_password', 'return_info'}
        for attr in attrs:
            self.assertIn(attr, attrs, msg='{} attribute missing.'.format(attr))

    def test_check_password_too_short(self):
        wrong = self.helper.check_password('som')
        self.assertEqual(wrong, 'Password too short.')

    def test_check_password_no_digit(self):
        wrong = self.helper.check_password('some')
        self.assertEqual(wrong, 'Password has no digit.')

    def test_check_password_no_uppercase(self):
        wrong = self.helper.check_password('som98')
        self.assertEqual(wrong, 'Password has no capital letter.')

    def test_check_password_no_lowercase(self):
        wrong = self.helper.check_password('SOM98')
        self.assertEqual(wrong, 'Password has no lowercase letter.')

    def test_check_password_no_symbol(self):
        wrong = self.helper.check_password('s98A')
        self.assertEqual(wrong, 'Password has no special character.')

    def test_check_password_success(self):
        correct = self.helper.check_password('s98A$')
        self.assertTrue(correct)

    def test_check_email_fail(self):
        invalid = self.helper.check_email('somemail')
        self.assertNotEqual(invalid, True)

    def test_check_email_sucess(self):
        correct = self.helper.check_email('some@mail.com')
        self.assertTrue(correct)
        self.assertEqual(correct, True)
        self.assertIsInstance(correct, bool)

    def test_register_name_short(self):
        name1 = self.helper.register_user('som', 'som', 'some@mail.com', 'Abcd8^', 1)
        name2 = self.helper.register_user('som', 'some', 'some@mail.com', 'Abcd8^', 1)
        self.assertEqual(name1, 'Username or name too short.')
        self.assertEqual(name2, 'Username or name too short.')


    def test_register_name_same(self):
        name1 = self.helper.register_user('some', 'some', 'some@mail.com', 'Abcd8^', 1)
        name2 = self.helper.register_user('SOME', 'some', 'some@mail.com', 'Abcd8^', 1)
        self.assertEqual(name1, 'Name and username cannot be the same.')
        self.assertEqual(name2, 'Name and username cannot be the same.')

    def test_register_invalid_age_cases(self):
        invalid_1 = self.helper.register_user('some', 'some', 'some@mail.com', 'Abcd8^', '1')
        invalid_2 = self.helper.register_user('some', 'some', 'some@mail.com', 'Abcd8^', 0)
        self.assertEqual(invalid_1, 'Invalid age.')
        self.assertEqual(invalid_2, 'Invalid age.')

    def test_invalid_email_valid_password(self):
        invalid = self.helper.register_user('Jack', 'someJack', 'some.com', 'Abcd8^', 1)
        self.assertFalse(invalid)

    def test_invalid_email_invalid_password(self):
        invalid = self.helper.register_user('Jack', 'someJack', 'some.com', 'Abcd8', 1)
        self.assertFalse(invalid)

    def test_valid_password_invalid_email(self):
        invalid = self.helper.register_user('Jack', 'someJack', 'some.com', 'Abcd8^', 1)
        self.assertFalse(invalid)

    def test_valid_email_valid_password(self):
        valid = self.helper.register_user('Jack', 'someJack', 'some@mail.com', 'Abcd8^', 1)
        self.assertTrue(valid)

    def test_register_user_entry_is_in_db(self):
        valid = self.helper.register_user('Jack', 'someJack', 'some@mail.com', 'Abcd8^', 1)
        self.assertNotEqual(len(self.helper.user_db), 0)

    def test_login_user_invalid(self):
        self.helper.register_user('Jack', 'someJack', 'some@mail.com', 'Abcd8^', 1)
        invalid = self.helper.login_user('some@mail.com', 'Abcd8')
        invalid_2 = self.helper.login_user('somemail.com', 'Abcd8^')
        self.assertFalse(invalid)
        self.assertFalse(invalid_2)

    def test_login_user_valid(self):
        self.helper.register_user('Jack', 'someJack', 'some@mail.com', 'Abcd8^', 1)
        valid = self.helper.login_user('some@mail.com', 'Abcd8^')
        self.assertTrue(valid)
        if valid:
            for user in self.helper.user_db:
                self.assertEqual(user.logged_in, True)

    def test_reset_password_success(self):
        self.helper.register_user('Jack', 'someJack', 'some@mail.com', 'Abcd8^', 1)
        self.helper.login_user('some@mail.com', 'Abcd8^')
        for user in self.helper.user_db:
            old_password = user.password
            self.helper.reset_password('Abcd8*')
            self.assertNotEqual(old_password, user.password)

    def test_reset_password_fail(self):
        self.helper.register_user('Jack', 'someJack', 'some@mail.com', 'Abcd8^', 1)
        for user in self.helper.user_db:
            self.helper.reset_password('Abcd8*')
            self.assertNotEqual('Abcd8*', user.password)

    def test_return_info_success(self):
        self.helper.register_user('Jack', 'someJack', 'some@mail.com', 'Abcd8^', 1)
        self.helper.login_user('some@mail.com', 'Abcd8^')
        for user in self.helper.user_db:
            user_info = self.helper.return_info()
            self.assertIsInstance(user_info, dict)

    def test_return_info_fail(self):
        self.helper.register_user('Jack', 'someJack', 'some@mail.com', 'Abcd8^', 1)
        for user in self.helper.user_db:
            user_info = self.helper.return_info()
            self.assertFalse(user_info)
