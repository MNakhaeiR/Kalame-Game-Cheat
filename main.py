import pyautogui
import time
from itertools import permutations, combinations_with_replacement, product
import threading
from queue import Queue
from persian_words import filter_words_by_letters, get_vajeyab_words, get_persian_words


class PersianWordBruteForceBot:
    def __init__(self):
        """Initialize the bot with manual coordinate configuration"""

        # =============================================================================
        # CONFIGURE THESE COORDINATES MANUALLY
        # =============================================================================

        # Letter button coordinates (RIGHT TO LEFT: 7, 6, 5, 4, 3, 2, 1)
        # You need to manually set these coordinates for each button position
        self.button_positions = {
            'pos_1': (417, 672),
            'pos_2': (380, 667),
            'pos_3': (330, 672),
            'pos_4': (283, 673),
            'pos_5': (245, 673),
            'pos_6': (192, 673),
            'pos_7': (153, 674),
        }
        self.clear_button = (181, 708)
        self.random_click = (368, 261)

        # =============================================================================

        # Game state
        self.current_letters = []
        self.tried_combinations = set()
        self.is_running = False

        # PyAutoGUI settings
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.03  # Fast clicking

        print("🎮 Persian Word Brute Force Bot Initialized")
        print("📝 Make sure to configure coordinates in the code!")

    def setup_coordinates(self):
        """Interactive coordinate setup helper"""
        print("\n🎯 COORDINATE SETUP HELPER")
        print("=" * 50)

        print("Move your mouse to each position and press Enter:")

        # Setup letter buttons
        for i in range(1, 8):
            input(
                f"Move mouse to letter button position {i} (right to left) and press Enter..."
            )
            x, y = pyautogui.position()
            self.button_positions[f"pos_{i}"] = (x, y)
            print(f"  Position {i}: ({x}, {y})")

        # Setup clear button
        input("\nMove mouse to CLEAR button (❌) and press Enter...")
        x, y = pyautogui.position()
        self.clear_button = (x, y)
        print(f"  Clear button: ({x}, {y})")

        # Setup random click
        input(
            "\nMove mouse to empty area (for closing notifications) and press Enter..."
        )
        x, y = pyautogui.position()
        self.random_click = (x, y)
        print(f"  Random click: ({x}, {y})")

        print("\n📋 COPY THESE COORDINATES TO YOUR CODE:")
        print("=" * 50)
        print("self.button_positions = {")
        for i in range(1, 8):
            pos = self.button_positions[f"pos_{i}"]
            print(f"    'pos_{i}': {pos},")
        print("}")
        print(f"self.clear_button = {self.clear_button}")
        print(f"self.random_click = {self.random_click}")

    def set_letters(self, letters):
        """Set the 7 letters for current game (RIGHT TO LEFT order)"""
        if len(letters) != 7:
            print(f"❌ Expected 7 letters, got {len(letters)}")
            return False

        self.current_letters = list(letters)
        self.tried_combinations.clear()

        print(f"🎯 Letters set (R→L): {' '.join(letters)}")
        print(f"📍 Button mapping:")
        for i, letter in enumerate(letters, 1):
            pos = self.button_positions[f"pos_{i}"]
            print(f"  {letter} → Position {i} {pos}")

        return True

    def click_clear(self):
        """Click the clear button"""
        try:
            pyautogui.click(self.clear_button)
            time.sleep(0.1)
            return True
        except Exception as e:
            print(f"❌ Error clicking clear: {e}")
            return False

    def click_random_area(self):
        """Click random area to close notifications"""
        try:
            pyautogui.click(self.random_click)
            time.sleep(0.1)
            return True
        except Exception as e:
            print(f"❌ Error clicking random area: {e}")
            return False

    def click_letter_sequence(self, word):
        """Click sequence of letters to form a word"""
        try:
            for letter in word:
                if letter not in self.current_letters:
                    print(f"❌ Letter '{letter}' not available")
                    return False

                # Find position of this letter
                letter_index = self.current_letters.index(letter) + 1
                position_key = f"pos_{letter_index}"

                if position_key in self.button_positions:
                    x, y = self.button_positions[position_key]
                    pyautogui.click(x, y)
                    time.sleep(0.05)  # Small delay between clicks
                else:
                    print(f"❌ Position {position_key} not configured")
                    return False

            # Small delay after completing word
            time.sleep(0.2)
            return True

        except Exception as e:
            print(f"❌ Error clicking sequence '{word}': {e}")
            return False

    def generate_smart_word_list(self):
        """Generate smart word list prioritizing vajehyab-validated words (3+ letters with repetition allowed)"""
        print("🧠 GENERATING SMART PERSIAN WORD LIST WITH VAJEHYAB VALIDATION")
        print("=" * 70)
        
        # Priority 1: Get words validated by vajehyab.com
        print("🌐 Validating words with vajehyab.com...")
        try:
            vajehyab_words = get_vajeyab_words(self.current_letters, max_candidates=50)  # Limit to avoid too many API calls
            print(f"✅ Found {len(vajehyab_words)} vajehyab-validated words")
        except Exception as e:
            print(f"⚠️ Error with vajehyab.com, falling back to local dictionary: {e}")
            vajehyab_words = []
        
        # Priority 2: Local Persian words that can be made from available letters (as fallback)
        print("📚 Finding local Persian words...")
        local_persian_words = filter_words_by_letters(
            self.current_letters, 
            min_length=3,  # Changed from 2 to 3+ letters as requested
            allow_repetition=True  # Allow letter repetition as requested
        )
        # Only include local words that weren't already found by vajehyab
        local_persian_words = [word for word in local_persian_words if word not in vajehyab_words]
        print(f"✅ Found {len(local_persian_words)} additional local Persian words")
        
        # Priority 3: Generate limited additional combinations if we don't have enough words
        total_validated_words = len(vajehyab_words) + len(local_persian_words)
        if total_validated_words < 20:  # Only generate additional if we have few validated words
            print("🔤 Generating limited additional combinations...")
            additional_combinations = []
            
            # Much more limited combinations since we prioritize validated words
            max_combinations_per_length = 200  # Reduced limit
            
            for length in range(3, 6):  # Reduced range (3 to 5 letters)
                print(f"📝 Generating {length}-letter combinations (max {max_combinations_per_length})...")
                
                count = 0
                # Use product to allow repetition of letters
                for combo in product(self.current_letters, repeat=length):
                    if count >= max_combinations_per_length:
                        break
                        
                    word = "".join(combo)
                    # Only add if not already in validated words
                    if word not in vajehyab_words and word not in local_persian_words:
                        additional_combinations.append(word)
                        count += 1
            
            # Remove duplicates from additional combinations
            additional_combinations = list(set(additional_combinations))
            print(f"🎯 Generated {len(additional_combinations)} additional combinations")
        else:
            additional_combinations = []
            print("🎯 Skipping additional combinations - enough validated words found")
        
        # Combine lists with priority: vajehyab words first, then local Persian, then additional
        all_words = list(vajehyab_words) + list(local_persian_words) + additional_combinations
        
        print(f"🚀 TOTAL WORD LIST: {len(all_words)} words")
        print(f"🌐 Vajehyab-validated words: {len(vajehyab_words)}")
        print(f"📚 Local Persian words: {len(local_persian_words)}")
        print(f"🔤 Additional combinations: {len(additional_combinations)}")
        print(f"🎯 Letters can be repeated as requested")
        print(f"📏 Minimum word length: 3+ letters")
        print(f"⚡ Prioritizes vajehyab.com validated words")
        
        return all_words

    def generate_all_combinations(self):
        """Legacy method - now calls the smart word generation"""
        return self.generate_smart_word_list()

    def brute_force_attack(self, delay_between_words=0.3):
        """Brute force all possible combinations"""
        if not self.current_letters:
            print("❌ No letters set! Use set_letters() first")
            return

        print(f"\n🚀 STARTING SMART BRUTE FORCE ATTACK WITH VAJEHYAB VALIDATION")
        print(f"📝 Letters: {' '.join(self.current_letters)}")
        print("🌐 Prioritizing vajehyab.com validated words + Persian dictionary + combinations")
        print("📏 Minimum word length: 3+ letters")
        print("=" * 70)

        # Generate smart word list
        combinations = self.generate_smart_word_list()

        self.is_running = True
        successful_attempts = 0

        try:
            for i, word in enumerate(combinations):
                if not self.is_running:
                    break

                if word in self.tried_combinations:
                    continue

                word_type = "📚" if word in get_persian_words() else "🔤"
                print(f"[{i+1:4d}/{len(combinations)}] Trying: {word_type} {word}")

                # Step 1: Clear previous input
                self.click_clear()

                # Step 2: Click letter sequence
                if self.click_letter_sequence(word):
                    successful_attempts += 1
                    print(f"✅ Successfully entered: {word}")
                else:
                    print(f"❌ Failed to enter: {word}")

                self.tried_combinations.add(word)

                # Delay between attempts
                time.sleep(delay_between_words)

                # Progress update every 50 attempts
                if (i + 1) % 50 == 0:
                    print(
                        f"\n📊 Progress: {i+1}/{len(combinations)} ({(i+1)/len(combinations)*100:.1f}%)"
                    )
                    print(f"✅ Successful attempts: {successful_attempts}")
                    print("-" * 30)

        except KeyboardInterrupt:
            print("\n⏹️ Brute force stopped by user")

        self.is_running = False

        print(f"\n🏁 BRUTE FORCE COMPLETED")
        print(f"📊 Total combinations tried: {len(self.tried_combinations)}")
        print(f"✅ Successful attempts: {successful_attempts}")

    def calibrate_coordinates(self):
        """Advanced coordinate calibration with visual feedback"""
        print("\n🎯 ADVANCED COORDINATE CALIBRATION")
        print("=" * 50)
        print("This will help you set precise coordinates with visual feedback")

        # Calibrate letter buttons
        print("\n📍 CALIBRATING LETTER BUTTONS (Right to Left)")
        print("The buttons are numbered 1-7 from RIGHT to LEFT")

        for i in range(1, 8):
            print(f"\n🎯 Setting up Letter Button Position {i}")
            print("Move your mouse to the button and press Enter...")

            while True:
                # Show current mouse position
                x, y = pyautogui.position()
                print(
                    f"\rCurrent mouse position: ({x}, {y}) - Press Enter when ready",
                    end="",
                    flush=True,
                )

                try:
                    # Non-blocking input check
                    import select
                    import sys

                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        input()
                        break
                except:
                    # Fallback for Windows
                    input()
                    break

                time.sleep(0.1)

            # Test click at this position
            print(f"\n🧪 Testing click at ({x}, {y})...")
            pyautogui.click(x, y)
            time.sleep(0.3)

            confirm = input("Was the click accurate? (y/n): ").lower().strip()
            if confirm == "y":
                self.button_positions[f"pos_{i}"] = (x, y)
                print(f"✅ Position {i} saved: ({x}, {y})")
            else:
                print("❌ Let's try again...")
                i -= 1  # Retry this position
                continue

        # Calibrate clear button
        print(f"\n🧹 CALIBRATING CLEAR BUTTON (❌)")
        print("Move your mouse to the clear/delete button...")

        while True:
            x, y = pyautogui.position()
            print(
                f"\rCurrent mouse position: ({x}, {y}) - Press Enter when ready",
                end="",
                flush=True,
            )

            try:
                import select
                import sys

                if select.select([sys.stdin], [], [], 0.1)[0]:
                    input()
                    break
            except:
                input()
                break

            time.sleep(0.1)

        print(f"\n🧪 Testing clear button click at ({x}, {y})...")
        pyautogui.click(x, y)
        time.sleep(0.3)

        confirm = (
            input("Did it click the clear button correctly? (y/n): ").lower().strip()
        )
        if confirm == "y":
            self.clear_button = (x, y)
            print(f"✅ Clear button saved: ({x}, {y})")

        # Calibrate random click area
        print(f"\n🎲 CALIBRATING RANDOM CLICK AREA")
        print("Move mouse to an empty area (for closing notifications)...")

        while True:
            x, y = pyautogui.position()
            print(
                f"\rCurrent mouse position: ({x}, {y}) - Press Enter when ready",
                end="",
                flush=True,
            )

            try:
                import select
                import sys

                if select.select([sys.stdin], [], [], 0.1)[0]:
                    input()
                    break
            except:
                input()
                break

            time.sleep(0.1)

        print(f"\n🧪 Testing random click at ({x}, {y})...")
        pyautogui.click(x, y)
        time.sleep(0.3)

        confirm = input("Is this a good empty area to click? (y/n): ").lower().strip()
        if confirm == "y":
            self.random_click = (x, y)
            print(f"✅ Random click area saved: ({x}, {y})")

        # Show final configuration
        print(f"\n📋 FINAL CALIBRATION RESULTS")
        print("=" * 50)
        print("Copy this configuration to your code:")
        print()
        print("self.button_positions = {")
        for i in range(1, 8):
            pos = self.button_positions[f"pos_{i}"]
            print(f"    'pos_{i}': {pos},  # Letter button {i} (R→L)")
        print("}")
        print(f"self.clear_button = {self.clear_button}  # Clear button (❌)")
        print(f"self.random_click = {self.random_click}  # Random click area")

        # Save to file option
        save_config = input("\nSave configuration to file? (y/n): ").lower().strip()
        if save_config == "y":
            self.save_calibration_to_file()

    def save_calibration_to_file(self):
        """Save calibrated coordinates to a file"""
        try:
            config_content = f"""# Persian Word Bot - Calibrated Coordinates
# Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}

# Letter button positions (Right to Left: 1, 2, 3, 4, 5, 6, 7)
button_positions = {{
"""
            for i in range(1, 8):
                pos = self.button_positions[f"pos_{i}"]
                config_content += f"    'pos_{i}': {pos},  # Letter button {i}\n"

            config_content += f"""}}

# Other coordinates
clear_button = {self.clear_button}  # Clear button (❌)
random_click = {self.random_click}  # Random click area

# How to use:
# 1. Copy the coordinates above
# 2. Replace the coordinates in your bot code
# 3. Test with option 3 in the menu
"""

            filename = f"bot_coordinates_{int(time.time())}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(config_content)

            print(f"✅ Configuration saved to: {filename}")

        except Exception as e:
            print(f"❌ Error saving configuration: {e}")

    def quick_calibration(self):
        """Quick calibration mode - just get coordinates"""
        print("\n⚡ QUICK CALIBRATION MODE")
        print("=" * 30)
        print("Quickly set all coordinates without testing")

        # Quick setup for all positions
        positions = [
            ("Letter Button 1 (rightmost)", "pos_1"),
            ("Letter Button 2", "pos_2"),
            ("Letter Button 3", "pos_3"),
            ("Letter Button 4 (middle)", "pos_4"),
            ("Letter Button 5", "pos_5"),
            ("Letter Button 6", "pos_6"),
            ("Letter Button 7 (leftmost)", "pos_7"),
            ("Clear Button (❌)", "clear"),
            ("Random Click Area", "random"),
        ]

        coordinates = {}

        for name, key in positions:
            input(f"\nMove mouse to {name} and press Enter...")
            x, y = pyautogui.position()
            coordinates[key] = (x, y)
            print(f"✅ {name}: ({x}, {y})")

        # Apply coordinates
        for i in range(1, 8):
            self.button_positions[f"pos_{i}"] = coordinates[f"pos_{i}"]
        self.clear_button = coordinates["clear"]
        self.random_click = coordinates["random"]

        print(f"\n🎯 Quick calibration completed!")
        print("Use 'Test coordinates' to verify everything works correctly.")

    def test_coordinates(self):
        """Test all configured coordinates"""
        print("\n🧪 TESTING COORDINATES")
        print("=" * 30)

        # Test clear button
        input("Press Enter to test CLEAR button...")
        self.click_clear()
        print("✅ Clear button tested")

        # Test random click
        input("Press Enter to test RANDOM CLICK...")
        self.click_random_area()
        print("✅ Random click tested")

        # Test each letter position
        for i in range(1, 8):
            input(f"Press Enter to test letter position {i} (button {i} from right)...")
            pos = self.button_positions[f"pos_{i}"]
            pyautogui.click(pos)
            time.sleep(0.2)
            print(f"✅ Position {i} tested: {pos}")

        print(f"\n🎯 All coordinates tested!")
        print("If any clicks were inaccurate, use calibration to fix them.")

    def quick_test_word(self, word):
        """Quick test to enter a specific word"""
        print(f"\n🧪 Testing word: {word}")

        if not self.current_letters:
            print("❌ No letters set!")
            return

        self.click_clear()
        time.sleep(0.2)

        if self.click_letter_sequence(word):
            print(f"✅ Successfully entered: {word}")
        else:
            print(f"❌ Failed to enter: {word}")

    def stop_brute_force(self):
        """Stop the brute force attack"""
        self.is_running = False
        print("🛑 Stopping brute force...")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    bot = PersianWordBruteForceBot()

    print("🎮 PERSIAN WORD GAME BRUTE FORCE BOT")
    print("=" * 50)

    while True:
        print("\n📋 MENU:")
        print("1. Interactive coordinate setup (first time)")
        print("2. Advanced calibration (with testing)")
        print("3. Quick calibration (fast setup)")
        print("4. Set letters and start brute force")
        print("5. Test coordinates")
        print("6. Quick test word")
        print("7. Test Persian word generation")
        print("8. Test vajehyab.com integration")
        print("9. Exit")

        choice = input("\nSelect option (1-9): ").strip()

        if choice == "1":
            bot.setup_coordinates()

        elif choice == "2":
            bot.calibrate_coordinates()

        elif choice == "3":
            bot.quick_calibration()

        elif choice == "4":
            letters = input("\nEnter 7 Persian letters (RIGHT to LEFT order): ").strip()

            if len(letters) == 7:
                if bot.set_letters(letters):
                    delay = input("Enter delay between words (default 0.3s): ").strip()
                    delay = float(delay) if delay else 0.3

                    print(f"\n⚠️  Make sure:")
                    print("1. Telegram is focused")
                    print("2. Game panel is visible")
                    print("3. You can see the letter buttons")

                    input("\nPress Enter to start brute force attack...")
                    bot.brute_force_attack(delay)
            else:
                print("❌ Please enter exactly 7 letters")

        elif choice == "5":
            bot.test_coordinates()

        elif choice == "6":
            if bot.current_letters:
                word = input("Enter word to test: ").strip()
                bot.quick_test_word(word)
            else:
                print("❌ Set letters first!")

        elif choice == "7":
            # Test Persian word generation
            letters = input("\nEnter 7 Persian letters to test word generation: ").strip()
            if len(letters) == 7:
                print(f"\n🧪 Testing Persian word generation for letters: {' '.join(letters)}")
                
                # Temporarily set letters
                temp_letters = bot.current_letters
                bot.current_letters = list(letters)
                
                # Generate words
                words = bot.generate_smart_word_list()
                
                # Show first 20 words
                print(f"\n📝 First 20 words (out of {len(words)} total):")
                for i, word in enumerate(words[:20], 1):
                    persian_word_indicator = "📚" if word in get_persian_words() else "🔤"
                    print(f"{i:2d}. {persian_word_indicator} {word}")
                
                if len(words) > 20:
                    print(f"... and {len(words) - 20} more words")
                
                # Restore previous letters
                bot.current_letters = temp_letters
            else:
                print("❌ Please enter exactly 7 letters")

        elif choice == "8":
            # Test vajehyab.com integration
            print("\n🌐 TESTING VAJEHYAB.COM INTEGRATION")
            print("=" * 50)
            
            # Test single word validation
            test_word = input("Enter a Persian word to test with vajehyab.com: ").strip()
            if test_word:
                from persian_words import validate_word_with_vajeyab
                print(f"\n🔍 Testing word '{test_word}' with vajehyab.com...")
                is_valid = validate_word_with_vajeyab(test_word)
                if is_valid:
                    print(f"✅ '{test_word}' is a valid word according to vajehyab.com")
                else:
                    print(f"❌ '{test_word}' is not recognized as a valid word by vajehyab.com")
            
            # Test with letters
            letters = input("\nEnter letters to test vajehyab integration (optional): ").strip()
            if letters:
                print(f"\n🔍 Testing vajehyab word generation with letters: {letters}")
                try:
                    vajehyab_words = get_vajeyab_words(list(letters), max_candidates=10)  # Limited test
                    if vajehyab_words:
                        print(f"\n✅ Found {len(vajehyab_words)} validated words:")
                        for i, word in enumerate(vajehyab_words, 1):
                            print(f"{i}. {word}")
                    else:
                        print("❌ No valid words found or vajehyab.com unavailable")
                except Exception as e:
                    print(f"❌ Error testing vajehyab integration: {e}")

        elif choice == "9":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice")

print("\n🎯 Tips for best results:")
print("- Use delay of 0.2-0.5 seconds between words")
print("- Make sure Telegram window stays focused")
print("- Position coordinates accurately")
print("- The bot now prioritizes vajehyab.com validated words first! 🌐")
print("- Letters can be repeated in words (as requested)")
print("- Minimum word length is now 3+ letters")
print("- Press Ctrl+C to stop brute force anytime")
print("- Use option 7 to test Persian word generation")
print("- Use option 8 to test vajehyab.com integration")
