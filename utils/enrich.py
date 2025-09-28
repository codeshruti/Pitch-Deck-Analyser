"""
Enricher module for AI-powered pitch deck analysis.

This module provides the core enrichment functionality that combines
pitch deck data with external web intelligence and AI analysis to generate
comprehensive investment insights.
"""

from dotenv import load_dotenv
load_dotenv()
import os
from tqdm import tqdm
from utils.web_enrich import fetch_company_profile, fetch_latest_news
import requests

# Load API key from environment variables
OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "")


class Enricher:
    """
    Core enrichment engine for pitch deck analysis.
    
    This class handles the complete enrichment pipeline including:
    - Company name extraction from pitch deck content
    - External data gathering from web sources
    - AI-powered analysis across multiple investment dimensions
    - Structured output generation for investment decision-making
    """
    
    def __init__(self, api_key=OPENROUTER_KEY, model_name="deepseek-v3"):
        """
        Initialize the Enricher with API credentials and model configuration.
        
        Args:
            api_key (str): OpenRouter API key for authentication.
            model_name (str): Name of the LLM model to use for analysis.
                             Defaults to "deepseek-v3".
                             
        Raises:
            Exception: If API key is not provided or empty.
        """
        self.api_key = api_key
        self.model_name = model_name
        if not self.api_key:
            raise Exception("OpenRouter API key is not set. Please export OPENROUTER_API_KEY.")

    def prompt_openrouter(self, prompt):
        """
        Send a prompt to the OpenRouter API and return the response.
        
        Args:
            prompt (str): The prompt to send to the LLM.
            
        Returns:
            str: The generated response from the LLM.
            
        Raises:
            requests.exceptions.HTTPError: If the API request fails.
            requests.exceptions.RequestException: If there's a network error.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            r = requests.post("https://openrouter.ai/api/v1/chat/completions",
            headers=headers, json=payload, timeout=60)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("OpenRouter error details:", r.text)  
            raise
        return r.json()["choices"][0]["message"]["content"]

    def enrich(self, deck_data):
        """
        Enrich pitch deck data with comprehensive AI analysis and external intelligence.
        
        This method performs the complete enrichment pipeline:
        1. Extracts company name from pitch deck content
        2. Gathers external web intelligence (company profile, news)
        3. Combines all data sources for context
        4. Generates structured analysis across 11 key investment dimensions
        
        Args:
            deck_data (dict): Dictionary containing parsed pitch deck data.
                             Must include 'raw_text' key with extracted text.
                             
        Returns:
            dict: Enriched data dictionary with the following sections:
                - Company Name: Extracted or inferred company name
                - Executive Summary: 3-5 line VC-focused summary
                - Team: Founder/team analysis with track record insights
                - Product: Technology and USP description
                - Market: TAM/SAM/SOM estimates and competitor analysis
                - Traction & Metrics: Key performance indicators and growth stats
                - Funding & Financials: Current and past funding information
                - Competitive Landscape Map: Mermaid chart of competitive positioning
                - Sentiment & Hype: Language analysis and risk assessment
                - AI Investment Signal Score: 1-10 scoring across key dimensions
                - Risks & Unique Strengths: Red flags and competitive advantages
                - Missing Info & Diligence Questions: Due diligence gaps and questions
        """
        # Extract company name using AI - limit text to first 3000 chars for efficiency
        prompt_name = f"Extract the full company name from this pitch deck. If absent, guess best. Output only the name:\n\n{deck_data['raw_text'][:3000]}"
        company_name = self.prompt_openrouter(prompt_name).strip().split('\n')[0]
        
        # Gather external intelligence from web sources
        web_profile = fetch_company_profile(company_name)
        news_snippet = fetch_latest_news(company_name)

        # Combine all data sources for comprehensive context
        deck_in_context = (
            f"Pitch Deck Text:\n{deck_data['raw_text']}\n\n"
            f"Web Profile Info (DuckDuckGo summary):\n{web_profile}\n\n"
            f"Recent News (DuckDuckGo):\n{news_snippet}"
        )

        # Define analysis sections with specific instructions for each
        sections = [
            ("Executive Summary", "Give a 3-5 line summary for a VC on this company."),
            ("Team", "Summarize team/founders. If LinkedIn/track record is available, add it or infer plausible founder profiles."),
            ("Product", "Describe product/technology and USP. Make it investor-focused."),
            ("Market", "Estimate market size, main competitors, TAM/SAM/SOM if possible."),
            ("Traction & Metrics", "Extract key metrics, growth stats, and highlight any recent news. Infer plausible stats if missing."),
            ("Funding & Financials", "Current round, past funding, cap table signals. Guess if not stated."),
            ("Competitive Landscape Map", "Create a Mermaid markdown chart that shows this company and at least 3 main competitors, indicating placement on a feature or market axis. Guess if insufficient data."),
            ("Sentiment & Hype", "Analyze the language for hype and sentiment. Point out risky or exaggerated claims from an investor perspective."),
            ("AI Investment Signal Score", "Give a score (1-10) for Product, Team, Market, and Investment Fit. Justify each briefly as if you were an AI analyst for an early-stage fund."),
            ("Risks & Unique Strengths", "List any red flags and unique strengths. If not mentioned, infer possible ones."),
            ("Missing Info & Diligence Questions", "What important due diligence questions are left open? What data gaps should an investor clarify? Provide 3+ questions.")
        ]
        
        # Initialize output with company name
        output = {"Company Name": company_name}
        
        # Process each analysis section with progress tracking
        for section, instr in tqdm(sections, desc="Enriching", total=len(sections)):
            prompt = (
                f"{instr}\n\nContext:\n{deck_in_context}\n\n"
                "Write output as markdown."
            )
            result = self.prompt_openrouter(prompt)
            output[section] = result.strip()
            
        return output
