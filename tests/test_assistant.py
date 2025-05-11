"""
Tests for the SmartStudyAssistant class
"""

import pytest
from unittest.mock import MagicMock, patch
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.assistant import SmartStudyAssistant

@pytest.fixture
def mock_config():
    return {
        "api_key": "fake_api_key",
        "model": "gemini-pro",
        "max_tokens": 2048,
        "temperature": 0.7
    }

@pytest.fixture
def mock_client():
    with patch("src.gemini_client.GeminiClient") as mock:
        client = mock.return_value
        client.generate_text.return_value = "Mocked response"
        client.chat.return_value = "Mocked chat response"
        yield client

@pytest.fixture
def assistant(mock_config, mock_client):
    with patch("src.assistant.GeminiClient", return_value=mock_client):
        return SmartStudyAssistant(mock_config)

def test_explain_concept(assistant, mock_client):
    result = assistant.explain_concept("quantum computing")
    
    # Check that the method returns the expected result
    assert result == "Mocked response"
    
    # Check that generate_text was called with a prompt containing "quantum computing"
    args, _ = mock_client.generate_text.call_args
    assert "quantum computing" in args[0]

def test_generate_quiz(assistant, mock_client):
    result = assistant.generate_quiz("biology", 3, "easy")
    
    assert result == "Mocked response"
    
    args, _ = mock_client.generate_text.call_args
    assert "biology" in args[0]
    assert "3" in args[0]
    assert "easy" in args[0]

def test_create_study_plan(assistant, mock_client):
    result = assistant.create_study_plan("calculus", 5, 2, "exam preparation")
    
    assert result == "Mocked response"
    
    args, _ = mock_client.generate_text.call_args
    assert "calculus" in args[0]
    assert "5" in args[0]
    assert "2" in args[0]
    assert "exam preparation" in args[0]

def test_chat(assistant, mock_client):
    result = assistant.chat("How do I study better?")
    
    assert result == "Mocked chat response"
    
    args, _ = mock_client.chat.call_args
    assert "study" in args[0].lower()