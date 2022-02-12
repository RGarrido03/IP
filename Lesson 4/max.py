def max2(a, b):
    if (a<b):
        return b
    elif (a==b):
        return "Valores iguais, como é que é suposto ver qual é o maior?"
    else:
        return a

def max3(a, b, c):
    max_1 = max2(a,b)
    max_2 = max2(max_1, c)
    return max_2

a = float(input("Qual é o valor de a? "))
b = float(input("Qual é o valor de b? "))
c = input("Existe c? Se sim, introduz o valor: ")

if(c == ""):
    print(max2(a,b))
else:
    c = float(c)
    print(max3(a,b,c))
