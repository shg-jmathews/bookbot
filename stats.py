#  new function that accepts the text from the book as a string, and returns the number of words in the string.
def get_num_words(path_to_file):
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

# new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
def get_num_chars(path_to_file):
    try:
        with open(path_to_file, 'r') as file:
            content = file.read()
            lower = content.lower()
            counts = {}
            for char in lower:
                counts[char] = counts.get(char, 0) + 1
            return counts
    except FileNotFoundError:
        print(f"File '{path_to_file}' not found.")
        return 0