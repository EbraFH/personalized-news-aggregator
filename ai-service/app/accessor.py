from transformers import pipeline
from semantic_kernel import Kernel
import logging

class AIAccessor:
    """Accessor class for interacting with external AI APIs to generate summaries."""

    def __init__(self):
        self.summarizer = pipeline("summarization")
        self.kernel = Kernel()

    def generate_summary(self, articles):
        """Generate summaries for the given news articles using Hugging Face API."""
        try:
            summaries = self.summarizer(articles, max_length=130, min_length=30, do_sample=False)
            return [summary['summary_text'] for summary in summaries]
        except Exception as e:
            logging.error(f"Failed to generate summary: {str(e)}")
            raise

    def generate_summary_with_kernel(self, articles):
        """Generate summaries for the given news articles using Semantic Kernel."""
        try:
            return [self.kernel.summarize(article) for article in articles]
        except Exception as e:
            logging.error(f"Failed to generate summary with Semantic Kernel: {str(e)}")
            raise