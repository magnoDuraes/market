from estoque import *
from funcionalidades import *
import os

#======Aqui eu defino Quanto de dinheiro o Usuário da pessoa Terá disponível.======
salario = input("Digite Quanto de saldo seu personagem terá: R$").strip() 
salario = saldo(float(salario))
os.system('cls')
#==================================================================================


while True: #Laço de repetição para acessar diferentes opções.
    print("Bem-vindo ao mercado dos crias!\n1 - Comprar\n2 - Sacar\n3 - Ver carrinho\n4 - Sair") #Apresentação de opções.
    op1 = input("Digite a opção desejada: ").strip() #Seleção da opção
    op1 = escolha(int(op1))




    # item = input("Digite o item desejado: ").strip() #Seleção do item
    # qnt = input("Digite a quantidade desejada: ").strip() #Número de itens à serem comprados
    # qnt = int(qnt) #Convertendo a quantidade dos itens em números para fazer cálculo
    # salario = comprar(item, qnt, salario) #Aqui eu chamo uma função importada do Estoque. e retorna o valor atualizado do saldo que é armazenado na variável disponível.