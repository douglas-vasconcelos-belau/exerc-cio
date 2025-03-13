import os

os.system ("clear")

nota1=float (input("digite sua primeira nota:"))
nota2=float (input("digite sua segunda nota:"))
soma = (nota1 + nota2)
media = soma / 2

print (f"media: {media}")

if media < 4 :
    print ("reprovado")
elif media == 5:
    print("recuperaçao")
else:
    print ("parabens voce foi aprovado")