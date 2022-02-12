#Ler a matrícula
matricula = input("Intorduz a matrícula no formato XX-XX-XX: ")

#Separar a matrícula
matricula_separada = matricula.split("-")

#Imprimir
print(matricula_separada[0].isnumeric(), matricula_separada[1].isalpha(), matricula_separada[2].isnumeric())
