def get_text(path):
    """Returns a string representation of file contents

    Parameters:
        path: path to the file being parsed, string, required

    Returns:
        String representation of the given file's contents
    """
    with open(path) as f:
        return f.read()

def get_word_count(given_string):
    """Returns the word count of a string

    Parameters:
        given_string: string, required

    Returns:
        Integer representing the number of words in a given string
    """
    # Split the string into list of words and remove whitespace
    words = given_string.split()
    return len(words)

def get_character_analysis(book):
    """Returns a dictionary containing unique characters and the number
    of times they appear in a given string.

    Parameters:
        book: string to be analyzed, string, required

    Returns:
        Dictionary with only unique characters and how many times the 
        character appeared in the string
        Example:
            {'p': 500, '*': 2, ...}
    """
    character_dict = {}
    # Change all characters to be lowercase so that duplicates do not occur
    book_lowercase = book.lower()

    # Look at each character in the string
    for character in book_lowercase:
        # Check if the character is already in the dictionary
        # If not, add the character to the dictionary with an initial value of 1
        # If yes, increment the character count by 1
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    
    return character_dict

def get_clean_analysis(character_dict):
    """Returns a list of character dictionaries ordered in decreasing
    order by number of time the character was found. 

    Parameters:
        character_dict: Dictionary containing characters with integer counts as values, dictionary, required

    Returns:
        Descending ordered list of character dictionaries based on the number
        of times the character was seen in a string.
    """
    clean_analysis = []

    # Add all characters to the clean_analysis array with a specific structure
    for character_object in character_dict:
        clean_analysis.append({"character": character_object, "num": character_dict[character_object]})

    # A function that takes a dictionary and returns the value of the "num" key
    # This is how the `.sort()` method knows how to sort the list of dictionaries
    def sort_on(dict):
        return dict['num']
    
    # Order the list in descending order
    clean_analysis.sort(reverse=True, key=sort_on)

    return clean_analysis

def main():
    book_path = "books/frankenstein.txt"
    book = get_text(book_path)

    print("--- Begin report of books/frankenstein.txt ---")
    word_num = get_word_count(book)
    print(str(word_num) + " words found in the document")
    char_analysis = get_character_analysis(book)
    ordered_analysis = get_clean_analysis(char_analysis)
    
    for character in ordered_analysis:
        # Only include non-alpha characters in the report
        if not character['character'].isalpha():
            continue
        print(f"The '{character['character']}' character was found {character['num']} times")

    print("--- End report ---")

main()
