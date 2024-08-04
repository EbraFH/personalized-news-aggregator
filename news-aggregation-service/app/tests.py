import unittest
from unittest.mock import patch, MagicMock
from app.manager import NewsManager

class NewsServiceTests(unittest.TestCase):

    def setUp(self):
        self.news_manager = NewsManager()

    @patch('app.accessor.NewsAccessor.fetch_news')
    @patch('app.accessor.TextSummarizer.summarize_text')
    def test_aggregate_news_success(self, mock_summarize, mock_fetch):
        mock_fetch.return_value = {'results': [{'description': 'Test news 1'}, {'description': 'Test news 2'}]}
        mock_summarize.side_effect = ['Summary 1', 'Summary 2']

        result = self.news_manager.aggregate_news('technology')

        self.assertEqual(result, ['Summary 1', 'Summary 2'])
        mock_fetch.assert_called_once_with('technology')
        self.assertEqual(mock_summarize.call_count, 2)

    @patch('app.accessor.NewsAccessor.fetch_news')
    def test_aggregate_news_fetch_failure(self, mock_fetch):
        mock_fetch.side_effect = Exception("API error")

        with self.assertRaises(Exception):
            self.news_manager.aggregate_news('technology')

    @patch('app.accessor.NewsAccessor.fetch_news')
    @patch('app.accessor.TextSummarizer.summarize_text')
    def test_aggregate_news_summarize_failure(self, mock_summarize, mock_fetch):
        mock_fetch.return_value = {'results': [{'description': 'Test news'}]}
        mock_summarize.side_effect = Exception("Summarization error")

        with self.assertRaises(Exception):
            self.news_manager.aggregate_news('technology')

if __name__ == '__main__':
    unittest.main()