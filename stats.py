#  accepts the text from the book as a string, and returns the number of words in the string.
def get_num_words(path_to_file):
    try:
        with open(path_to_file, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"File '{path_to_file}' not found.")
        return 0

# takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
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
    
# takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
def sort_characters(path_to_file):
    try:
        with open(path_to_file, 'r') as file:
            content = file.read()
            lower = content.lower()
            counts = {}
            for char in lower:
                if char.isalpha() == True:
                    counts[char] = counts.get(char, 0) + 1
            sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
            return sorted_counts
    except FileNotFoundError:
        print(f"File '{path_to_file}' not found.")
        return 0


