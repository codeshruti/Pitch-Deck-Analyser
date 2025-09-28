"""
Test module for the PowerPoint parser functionality.

This module contains unit tests for the parse_ppt function,
verifying that it correctly extracts text from PowerPoint files.
"""

from utils.ppt_parser import parse_ppt


def test_ppt_parser():
    """
    Test the parse_ppt function with a sample PowerPoint file.
    
    This test verifies that the parse_ppt function correctly:
    1. Extracts text content from a PowerPoint file
    2. Returns a dictionary with the expected structure
    3. Contains 'raw_text' key with string content
    
    Note:
        Requires a sample PowerPoint file at 'tests/sample.pptx' to run successfully.
    """
    data = parse_ppt("tests/sample_ppt.pptx")
    assert "raw_text" in data and isinstance(data["raw_text"], str)
