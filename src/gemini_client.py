"""
Google Gemini API client wrapper
"""

import google.generativeai as genai
from typing import Dict, Any, List, Optional

class GeminiClient:
    """
    Wrapper for interacting with the Google Gemini API
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the Gemini client
        
        Args:
            config: Configuration dictionary with API settings
        """
        self.config = config
        genai.configure(api_key=config["api_key"])
        self.model = genai.GenerativeModel(
            model_name=config["model"],
            generation_config={
                "max_output_tokens": config["max_tokens"],
                "temperature": config["temperature"],
            }
        )
        self.history = []
    
    def generate_text(self, prompt: str) -> str:
        """
        Generate text from a prompt
        
        Args:
            prompt: The prompt to send to the model
            
        Returns:
            The generated text response
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def chat(self, message: str, history: Optional[List[Dict[str, str]]] = None) -> str:
        """
        Send a message in a chat context
        
        Args:
            message: The user message
            history: Optional chat history to use instead of the internal history
            
        Returns:
            The generated response
        """
        chat_history = history if history is not None else self.history
        
        try:
            # Add the new message to history
            chat_history.append({"role": "user", "parts": [message]})
            
            # Create a chat session
            chat = self.model.start_chat(history=chat_history)
            
            # Get response
            response = chat.send_message(message)
            
            # Add response to history
            chat_history.append({"role": "model", "parts": [response.text]})
            
            return response.text
            
        except Exception as e:
            return f"Error in chat: {str(e)}"
    
    def clear_history(self) -> None:
        """Clear the chat history"""
        self.history = []