matricula = input("Introduz a matrícula: ")

if(len(matricula) != 8):
    print("A matrícula é inválida.")
    print("Razão: Não possui oito caracteres.")

elif(matricula[2] != "-" or matricula[5] != "-"):
    print("A matrícula é inválida.")
    print("Razão: O terceiro e/ou o sexto caracteres não são se encontram no formato correto.")

elif((matricula[0:2].isdigit() == False) or (matricula[6:8].isdigit() == False)):
    print("A matrícula é inválida.")
    print("Razão: Os primeiros dois e/ou os dois últimos caracteres não são números.")

elif(matricula[3:5].isalpha() == False):
    print("A matrícula é inválida.")
    print("Razão: Os caracteres centrais não são letras.")

else:
    print("A matrícula é válida, congrats.")
