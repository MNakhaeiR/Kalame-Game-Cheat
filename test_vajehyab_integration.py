#!/usr/bin/env python3
"""
Test the vajehyab.com integration functionality
"""

import sys
import os

# Add current directory to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from persian_words import validate_word_with_vajeyab, get_vajeyab_words

def test_word_validation():
    """Test word validation with vajehyab.com"""
    print("🧪 TESTING VAJEHYAB.COM WORD VALIDATION")
    print("=" * 50)
    
    test_words = ['سلام', 'کتاب', 'ابcd123', 'نزدیک']
    
    for word in test_words:
        print(f"\nTesting word: {word}")
        result = validate_word_with_vajeyab(word)
        print(f"Result: {'✅ Valid' if result else '❌ Invalid/Error'}")

def test_word_generation():
    """Test word generation with vajehyab validation"""
    print("\n\n🧪 TESTING VAJEHYAB.COM WORD GENERATION")
    print("=" * 50)
    
    test_letters = ['ا', 'ب', 'ر', 'د']
    print(f"Testing with letters: {test_letters}")
    
    # Test with very limited candidates to avoid too many network calls
    try:
        words = get_vajeyab_words(test_letters, max_candidates=5)
        print(f"\nFound {len(words)} validated words:")
        for i, word in enumerate(words, 1):
            print(f"{i}. {word}")
    except Exception as e:
        print(f"Error during word generation: {e}")

def test_smart_word_list_generation():
    """Test the smart word list generation that includes vajehyab validation"""
    print("\n\n🧪 TESTING SMART WORD LIST GENERATION")
    print("=" * 50)
    
    # Import the bot class
    from main import PersianWordBruteForceBot
    
    bot = PersianWordBruteForceBot()
    bot.current_letters = ['ا', 'ب', 'ر', 'د']
    
    print(f"Testing with letters: {bot.current_letters}")
    
    try:
        words = bot.generate_smart_word_list()
        print(f"\nGenerated {len(words)} total words")
        
        # Show first 10 words
        print("\nFirst 10 words:")
        for i, word in enumerate(words[:10], 1):
            print(f"{i:2d}. {word}")
            
    except Exception as e:
        print(f"Error during smart word list generation: {e}")

if __name__ == "__main__":
    print("🚀 VAJEHYAB.COM INTEGRATION TESTS")
    print("=" * 60)
    print("Note: Network access to vajehyab.com may be restricted in this environment")
    print("Tests will show the behavior and fallback mechanisms.")
    print()
    
    # Run tests
    test_word_validation()
    test_word_generation() 
    test_smart_word_list_generation()
    
    print("\n✅ TESTS COMPLETED")
    print("=" * 60)
    print("💡 In a real environment with network access:")
    print("   - vajehyab.com would be contacted to validate words")
    print("   - Only verified words would be used in the brute force")
    print("   - This provides much more accurate word validation")