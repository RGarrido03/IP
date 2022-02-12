x1 = float(input("Qual é o primeiro número? "))
x2 = float(input("E o segundo número? "))
x3 = float(input("E o terceiro? "))

if(x1 >= x2):
    maximum = x1
else:
    maximum = x2

if(maximum >= x3):
    print(f"O maior número é {maximum}.")

else:
    print(f"O maior número é {x3}.")



# OUTRA FORMA
"""if(x1>x2 and x1>x3):
    print(f"O maior número é: {x1}.")

elif(x2>x1 and x2>x3):
    print(f"O maior número é {x2}.")

else:
    print(f"O maior número é {x3}.")"""
