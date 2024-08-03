import unittest
from app.manager import AIManager

class AIServiceTest(unittest.TestCase):
    """Unit tests for the AI service."""

    def setUp(self):
        self.ai_manager = AIManager()

    def test_generate_summary(self):
        """Test generating a summary for articles."""
        articles = [
            "This is the content of article 1.",
            "This is the content of article 2."
        ]
        try:
            summary = self.ai_manager.generate_summary(articles)
            self.assertIsInstance(summary, list)
            self.assertGreater(len(summary), 0)
            for item in summary:
                self.assertIsInstance(item, str)
        except Exception as e:
            self.fail(f"generate_summary raised an exception: {str(e)}")

    def test_generate_summary_with_kernel(self):
        """Test generating a summary for articles using Semantic Kernel."""
        articles = [
            "This is the content of article 1.",
            "This is the content of article 2."
        ]
        try:
            summary = self.ai_manager.generate_summary_with_kernel(articles)
            self.assertIsInstance(summary, list)
            self.assertGreater(len(summary), 0)
            for item in summary:
                self.assertIsInstance(item, str)
        except Exception as e:
            self.fail(f"generate_summary_with_kernel raised an exception: {str(e)}")

if __name__ == '__main__':
    unittest.main()