import sys
from stats import (count_chars, chars_dict_to_sorted_list, count_words)

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) != 2:
		print(f"Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	word_count = count_words(book_text)
	char_dict = count_chars(book_text)
	chars_sorted_list = chars_dict_to_sorted_list(char_dict)
	print_report(book_path, word_count, chars_sorted_list)

def print_report(book_path, word_count, chars_sorted_list):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for item in chars_sorted_list:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

main() 
