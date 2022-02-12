# Exercise 2 from aula05

# Show a table of the squares of the first four numbers
print(" {:2s}  {:2s}       {:2s}".format("n", "n²", "2ⁿ"))
for n in range(1,21):
    print("{:2d}  {:3d}  {:7d}".format(n, n**2, 2**n))
