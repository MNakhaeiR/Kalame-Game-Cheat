# Persian Words Dictionary
# A collection of common Persian words for the Kalame game

# Common Persian words (3+ letters)
PERSIAN_WORDS = {
    # 3-letter words
    'آب', 'آن', 'این', 'من', 'تو', 'او', 'ما', 'شما', 'آنها',
    'کار', 'خانه', 'راه', 'روز', 'شب', 'صبح', 'عصر', 'ظهر',
    'دست', 'پا', 'سر', 'چشم', 'دل', 'جان', 'خون', 'مو',
    'نان', 'آب', 'شیر', 'گوشت', 'برنج', 'نمک', 'قند', 'چای',
    'کتاب', 'قلم', 'کاغذ', 'میز', 'صندلی', 'درب', 'پنجره', 'دیوار',
    'آسمان', 'زمین', 'خورشید', 'ماه', 'ستاره', 'ابر', 'باد', 'باران',
    'درخت', 'گل', 'برگ', 'میوه', 'سیب', 'پرتقال', 'موز', 'انگور',
    'سگ', 'گربه', 'اسب', 'گاو', 'پرنده', 'ماهی', 'مار', 'شیر',
    
    # 4-letter words
    'انسان', 'مردم', 'زندگی', 'دنیا', 'جهان', 'کشور', 'شهر', 'روستا',
    'مدرسه', 'دانشگاه', 'بیمارستان', 'مغازه', 'رستوران', 'هتل', 'پارک', 'باغ',
    'خانواده', 'پدر', 'مادر', 'برادر', 'خواهر', 'پسر', 'دختر', 'فرزند',
    'دوست', 'همسایه', 'استاد', 'دانشجو', 'دکتر', 'پزشک', 'مهندس', 'معلم',
    'ماشین', 'اتوبوس', 'قطار', 'هواپیما', 'دوچرخه', 'موتور', 'کشتی', 'تاکسی',
    'غذا', 'صبحانه', 'ناهار', 'شام', 'میوه', 'سبزیجات', 'گوشت', 'مرغ',
    'لباس', 'کفش', 'کلاه', 'عینک', 'ساعت', 'انگشتر', 'گردنبند', 'دستبند',
    'موسیقی', 'آهنگ', 'فیلم', 'تئاتر', 'نمایش', 'کنسرت', 'رقص', 'بازی',
    
    # 5-letter words
    'کامپیوتر', 'تلفن', 'تلویزیون', 'رادیو', 'اینترنت', 'ایمیل', 'وبسایت', 'برنامه',
    'ورزش', 'فوتبال', 'والیبال', 'بسکتبال', 'تنیس', 'شنا', 'دویدن', 'پیاده‌روی',
    'کتابخانه', 'موزه', 'تئاتر', 'سینما', 'باشگاه', 'استخر', 'زمین‌بازی', 'سالن',
    'هنرمند', 'نویسنده', 'شاعر', 'خواننده', 'بازیگر', 'کارگردان', 'نقاش', 'عکاس',
    'تاریخ', 'جغرافیا', 'ریاضی', 'فیزیک', 'شیمی', 'زیست‌شناسی', 'ادبیات', 'زبان',
    'سلامتی', 'بیماری', 'درمان', 'دارو', 'عمل', 'آزمایش', 'معاینه', 'ویزیت',
    'اقتصاد', 'سیاست', 'فرهنگ', 'مذهب', 'اجتماع', 'محیط‌زیست', 'طبیعت', 'آلودگی',
    
    # 6+ letter words
    'دانشمند', 'مهندسی', 'پزشکی', 'معماری', 'حسابداری', 'مدیریت', 'اقتصاد', 'حقوق',
    'تکنولوژی', 'اطلاعات', 'ارتباطات', 'مخابرات', 'صنعت', 'کشاورزی', 'تجارت', 'بازرگانی',
    'فرهنگستان', 'دانشگاه', 'آموزشگاه', 'پژوهشگاه', 'آزمایشگاه', 'کتابخانه', 'کارخانه', 'اداره',
    'جمهوری', 'دموکراسی', 'آزادی', 'عدالت', 'برابری', 'حقوق‌بشر', 'صلح', 'امنیت',
    'محیط‌زیست', 'گرمایش', 'آلودگی', 'طبیعت', 'حیوانات', 'گیاهان', 'جنگل', 'بیابان',
}

def get_persian_words():
    """Return set of Persian words"""
    return PERSIAN_WORDS

def filter_words_by_letters(available_letters, min_length=3, allow_repetition=True):
    """
    Filter Persian words that can be made from available letters
    
    Args:
        available_letters: List of available letters
        min_length: Minimum word length (default 3)
        allow_repetition: Whether letters can be repeated (default True)
    
    Returns:
        List of valid Persian words that can be made from available letters
    """
    valid_words = []
    available_letters_lower = [letter.lower() for letter in available_letters]
    
    for word in PERSIAN_WORDS:
        if len(word) < min_length:
            continue
            
        word_lower = word.lower()
        can_make_word = True
        
        if allow_repetition:
            # Check if all letters in word are available (can repeat)
            for letter in word_lower:
                if letter not in available_letters_lower:
                    can_make_word = False
                    break
        else:
            # Check if we have enough of each letter (no repetition)
            word_letter_count = {}
            for letter in word_lower:
                word_letter_count[letter] = word_letter_count.get(letter, 0) + 1
            
            available_letter_count = {}
            for letter in available_letters_lower:
                available_letter_count[letter] = available_letter_count.get(letter, 0) + 1
            
            for letter, needed_count in word_letter_count.items():
                if letter not in available_letter_count or available_letter_count[letter] < needed_count:
                    can_make_word = False
                    break
        
        if can_make_word:
            valid_words.append(word)
    
    # Sort by length (shorter words first for faster discovery)
    valid_words.sort(key=len)
    return valid_words

def validate_word_with_vajeyab(word, mock_mode=False):
    """
    Validate a single word using vajehyab.com
    
    Args:
        word: The Persian word to validate
        mock_mode: If True, use mock validation for testing (when vajehyab.com is unavailable)
    
    Returns:
        True if the word is valid according to vajehyab.com, False otherwise
    """
    import requests
    import urllib.parse
    import time
    
    # Mock mode for testing when vajehyab.com is not accessible
    if mock_mode:
        # Mock some common Persian words as valid
        common_words = {
            'سلام', 'کتاب', 'نزدیک', 'درب', 'ابر', 'باد', 'دست', 'نان', 
            'اسب', 'برادر', 'انسان', 'استاد', 'باران', 'دستبند'
        }
        is_valid = word in common_words
        print(f"🧪 Mock validation for '{word}': {'✅ Valid' if is_valid else '❌ Invalid'}")
        return is_valid
    
    try:
        # URL encode the Persian word
        encoded_word = urllib.parse.quote(word)
        url = f'https://vajehyab.com/?q={encoded_word}'
        
        # Make request with timeout
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            # Check for indicators that the word is valid
            # Look for common Persian dictionary indicators
            content = response.text.lower()
            
            # These are common indicators that a word definition was found
            valid_indicators = [
                'معنی',  # meaning
                'تعریف',  # definition  
                'کلمه',   # word
                'واژه',   # vocabulary
                'اسم',    # noun
                'فعل',    # verb
                'صفت',    # adjective
                'definition',
                'meaning'
            ]
            
            # Check if any valid indicators are present
            for indicator in valid_indicators:
                if indicator in content:
                    print(f"✅ Valid word found on vajehyab: {word}")
                    return True
            
            # If no indicators found, likely not a valid word
            print(f"❌ Invalid word on vajehyab: {word}")
            return False
        else:
            print(f"⚠️ vajehyab.com returned status {response.status_code} for word: {word}")
            return False
            
    except Exception as e:
        print(f"⚠️ Error validating word '{word}' with vajehyab.com: {e}")
        return False

def get_vajeyab_words(letters, max_candidates=100, mock_mode=False):
    """
    Get words from Vajeyab website by generating candidates and validating them
    
    Args:
        letters: Available letters
        max_candidates: Maximum number of candidates to test (to avoid too many API calls)
        mock_mode: If True, use mock validation for testing
    
    Returns:
        List of valid words from Vajeyab
    """
    from itertools import product
    import time
    
    print(f"🔍 Generating candidates from letters {letters} and validating with vajehyab.com...")
    if mock_mode:
        print("🧪 Using mock mode for testing")
        
    valid_words = []
    candidates_tested = 0
    
    # Generate candidates of different lengths (3-6 letters for efficiency)
    for length in range(3, min(7, len(letters) + 1)):
        if candidates_tested >= max_candidates:
            break
            
        print(f"📝 Testing {length}-letter combinations...")
        
        # Generate combinations with repetition allowed
        for combo in product(letters, repeat=length):
            if candidates_tested >= max_candidates:
                break
                
            word = "".join(combo)
            candidates_tested += 1
            
            print(f"[{candidates_tested}/{max_candidates}] Testing: {word}")
            
            # Validate with vajehyab.com (or mock)
            if validate_word_with_vajeyab(word, mock_mode=mock_mode):
                valid_words.append(word)
                print(f"✅ Added valid word: {word}")
            
            # Small delay to be respectful to the server (only in real mode)
            if not mock_mode:
                time.sleep(0.1)
    
    print(f"🎯 Found {len(valid_words)} valid words from vajehyab.com out of {candidates_tested} candidates tested")
    return valid_words

if __name__ == "__main__":
    # Test the functions
    test_letters = ['ا', 'ب', 'ر', 'د', 'س', 'ت', 'ن']
    words = filter_words_by_letters(test_letters)
    print(f"Found {len(words)} words from letters: {test_letters}")
    for word in words[:10]:  # Show first 10
        print(f"- {word}")