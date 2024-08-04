import unittest
from unittest.mock import patch
from app.manager import AIManager

class AIServiceTest(unittest.TestCase):
    """Unit tests for the AI service."""

    def setUp(self):
        self.ai_manager = AIManager()

    @patch('app.accessor.AIAccessor.generate_summary')
    def test_generate_summary(self, mock_generate_summary):
        """Test generating a summary for articles."""
        articles = [
            "This is the content of article 1.",
            "This is the content of article 2."
        ]
        mock_generate_summary.return_value = ["Summary 1", "Summary 2"]
        
        summary = self.ai_manager.generate_summary(articles)
        
        self.assertIsInstance(summary, list)
        self.assertEqual(len(summary), 2)
        for item in summary:
            self.assertIsInstance(item, str)

    @patch('app.accessor.AIAccessor.generate_summary_with_kernel')
    def test_generate_summary_with_kernel(self, mock_generate_summary_with_kernel):
        """Test generating a summary for articles using Semantic Kernel."""
        articles = [
            "This is the content of article 1.",
            "This is the content of article 2."
        ]
        mock_generate_summary_with_kernel.return_value = ["Summary 1", "Summary 2"]
        
        summary = self.ai_manager.generate_summary_with_kernel(articles)
        
        self.assertIsInstance(summary, list)
        self.assertEqual(len(summary), 2)
        for item in summary:
            self.assertIsInstance(item, str)

if __name__ == '__main__':
    unittest.main()