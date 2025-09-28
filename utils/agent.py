"""
Agent module for orchestrating pitch deck enrichment.

This module provides the Agent class which serves as a high-level interface
for enriching pitch deck data using AI-powered analysis.
"""

from utils.enrich import Enricher
from dotenv import load_dotenv
load_dotenv()
import os

# Load API key from environment variables
OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "")


class Agent:
    """
    High-level agent for pitch deck analysis and enrichment.
    
    This class provides a simplified interface for enriching pitch deck data
    using AI models through the OpenRouter API. It encapsulates the complexity
    of the enrichment process behind a clean API.
    """
    
    def __init__(self, api_key=OPENROUTER_KEY, model_name='deepseek-v3'):
        """
        Initialize the Agent with API credentials and model configuration.
        
        Args:
            api_key (str): OpenRouter API key for authentication. 
                          Defaults to OPENROUTER_KEY environment variable.
            model_name (str): Name of the LLM model to use for analysis.
                             Defaults to 'deepseek-v3'.
        """
        self.enricher = Enricher(api_key, model_name)

    def enrich_company_info(self, deck_data):
        """
        Enrich pitch deck data with AI-powered analysis and external information.
        
        This method takes raw pitch deck data and enriches it with:
        - Company profile information from web sources
        - Recent news and market intelligence
        - AI-generated analysis across multiple dimensions
        - Investment signals and risk assessment
        
        Args:
            deck_data (dict): Dictionary containing parsed pitch deck data.
                             Must include 'raw_text' key with extracted text.
                             
        Returns:
            dict: Enriched data dictionary with analysis sections including
                  Executive Summary, Team, Product, Market, Traction, etc.
        """
        return self.enricher.enrich(deck_data)
