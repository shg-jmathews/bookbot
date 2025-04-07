# new function called get_book_text. It takes a filepath as input and returns the contents of the file as a string.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

#  new function that accepts the text from the book as a string, and returns the number of words in the string.
def word_count(path_to_file):
    try:
        with open(path_to_file, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
    except FileNotFoundError:
        print(f"File '{path_to_file}' not found.")
        return 0
    
    total_words = f"{word_count} words found in the document"
    return total_words


# a main function that uses get_book_text with the relative path to your frankenstein.txt file to print the entire contents of the book to the console.
def main():
    filepath = "/home/jmathews/workspace/github.com/shg-jmathews/bookbot/books/frankenstein.txt"
    text = get_book_text(filepath)
    wrd_count = word_count(filepath)
    print (wrd_count)


# call main
main()