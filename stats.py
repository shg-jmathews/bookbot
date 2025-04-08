def get_num_words(path_to_file):
    """Returns the Number of Words in the file"""
    try:
        with open(path_to_file,"r", encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"File '{path_to_file}' not found.")
        return 0

def get_num_chars(path_to_file):
    """Returns the Number of Characters in the file."""
    try:
        with open(path_to_file,"r", encoding="utf-8") as file:
            content = file.read()
            lower = content.lower()
            counts = {}
            for char in lower:
                counts[char] = counts.get(char, 0) + 1
            return counts
    except FileNotFoundError:
        print(f"File '{path_to_file}' not found.")
        return 0
    
def sort_characters(path_to_file):
    """Returns the Number of Characters in the file, sorted by amount"""
    try:
        with open(path_to_file,"r", encoding="utf-8") as file:
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

def get_book_text(path_to_file):
    """Returns the contents of the file as a string"""
    with open(path_to_file,"r", encoding="utf-8") as f:
        return f.read()

