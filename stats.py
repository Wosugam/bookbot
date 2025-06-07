def count_words(text):
        words = text.split()
        return len(words)

def count_chars(text):
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1  # Count every character
    return char_counts
