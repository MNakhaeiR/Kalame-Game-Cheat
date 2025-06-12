## Persian Word Game Brute Force Bot

An intelligent bot that automatically plays Persian word games like Kalame by prioritizing real Persian words and allowing letter repetition.

## New Features (Enhanced)

🧠 **Smart Persian Word Dictionary**: Prioritizes real Persian words over random combinations
📚 **Persian Word Database**: Built-in database of common Persian words
🔄 **Letter Repetition**: Letters can be repeated in words (as requested)
📏 **Minimum 3+ Letters**: Only tries words with 3 or more letters
⚡ **Optimized Performance**: Limits combinations to ~5K for practical use
🎯 **Word Prioritization**: Real Persian words are tried first

## Requirements

- pyautogui
- aiohttp
- asyncio
- requests
- pygetwindow

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Menu Options

1. Interactive coordinate setup (first time)
2. Advanced calibration (with testing)
3. Quick calibration (fast setup)
4. Set letters and start brute force
5. Test coordinates
6. Quick test word
7. **Test Persian word generation** (NEW)
8. Exit

## How It Works

1. **Persian Word Priority**: The bot first tries real Persian words that can be made from your available letters
2. **Letter Repetition**: Unlike the old version, letters can now be repeated in words
3. **Smart Generation**: Uses a built-in Persian word database to find meaningful words first
4. **Fallback Combinations**: If Persian words don't work, tries additional letter combinations
5. **Minimum Length**: Only tries words with 3+ letters (more likely to be valid)

## Persian Word Database

The bot includes a comprehensive database of common Persian words including:
- Common nouns and verbs
- Family and relationship terms  
- Technology and modern terms
- Nature and environment words
- Food and daily life terms
- And many more...

## Testing

Test the Persian word functionality without GUI:

```bash
python test_persian_words.py
python test_smart_generation.py
```