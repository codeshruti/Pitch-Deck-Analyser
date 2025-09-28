"""
PDF parser module for extracting text from PDF pitch decks.

This module provides functionality to extract text content from PDF files
using PyPDF2, handling multi-page documents and formatting issues.
"""

from PyPDF2 import PdfReader


def parse_pdf(filepath):
    """
    Extract text content from a PDF file.
    
    This function reads a PDF file and extracts all text content from each page,
    concatenating them into a single string for further processing.
    
    Args:
        filepath (str): Path to the PDF file to parse.
        
    Returns:
        dict: Dictionary containing:
            - source (str): File format identifier ("pdf")
            - raw_text (str): Extracted text content from all pages
            
    Note:
        The function handles empty pages gracefully by checking if text
        extraction returns non-empty content before adding to the result.
        Each page's text is separated by a newline character.
    """
    reader = PdfReader(filepath)
    text = ""
    
    # Extract text from each page
    for page in reader.pages:
        t = page.extract_text()
        # Only add non-empty text to avoid unnecessary newlines
        if t:
            text += t + "\n"
    
    return {
        "source": "pdf",
        "raw_text": text
    }
