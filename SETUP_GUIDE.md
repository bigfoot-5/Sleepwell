# Sleepwell Setup and Usage Guide

## Overview

Sleepwell is a sleep tracking CLI tool that:
1. **Logs** your daily sleep data (caffeine, alcohol, workouts, naps, mood, sleep duration, etc.)
2. **Scores** your sleep quality using a weighted formula
3. **Evaluates rules** to generate rule-based remedies (e.g., "Reduce caffeine if > 80mg")
4. **Generates AI suggestions** using Ollama (local LLM) to provide personalized sleep improvement advice

## Prerequisites

1. **Python 3.8+** installed
2. **Ollama** installed and running locally
3. **qwen3:1.7b model** pulled in Ollama

## Setup Instructions

### Step 1: Install Python Dependencies

```bash
# Navigate to the project directory
cd Sleepwell  # or wherever you cloned/extracted the project

# Activate virtual environment (if you have one)
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Install and Setup Ollama

1. **Download Ollama**: https://ollama.com/
2. **Install Ollama** on your system
3. **Pull the required model**:
   ```bash
   ollama pull qwen3:1.7b
   ```
4. **Verify Ollama is running**:
   ```bash
   ollama list
   ```
   You should see `qwen3:1.7b` in the list.

5. **Start Ollama service** (if not already running):
   - On macOS: Ollama should start automatically, or run `ollama serve`
   - The service runs on `http://localhost:11434` by default

### Step 3: Verify Data Files Exist

The project uses two JSON files:
- `data/logs.json` - Stores your sleep log entries
- `data/rules.json` - Contains rule-based remedies

These should already exist in the project. If not, create them:
- `data/logs.json`: `[]` (empty array)
- `data/rules.json`: Copy from the existing file structure

## Environment Variables (.env file)

**You do NOT need a .env file!**

This project uses **Ollama locally**, which:
- Runs on your machine (no cloud API)
- Doesn't require API keys
- Uses the hardcoded URL: `http://localhost:11434/api/generate`
- Uses the hardcoded model: `qwen3:1.7b`

If you want to customize the Ollama URL or model, you would need to modify `sleepwell-cli/suggestion.py` directly.

## How to Run

### Running the CLI

The CLI is run from the `sleepwell-cli` directory:

```bash
cd sleepwell-cli
python cli.py <command> [options]
```

### Command 1: Log Sleep Data

Log your sleep data for a specific user and date. This command:

1. Creates a log entry dictionary with all the provided data
2. Saves it to `data/logs.json` (creates the file if it doesn't exist)
3. If an entry already exists for that user/date, it **updates** the existing entry (upsert behavior)
4. Displays a confirmation message: `"Log entry saved for [user] [date]"`

**Example:**

```bash
python cli.py log \
  --user "user_123" \
  --date "2025-01-15" \
  --took_tab1 "True" \
  --took_tab2 "False" \
  --took_tab3 "True" \
  --caffeine 120.0 \
  --alcohol 0.5 \
  --workout 30.0 \
  --nap 10.0 \
  --mood 7.0 \
  --sleep_time 7.5 \
  --outdoor 1.0 \
  --wakeups 1 \
  --continuity 90.0
```

**Required options:**
- `--user`: User ID (string)
- `--date`: Date in YYYY-MM-DD format

**Optional options** (all default to 0 or False):
- `--took_tab1`, `--took_tab2`, `--took_tab3`: Boolean values passed as strings "True" or "False" (must be in quotes)
- `--caffeine`: Caffeine intake in mg (float)
- `--alcohol`: Alcohol intake in units (float)
- `--workout`: Workout duration in minutes (float)
- `--nap`: Nap duration in minutes (float)
- `--mood`: Mood rating (float, typically 0-10)
- `--sleep_time`: Sleep duration in hours (float)
- `--outdoor`: Outdoor activity hours (float)
- `--wakeups`: Number of wakeups during sleep (int)
- `--continuity`: Sleep continuity score (float, typically 0-100)

### Command 2: Generate Suggestions

Generate AI-powered sleep improvement suggestions:

```bash
python cli.py suggest \
  --user "user_123" \
  --date "2025-01-15"
```

This command will:
1. Load the log entry for the specified user/date from `data/logs.json`
2. Calculate a sleep score using the formula in `scoring.py`
3. Evaluate rule-based remedies from `data/rules.json` (e.g., if caffeine > 80mg, add remedy)
4. Send log data + remedies to Ollama LLM (`qwen3:1.7b` model) to generate personalized suggestions
5. Save the suggestions back to the log entry in `data/logs.json`
6. Display the LLM-generated suggestion in the terminal

**Note:** If no log entry exists for that user/date, you'll see: `"No log entry found for that date."`

## Example Workflow

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# 1. Log your sleep data
cd sleepwell-cli
python cli.py log --user "john" --date "2025-01-15" \
  --took_tab1 "True" \
  --caffeine 150.0 \
  --sleep_time 6.5 \
  --mood 6.0 \
  --continuity 75.0

# 2. Generate suggestions
python cli.py suggest --user "john" --date "2025-01-15"
```

**Expected output:**
- After logging: `Log entry saved for john 2025-01-15`
- After suggesting: `Suggestion: [AI-generated personalized suggestion]`

## How It Works Internally

1. **Logging** (`cli.py log`):
   - Creates a log entry dictionary
   - Saves to `data/logs.json` via `storage.py`

2. **Scoring** (`scoring.py`):
   - Formula: `(sleep_time_hours / 8 * 40) + (continuity_score * 40) + (mood_rating * 20)`
   - Maximum score: 100 (if 8+ hours, 100% continuity, 10 mood)
   - The score is calculated and saved to the log entry automatically

3. **Rule Evaluation** (`rules_engine.py`):
   - Reads `data/rules.json`
   - Evaluates conditions (e.g., `caffeine_intake_mg > 80`)
   - Returns matching remedies (e.g., "Reduce caffeine intake especially in evening")

4. **AI Suggestions** (`suggestion.py`):
   - Combines log entry + rule-based remedies
   - Sends prompt to Ollama API
   - Returns LLM-generated personalized suggestion
   - Saves suggestions back to log entry

## Troubleshooting

### "Connection refused" or "Cannot connect to Ollama"
- Ensure Ollama is running: `ollama serve` or check if it's running in the background
- Verify the service is on `http://localhost:11434`

### "Model not found"
- Pull the model: `ollama pull qwen3:1.7b`
- Verify: `ollama list`

### "Module not found: click"
- Install dependencies: `pip install -r requirements.txt`

### "No log entry found"
- Make sure you've logged data for that user/date first
- Check `data/logs.json` to see existing entries

## Data Structure

### Log Entry Structure
```json
{
  "user_id": "user_123",
  "date": "2025-01-15",
  "took_tab1": true,
  "took_tab2": false,
  "took_tab3": true,
  "caffeine_intake_mg": 120.0,
  "alcohol_intake_units": 0.5,
  "workout_minutes": 30.0,
  "nap_duration_minutes": 10.0,
  "mood_rating": 7.0,
  "sleep_time_hours": 7.5,
  "outdoor_activity_hours": 1.0,
  "wake_up_time": null,
  "number_of_wakeups": 1,
  "continuity_score": 90.0,
  "sleep_score": 3777.5,
  "suggestions": ["rule-based remedy", "LLM-generated suggestion"]
}
```

## Notes

- The project uses **local LLM** (Ollama), so no internet connection is needed for AI suggestions (after initial model download)
- All data is stored locally in JSON files - your privacy is protected
- **No API keys required** - everything runs on your machine
- Suggestions are saved back to the log entry automatically
- Running the same log command with the same user/date will **update** the existing entry (upsert behavior)
- Boolean values for `--took_tab1`, `--took_tab2`, `--took_tab3` must be passed as strings: `"True"` or `"False"` (with quotes)

## Command Reference

### View Help

```bash
cd sleepwell-cli
python cli.py --help           # List all commands
python cli.py log --help       # Show log command options
python cli.py suggest --help   # Show suggest command options
```

### View Your Logged Data

All your sleep logs are stored in `data/logs.json`. You can view them using:

```bash
# From the project root directory
cat data/logs.json | python3 -m json.tool  # Pretty-print JSON
# OR
cat data/logs.json  # Raw JSON
```

The logs are stored as an array of log entries. Each entry contains:
- All the data you logged
- Calculated `sleep_score` (after running suggest command)
- `suggestions` array containing rule-based remedies and AI-generated suggestions

