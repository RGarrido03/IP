# Exercise 10 from aula05

def isPrime(n):
    for divisor in range(2, n):         # Define divisor (from 2 to the number itself, excluding).
        division = n/divisor
        
        if division.is_integer():       # If the divison result is an integer, return False (and break the definition).
            return False
        
        else:                           # Else, add 1 to the divisor and run the loop again.
            divisor += 1
    return True                         # If there's no number that matches the conditions above, then return True (thus n is a prime number).

for n in range(1,101):
    print(n, isPrime(n))