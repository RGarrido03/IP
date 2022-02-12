def noAdjacentDuplicateCharacter(string):
    new_string = string[0]

    for character in string[1:]:
        if character != new_string[-1]:
            new_string += character
    
    return new_string
