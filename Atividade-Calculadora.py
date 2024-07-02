import os

os.system("cls")

print("Atividade Calculadora Simples")

# 1 Passo - Entrada
v1 = float(input("Digite o primeiro número: "))
v2 = float(input("Digite o segundo número: "))

print("Escolha a operação desejada")
operacao = int(input(" 1 - Somar, \n 2 - Subtração, \n 3 - Divisão, \n 4 - Multiplicação \n "))

# 2 Passo - Processamento
if operacao == 1:
    resultado = v1 + v2
    print("O resultado é da SOMA: ", resultado)

elif operacao == 2:
    resultado = v1 - v2

    print("O resultado é da SubTração: ", resultado)

elif operacao == 3:
    resultado = v1 / v2
    print("O resultado é da Divisão: ", resultado)

elif operacao == 4:
    resultado = v1 * v2
    print("O resultado é da Multiplicação: ", resultado)
else:
    print("Operação Inválida")

input("Pressione <Enter> para continuar...")