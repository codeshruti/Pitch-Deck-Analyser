"""
BoxOne PitchDeck Insights - Main Application Entry Point

This module serves as the main entry point for the pitch deck analysis application.
It orchestrates the parsing, enrichment, and output generation pipeline.
"""

from dotenv import load_dotenv
load_dotenv()
import sys
import os
import yaml
from datetime import datetime
from utils.pdf_parser import parse_pdf
from utils.ppt_parser import parse_ppt
from utils.agent import Agent
from utils.markdown_writer import write_markdown


def load_config(config_path="config.yaml"):
    """
    Load configuration settings from YAML file.
    
    Args:
        config_path (str): Path to the configuration file. Defaults to "config.yaml".
        
    Returns:
        dict: Configuration dictionary containing LLM model and output file settings.
        
    Raises:
        FileNotFoundError: If the configuration file doesn't exist.
        yaml.YAMLError: If the YAML file is malformed.
    """
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def generate_output_filename(input_file, config):
    """
    Generate a unique output filename based on input file and timestamp.
    
    Args:
        input_file (str): Path to the input pitch deck file.
        config (dict): Configuration dictionary with output file settings.
        
    Returns:
        str: Generated output filename with timestamp.
    """
    # Get base filename without extension
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Get output file extension from config or default to .md
    output_file = config.get("output_file", "output.md")
    file_ext = os.path.splitext(output_file)[1] or ".md"
    
    # Create unique filename
    unique_filename = f"{base_name}_{timestamp}{file_ext}"
    
    return unique_filename


def main(file_path, config):
    """
    Main processing pipeline for pitch deck analysis.
    
    This function orchestrates the complete workflow:
    1. Validates input file existence and format
    2. Parses the pitch deck (PDF or PPT/PPTX)
    3. Enriches the data using AI analysis
    4. Generates markdown output with unique filename
    
    Args:
        file_path (str): Path to the pitch deck file to analyze.
        config (dict): Configuration dictionary with model and output settings.
        
    Returns:
        None: Output is written to file and status printed to console.
    """
    # Extract configuration settings with fallback defaults
    model_name = config.get("llm_model", "deepseek-v3")
    
    # Validate file existence
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return
    
    # Parse pitch deck based on file format
    if file_path.lower().endswith('.pdf'):
        deck_data = parse_pdf(file_path)
    elif file_path.lower().endswith(('.ppt', '.pptx')):
        deck_data = parse_ppt(file_path)
    else:
        print("Unsupported file format.")
        return
    
    # Initialize AI agent and enrich the pitch deck data
    agent = Agent(model_name=model_name)
    enriched = agent.enrich_company_info(deck_data)
    
    # Generate unique output filename
    output_file = generate_output_filename(file_path, config)
    
    # Generate markdown output
    write_markdown(enriched, output_file)
    print(f"Output generated: {output_file}")

if __name__ == "__main__":
    config = load_config()
    if len(sys.argv) != 2:
        print("Usage: python main.py <pitchdeck.pdf|ppt|pptx>")
        print("Check config.yaml to set defaults (model, output file).")
    else:
        main(sys.argv[1], config)
