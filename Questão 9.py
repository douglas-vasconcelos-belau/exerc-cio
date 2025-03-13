import os

os.system ("clear")

valord = float(input("digite o valor desejado: "))
rendam = float(input("digite o valor da sua renda mensal: "))
quantidadep = float(input("digite a quantidade de parcelas: "))

valor_maximo_emprestimo = rendam * 10
valor_maximo_prestacoes = rendam * 0.30
valor_parcela = valord/ quantidadep

if valord <= valor_maximo_emprestimo and valor_parcela <= valor_maximo_prestacoes:
    print("autorizado")
else:
    print("negado")

print()
print (F" valor desejado:{valord}")
print (F" quantidade de parcelas:{quantidadep}")
print (F" valor por parcelarcel:{valor_parcela}")