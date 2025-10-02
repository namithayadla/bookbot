import sys
from stats import num_of_words
from stats import count_chars
from stats import sort_on

def get_book_text(filepath):
    print("Analyzing book found at books/frankenstein.txt...")
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    result = num_of_words(book_text)
    print(result)
    chars_count = count_chars(book_text)
    sorted_chars_count = dict(sorted(chars_count.items(), reverse=True, key=lambda item: item[1]))
    for char, count in sorted_chars_count.items():
        print(f"{char}: {count}")
    print("============= END ===============")
main()