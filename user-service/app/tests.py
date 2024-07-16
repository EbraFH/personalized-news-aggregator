"""
User Service Tests
"""

import unittest
from app import app, db
from app.resource import User

class UserServiceTests(unittest.TestCase):

    def setUp(self):
        """
        Set up test variables.
        """
        self.app = app.test_client()
        self.app.testing = True

        db.create_all()

    def tearDown(self):
        """
        Tear down test variables.
        """
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        """
        Test user registration.
        """
        response = self.app.post('/api/register', json={'email': 'test@example.com', 'preferences': 'technology'})
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        """
        Test user login.
        """
        self.app.post('/api/register', json={'email': 'test@example.com', 'preferences': 'technology'})
        response = self.app.post('/api/login', json={'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
