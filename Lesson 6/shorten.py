def shorten (string):
    count = 0
    new_string = ""

    for character in string:
        if character.isupper():
            new_string += character
    
    return new_string
