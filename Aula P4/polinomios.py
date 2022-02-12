for x in [0, 1, 2]:
    print(f"p({x}) = {x**2 + 2 * x + 3}")

p1 = 6
p_p1 = p1**2 + 2 * p1 + 3
print(f"p(p(1)) = {p_p1}")

# Outra forma
print()
print("Outra forma:")
def p(x):
    p_x = x**2 + 2 * x + 3
    return p_x

print(p(1), p(2), p(3), p(p(1)))