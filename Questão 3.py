import os

os.system ("clear")

numero1= int (input("digite o primeiro numero:"))
numero2 = int (input("digite o segundo numero:"))
soma = numero1 + numero2
mult = numero1 * numero2

if numero1 == numero2:
    print (f"o resultado é : {soma}")
else:
    print (f"o resultado é : {mult}")