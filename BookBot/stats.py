# This file contains the logic of counting the words and syllables in a book

def book_word_count(book: str) -> int:
    words = book.split()

    return len(words)
