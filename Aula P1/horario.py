import math

#converter horas em minutos
minutos_saida = 6*60+52

#velocidades
velocidade_passo = 10 #min/km
velocidade_corrida = 6 #min/km

#passo de 1km
tempo_passo_1 = velocidade_passo * 1
minutos_passo_1 = minutos_saida + tempo_passo_1

#treino de 3km
tempo_corrida = velocidade_corrida * 3
minutos_corrida = minutos_passo_1 + tempo_corrida

#passo de 4km
tempo_passo_2 = velocidade_passo * 4
minutos_passo_2 = minutos_corrida + tempo_passo_2

#converter minutos em horas
hora_final = math.floor(minutos_passo_2/60)
minutos_final = (minutos_passo_2%60)

print("Chegaria a casa às", hora_final, "horas e", minutos_final, "minutos.")
