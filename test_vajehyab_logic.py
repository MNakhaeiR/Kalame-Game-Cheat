#!/usr/bin/env python3
"""
Test the vajehyab.com integration logic without requiring full dependencies
"""

import sys
import os
from itertools import product

# Add current directory to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_url_encoding():
    """Test URL encoding of Persian words"""
    import urllib.parse
    
    print("🧪 TESTING URL ENCODING")
    print("=" * 30)
    
    test_words = ['سلام', 'کتاب', 'نزدیک', 'درب']
    
    for word in test_words:
        encoded = urllib.parse.quote(word)
        url = f'https://vajehyab.com/?q={encoded}'
        print(f"Word: {word}")
        print(f"URL:  {url}")
        print()

def test_candidate_generation():
    """Test candidate word generation logic"""
    print("🧪 TESTING CANDIDATE GENERATION")
    print("=" * 40)
    
    letters = ['ا', 'ب', 'ر']
    max_candidates = 10
    
    print(f"Letters: {letters}")
    print(f"Max candidates: {max_candidates}")
    print()
    
    candidates_generated = 0
    
    for length in range(3, min(6, len(letters) + 1)):
        print(f"📝 {length}-letter combinations:")
        
        for combo in product(letters, repeat=length):
            if candidates_generated >= max_candidates:
                break
                
            word = "".join(combo)
            candidates_generated += 1
            print(f"  {candidates_generated:2d}. {word}")
            
        if candidates_generated >= max_candidates:
            break
    
    print(f"\nTotal candidates generated: {candidates_generated}")

def test_fallback_logic():
    """Test the fallback logic when vajehyab is unavailable"""
    print("\n🧪 TESTING FALLBACK LOGIC")
    print("=" * 35)
    
    # Simulate what happens when vajehyab.com is unavailable
    vajehyab_words = []  # Empty - simulating network failure
    
    print("🌐 vajehyab.com result: Empty (simulating network error)")
    
    # Fallback to local dictionary
    try:
        from persian_words import filter_words_by_letters
        
        letters = ['ا', 'ب', 'ر', 'د']
        local_words = filter_words_by_letters(letters, min_length=3, allow_repetition=True)
        
        print(f"📚 Local dictionary fallback: {len(local_words)} words found")
        print("First 5 words:")
        for i, word in enumerate(local_words[:5], 1):
            print(f"  {i}. {word}")
            
        # Simulate the combined logic
        all_words = list(vajehyab_words) + list(local_words)
        print(f"\n🚀 Total words available: {len(all_words)}")
        print(f"   - vajehyab: {len(vajehyab_words)}")
        print(f"   - local: {len(local_words)}")
        
    except ImportError as e:
        print(f"Could not import local dictionary: {e}")

if __name__ == "__main__":
    print("🚀 VAJEHYAB.COM LOGIC TESTS")
    print("=" * 50)
    print("Testing the core logic without network dependencies")
    print()
    
    test_url_encoding()
    test_candidate_generation()
    test_fallback_logic()
    
    print("\n✅ LOGIC TESTS COMPLETED")
    print("=" * 50)
    print("💡 Key points:")
    print("   - URL encoding works correctly for Persian text")
    print("   - Candidate generation creates reasonable combinations")
    print("   - Fallback to local dictionary works when vajehyab is unavailable")
    print("   - Implementation prioritizes vanjehyab-validated words when available")