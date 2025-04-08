import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_characters
from stats import get_book_text

def formatted(path_to_file):
    """Message to Print"""
    wrd_count = get_num_words(path_to_file)
    sorted_characters = sort_characters(path_to_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {wrd_count} total words")
    print("--------- Character Count -------")
    for key in sorted_characters:
        print(f"{key}: {sorted_characters[key]}")
    print("============= END ===============")
    return

def main():
    """This is Main Function"""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        arguments = sys.argv[1:]
        filepath = ' '.join(arguments)
        formatted(filepath)

if __name__ == "__main__":
    """Call Main"""
    main()
