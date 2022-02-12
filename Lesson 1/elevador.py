import math

#Quantos dias tem o ano
dias=float(input("Quantos dias tem o ano? "))

#1 andar
piso1 = 3
piso1_4vezes = piso1 * 4

#2 andar
piso2 = 6
piso2_4vezes = piso2 * 4

#3 andar
piso3 = 9
piso3_4vezes = piso3 * 4

#distância por ano
distancia_ano = (piso1_4vezes + piso2_4vezes + piso3_4vezes)*dias/1000 #km

#horas por ano
horas_ano = math.floor((piso1_4vezes + piso2_4vezes + piso3_4vezes)*dias/3600) #hora
minutos_ano = math.floor((piso1_4vezes + piso2_4vezes + piso3_4vezes)*dias/60 - horas_ano*60)

print("O elevador percorre", distancia_ano, "km por ano, num total de", horas_ano, "horas e", minutos_ano, "minutos.")
