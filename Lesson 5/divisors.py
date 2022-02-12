# Exercise 11 from aula05

n = int(input("Please input a positive integer: "))
assert n > 0                                # Check if the number is positive.

# Calculate all the divisors:
divisors_list = []                          # Create an empty list where the divisors of n will be stored.

for divisor in range(1,n):
    division = n/divisor
        
    if division.is_integer():
        divisors_list.append(divisor)       # Add the divisor to a list.
        
    else:
        divisor += 1                        # Add 1 to the divisor and run the loop again.

print(f"Divisors of {n}: {divisors_list}")



# Check if n is defective, perfect or excessive:
sum_of_divisors = sum(divisors_list)

if sum_of_divisors < n:
    print(f"{n} is a defective number ({sum_of_divisors} < {n}).")

elif sum_of_divisors == n:
    print(f"{n} is a perfect number ({sum_of_divisors} = {n}).")

else:
    print(f"{n} is an excessive number ({sum_of_divisors} > {n}).")
