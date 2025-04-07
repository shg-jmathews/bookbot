from stats import get_num_words
from stats import get_num_chars

# new function called get_book_text. It takes a filepath as input and returns the contents of the file as a string.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# a main function that uses get_book_text with the relative path to your frankenstein.txt file to print the entire contents of the book to the console.
def main():
    filepath = "/home/jmathews/workspace/github.com/shg-jmathews/bookbot/books/frankenstein.txt"
    text = get_book_text(filepath)
    wrd_count = get_num_words(filepath)
    print (wrd_count)
    characters = get_num_chars(filepath)
    print (characters)


# call main
main()