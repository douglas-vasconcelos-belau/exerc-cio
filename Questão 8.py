import os

os.system ("clear")

cor = str (input("digite a cor do produto: "))
verde = "verde"
azul = "azul"
amarelo = "amarelo"
vermelho = "vermelho"

match cor:
    case "verde" :
        print("o valor é: $10,00")
    case "azul":
        print ("o valor é: $20,00")
    case "amarelo":
        print ("o valor é: $30,00")
    case "vermelho":
        print ("o valor é: $40,00")
    case _:
        print ("cor invalida.")