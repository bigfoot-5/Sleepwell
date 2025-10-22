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
   pip install -r requirements.txt
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

## Logging User Data via Command Line
Sleepwell supports logging sleep data and generating suggestions directly via command line interface (CLI) commands for ease of use.

To log sleep data, use a command such as:
```
python log_sleep.py --date 2024-06-01 --start 22:30 --end 06:30 --quality 7 --notes "Had coffee in the afternoon"
```
This command records your sleep details for the specified date.

To generate personalized suggestions based on your logged data, run:
```
python generate_suggestions.py --date 2024-06-01
```
This will analyze the sleep data for the given date and output AI-generated advice to help improve your sleep quality.

Using these CLI commands, you can conveniently manage your sleep logs and receive actionable insights without manually editing JSON files.
