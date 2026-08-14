# This file contains the main logic of reading the contents of the book
from stats import book_word_count, count_characters

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "books/frankenstein.txt"
    book_contents = get_book_text(filepath)
    num_words = book_word_count(book_contents)
    print(f"Found {num_words} total words")
    letters: dict[str, int] = count_characters(book_contents)
    print(letters)

main()
