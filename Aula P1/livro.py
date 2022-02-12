#Valores
pf = 20
pc = 24.95
imp = 23
spa = 0.20

#Fórmula geral
#pc = (pf + lucro)*(1 + (imp/100)) + spa

#Lucro
lucro = (pc - spa)/(1 + (imp/100)) - pf
lucro_500livros = 500*lucro

#Impostos
imposto = (pc - spa) - (pc - spa)/(1 + (imp/100))
imposto_500livros = 500*imposto

#taxas
taxa = imposto + spa
taxa_500livros = 500*taxa

print("O lucro da tiragem dos 500 exemplares é", round(lucro_500livros, 2), "€.")
print("Foram coletados", round(imposto_500livros, 2), "€ em impostos.")
print ("Foram reunidos", round(taxa_500livros, 2), "€ em taxas.")
