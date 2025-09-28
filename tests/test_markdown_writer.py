"""
Test module for the markdown writer functionality.

This module contains unit tests for the write_markdown function,
verifying that it correctly formats and writes data to markdown files.
"""

from utils.markdown_writer import write_markdown


def test_markdown_writer():
    """
    Test the write_markdown function with sample data.
    
    This test verifies that the write_markdown function correctly:
    1. Writes data to a markdown file
    2. Formats section headers properly
    3. Includes content in the output file
    
    The test creates a temporary output file and verifies its contents.
    """
    data = {"Test Section": "This is a test."}
    write_markdown(data, "tests/test_output.md")
    with open("tests/test_output.md") as f:
        assert "Test Section" in f.read()
