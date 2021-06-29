#!/usr/bin/python3
"""Module tests for usr.py"""

import models
import unittest
from models.user import User


class testUser_instantination(unittest.TestCase):
    """Test for instantiation"""

    def test_no_args_instantinates(self):
        self.assertEqual(User, type(User()))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

if __name__ == "__main__":
    unittest.main()
