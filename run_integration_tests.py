import requests
import unittest

BASE_URL = "http://localhost:5000/api"

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.test_email = "test@example.com"
        self.test_password = "testpassword"
        self.token = None

    def tearDown(self):
        # Clean up: Delete test user if exists
        if self.token:
            headers = {"Authorization": f"Bearer {self.token}"}
            requests.delete(f"{BASE_URL}/user", headers=headers)

    def test_user_flow(self):
        # Register
        register_data = {
            "email": self.test_email,
            "password": self.test_password,
            "preferences": "technology,science"
        }
        response = requests.post(f"{BASE_URL}/register", json=register_data)
        self.assertEqual(response.status_code, 201)

        # Login
        login_data = {"email": self.test_email, "password": self.test_password}
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        self.assertEqual(response.status_code, 200)
        self.token = response.json()["access_token"]

        # Update preferences
        headers = {"Authorization": f"Bearer {self.token}"}
        pref_data = {"preferences": "sports,entertainment"}
        response = requests.post(f"{BASE_URL}/preferences", json=pref_data, headers=headers)
        self.assertEqual(response.status_code, 200)

        # Fetch news
        response = requests.get(f"{BASE_URL}/news", headers=headers)
        self.assertEqual(response.status_code, 200)
        news_data = response.json()
        self.assertIn("news_summary", news_data)
        self.assertTrue(len(news_data["news_summary"]) > 0)

    def test_invalid_login(self):
        login_data = {"email": "nonexistent@example.com", "password": "wrongpassword"}
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unittest.main()