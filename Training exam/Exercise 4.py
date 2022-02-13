# A função main define uma lista de tuplos com informação sobre acções de diversas empresas transacionadas em bolsas de várias cidades. Cada tuplo contém os campos: empresa, cidade, preço-de-abertura, preço-de-fecho, volume.
#
# Defina uma função printStocks(stocks) para mostrar a tabela com as colunas formatadas como no exemplo abaixo. Inclua uma coluna com a valorização da ação em percentagem. Por exemplo, se o preço de abertura for 10.00 e o de fecho for 9.50, a valorização será de -5\%. Note que esta função é chamada pela função main e não deve modificar a lista passada no argumento.
#
#    INTC      London              34.25     34.45   1792860    0.6%
#    TSLA      London             221.33    229.63    398520    3.8%
#    EA        Paris               72.63     68.98   1189510   -5.0%
#    INTC      Tokyo               33.22     34.29   4509110    3.2%
#    TSLA      Paris              217.35    217.75    252500    0.2%
#    ATML      Frankfurt            8.23      8.36    810440    1.6%

def printStocks(stocks):
   for a in stocks:
      valorization = (a[3] - a[2])/a[2] * 100
      print(f"{a[0]:4s}      {a[1]:19s}{str(round(a[2],2)):>6s}    {str(round(a[3],2)):>6s} 
