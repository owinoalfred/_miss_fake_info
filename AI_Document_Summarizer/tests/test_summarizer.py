import unittest
from summarizer import summarize_document

class TestSummarizer(unittest.TestCase):
    def test_summary_length(self):
        doc = "This is a long document for testing summarization."
        summary = summarize_document(doc)
        self.assertTrue(len(summary) < len(doc))
