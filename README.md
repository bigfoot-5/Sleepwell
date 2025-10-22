# Sleepwell

## Project Overview
Sleepwell is an MVP for a sleep tracking product that leverages AI to analyze sleep patterns and provide personalized suggestions for improving sleep quality. By logging user data and utilizing advanced language models, Sleepwell aims to help users achieve better rest and overall well-being.

## Requirements
- Python 3.8 or higher
- Ollama AI platform installed and configured
- `requests` Python package (for API interactions)
- Access to the `qwen3:1.7b` model on Ollama

## Setting up Python Environment
1. Install Python 3.8+ if not already installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required Python packages:
   ```
   pip install requests
   ```

## Setting up Ollama with qwen3:1.7b
1. Download and install Ollama from [https://ollama.com/](https://ollama.com/).
2. Pull the `qwen3:1.7b` model by running:
   ```
   ollama pull qwen3:1.7b
   ```
3. Verify the model is installed by listing available models:
   ```
   ollama list
   ```
4. Ensure Ollama is running and accessible for your Python scripts.

## Logging User Data
Sleepwell requires users to log their daily sleep data, including:
- Sleep start time
- Sleep end time
- Quality of sleep (subjective rating)
- Notes on factors affecting sleep (e.g., caffeine intake, stress)

You can log data by storing it in a simple JSON file or database. Example JSON structure:
```json
{
  "date": "2024-06-01",
  "sleep_start": "22:30",
  "sleep_end": "06:30",
  "quality": 7,
  "notes": "Had coffee in the afternoon"
}
```

## Generating Suggestions
Sleepwell uses the `qwen3:1.7b` model through Ollama to analyze logged sleep data and generate personalized suggestions. The AI model evaluates patterns and provides actionable advice such as adjusting bedtime, reducing caffeine, or improving sleep hygiene.

Example prompt to the model:
```
Analyze the following sleep data and provide suggestions to improve sleep quality:

Date: 2024-06-01
Sleep Start: 22:30
Sleep End: 06:30
Quality: 7
Notes: Had coffee in the afternoon
```

## Testing / Example Commands
To test Sleepwell functionality, you can run example Python scripts or commands that:
- Load sample sleep data
- Send prompts to Ollama's `qwen3:1.7b` model
- Receive and display AI-generated suggestions

Example command to generate suggestions:
```
python generate_suggestions.py --data sample_sleep_data.json
```

Replace `generate_suggestions.py` and `sample_sleep_data.json` with your actual script and data file names.

---

For more detailed instructions and code examples, please refer to the project documentation or contact the developer.
