"""
Study tips and techniques functionality for Smart Study Assistant
"""

from typing import Dict, Any, Optional, List
from src.gemini_client import GeminiClient

class StudyTips:
    """
    Provide evidence-based study techniques and tips
    """
    
    def __init__(self, client: GeminiClient):
        """
        Initialize the study tips provider
        
        Args:
            client: GeminiClient instance for API calls
        """
        self.client = client
    
    def get_general_tips(self) -> str:
        """
        Get general evidence-based study tips
        
        Returns:
            Study tips and techniques
        """
        prompt = """
        Provide evidence-based general study techniques that can improve learning effectiveness.
        
        Include:
        1. 5 specific, practical techniques
        2. The psychological or neurological basis for why each technique works
        3. Step-by-step instructions for implementing each technique
        4. Common mistakes or pitfalls to avoid
        5. How to adapt each technique for different types of learners
        
        Format your response using Markdown with clear headings, bullet points, and emphasis
        on key information.
        """
        
        return self.client.generate_text(prompt)
    
    def get_specific_tips(self, topic: str) -> str:
        """
        Get tips for a specific study area or challenge
        
        Args:
            topic: Specific area (e.g., "memorization", "focus", "math", "language learning")
            
        Returns:
            Targeted study tips
        """
        prompt = f"""
        Provide evidence-based study techniques and tips specifically for "{topic}".
        
        Include:
        1. 4-5 specific, practical techniques tailored to this area
        2. The science behind why each technique works for this specific area
        3. Step-by-step instructions for implementing each technique
        4. Common mistakes to avoid
        5. How to measure progress and effectiveness
        
        Format your response using Markdown with clear headings, bullet points, and emphasis
        on key information.
        """
        
        return self.client.generate_text(prompt)
    
    def get_tips_for_learning_style(self, learning_style: str) -> str:
        """
        Get study tips customized for a particular learning style
        
        Args:
            learning_style: Learning style (visual, auditory, reading/writing, kinesthetic)
            
        Returns:
            Learning style-specific tips
        """
        prompt = f"""
        Provide study techniques and strategies optimized for {learning_style} learners.
        
        Include:
        1. 5 specific study techniques that leverage {learning_style} learning strengths
        2. How to adapt standard study materials to better suit this learning style
        3. Recommended study tools or resources particularly effective for this style
        4. How to work with materials that don't naturally align with this style
        5. How to combine this learning style with others for more effective learning
        
        Format your response using Markdown with clear, helpful organization.
        While acknowledging that the strict learning styles theory has been questioned,
        focus on practical strategies that work well for people who prefer {learning_style}
        information processing.
        """
        
        return self.client.generate_text(prompt)
    
    def overcome_challenge(self, challenge: str) -> str:
        """
        Get strategies to overcome specific study challenges
        
        Args:
            challenge: Study challenge (e.g., "procrastination", "test anxiety")
            
        Returns:
            Strategies to overcome the challenge
        """
        prompt = f"""
        Provide practical, evidence-based strategies to overcome "{challenge}" while studying.
        
        Include:
        1. 4-5 specific techniques to address this challenge
        2. The psychological principles behind these strategies
        3. Short-term tactics for immediate relief or improvement
        4. Long-term strategies for sustainable change
        5. When to consider seeking additional help
        
        Format your response using Markdown with clear sections and actionable advice.
        Keep the tone supportive and encouraging.
        """
        
        return self.client.generate_text(prompt)