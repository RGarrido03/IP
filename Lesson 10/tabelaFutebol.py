import matplotlib.pyplot as plt

tabela = [
    ("Rio Ave", 5, 3, 2, 17, 13),
    ("Tondela", 2, 3, 5, 12, 14),
    ("Moreirense", 5, 1, 4, 11, 14),
    ("Feirense", 2, 3, 5, 7, 11),
    ("Maritimo", 3, 1, 6, 6, 13),
    ("Benfica", 6, 2, 2, 19, 11),
    ("Setúbal", 4, 2, 4, 13, 11),
    ("Portimonense", 3, 2, 5, 12, 18),
    ("Guimaraes", 4, 3, 3, 15, 12),
    ("Boavista", 2, 3, 5, 8, 14),
    ("Nacional", 2, 3, 5, 10, 19),
    ("Belenenses", 2, 6, 2, 7, 8),
    ("Santa Clara", 4, 2, 4, 17, 16),
    ("FC Porto", 8, 0, 2, 21, 6),
    ("Braga", 6, 3, 1, 19, 10),
    ("Sporting", 7, 1, 2, 18, 10),
    ("Aves", 3, 1, 6, 11, 15),
    ("Chaves", 2, 1, 7, 9, 17) ]

# Cada registo na tabela classificativa contém:
#   Nome, Vitórias, Empates, Derrotas, Golos Marcados e Golos Sofridos
# Pode usar estes identificadores para os campos:
N,V,E,D,GM,GS = 0,1,2,3,4,5

def printTabela(tabela):
    print()
    print("{:19s} {:>3} {:>3} {:>3} {:>3} {:>3}:{:<3} {:>3}".format(
            "Equipa", "J", "V", "E", "D", "GM", "GS", "P"))
    for reg in tabela:
        nome,v,e,d,gm,gs = reg
        print(f"{nome:19s} {numJogos(reg):3d} {v:3d} {e:3d} {d:3d} {gm:3d} {gs:<3d} {pontos(reg):3d}")

# numJogos é uma função definida por uma expressão lambda que,
# dado um registo de uma equipa, devolve o número de jogos que a equipa jogou.
numJogos = lambda reg: reg[V]+reg[E]+reg[D]

# a)
# Complete a expressão lambda para definir uma função que,
# dado um registo de uma equipa, devolva o número de pontos da equipa.
# (Cada vitória vale 3 pontos, cada empate vale 1 ponto.)
pontos = lambda reg: reg[V]*3 + reg[E]

def main():
    # Teste:
    '''print(tabela[3][N], numJogos(tabela[3]))  # Feirense 10?

    print(tabela[-1][N], pontos(tabela[-1]))  # Chaves 7?'''


    # Mostra a tabela classificativa original, não ordenada:
    '''printTabela(tabela)'''

    # b)
    # Acrescente os argumentos adequados à função sorted para
    # obter uma tabela ordenada por ordem decrescente de pontos:
    '''tab = sorted(tabela, key=lambda reg: pontos(reg), reverse=True)
    printTabela(tab)'''

    # c)
    # Acrescente os argumentos adequados à função sorted para
    # obter uma tabela ordenada por ordem decrescente da diferença GM-GS:
    '''tab = sorted(tabela, key=lambda reg: reg[4]-reg[5], reverse=True)
    printTabela(tab)'''

    # d)
    # Acrescente os argumentos adequados à função sorted para
    # obter uma tabela ordenada por ordem decrescente de pontos e,
    # se iguais, por ordem da diferença GM-GS:
    tab = sorted(tabela, key=lambda reg: (pontos(reg), reg[4]-reg[5]), reverse=True)
    printTabela(tab)

    # Exercise 3 from aula10:
    teams = [x[0] for x in tab]
    points = [pontos(x) for x in tab]
    plt.figure(1)
    plt.barh(teams, points) # O barh() permite fazer o gráfico na horizontal.
    plt.xlabel("Pontos")
    plt.ylabel("Equipas")
    plt.show()

if __name__ == "__main__":
    main()

