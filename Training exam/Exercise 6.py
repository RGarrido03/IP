# A função main define uma lista de tuplos com informação sobre acções de diversas empresas transacionadas em bolsas de várias cidades. Cada tuplo contém os campos: empresa, cidade, preço-de-abertura, preço-de-fecho, volume.
#
# Acrescente os argumentos adequados à função sorted para obter uma tabela ordenada alfabeticamente pelo nome da cidade e, para a mesma cidade, por ordem do nome da empresa.

stocks2 = sorted(stocks, key=lambda a:(a[1], a[0]))
