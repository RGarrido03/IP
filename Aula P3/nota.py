# Obter valores da componente teórico-prática
atp1 = float(input("Qual a classificação do exame teórico-prático 1? "))
atp2 = float(input("Qual a classificação do exame teórico-prático 2? "))

# Obter valores da componente prática
ap1 = float(input("Qual a classificação do exame prático 1? "))
ap2 = float(input("Qual a classificação do exame prático 2? "))

# Calcular componentes
tp = (atp1 + atp2)/2
p = (ap1 + ap2)/2

# Verificar se alguma componente é inferior à nota mínima
if (tp < 7) or (p < 7):
    print("A nota final corresponde ao código 66.")
    exit()

# Calcular a nota final
nota_final = 0.4 * tp + 0.6 * p

# Caso a nota final seja negativa, pedir notas de recurso e calcular a nova nota final
if nota_final < 10:
    print("A nota final é negativa. Insere as notas de recurso.")
    atpr = float(input("Componente teórico-prática: "))
    apr = float(input("Componente prática: "))
    nota_final = (atpr + apr)/2

# Dar output da nota final.
if str(nota_final)[3] == "5":
    nota_final = nota_final + 0.1
    print(f"A nota final é {nota_final:.0f} valores.")
else:
    print(f"A nota final é {nota_final:.0f} valores.")