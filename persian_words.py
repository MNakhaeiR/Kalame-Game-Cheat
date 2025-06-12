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

def get_vajeyab_words(letters):
    """
    Get words from Vajeyab website (placeholder implementation)
    In a real implementation, this would make API calls to vajeyab.com
    
    Args:
        letters: Available letters
    
    Returns:
        List of words from Vajeyab
    """
    # Placeholder - in real implementation, would call Vajeyab API
    # For now, return filtered words from our local dictionary
    return filter_words_by_letters(letters, min_length=3, allow_repetition=True)

if __name__ == "__main__":
    # Test the functions
    test_letters = ['ا', 'ب', 'ر', 'د', 'س', 'ت', 'ن']
    words = filter_words_by_letters(test_letters)
    print(f"Found {len(words)} words from letters: {test_letters}")
    for word in words[:10]:  # Show first 10
        print(f"- {word}")