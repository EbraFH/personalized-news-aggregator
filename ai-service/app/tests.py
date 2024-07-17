import unittest
from app.manager import AIManager

class AIServiceTest(unittest.TestCase):
    """
    Unit tests for the AI service.
    """

    def setUp(self):
        self.ai_manager = AIManager()

    def test_generate_summary(self):
        """
        Test generating a summary for articles.
        """
        articles = [
            {"title": "Article 1", "content": "This is the content of article 1."},
            {"title": "Article 2", "content": "This is the content of article 2."}
        ]
        try:
            summary = self.ai_manager.generate_summary(articles)
            success = True
        except Exception:
            success = False
            summary = []
        
        # Check that summary was successfully generated
        self.assertTrue(success)
        # Check that summary is not empty
        self.assertIsInstance(summary, list)
        self.assertGreater(len(summary), 0)
        # Check that the summary contains strings
        for item in summary:
            self.assertIsInstance(item, str)

if __name__ == '__main__':
    unittest.main()
