# Exercise 6 from aula05

def leibnizPi4(n):
    i = 0
    summation = ((-1)**i)/(2*i + 1)
    
    while n > 1:
        i += 1
        summation += ((-1)**i)/(2*i + 1)
        n -= 1
    
    return summation

n = int(input("What's the value of n? "))
print(leibnizPi4(n))