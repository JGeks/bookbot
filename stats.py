def num_of_words(book_text):
    num_words = len(book_text.split())

    return num_words

from collections import defaultdict

def character_count(book_text):
    char_count = defaultdict(int)

    for character in book_text.lower():
        char_count[character] += 1

    return char_count