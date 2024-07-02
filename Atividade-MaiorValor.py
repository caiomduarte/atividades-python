
import os

os.system("cls")

print("Atividade Maior e Menor Valor")

# 1 Passo - Entrada
valor01 = int(input("Digite o primeiro valor: "))
valor02 = int(input("Digite o segundo valor: "))

# 2 Passo - Processamento / Saída
if valor01 > valor02:
    print("O maior valor é: ", valor01, " e menor valor é: ", valor02)

elif valor02 > valor01:
     print("O maior valor é: ", valor02, " e menor valor é: ", valor01)

else: 
     print("Os Valores são Iguais")

input("Pressione <Enter> para continuar...")     