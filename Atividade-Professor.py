import os

os.system("cls")

print("Atividade Salário do Professor")

# 1 Passo - Entrada
nivel_professor = int(input("Digite o nível do professor: "))
qtd_de_aulas = int(input("Digite a qtd de aulas por semana: "))

# 2 Passo - Processamento
if nivel_professor == 1:
    salario = qtd_de_aulas * 12

elif nivel_professor == 2:
    salario = qtd_de_aulas * 17

elif nivel_professor == 3:
    salario = qtd_de_aulas * 25
    
else:
    print("O nível digitado é inválido")

input("Pressione <ENTER> para continuar...")         