import requests
import unittest

BASE_URL = "http://localhost:5000/api"

class IntegrationTests(unittest.TestCase):
    def test_user_registration_and_login(self):
        # Register a new user
        register_data = {
            "email": "test@example.com",
            "preferences": "technology,science"
        }
        response = requests.post(f"{BASE_URL}/register", json=register_data)
        self.assertEqual(response.status_code, 201)

        # Login with the registered user
        login_data = {"email": "test@example.com"}
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())

    def test_news_fetching(self):
        # Login to get the token
        login_data = {"email": "test@example.com"}
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        token = response.json()["access_token"]

        # Fetch news
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(f"{BASE_URL}/news", json=login_data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("news_summary", response.json())

    def test_preference_update(self):
        # Login to get the token
        login_data = {"email": "test@example.com"}
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        token = response.json()["access_token"]

        # Update preferences
        headers = {"Authorization": f"Bearer {token}"}
        pref_data = {
            "email": "test@example.com",
            "preferences": "sports,entertainment"
        }
        response = requests.post(f"{BASE_URL}/preferences", json=pref_data, headers=headers)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()