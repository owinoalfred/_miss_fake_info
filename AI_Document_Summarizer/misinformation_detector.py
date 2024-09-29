# misinformation_detector.py

from transformers import pipeline

class MisinformationDetector:
    def __init__(self):
        # Initialize a zero-shot classification model for detecting misinformation
        self.classifier = pipeline("zero-shot-classification")

    def check_misinformation(self, statement):
        # Define candidate labels for classification
        candidate_labels = ["true", "false", "unverified"]
        
        # Run classification
        result = self.classifier(statement, candidate_labels)
        
        # Return the classification result
        return {
            "label": result["labels"][0],  # The most probable label
            "score": result["scores"][0]    # The score for that label
        }

# Example usage (can be removed or commented out in production)
if __name__ == "__main__":
    detector = MisinformationDetector()
    statement = "The Earth is flat."
    result = detector.check_misinformation(statement)
    print(f"Statement: '{statement}' - Detection Result: {result}")
