from transformers import pipeline
from semantic_kernel import Kernel

class AIAccessor:
    """
    Accessor class for interacting with the external AI API to generate summaries.
    """

    def __init__(self):
        self.summarizer = pipeline("summarization")
        self.kernel = Kernel()

    def generate_summary(self, articles):
        """
        Generate a summary for the given news articles using Hugging Face API.
        """
        try:
            summaries = self.summarizer(articles, max_length=130, min_length=30, do_sample=False)
            return [summary['summary_text'] for summary in summaries]
        except Exception as e:
            raise Exception(f"Failed to generate summary: {str(e)}")

    def generate_summary_with_kernel(self, articles):
        """
        Generate a summary for the given news articles using Semantic Kernel.
        """
        try:
            summaries = [self.kernel.summarize(article) for article in articles]
            return summaries
        except Exception as e:
            raise Exception(f"Failed to generate summary with Semantic Kernel: {str(e)}")
