## Persian Word Game Brute Force Bot

An intelligent bot that automatically plays Persian word games like Kalame by using vajehyab.com word validation and prioritizing verified Persian words.

## New Features (Enhanced with vajehyab.com Integration)

🌐 **vajehyab.com Integration**: Validates words using the official Persian dictionary website
🧠 **Smart Word Validation**: Only tries words that are confirmed valid by vajehyab.com  
📚 **Fallback Dictionary**: Uses built-in Persian word database when vajehyab.com is unavailable
🔄 **Letter Repetition**: Letters can be repeated in words (as requested)
📏 **Minimum 3+ Letters**: Only tries words with 3 or more letters
⚡ **Optimized Performance**: Limits API calls to avoid overwhelming vajehyab.com
🎯 **Word Prioritization**: vajehyab-validated words are tried first, then local dictionary

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
7. **Test Persian word generation**
8. **Test vajehyab.com integration** (NEW)
9. Exit

## How It Works

1. **vajehyab.com Validation**: The bot generates word candidates and validates each one with vajehyab.com
2. **Word-by-Word Checking**: Each potential word is checked for validity before being tried in Telegram
3. **Smart Prioritization**: vajehyab-validated words are tried first, followed by local dictionary words
4. **Letter Repetition**: Letters can be repeated in words (as requested)
5. **Fallback System**: Uses built-in Persian word database when vajehyab.com is unavailable
6. **Minimum Length**: Only tries words with 3+ letters (more likely to be valid)

## vajehyab.com Integration

The bot now integrates with vajehyab.com (the official Persian dictionary website) to validate words:

- **Real-time Validation**: Each generated word is checked against vajehyab.com
- **Sample URL**: `https://vajehyab.com/?q=نزدیک` (for the word "نزدیک")
- **Accuracy**: Only words confirmed as valid by vajehyab.com are used
- **Respectful Usage**: Limited API calls with delays to avoid overwhelming the server
- **Fallback**: Automatically falls back to local dictionary if vajehyab.com is unavailable

## Persian Word Database

The bot includes a comprehensive database of common Persian words as fallback:
- Common nouns and verbs
- Family and relationship terms  
- Technology and modern terms
- Nature and environment words
- Food and daily life terms
- And many more...

## Testing

Test the functionality without GUI:

```bash
python test_persian_words.py
python test_smart_generation.py
python test_comprehensive_vajehyab.py  # Test vajehyab.com integration
```