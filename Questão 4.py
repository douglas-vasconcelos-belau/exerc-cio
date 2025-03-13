import os

os.system ("clear")


quantidade_morango = int (input("digite a quantidade de maças: "))
quantidade_maça = int (input("a qualtidade de mças:"))

if quantidade_maça <= 5 :
    preço_da_maça = 1.80
else:
    preço_da_maça = 1.50

if quantidade_morango <=5:
    peço_do_morango = 2.50
else:
    preco_do_morango =2.20

precototalm = preço_da_maça * quantidade_maça
precototalmo = preco_do_morango* quantidade_morango

preco_total = precototalm + precototalmo
quantidade_total = quantidade_maça = quantidade_morango

if quantidade_total >= 10 or preco_total >15:
    desconto = preco_total * 0.10
else:
    desconto = 0

valorpa = preco_total - (preco_total * desconto) 

print (f"preço total de maças: {precototalm}")
print (f"preço total demorango: {precototalmo}")
print (f"quantidade de maças: {quantidade_maça}")
print (f"quantidade de morangos {quantidade_morango}")
print (f"preço total: {preco_total}")
print (f"desconto aplicado: {desconto}")
print (f"preço a pagar: {valorpa}")