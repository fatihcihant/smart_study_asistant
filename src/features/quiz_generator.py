"""
Quiz generation functionality for Smart Study Assistant
"""

from typing import Dict, Any, List
from src.gemini_client import GeminiClient

class QuizGenerator:
    """
    Generate quizzes on specific topics with customizable difficulty
    """
    
    def __init__(self, client: GeminiClient):
        """
        Initialize the quiz generator
        
        Args:
            client: GeminiClient instance for API calls
        """
        self.client = client
    
    def generate_quiz(self, topic: str, num_questions: int = 5, 
                    difficulty: str = "medium", 
                    question_types: List[str] = None) -> str:
        """
        Generate a quiz on a specific topic with various options
        
        Args:
            topic: The topic for the quiz
            num_questions: Number of questions to generate
            difficulty: Difficulty level (easy, medium, hard)
            question_types: Types of questions to include (multiple choice, true/false, etc.)
                         Defaults to multiple choice if None.
            
        Returns:
            A formatted quiz with questions and answers
        """
        # Default to multiple choice if not specified
        if question_types is None:
            question_types = ["multiple choice"]
        
        question_types_str = ", ".join(question_types)
        
        prompt = f"""
        Create a {difficulty} difficulty quiz about "{topic}" with {num_questions} questions.
        Include the following types of questions: {question_types_str}.
        
        For each question:
        1. Write a clear, specific question that tests understanding, not just memorization
        2. For multiple choice, provide 4 options (A, B, C, D) where only one is correct
        3. For true/false, clearly state the statement to evaluate
        4. Indicate the correct answer
        5. Include a brief explanation of why the answer is correct
        
        Format the quiz using Markdown with each question numbered, followed by choices,
        then the answer and explanation in a collapsed details section.
        
        Example format:
        ```
        ## {topic} Quiz ({difficulty} difficulty)
        
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
    
    def generate_flashcards(self, topic: str, num_cards: int = 10) -> str:
        """
        Generate flashcards for studying a topic
        
        Args:
            topic: The topic for the flashcards
            num_cards: Number of flashcards to generate
            
        Returns:
            A formatted set of flashcards
        """
        prompt = f"""
        Create {num_cards} flashcards about "{topic}" for effective studying.
        
        For each flashcard:
        1. Write a clear question or prompt on the front
        2. Provide a concise answer on the back
        3. Focus on key concepts, definitions, examples, and relationships
        
        Format the flashcards using Markdown with each card numbered and using
        collapsible sections for the answers.
        
        Example format:
        ```
        ## {topic} Flashcards
        
        ### Card 1
        **Front:** What is...?
        
        <details>
        <summary>Back</summary>
        
        The definition or answer...
        </details>
        ```
        """
        
        return self.client.generate_text(prompt)
        
    def check_answer(self, question: str, user_answer: str, topic: str = None) -> str:
        """
        Check if a user's answer to a question is correct
        
        Args:
            question: The question being answered
            user_answer: The user's answer
            topic: Optional topic for context
            
        Returns:
            Feedback on the answer's correctness with explanation
        """
        topic_context = f" about {topic}" if topic else ""
        
        prompt = f"""
        Evaluate the correctness of the user's answer to this question{topic_context}.
        
        Question: {question}
        User's answer: {user_answer}
        
        Please:
        1. Determine if the answer is correct, partially correct, or incorrect
        2. Explain why in a constructive, educational way
        3. If incorrect or partially correct, provide the correct answer
        4. Give a helpful tip for remembering the correct answer
        
        Format your response in a friendly, encouraging tone.
        """
        
        return self.client.generate_text(prompt)