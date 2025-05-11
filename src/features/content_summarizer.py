"""
Content summarization functionality for Smart Study Assistant
"""

from typing import Dict, Any, Optional
from src.gemini_client import GeminiClient

class ContentSummarizer:
    """
    Summarize study content into concise, digestible formats
    """
    
    def __init__(self, client: GeminiClient):
        """
        Initialize the content summarizer
        
        Args:
            client: GeminiClient instance for API calls
        """
        self.client = client
    
    def summarize_text(self, content: str, format_type: str = "concise") -> str:
        """
        Summarize study content
        
        Args:
            content: The content to summarize
            format_type: Type of summary (concise, detailed, bullet_points, etc.)
            
        Returns:
            A summary of the content
        """
        format_instructions = {
            "concise": "Create a brief summary capturing only the most essential points",
            "detailed": "Create a comprehensive summary that includes all key points and supporting details",
            "bullet_points": "Format the summary as bullet points for quick review",
            "concept_map": "Structure the summary as a textual concept map showing relationships between ideas",
            "questions": "Transform the content into key questions and answers"
        }.get(format_type, "Create a clear, concise summary")
        
        prompt = f"""
        Summarize the following study material.
        {format_instructions}.
        
        Focus on:
        1. Main topic and core ideas
        2. Key concepts, definitions, and principles
        3. Important relationships between concepts
        4. Examples or applications, if relevant
        5. Maintaining accuracy while condensing information
        
        Format your summary using Markdown with appropriate headings, bullet points, 
        and emphasis on key terms.
        
        Content to summarize:
        ```
        {content[:8000]}  # Limiting content to avoid token limits
        ```
        """
        
        return self.client.generate_text(prompt)
    
    def extract_key_points(self, content: str, num_points: int = 5) -> str:
        """
        Extract the most important points from study content
        
        Args:
            content: The content to analyze
            num_points: Number of key points to extract
            
        Returns:
            A list of key points
        """
        prompt = f"""
        Extract the {num_points} most important key points from the following study material.
        Focus on the core concepts, principles, and takeaways.
        
        For each key point:
        1. State it clearly and concisely
        2. Explain why it's important
        3. Include a brief supporting detail or example if available
        
        Format your response using Markdown with numbered points.
        
        Content to analyze:
        ```
        {content[:8000]}  # Limiting content to avoid token limits
        ```
        """
        
        return self.client.generate_text(prompt)
    
    def create_study_notes(self, content: str) -> str:
        """
        Transform content into effective study notes
        
        Args:
            content: The content to transform
            
        Returns:
            Formatted study notes
        """
        prompt = f"""
        Transform the following content into effective, well-structured study notes.
        
        Create notes that:
        1. Organize information hierarchically with clear headings and subheadings
        2. Use bullet points for lists and details
        3. Bold key terms and definitions
        4. Include visual elements described in text (diagrams, tables, etc.)
        5. Add mnemonics or memory aids where helpful
        6. Include summary questions at the end of each section
        
        Format your notes using Markdown with appropriate formatting for
        readability and information hierarchy.
        
        Content to transform:
        ```
        {content[:8000]}  # Limiting content to avoid token limits
        ```
        """
        
        return self.client.generate_text(prompt)