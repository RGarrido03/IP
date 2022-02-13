# PARTE 1
# Qual o valor investido na totalidade dos produtos em stock?
def stockValue(s):
   count = 0
   for value in s.values():    # Escolhi values uma vez que não interessa o nome do produto (aka as keys do dicionário).
      count += (value["quantity"] * value["price"])
   return count



# PARTE 2
# Atualizar as quantidades existentes no supermercado após a venda dos produtos que o cliente comprou.
def purchase(shopList, S):
   for item in shopList:
      if item[0] in S:    # Caso o item da shop list exista no supermercado:
         S[item[0]]["quantity"] -= item[1]
         if S[item[0]]["quantity"] < 0:    # Caso a quantidade, após a venda, seja menor do que 0:
            S[item[0]]["quantity"] = 0
