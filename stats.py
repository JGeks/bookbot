def num_of_words(book_text):
    num_words = len(book_text.split())

    return num_words

from collections import defaultdict

def character_count(book_text):
    char_count = defaultdict(int)

    for character in book_text.lower():
        char_count[character] += 1

    return char_count

def sort_on(char_count):
    return char_count["count"]

def chars_to_sorted_list(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    return char_list