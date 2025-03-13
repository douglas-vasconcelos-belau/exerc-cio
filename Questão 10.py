import os

os.system ("clear")

tipo_combustivel = input("A = alcool / G = gasolina ; digite o tipo de combustivel: ").upper()
quantidade = float(input("digite a quantidade de combustivel> "))

preco_al = 3.79
preco_ga = 6.59

match tipo_combustivel:
    case "A":
        if quantidade <=25:
            desconto = preco_al * 0.2
        else:
            desconto = preco_al * 0.4
    case "G":
        if quantidade <=25:
            desconto = preco_ga * 0.3
        else:
            desconto = preco_ga * 0.5
