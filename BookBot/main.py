# This file contains the main logic of reading the contents of the book
import sys
from stats import book_word_count, chars_dict_to_sorted_list, count_characters

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(filepath:str, num_words: int, sorted_characters: list[tuple[str,int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character[0].isalpha():
            print(f"{character[0]}: {character[1]}")
    print("============= END ===============")
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    num_words = book_word_count(book_contents)
    characters: dict[str, int] = count_characters(book_contents)
    sorted_characters: list[tuple[str, int]] = chars_dict_to_sorted_list(characters)
    print_report(filepath, num_words, sorted_characters)

main()
