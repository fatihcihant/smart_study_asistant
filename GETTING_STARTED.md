# Getting Started with Smart Study Assistant

This guide will help you set up and use the Smart Study Assistant effectively.

## Prerequisites

Before you begin, make sure you have:

1. Python 3.8 or higher installed
2. A Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))
3. Git installed (to clone the repository)

## Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/fatihcihant/smart_study_asistant.git
cd smart-study-assistant
```

### Step 2: Set Up a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Your API Key

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Basic Usage

### Interactive Mode

The simplest way to use Smart Study Assistant is in interactive mode:

```bash
python main.py
```

This will start a conversation where you can ask any study-related questions.

### Command-Line Features

#### Get a Concept Explanation

```bash
python main.py explain "photosynthesis"
```

#### Generate a Quiz

```bash
python main.py quiz "World War II" --questions 5 --difficulty "medium"
```

#### Create a Study Plan

```bash
python main.py plan "organic chemistry" --days 14 --hours-per-day 2 --goal "exam preparation"
```

#### Summarize Content

```bash
# Summarize text from a file
python main.py summarize --file my_lecture_notes.txt

# Or provide text directly
python main.py summarize --text "Long paragraph of content to summarize..."
```

#### Get Study Tips

```bash
# General study tips
python main.py tips

# Topic-specific tips
python main.py tips "memorization techniques"
```

## Advanced Usage

### Customizing the Assistant

You can modify the configuration settings in the `.env` file:

```
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-pro
MAX_TOKENS=2048
TEMPERATURE=0.7
```

- **MODEL_NAME**: The Gemini model to use
- **MAX_TOKENS**: Maximum output length
- **TEMPERATURE**: Controls creativity (0.0-1.0, higher is more creative)

### Extending the Assistant

The modular design makes it easy to add new features:

1. Create a new module in the `src/features/` directory
2. Add the functionality to the `SmartStudyAssistant` class in `src/assistant.py`
3. Add a new command in `main.py`

## Troubleshooting

### API Key Issues

If you get authentication errors:
- Verify your API key is correct
- Check that the `.env` file is in the project root directory
- Make sure the virtual environment is activated

### Token Limits

If you get errors about token limits when summarizing large content:
- Try breaking the content into smaller chunks
- Adjust the `MAX_TOKENS` value in your `.env` file

### Python Version Errors

If you get syntax errors or import errors:
- Verify you're using Python 3.8 or higher
- Make sure all dependencies are installed

## Next Steps

Once you're comfortable with the basic functionality, consider:

1. Adding your own custom study materials
2. Contributing to the project by adding new features
3. Setting up a regular study routine using the generated study plans
4. Sharing feedback or reporting issues on GitHub

Happy studying!