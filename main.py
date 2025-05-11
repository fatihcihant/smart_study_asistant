#!/usr/bin/env python3
"""
Smart Study Assistant - CLI tool for study help powered by Google Gemini
"""

import os
import sys
import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.assistant import SmartStudyAssistant
from src.config import load_config

console = Console()

@click.group()
@click.version_option(version="0.1.0")
def cli():
    """Smart Study Assistant - Your AI-powered study companion."""
    pass

@cli.command()
@click.argument("query")
def explain(query):
    """Get a clear explanation of a concept or topic."""
    with console.status("[bold green]Getting explanation..."):
        config = load_config()
        assistant = SmartStudyAssistant(config)
        result = assistant.explain_concept(query)
    
    console.print(Panel(Markdown(result), title=f"📚 Explanation: {query}", expand=False))

@cli.command()
@click.argument("topic")
@click.option("--questions", "-q", default=5, help="Number of questions to generate")
@click.option("--difficulty", "-d", default="medium", 
              type=click.Choice(["easy", "medium", "hard"]), 
              help="Difficulty level of the quiz")
def quiz(topic, questions, difficulty):
    """Generate a quiz on a specific topic."""
    with console.status(f"[bold green]Creating a {difficulty} quiz with {questions} questions..."):
        config = load_config()
        assistant = SmartStudyAssistant(config)
        result = assistant.generate_quiz(topic, questions, difficulty)
    
    console.print(Panel(Markdown(result), title=f"🎯 Quiz: {topic}", expand=False))

@cli.command()
@click.argument("subject")
@click.option("--days", "-d", default=7, help="Number of days for the study plan")
@click.option("--hours-per-day", "-h", default=1, help="Hours to study per day")
@click.option("--goal", "-g", default="mastery", help="Your study goal")
def plan(subject, days, hours_per_day, goal):
    """Create a personalized study plan."""
    with console.status(f"[bold green]Creating a {days}-day study plan..."):
        config = load_config()
        assistant = SmartStudyAssistant(config)
        result = assistant.create_study_plan(subject, days, hours_per_day, goal)
    
    console.print(Panel(Markdown(result), title=f"📆 Study Plan: {subject}", expand=False))

@cli.command()
@click.option("--file", "-f", type=click.File("r"), help="File to summarize")
@click.option("--text", "-t", help="Text to summarize")
def summarize(file, text):
    """Summarize study content."""
    if not file and not text:
        click.echo("Error: Please provide either a file or text to summarize")
        return
    
    content = text if text else file.read()
    
    with console.status("[bold green]Summarizing content..."):
        config = load_config()
        assistant = SmartStudyAssistant(config)
        result = assistant.summarize_content(content)
    
    console.print(Panel(Markdown(result), title="📝 Summary", expand=False))

@cli.command()
@click.argument("topic", required=False)
def tips(topic):
    """Get evidence-based study technique recommendations."""
    with console.status("[bold green]Finding study tips..."):
        config = load_config()
        assistant = SmartStudyAssistant(config)
        result = assistant.get_study_tips(topic)
    
    console.print(Panel(Markdown(result), title="💡 Study Tips", expand=False))

@cli.command()
def interactive():
    """Start an interactive session with the study assistant."""
    config = load_config()
    assistant = SmartStudyAssistant(config)
    
    console.print(Panel(
        "Welcome to Smart Study Assistant! Ask me anything about your studies.\n"
        "Type 'exit' or 'quit' to end the session.",
        title="🧠 Interactive Mode", 
        expand=False
    ))
    
    while True:
        query = click.prompt("\n[bold blue]You[/]", prompt_suffix="")
        if query.lower() in ["exit", "quit", "bye"]:
            console.print("[bold green]Goodbye! Happy studying![/]")
            break
        
        with console.status("[bold green]Thinking..."):
            response = assistant.chat(query)
        
        console.print(f"\n[bold green]Assistant[/]")
        console.print(Markdown(response))

if __name__ == "__main__":
    # If no arguments provided, start interactive mode
    if len(sys.argv) == 1:
        sys.argv.append("interactive")
    cli()