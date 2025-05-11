"""
Concept explanation functionality for Smart Study Assistant
"""

from typing import Dict, Any, Optional
from src.gemini_client import GeminiClient

class ConceptExplainer:
    """
    Generate clear explanations of concepts for effective learning
    """
    
    def __init__(self, client: GeminiClient):
        """
        Initialize the concept explainer
        
        Args:
            client: GeminiClient instance for API calls
        """
        self.client = client
    
    def explain_concept(self, concept: str, detail_level: str = "medium", 
                        audience: str = "student") -> str:
        """
        Get a clear explanation of a concept
        
        Args:
            concept: The concept to explain
            detail_level: How detailed the explanation should be (basic, medium, advanced)
            audience: Target audience (e.g., "middle school", "undergraduate", "professional")
            
        Returns:
            An explanation of the concept
        """
        prompt = f"""
        Explain the concept of "{concept}" in a {detail_level} level of detail for a {audience}.
        
        Follow these guidelines:
        1. Start with a simple, clear definition
        2. Explain the core principles or mechanics
        3. Use analogies, examples, or visual descriptions to make it more understandable
        4. Mention any important related concepts or prerequisites
        5. For complex topics, break them down into smaller, manageable pieces
        6. If relevant, mention real-world applications or why this concept matters
        
        Format your response using Markdown with appropriate headings, bullet points,
        and emphasis for key terms.
        """
        
        return self.client.generate_text(prompt)
    
    def explain_relationships(self, concept1: str, concept2: str) -> str:
        """
        Explain the relationship between two concepts
        
        Args:
            concept1: First concept
            concept2: Second concept
            
        Returns:
            An explanation of how the concepts relate
        """
        prompt = f"""
        Explain the relationship between "{concept1}" and "{concept2}".
        
        Include the following in your explanation:
        1. Brief definitions of both concepts
        2. How these concepts are connected or related
        3. Key similarities and differences
        4. How understanding one helps in understanding the other
        5. Real-world examples showing their relationship
        
        Format your response using Markdown with clear structure.
        """
        
        return self.client.generate_text(prompt)
    
    def simplify_complex_text(self, text: str, target_audience: str = "student") -> str:
        """
        Simplify complex educational text to make it more accessible
        
        Args:
            text: The complex text to simplify
            target_audience: The target audience for the simplified text
            
        Returns:
            A simplified version of the text
        """
        prompt = f"""
        Simplify the following educational text to make it more accessible for a {target_audience},
        while preserving the key information and concepts.
        
        Original text:
        ```
        {text[:8000]}  # Limit to avoid token issues
        ```
        
        Please:
        1. Use simpler vocabulary and shorter sentences
        2. Explain technical terms or jargon
        3. Add helpful analogies where appropriate
        4. Break down complex ideas into simpler components
        5. Maintain all the important information and concepts
        
        Format your response as clear, readable text using Markdown.
        """
        
        return self.client.generate_text(prompt)