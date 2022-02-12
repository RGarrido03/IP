combustivel = float(input("Quantos litros de combustível foram gastos? "))
distancia = float(input("Qual foi a distância percorrida, em km? "))

consumo = 100*combustivel/distancia
print("O automóvel consome", round(consumo, 2), "l/100km.")
