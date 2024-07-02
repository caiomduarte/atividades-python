import os

os.system("cls")

print("Atividade Calculando Desconto")

# 1 Passo -  Entrada
descricao = input("Digite a descrição do produto: ")
qtd = int(input("Digite a quantidade desejada: "))
preco = float(input("Digite o preço unitário do produto:"))

# 2 Passo - Processamento

# Calculando o total sem desconto
total_sem_desconto = preco * qtd

# Calculando o desconto caso a qtd <= 5
if qtd <= 5:
    desconto = total_sem_desconto * 0.02
    total_com_desconto = total_sem_desconto - desconto
    print("O total sem desconto: ", total_sem_desconto)
    print("O seu desconto foi: ", desconto) 
    print("Total com desconto: ", total_com_desconto)   

elif qtd >5 and qtd <=10:
    desconto = total_sem_desconto * 0.03
    total_com_desconto = total_sem_desconto - desconto
    print("O total sem desconto: ", total_sem_desconto)
    print("O seu desconto foi: ", desconto) 
    print("Total com desconto: ", total_com_desconto) 

else:
    desconto = total_sem_desconto * 0.05
    total_com_desconto = total_sem_desconto - desconto
    print("O total sem desconto: ", total_sem_desconto)
    print("O seu desconto foi: ", desconto) 
    print("Total com desconto: ", total_com_desconto)    

input("Pressione <Enter> para Continuar...")