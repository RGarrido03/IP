cidade1 = input("Qual é o nome da primeira cidade? ").capitalize()
cidade2 = input("Qual é o nome da segunda cidade? ").capitalize()
cidade3 = input("Qual é o nome da terceira cidade? ").capitalize()
cidade4 = input("Qual é o nome da quarta cidade? ").capitalize()

if(cidade1 < cidade2):
    a = cidade1
else:
    a = cidade2

if(a < cidade3):
    b = a
else:
    b = cidade3

if(b < cidade4):
    print(f"A cidade que deverá vir em primeiro lugar é {b}, period.")
else:
    print(f"A cidade que deverá vir em primeiro lugar é {cidade4}, period.")
