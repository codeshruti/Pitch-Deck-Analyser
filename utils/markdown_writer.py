"""
Markdown writer module for generating formatted output files.

This module provides functionality to convert enriched pitch deck data
into well-formatted markdown files for easy reading and sharing.
"""


def write_markdown(enriched, outfile="output.md"):
    """
    Write enriched pitch deck data to a markdown file.
    
    This function takes the enriched data dictionary and formats it as a
    structured markdown document with proper headings and spacing.
    
    Args:
        enriched (dict): Dictionary containing enriched pitch deck analysis.
                        Keys are section names, values are content strings.
        outfile (str): Output file path for the markdown file. 
                      Defaults to "output.md".
                      
    Returns:
        None: Output is written directly to the specified file.
        
    Note:
        The function uses UTF-8 encoding to handle international characters
        and special symbols that may appear in company names or content.
    """
    with open(outfile, "w", encoding="utf-8") as f:
        for section, content in enriched.items():
            # Write section header as H1 markdown
            f.write(f"# {section}\n\n")
            # Write content with proper spacing and strip extra whitespace
            f.write(content.strip() + "\n\n")
