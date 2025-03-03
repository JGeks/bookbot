def num_of_words(book_text):
    num_words = len(book_text.split())

    return num_words

def get_book_text(book_location):

    with open(book_location) as f:
        return f.read()

def main():

    book_text = get_book_text("books/frankenstein.txt")
    num_words = num_of_words(book_text)
    print(f"{num_words} words found in the document")

main()