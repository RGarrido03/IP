import sys

def countLetters(filename):
    file = open(filename, 'r', encoding='UTF-8')        # Open the file.
    letters = {}                                        # Initialize the dictionary.

    for line in file:
        line_lower = line.strip().lower()               # Generate a new line without "\n" and in lowercase letters.

        for character in line_lower:
            if character.isalpha():                     # If the caracter is a letter...
                if character not in letters:            # If the character is not in the dictionary...
                    letters[character] = 1              # Create a new key. 1 is the default value.
                else:
                    letters[character] += 1             # Add 1 to the value.
    
    file.close()                                        # Close the file.
    letters_sorted = sorted(letters.items())            # Sort the dictionary. NOTE: This generates a list!
    letters_sorted_dict = dict(letters_sorted)          # Turn the previous line's list into a dictionary.

    return letters_sorted_dict                          # Return.


def main():
    filename = sys.argv[1]                              # Get the filename through the argument (i.e. "./countLetters.py lusiadas.txt")
    
    for key, value in countLetters(filename).items():
        print(key, value)                               # Print each item in a new line

main()