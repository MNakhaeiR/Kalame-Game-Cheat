#!/usr/bin/env python3
"""
Test script for Persian word functionality without GUI dependencies
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from persian_words import filter_words_by_letters, get_persian_words

def test_persian_word_generation():
    """Test the Persian word generation functionality"""
    print("🧪 TESTING PERSIAN WORD GENERATION")
    print("=" * 50)
    
    # Test with sample letters
    test_letters = ['ا', 'ب', 'ر', 'د', 'س', 'ت', 'ن']
    print(f"Test letters: {' '.join(test_letters)}")
    
    # Test with repetition allowed
    words_with_repetition = filter_words_by_letters(
        test_letters, 
        min_length=3, 
        allow_repetition=True
    )
    
    print(f"\n📚 Found {len(words_with_repetition)} Persian words (with repetition):")
    for i, word in enumerate(words_with_repetition[:15], 1):
        print(f"{i:2d}. {word}")
    
    if len(words_with_repetition) > 15:
        print(f"... and {len(words_with_repetition) - 15} more words")
    
    # Test with different letters
    test_letters_2 = ['م', 'ن', 'ز', 'ل', 'ک', 'ت', 'ب']
    print(f"\n\nTest letters 2: {' '.join(test_letters_2)}")
    
    words_2 = filter_words_by_letters(
        test_letters_2, 
        min_length=3, 
        allow_repetition=True
    )
    
    print(f"\n📚 Found {len(words_2)} Persian words:")
    for i, word in enumerate(words_2[:15], 1):
        print(f"{i:2d}. {word}")
    
    if len(words_2) > 15:
        print(f"... and {len(words_2) - 15} more words")
    
    print(f"\n✅ Persian word generation test completed!")
    print(f"📊 Total Persian words in dictionary: {len(get_persian_words())}")

if __name__ == "__main__":
    test_persian_word_generation()