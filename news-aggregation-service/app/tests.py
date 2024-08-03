import unittest
from unittest.mock import patch
from app.manager import NewsManager

class NewsServiceTests(unittest.TestCase):

    def setUp(self):
        self.news_manager = NewsManager()

    @patch('app.accessor.NewsAccessor.fetch_news')
    @patch('app.accessor.TextSummarizer.summarize_text')
    def test_aggregate_news(self, mock_summarize, mock_fetch):
        mock_fetch.return_value = {'results': [{'description': 'Test news'}]}
        mock_summarize.return_value = 'Summarized news'

        result = self.news_manager.aggregate_news('technology')

        self.assertEqual(result, ['Summarized news'])
        mock_fetch.assert_called_once_with('technology')
        mock_summarize.assert_called_once_with('Test news')

if __name__ == '__main__':
    unittest.main()