"""
Study planning functionality for Smart Study Assistant
"""

from typing import Dict, Any, List, Optional
from src.gemini_client import GeminiClient

class StudyPlanner:
    """
    Create personalized study plans based on various parameters
    """
    
    def __init__(self, client: GeminiClient):
        """
        Initialize the study planner
        
        Args:
            client: GeminiClient instance for API calls
        """
        self.client = client
    
    def create_study_plan(self, subject: str, days: int = 7, 
                         hours_per_day: int = 1, goal: str = "mastery",
                         prior_knowledge: str = "intermediate") -> str:
        """
        Create a personalized study plan
        
        Args:
            subject: The subject to study
            days: Number of days for the plan
            hours_per_day: Hours to study per day
            goal: Study goal (e.g., "exam preparation", "mastery")
            prior_knowledge: Level of existing knowledge (beginner, intermediate, advanced)
            
        Returns:
            A formatted study plan
        """
        prompt = f"""
        Create a {days}-day study plan for "{subject}" with {hours_per_day} hour(s) per day.
        The study goal is: {goal}.
        The student's prior knowledge level is: {prior_knowledge}.
        
        Your study plan should:
        1. Break down the subject into logical sub-topics based on priority and dependencies
        2. Distribute learning across the available days in an optimal sequence
        3. Allocate time for initial learning, practice, review, and self-assessment
        4. Include a variety of study activities (reading, practice problems, flash cards, etc.)
        5. Suggest specific study techniques appropriate for the material
        6. Recommend types of resources (not specific titles)
        7. Include regular breaks using effective time management techniques
        8. Add periodic review sessions to reinforce learning
        
        Format the plan using Markdown with:
        - A brief introduction explaining the approach
        - Clear day-by-day breakdown with topics and activities
        - Study tips specific to this subject
        - A checklist for tracking progress
        """
        
        return self.client.generate_text(prompt)
    
    def prioritize_topics(self, subject: str, topics: List[str], 
                         time_available: int, goal: str) -> str:
        """
        Prioritize topics within a subject based on available time and goals
        
        Args:
            subject: The main subject
            topics: List of topics within the subject
            time_available: Available time in hours
            goal: Study goal (e.g., "exam preparation", "general understanding")
            
        Returns:
            Prioritized list of topics with reasoning
        """
        topics_formatted = "\n".join([f"- {topic}" for topic in topics])
        
        prompt = f"""
        For the subject "{subject}", help prioritize the following topics given {time_available} hours
        of available study time and a goal of "{goal}".
        
        Topics:
        {topics_formatted}
        
        Please:
        1. Rank the topics in order of priority (most to least important)
        2. Explain why each topic has its priority ranking
        3. Estimate how much time to spend on each topic
        4. Identify any dependencies between topics (what should be learned first)
        5. Note any topics that could be skipped or minimized given the constraints
        
        Format your response using Markdown with clear sections.
        """
        
        return self.client.generate_text(prompt)
    
    def create_spaced_repetition_schedule(self, topic: str, 
                                        start_date: str, 
                                        end_date: str) -> str:
        """
        Create a spaced repetition schedule for effective long-term learning
        
        Args:
            topic: The topic to learn
            start_date: Study start date (YYYY-MM-DD)
            end_date: Study end date (YYYY-MM-DD)
            
        Returns:
            A spaced repetition schedule
        """
        prompt = f"""
        Create a spaced repetition study schedule for learning "{topic}" from {start_date} to {end_date}.
        
        Follow these guidelines:
        1. Use scientifically-backed spaced repetition intervals (e.g., 1 day, 3 days, 7 days, etc.)
        2. Break the topic into logical sub-components
        3. Schedule initial learning sessions followed by increasingly spaced review sessions
        4. Include different types of practice for each review session
        5. Add brief self-assessment checkpoints
        
        Format the schedule using Markdown with clear dates and activities.
        Include a brief explanation of how spaced repetition works and why it's effective.
        """
        
        return self.client.generate_text(prompt)