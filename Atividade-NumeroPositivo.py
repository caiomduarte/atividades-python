import os

os.system("cls")

print("Atividade - Número Positivo ou Negativo")

# 1 Passo - Entrada
numero = int(input("Digite um número: "))

# 2 Passo - Processamento / Saída
if numero > 0:
    print("O Número digitado é Positivo")

elif numero <= 0:
    print("O Número é negativo")

else:
    print("O número é ZERO")

input("Pressione <ENTER> para continuar...-1")