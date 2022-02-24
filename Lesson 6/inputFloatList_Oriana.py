# Exercício 2a)

def inputFloatList():
    n = input("Introduza um número: ")
    lst = []
    
    while n != "":
        if float(n).is_integer():
            lst += [int(n)]
        else:
            lst += [float(n)]
        n = input("Introduza um número: ")
    
    return lst

# Exercício 2b)
lst = inputFloatList()
v = float(input("Introduza o valor de v: "))

def countLower(lst, v):
    lst2 = []
    count = 0

    for i in lst:
        if i < v:
            lst2 += [i]
            count += 1
    
    return lst2, count

lst2 = countLower(lst, v)[0]
count = countLower(lst, v)[1]

print(f"Lista dos números inferiores a {v}: {lst2}")
print("Valor do count:", count)