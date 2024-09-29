# summarizer.py

from transformers import pipeline

class DocumentSummarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization")

    def summarize(self, text):
        summary = self.summarizer(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']

# Example usage
if __name__ == "__main__":
    summarizer = DocumentSummarizer()
    text = "Your long document text goes here."
    print(summarizer.summarize(text))
