from stats import num_of_words
from stats import character_count

def get_book_text(book_location):

    with open(book_location) as f:
        return f.read()

def main():

    book_text = get_book_text("books/frankenstein.txt")
    num_words = num_of_words(book_text)
    print(f"{num_words} words found in the document")

    char_count = character_count(book_text)
    print(char_count)

main()