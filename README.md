# Sleepwell

## Project Overview
Sleepwell is an MVP for a sleep tracking product that leverages AI to analyze sleep patterns and provide personalized suggestions for improving sleep quality. By logging user data and utilizing advanced language models, Sleepwell aims to help users achieve better rest and overall well-being.

## Features

1. **Log Sleep Data** - Track your daily sleep metrics including:
   - Medication intake (tabs 1-3)
   - Caffeine and alcohol consumption
   - Workout duration and outdoor activity
   - Nap duration
   - Mood rating
   - Sleep duration and continuity
   - Number of wakeups

2. **Automatic Sleep Scoring** - Calculate sleep quality scores based on:
   - Sleep duration (hours)
   - Sleep continuity score
   - Mood rating

3. **Rule-Based Remedies** - Get automatic suggestions based on trigger conditions:
   - High caffeine intake (>80mg) → "Reduce caffeine intake especially in evening"
   - Missing medication → "Take tab2 as prescribed to help sleep continuity"
   - Long naps (>30 min) → "Limit naps to 20–30 min max"
   - And more rules defined in `data/rules.json`

4. **AI-Powered Suggestions** - Receive personalized sleep improvement advice using local LLM (Ollama):
   - Analyzes your log data
   - Combines rule-based remedies with AI insights
   - Generates actionable suggestions for better sleep

## Requirements
- Python 3.8 or higher
- Ollama AI platform installed and configured
- `qwen3:1.7b` model installed in Ollama
- Python packages: `click`, `requests` (see `requirements.txt`)

## Quick Start

### 1. Setup Environment

```bash
# Clone/navigate to project directory
cd Sleepwell

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Setup Ollama

```bash
# Install Ollama from https://ollama.com/
# Then pull the required model:
ollama pull qwen3:1.7b

# Verify installation
ollama list  # Should show qwen3:1.7b

# Ensure Ollama is running (usually starts automatically)
# If not: ollama serve
```

### 3. Use the CLI

#### Log Your Sleep Data

Navigate to the `sleepwell-cli` directory and log your data:

```bash
cd sleepwell-cli

python cli.py log \
  --user "your_user_id" \
  --date "2025-01-21" \
  --took_tab1 "True" \
  --took_tab2 "False" \
  --caffeine 120.0 \
  --sleep_time 7.5 \
  --mood 8.0 \
  --workout 30.0 \
  --continuity 90.0
```

**Required parameters:**
- `--user`: Your user ID (any string identifier)
- `--date`: Date in YYYY-MM-DD format

**Optional parameters** (all have defaults):
- `--took_tab1`, `--took_tab2`, `--took_tab3`: "True" or "False" (as strings)
- `--caffeine`: Caffeine intake in mg (float, default: 0.0)
- `--alcohol`: Alcohol intake in units (float, default: 0.0)
- `--workout`: Workout duration in minutes (float, default: 0.0)
- `--nap`: Nap duration in minutes (float, default: 0.0)
- `--mood`: Mood rating 0-10 (float, default: 0.0)
- `--sleep_time`: Sleep duration in hours (float, default: 0.0)
- `--outdoor`: Outdoor activity hours (float, default: 0.0)
- `--wakeups`: Number of wakeups during sleep (integer, default: 0)
- `--continuity`: Sleep continuity score 0-100 (float, default: 0.0)

#### Generate AI Suggestions

After logging your data, generate personalized suggestions:

```bash
python cli.py suggest \
  --user "your_user_id" \
  --date "2025-01-21"
```

This will:
1. Load your log entry for the specified date
2. Calculate your sleep score
3. Evaluate rule-based remedies
4. Generate AI-powered personalized suggestions
5. Save suggestions back to your log entry
6. Display the suggestion

## Complete Example Workflow

```bash
# Activate virtual environment
source venv/bin/activate

# Navigate to CLI directory
cd sleepwell-cli

# 1. Log your sleep data
python cli.py log --user "john" --date "2025-01-21" \
  --took_tab1 "True" \
  --caffeine 150.0 \
  --sleep_time 7.0 \
  --mood 7.5 \
  --workout 30.0 \
  --continuity 85.0

# 2. Generate suggestions
python cli.py suggest --user "john" --date "2025-01-21"
```

## How It Works

1. **Logging** - Your sleep data is saved to `data/logs.json` as JSON entries
2. **Scoring** - Sleep score is calculated: `(sleep_time_hours / 8 * 40) + (continuity_score * 40) + (mood_rating * 20)`
3. **Rule Evaluation** - Conditions in `data/rules.json` are evaluated (e.g., caffeine > 80mg triggers a remedy)
4. **AI Suggestions** - Rule-based remedies + log data are sent to Ollama LLM to generate personalized advice

## Data Storage

All data is stored locally in JSON files:
- `data/logs.json` - Your sleep log entries
- `data/rules.json` - Rule-based remedies configuration

## Notes

- **Local LLM**: Uses Ollama running on your machine (no cloud API, no internet required after setup)
- **No API Keys**: No authentication needed - everything runs locally
- **Privacy**: All your data stays on your machine
- **Updates**: Running the same log command with same user/date will update the existing entry

## Troubleshooting

- **"Connection refused"**: Make sure Ollama is running (`ollama serve`)
- **"Model not found"**: Pull the model (`ollama pull qwen3:1.7b`)
- **"Module not found"**: Install dependencies (`pip install -r requirements.txt`)
- **"No log entry found"**: Make sure you've logged data for that user/date first

For detailed setup instructions and more examples, see [SETUP_GUIDE.md](SETUP_GUIDE.md).
