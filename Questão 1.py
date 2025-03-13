import os

os.system ("clear")

numero1= int (input("digite o primeiro numero:"))
numero2 = int (input("digite o segundo numero:"))
numero3 = int (input("digite o terceiro numero:"))
soma = numero1 + numero2

if soma > numero3:
    print (f"o numero {soma} é maior que {numero3}")
else:
    print (f"o numero {soma} é menor que {numero3}")
