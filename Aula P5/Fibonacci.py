# Exercise 9 from aula05

def fibonacci(n):    
    if n == 0:              # F0 = 0
        return 0
    elif n == 1:            # F1 = 1
        return 1
    
    fn1 = 1                 # When F2, F(n-1) = F1 = 1
    fn2 = 0                 # When F2, F(n-2) = F0 = 0
    
    while ((n-1) != 0):
        f = fn1 + fn2       # Calculate Fibonacci sequence
        n -= 1
        fn2 = fn1           # Save the value for F(n-2)
        fn1 = f             # Save the value for F(n-1)

    return f

n = int(input("Please input the number: "))
print(fibonacci(n))