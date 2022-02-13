def listContacts(dic):
    print("{:>12s} : {:^22} : {}".format("Número", "Nome", "Morada"))
    for num in dic:
        print("{:>12s} : {:^22} : {}".format(num, dic.get(num)[0], dic.get(num)[1]))

def addContact(dic):
    name = input("What's the name? ")
    number = input("What's the number? ")
    dic[number] = name

def removeContact(dic):
    number = input("Which number do you want to remove? ")
    dic.pop(number)

def searchNumber(dic):
    number = str(input("Which number do you want to search? "))
    if dic.get(number) != None:
        print(dic.get(number))
    else:
        print(number)

def filterPartName(contacts, partName):
    partNameList = []
    for key, val in contacts.items():
        if partName in val.lower():
            partNameList.append((key, val))
    print(partNameList)


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ["Universidade de Aveiro", "Santiago, Aveiro"],
        "727392822": ["Cristiano Aveiro", "Madeira"],
        "387719992": ["Maria Matos", "Murtosa"],
        "887555987": ["Marta Maia", "Coimbra"],
        "876111333": ["Carlos Martins", "Porto"],
        "433162999": ["Ana Bacalhau", "Lisboa"]
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            addContact(contactos)
        elif op == "R":
            removeContact(contactos)
        elif op == "N":
            searchNumber(contactos)
        elif op == "P":
            partName = input("Which name do you wanna search? ")
            partName_lower = partName.lower()
            filterPartName(contactos, partName_lower)
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

