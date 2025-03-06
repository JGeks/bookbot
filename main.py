import sys
from stats import num_of_words
from stats import character_count
from stats import chars_to_sorted_list

def get_book_text(book_location):

    with open(book_location) as f:
        return f.read()

def main():

    args = sys.argv
    if args[1] == None:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(args[1])
    num_words = num_of_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_count = character_count(book_text)

    sorted_chars = chars_to_sorted_list(char_count)
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

main()