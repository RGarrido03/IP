def isPalindrome(word):
    length = len(word)
    divisor = int(length/2)

    if length % 2 == 0:
        if word[:divisor] == word[:(divisor - 1):-1]:
            return True
        else:
            return False
    
    else:
        if word[:divisor] == word[:divisor:-1]:
            return True
        else:
            return False
