from stats import get_num_words
from stats import get_num_chars
from stats import sort_characters

# new function called get_book_text. It takes a filepath as input and returns the contents of the file as a string.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# Message to Print
def formatted(path_to_file):
    wrd_count = get_num_words(path_to_file)
    sorted_characters = sort_characters(path_to_file)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wrd_count} total words")
    print("--------- Character Count -------")
    for key in sorted_characters:
        print(f"{key}: {sorted_characters[key]}")
    print("============= END ===============")
    return

# a main function that uses get_book_text with the relative path to your frankenstein.txt file to print the entire contents of the book to the console.
def main():
    filepath = "/home/jmathews/workspace/github.com/shg-jmathews/bookbot/books/frankenstein.txt"
    formatted(filepath)


# call main
main()