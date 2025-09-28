"""
Web enrichment module for gathering external company intelligence.

This module provides functionality to fetch company profiles and news
from web sources using DuckDuckGo search, providing external context
for pitch deck analysis.
"""

import requests
from bs4 import BeautifulSoup


def fetch_company_profile(company_name, num_results=2):
    """
    Fetch company profile information from DuckDuckGo search results.
    
    This function searches for company information using DuckDuckGo and
    extracts relevant profile snippets from the search results.
    
    Args:
        company_name (str): Name of the company to search for.
        num_results (int): Maximum number of search results to return.
                          Defaults to 2.
                          
    Returns:
        str: Concatenated text from search result titles, separated by newlines.
             Returns empty string if search fails or no results found.
             
    Note:
        Uses DuckDuckGo's HTML interface to avoid API rate limits.
        Includes proper User-Agent header to avoid blocking.
    """
    url = f"https://html.duckduckgo.com/html/?q={company_name} company"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        r = requests.get(url, headers=headers)
        if not r.ok:
            return ""
    except requests.RequestException:
        return ""
    
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []
    
    # Extract search result titles
    for a in soup.find_all('a', class_='result__a', limit=num_results):
        results.append(a.text)
    
    snippet = "\n".join(results)
    return snippet


def fetch_latest_news(company_name, num_results=2):
    """
    Fetch latest news about a company from DuckDuckGo search results.
    
    This function searches for recent news about the company using DuckDuckGo
    and extracts relevant news headlines from the search results.
    
    Args:
        company_name (str): Name of the company to search for.
        num_results (int): Maximum number of news results to return.
                          Defaults to 2.
                          
    Returns:
        str: Concatenated text from news headlines, separated by newlines.
             Returns empty string if search fails or no results found.
             
    Note:
        Uses DuckDuckGo's HTML interface to avoid API rate limits.
        Includes proper User-Agent header to avoid blocking.
        Searches specifically for news by appending "company news" to query.
    """
    url = f"https://html.duckduckgo.com/html/?q={company_name} company news"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        r = requests.get(url, headers=headers)
        if not r.ok:
            return ""
    except requests.RequestException:
        return ""
    
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []
    
    # Extract news result titles
    for a in soup.find_all('a', class_='result__a', limit=num_results):
        results.append(a.text)
    
    snippet = "\n".join(results)
    return snippet
