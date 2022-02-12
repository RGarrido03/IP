# Exercise 5

# Ask for people's names.
nome_proprio = input("Qual o nome próprio? ")
nome_mae = input("Qual o nome da mãe? ")
nome_pai = input("Qual o nome do pai? ")

# Get the surname.
apelido_mae = nome_mae.split( )
apelido_pai = nome_pai.split( )

# Print the name.
print(f"Bestie, o teu nome é {nome_proprio.capitalize()} {apelido_mae[-1].capitalize()} {apelido_pai[-1].upper()}, period.")
