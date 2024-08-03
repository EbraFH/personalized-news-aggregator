import unittest
from app import create_app
from app.resource import db, User, Preferences

class UserServiceTests(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.app, self.db = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Tear down test variables."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_user(self):
        """Test user registration."""
        response = self.client.post('/api/register', json={
            'email': 'test@example.com', 
            'preferences': {'technology': 'daily', 'science': 'weekly'}
        })
        self.assertEqual(response.status_code, 201)
        user = User.query.filter_by(email='test@example.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(len(user.preferences), 2)

    def test_login_user(self):
        """Test user login."""
        self.client.post('/api/register', json={
            'email': 'test@example.com', 
            'preferences': {'technology': 'daily'}
        })
        response = self.client.post('/api/login', json={'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

if __name__ == '__main__':
    unittest.main()