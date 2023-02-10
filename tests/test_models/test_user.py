#!/usr/bin/python3
"""
unit test for User class
"""
import unittest
from models.user import User


class UserTest(TestCase):
    """ test case class for User class """
    def test_type(self):
        """ checks the type of the attribute """
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_attr(self):
        """ tests if the given attribute exists """
        user = User()
        self.assertTrue(user, 'email')
        self.assertTrue(user, 'password')
        self.assertTrue(user, 'first_name')
        self.assertTrue(user, 'last_name')

if __name__ == '__main__':
    unittest.main()
