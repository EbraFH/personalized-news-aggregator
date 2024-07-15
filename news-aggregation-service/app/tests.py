"""
News Aggregation Service Tests
"""

import unittest
from app import app

class NewsServiceTests(unittest.TestCase):

    def setUp(self):
        """
        Set up test variables.
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_get_news(self):
        """
        Test fetching news.
        """
        response = self.app.post('/api/news', json={'preferences': 'technology'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
