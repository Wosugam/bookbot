def count_words(text):
        words = text.split()
        return len(words)

def count_chars(text):
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1  # Count every character
    return char_counts

def sort_on(dict):
     return dict["num"]

def chars_dict_to_sorted_list(char_dict):
     sorted_list = []
     for char in char_dict:
          sorted_list.append({"char": char, "num": char_dict[char]})
     sorted_list.sort(reverse=True, key=sort_on)
     return sorted_list