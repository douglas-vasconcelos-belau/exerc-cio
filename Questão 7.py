import os

os.system ("clear")

nome_p = (input("digite o nome do produto: "))
preco_p = (input("digite o preço do produto: "))
quantidade = (input("digite a quantidade de produtos: "))
preco_t =quantidade * preco_p

if quantidade <=5:
    desconto = 0.2
elif quantidade <= 10:
    desconto = 0.3   
else:
    desconto = 0.5

valorap = preco_t - desconto

print()
print (f"nome do produto:{nome_p}")
print (f"quantidade do produto:{quantidade}")
print (f"preço total:{preco_t}")
print (f"desconto:{desconto}")
print (f"total a pagar:{valorap}")