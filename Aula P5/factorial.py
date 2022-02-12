# Exercise 4 from aula05

def factorial(n):
    assert isinstance(n, int)   # Check if n is an integer.
    assert n >= 0               # Check if n is positive or zero.

    fact = n

    if n == 0:
        fact = 1                # 0! is 1.

    else:    
        while (n > 1):
            n -= 1
            fact = fact * (n)

    return fact

n = int(input("What is the value of n, sis? "))

print(f"{n}! is {factorial(n)}.")