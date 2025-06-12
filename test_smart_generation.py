#!/usr/bin/env python3
"""
Test the smart word generation functionality from main.py without GUI
"""

import sys
import os
from itertools import product

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from persian_words import filter_words_by_letters, get_persian_words

class TestPersianWordGenerator:
    """Test class that mimics the word generation from main.py"""
    
    def __init__(self):
        self.current_letters = []
    
    def set_letters(self, letters):
        """Set the 7 letters for current game"""
        self.current_letters = list(letters)
        return True
    
    def generate_smart_word_list(self):
        """Generate smart word list prioritizing real Persian words (3+ letters with repetition allowed)"""
        print("🧠 GENERATING SMART PERSIAN WORD LIST")
        print("=" * 50)
        
        # Priority 1: Real Persian words that can be made from available letters
        print("📚 Finding real Persian words...")
        persian_words = filter_words_by_letters(
            self.current_letters, 
            min_length=3,  # Changed from 2 to 3+ letters as requested
            allow_repetition=True  # Allow letter repetition as requested
        )
        print(f"✅ Found {len(persian_words)} real Persian words")
        
        # Priority 2: Generate additional combinations with repetition allowed (limited for performance)
        print("🔤 Generating additional combinations with letter repetition...")
        additional_combinations = []
        
        # Limit combinations to avoid excessive generation
        max_combinations_per_length = 1000  # Reasonable limit
        
        for length in range(3, 8):  # 3 to 7 letters (changed from 2)
            print(f"📝 Generating {length}-letter combinations (max {max_combinations_per_length})...")
            
            count = 0
            # Use product to allow repetition of letters
            for combo in product(self.current_letters, repeat=length):
                if count >= max_combinations_per_length:
                    break
                    
                word = "".join(combo)
                # Only add if not already in Persian words
                if word not in persian_words:
                    additional_combinations.append(word)
                    count += 1
        
        # Remove duplicates from additional combinations
        additional_combinations = list(set(additional_combinations))
        print(f"🎯 Generated {len(additional_combinations)} additional combinations")
        
        # Combine lists: Persian words first (priority), then additional combinations
        all_words = list(persian_words) + additional_combinations
        
        # Sort by priority: Persian words first, then by length
        persian_word_set = set(persian_words)
        all_words.sort(key=lambda x: (x not in persian_word_set, len(x)))
        
        print(f"🚀 TOTAL WORD LIST: {len(all_words)} words")
        print(f"📊 Real Persian words: {len(persian_words)}")
        print(f"📊 Additional combinations: {len(additional_combinations)}")
        print(f"🎯 Letters can be repeated as requested")
        print(f"📏 Minimum word length: 3+ letters")
        print(f"⚡ Optimized for practical use (max ~5K additional combinations)")
        
        return all_words

def test_smart_generation():
    """Test the smart word generation"""
    print("🧪 TESTING SMART WORD GENERATION")
    print("=" * 50)
    
    generator = TestPersianWordGenerator()
    
    # Test case 1
    test_letters = ['ا', 'ب', 'ر', 'د', 'س', 'ت', 'ن']
    print(f"\nTest 1 - Letters: {' '.join(test_letters)}")
    generator.set_letters(test_letters)
    words = generator.generate_smart_word_list()
    
    print(f"\nFirst 20 words (prioritized):")
    persian_words_set = get_persian_words()
    for i, word in enumerate(words[:20], 1):
        word_type = "📚" if word in persian_words_set else "🔤"
        print(f"{i:2d}. {word_type} {word}")
    
    # Test case 2
    test_letters_2 = ['م', 'ن', 'ز', 'ل', 'ک', 'ت', 'ب']
    print(f"\n\nTest 2 - Letters: {' '.join(test_letters_2)}")
    generator.set_letters(test_letters_2)
    words_2 = generator.generate_smart_word_list()
    
    print(f"\nFirst 15 words (prioritized):")
    for i, word in enumerate(words_2[:15], 1):
        word_type = "📚" if word in persian_words_set else "🔤"
        print(f"{i:2d}. {word_type} {word}")
    
    print(f"\n✅ Smart word generation test completed!")

if __name__ == "__main__":
    test_smart_generation()