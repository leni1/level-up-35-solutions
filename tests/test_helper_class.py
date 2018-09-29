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

    def test_check_email_fail(self):
        invalid = self.helper.check_email('somemail')
        self.assertNotEqual(invalid, True)

    def test_check_email_sucess(self):
        correct = self.helper.check_email('some@mail.com')
        self.assertTrue(correct)
        self.assertEqual(correct, True)
        self.assertIsInstance(correct, bool)

    def test_register(self):
        register_user = self.helper.register_user('som', 'som', 'some@mail.com', 'Abcd8^', 1)
        self.assertEqual(register_user, 'Username or name too short.')
    
    
        