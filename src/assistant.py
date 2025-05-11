"""
Core Smart Study Assistant implementation
"""

from typing import Dict, Any, List, Optional
from src.gemini_client import GeminiClient

class SmartStudyAssistant:
    """
    Smart Study Assistant that provides various study-related functionalities
    using the Google Gemini API
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the Smart Study Assistant
        
        Args:
            config: Configuration dictionary
        """
        self.client = GeminiClient(config)
    
    def chat(self, message: str) -> str:
        """
        Have a conversation with the study assistant
        
        Args:
            message: User's message
            
        Returns:
            Assistant's response
        """
        system_context = """
        You are a helpful Study Assistant powered by AI. Your goal is to help students learn
        effectively. Be concise, clear, and educational in your responses. Focus on providing
        accurate information and useful study strategies.
        """
        
        prompt = f"{system_context}\n\nUser: {message}"
        return self.client.chat(prompt)
    
    def explain_concept(self, concept: str) -> str:
        """
        Get a clear explanation of a concept
        
        Args:
            concept: The concept to explain
            
        Returns:
            An explanation of the concept
        """
        prompt = f"""
        Explain the concept of "{concept}" in a clear, educational way.
        
        Follow these guidelines:
        1. Start with a simple definition
        2. Explain the core principles
        3. Use analogies or examples to make it more understandable
        4. Mention any important related concepts
        5. Keep your explanation concise but thorough
        
        Format your response using Markdown.
        """
        
        return self.client.generate_text(prompt)
    
    def generate_quiz(self, topic: str, num_questions: int = 5, difficulty: str = "medium") -> str:
        """
        Generate a quiz on a specific topic
        
        Args:
            topic: The topic for the quiz
            num_questions: Number of questions to generate
            difficulty: Difficulty level (easy, medium, hard)
            
        Returns:
            A formatted quiz with questions and answers
        """
        prompt = f"""
        Create a {difficulty} difficulty quiz about "{topic}" with {num_questions} questions.
        
        For each question:
        1. Write a clear, specific question
        2. Provide multiple choice options (A, B, C, D)
        3. Indicate the correct answer
        4. Include a brief explanation of why the answer is correct
        
        Format the quiz using Markdown with each question numbered, followed by choices,
        then the answer and explanation in a collapsed details section.
        
        Example format:
        ```
        ## {topic} Quiz
        
        ### Question 1
        What is...?
        A) Option 1
        B) Option 2
        C) Option 3
        D) Option 4
        
        <details>
        <summary>Answer</summary>
        
        **Correct Answer: B**
        
        Explanation: This is correct because...
        </details>
        ```
        """
        
        return self.client.generate_text(prompt)
    
    def create_study_plan(self, subject: str, days: int = 7, 
                          hours_per_day: int = 1, goal: str = "mastery") -> str:
        """
        Create a personalized study plan
        
        Args:
            subject: The subject to study
            days: Number of days for the plan
            hours_per_day: Hours to study per day
            goal: Study goal (e.g., "exam preparation", "mastery")
            
        Returns:
            A formatted study plan
        """
        prompt = f"""
        Create a {days}-day study plan for "{subject}" with {hours_per_day} hour(s) per day.
        The goal is: {goal}.
        
        Your study plan should:
        1. Break down the subject into logical sub-topics
        2. Distribute learning across the available days
        3. Allocate time for initial learning, practice, and review
        4. Suggest specific activities for each study session
        5. Recommend resources (general types, not specific titles)
        6. Include regular assessments to check understanding
        
        Format the study plan using Markdown with clear headings, days, and activities.
        """
        
        return self.client.generate_text(prompt)
    
    def summarize_content(self, content: str) -> str:
        """
        Summarize study content
        
        Args:
            content: The content to summarize
            
        Returns:
            A concise summary of the content
        """
        prompt = f"""
        Summarize the following study material concisely while preserving the key points.
        Focus on the main concepts and their relationships.
        
        Use the following format:
        1. Main topic and core idea (1-2 sentences)
        2. Key points (bullet points)
        3. Important relationships or connections
        4. Questions to test understanding
        
        Format your response using Markdown.
        
        Content to summarize:
        ```
        {content[:8000]}  # Limiting content to 8000 chars to avoid token limits
        ```
        """
        
        return self.client.generate_text(prompt)
    
    def get_study_tips(self, topic: Optional[str] = None) -> str:
        """
        Get evidence-based study technique recommendations
        
        Args:
            topic: Optional specific area to focus on (e.g., "memorization", "staying focused")
            
        Returns:
            Study tips and techniques
        """
        if topic:
            prompt = f"""
            Provide evidence-based study techniques and tips for "{topic}".
            
            Include:
            1. 3-5 practical, specific techniques
            2. The science behind why each technique works
            3. How to implement each technique effectively
            4. Common mistakes to avoid
            
            Format your response using Markdown with clear headings and bullet points.
            """
        else:
            prompt = """
            Provide general evidence-based study techniques that can improve learning effectiveness.
            
            Include:
            1. 3-5 practical, specific techniques
            2. The science behind why each technique works
            3. How to implement each technique effectively
            4. Common mistakes to avoid
            
            Format your response using Markdown with clear headings and bullet points.
            """
        
        return self.client.generate_text(prompt)