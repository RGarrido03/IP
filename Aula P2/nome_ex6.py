# Exercise 6

nome_completo = input("Qual é o teu nome? ")    # This line asks the user for the name.

# The next line splits the name so the print function can pick up the three words.
nome_dividido = nome_completo.split( )

# The next line prints the name in the new style, with a friendly message.
print(f"Bestie, o teu nome ordenado desta forma manhosa fica assim: {nome_dividido[-1]}, {nome_dividido[-3]} {nome_dividido[-2]}. 💅")
