# app.py

import streamlit as st
from summarizer import DocumentSummarizer
from misinformation_detector import MisinformationDetector  # Import the detector

# Initialize the summarizer and detector
summarizer = DocumentSummarizer()
detector = MisinformationDetector()

st.title("Document Summarizer and Misinformation Detector")

# Input for document summarization
document_input = st.text_area("Enter the document text to summarize:")

if st.button("Summarize"):
    if document_input:
        summary = summarizer.summarize(document_input)
        st.subheader("Summary")
        st.write(summary)
        
        # Check the summarized text for misinformation
        check_result = detector.check_misinformation(summary)  # Check the summary
        st.subheader("Misinformation Check Result")
        st.write(check_result)  # Display the result
    else:
        st.warning("Please enter a document to summarize.")

# Input for misinformation check (optional)
claim_input = st.text_area("Enter a claim to check for misinformation:")

if st.button("Check Misinformation"):
    if claim_input:
        check_result = detector.check_misinformation(claim_input)  # Use the detector
        st.subheader("Misinformation Check Result for Claim")
        st.write(check_result)
    else:
        st.warning("Please enter a claim to check.")
