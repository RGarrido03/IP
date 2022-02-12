litros = float(input("Introduz o número de litros que pretendes abastecer: "))

if(litros <= 40):
    print(f"Pagarás {round(litros * 1.40, 2)}€.")

else:
    print(f"Pagarás {round(litros * 1.40 * 0.9, 2)}€.")
