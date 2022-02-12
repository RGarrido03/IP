selection=True
while selection: 
    print ("""
    0. Domingo
    1. Segunda-feira
    2. Terça-feira
    3. Quarta-feira
    4. Quinta-feira
    5. Sexta-feira
    6. Sábado
    """)

    selection=input("Escolhe o dia da semana (usa os números): ") 
    if selection =='0': 
      numero_ida = 0
      break
    elif selection == '1': 
      numero_ida = 1
      break
    elif selection == '2':
      numero_ida = 2
      break
    elif selection == '3': 
      numero_ida = 3
      break
    elif selection == '4': 
      numero_ida = 4
      break
    elif selection == '5': 
      numero_ida = 5
      break
    elif selection == '6': 
      numero_ida = 6
      break
    else: 
      print("Opção sem correspondência.")
      break


dias_de_ferias = int(input("Quantos dias de férias? "))

#calcular dia de chegada
dia_de_chegada = numero_ida + dias_de_ferias

#transformar em dia de semana (0 a 6)
numero_volta = dia_de_chegada%7

#imprimir o dia da semana
if(numero_volta == 0):
	print("Chegarás de férias a um domingo.")

if(numero_volta == 1):
	print("Chegarás de férias a uma segunda-feira.")

if(numero_volta == 2):
	print("Chegarás de férias a uma terça-feira.")

if(numero_volta == 3):
	print("Chegarás de férias a uma quarta-feira.")

if(numero_volta == 4):
	print("Chegarás de férias a uma quinta-feira.")

if(numero_volta == 5):
	print("Chegarás de férias a uma sexta-feira.")

if(numero_volta == 6):
	print("Chegarás de férias a um sábado.")
