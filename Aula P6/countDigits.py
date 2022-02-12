def countDigits(string):
    count = 0

    for character in string:
        if character.isdigit():
            count += 1
    
    return count
