def evenThenOdd(string):
    new_string = ""
    
    for index in range(0, len(string), 2):
        new_string += string[index]
    
    for index in range(1, len(string), 2):
        new_string += string[index]
    
    return new_string
