import cmath
import math
import fractions

#Input coefficients
a = float(input("Qual é o valor de a? "))
b = float(input("Qual é o valor de b? "))
c = float(input("Qual é o valor de c? "))

#Calculate the roots
if(a == 0):
    if(b != 0):
        print(f"Bestie, a raiz do polinómio é {fractions.Fraction(-c / b).limit_denominator(1000)}.")
    
    if(b == 0):
        print("O polinómio não tem raízes, period.")

if(a != 0):
    delta = b**2 - 4 * a * c
    if(delta < 0):
        print("O polinómio não tem raízes reais, periodt.")
        raiz1 = (-b - cmath.sqrt(delta)) / (2 * a)
        raiz2 = ((-b + cmath.sqrt(delta)) / (2 * a))
        print(f"No entanto, as raízes complexas são {raiz1} e {raiz2}.")

    if(delta == 0):
        raiz1 = fractions.Fraction((-b) / (2 * a)).limit_denominator(1000)
        print(f"Bestie, a raiz do polinómio é {raiz1}.")

    if(delta > 0):
        raiz1 = fractions.Fraction((-b - math.sqrt(delta)) / (2 * a)).limit_denominator(1000)
        raiz2 = fractions.Fraction((-b + math.sqrt(delta)) / (2 * a)).limit_denominator(1000)
        print(f"Bestie, as raízes do polinómio são {raiz1} e {raiz2}.")
