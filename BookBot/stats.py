# This file contains the logic of counting the words and syllables in a book

# Returns how many words there are in the book
def book_word_count(book: str) -> int:
    words = book.split()

    return len(words)

# Returns a dict[str, int] which has every character and the amount each character appears
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

# Returns the amount value of a single character in a book
def sort_on(character: tuple[str,int]) -> int:
    count_value = character[1]
    return count_value

# Turns the dictionary of characters into a list of tuples and sorts them from biggest to lowest
def chars_dict_to_sorted_list(characters: dict[str,int]) -> list[tuple[str,int]]:
    character_list: list[tuple[str, int]] = []

    for character, value in characters.items():
        character_list.append((character, value))

    sorted_character_list = sorted(character_list, reverse=True, key=sort_on)
    return sorted_character_list
