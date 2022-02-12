#Pedir velocidades
v1 = float(input("Qual foi a velocidade de ida, v1? "))
v2 = float(input("Qual foi a velocidade de volta, v2? "))

vm = (2 * v1 * v2)/(v1 + v2)	# Cálculo da velocidade média
print("A velocidade média dos dois percursos foi", round(vm, 2), "km/h.")
