import math

#Ler valores dos catetos
cateto_a = float(input("Introduz a medida do cateto A: "))
cateto_b = float(input("Introduz a medida do cateto B: "))

#Determinar hipotenusa
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)

#Determinar o ângulo
angulo = math.atan(cateto_b / cateto_a)
angulo_graus = math.degrees(angulo)

#Imprimir
print(f"A hipotenusa mede {hipotenusa:0.2f} cm e o ângulo entre o lado A e a hipotenusa é de {angulo_graus:0.2f} graus.")