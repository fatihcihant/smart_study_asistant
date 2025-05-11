
"""
Configuration management for the Smart Study Assistant
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

def load_config() -> Dict[str, Any]:
    """
    Load configuration from environment variables
    
    Returns:
        Dict[str, Any]: Configuration dictionary
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Required configuration
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY environment variable is not set. "
            "Please create a .env file based on .env.example."
        )
    
    # Optional configuration with defaults
    config = {
        "api_key": api_key,
        "model": os.getenv("MODEL_NAME", "gemini-2.0-flash"),
        "max_tokens": int(os.getenv("MAX_TOKENS", "2048")),
        "temperature": float(os.getenv("TEMPERATURE", "0.7")),
    }
    
    return config