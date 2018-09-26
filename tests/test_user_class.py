import unittest

from models.user_class import User


class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = User('chicken', 5,
                         'chick@chi.chi', 'somepassword',
                         'chicky')

    def test_user_has_logged_in_attribute(self):
        self.assertTrue(hasattr(User, 'logged_in'),
                        msg='\'logged\' in argument is missing')

    def test_user_class_has_valid_properties(self):
        args = {'name', 'user_name', 'email', 'age', 'password'}
        for arg in args:
            self.assertTrue(hasattr(self.user, arg),
                            msg='{} argument is missing.'.format(arg))

    def test_user_instance_valid(self):
        self.assertIsInstance(self.user, User)

    def test_login_attribute_false(self):
        self.assertEqual(self.user.logged_in, False)

    def test_login_attribute_can_be_set(self):
        self.user.logged_in = True
        self.assertEqual(self.user.logged_in, True)

    def test_login_attribute_can_have_diff_values_per_user(self):
        self.user_2 = User('chicken', 5, 'chick@chi.chi',
                           'somepassword', 'chicky')
        self.user_2.logged_in = True
        self.assertEqual(self.user.logged_in, False)
        self.assertEqual(self.user_2.logged_in, True)
