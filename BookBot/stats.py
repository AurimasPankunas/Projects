# This file contains the logic of counting the words and syllables in a book

def book_word_count(book: str) -> int:
    words = book.split()

    return len(words)

def count_characters(book: str) -> dict[str,int]:
    characters: dict[str,int] = {}
    for word in book:
        for character in word:
            lower_character = character.lower()
            if lower_character not in characters:
                characters[lower_character] = 1
                continue
            characters[lower_character] += 1
    return characters
