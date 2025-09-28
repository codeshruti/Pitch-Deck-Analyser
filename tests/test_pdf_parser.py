"""
Test module for the PDF parser functionality.

This module contains unit tests for the parse_pdf function,
verifying that it correctly extracts text from PDF files.
"""

from utils.pdf_parser import parse_pdf


def test_pdf_parser():
    """
    Test the parse_pdf function with a sample PDF file.
    
    This test verifies that the parse_pdf function correctly:
    1. Extracts text content from a PDF file
    2. Returns a dictionary with the expected structure
    3. Contains 'raw_text' key with string content
    
    Note:
        Requires a sample PDF file at 'tests/sample.pdf' to run successfully.
    """
    data = parse_pdf("tests/sample_pdf.pdf")
    assert "raw_text" in data and isinstance(data["raw_text"], str)
