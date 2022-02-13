# A função main define uma lista de tuplos com informação sobre acções de diversas empresas transacionadas em bolsas de várias cidades. Cada tuplo contém os campos: empresa, cidade, preço-de-abertura, preço-de-fecho, volume.
# 
# O ficheiro stocks.txt contém informação de mais ações. Cada linha corresponde a uma ação, com os campos separados por TABs. como neste excerto:
#
# ERIC    Lisbon  9.1 9.58283128  428800
# TSLA    London  221.33  229.63  398520
# INTC    Tokyo   33.22001    34.28999    4509110
# Complete a função load para ler ficheiros com esse formato e devolver uma lista de tuplos com o mesmo formato (tipos) da variável stocks.

def load(fname):
   fileobj = open(fname, "r", encoding="UTF-8")
   lst = []
   
    for line in fileobj:
      line_sep = line.strip().split("\t")
      lst += [(line_sep[0], line_sep[1], float(line_sep[2]), float(line_sep[3]), int(line_sep[4]))]
   
   return lst

# O resto é introduzido pelo CodeCheck.
