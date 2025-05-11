# 🧠 Smart Study Assistant

A CLI-based study companion powered by Google Gemini that helps you learn more effectively.


## 🌟 Features

- **Concept Explanation**: Get clear, simple explanations of complex topics
- **Quiz Generation**: Test your knowledge with auto-generated quizzes
- **Study Plan Creation**: Get personalized study plans based on your goals
- **Content Summarization**: Summarize lengthy study materials
- **Learning Tips**: Receive evidence-based study technique recommendations

## 📋 Requirements

- Python 3.8+
- Google Gemini API key

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/smart-study-assistant.git
   cd smart-study-assistant
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Google Gemini API key:
   ```bash
   cp .env.example .env
   ```
   Then edit the `.env` file to add your API key.

## 🚀 Usage

Run the assistant with:
```bash
python main.py
```

Or use specific modules directly:

```bash
# Get explanation for a concept
python main.py explain "Quantum entanglement"

# Generate a quiz on a topic
python main.py quiz "American Civil War" --questions 5

# Create a study plan
python main.py plan "Machine Learning" --days 30 --hours-per-day 2

# Summarize content
python main.py summarize --file study_material.txt

# Get study tips
python main.py tips "memorization techniques"
```

## 📊 Project Structure

```
smart-study-assistant/
├── main.py                 # CLI entry point
├── requirements.txt        # Dependencies
├── .env.example            # Environment variable template
├── README.md               # Project documentation
├── LICENSE                 # MIT license
├── src/
│   ├── __init__.py
│   ├── assistant.py        # Core assistant class
│   ├── config.py           # Configuration management
│   ├── gemini_client.py    # Google Gemini API wrapper
│   └── features/
│       ├── __init__.py
│       ├── concept_explainer.py
│       ├── quiz_generator.py
│       ├── study_planner.py
│       ├── content_summarizer.py
│       └── study_tips.py
└── tests/
    ├── __init__.py
    ├── test_assistant.py
    ├── test_concept_explainer.py
    ├── test_quiz_generator.py
    └── test_study_planner.py
```

## 🤖 How It Works

The Smart Study Assistant uses the Google Gemini API to process natural language requests for studying assistance.

Each feature is implemented as a separate module with carefully crafted prompts to get optimal results from the language model. The application maintains a simple conversation history to provide context-aware responses.

## 🛣️ Roadmap

- [ ] Add spaced repetition scheduling
- [ ] Implement flashcard generation
- [ ] Add support for uploading study materials
- [ ] Create interactive quiz mode
- [ ] Add visualization for study progress

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.