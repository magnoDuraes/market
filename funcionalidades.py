from estoque import *
def funcionalidade1():
    print("-------- COMPRAS --------\n")
    print("teste")
    
    input("Digite o item que você procura: ")
def funcionalidade2():
    print("Você escolheu a opção 2\n")
    print (f"{estoque()}")
def funcionalidade3():
    print("Você escolheu a opção 3")
def funcionalidade4():
    print("Você escolheu a opção 4")
opcoes = {
    1: funcionalidade1,
    2: funcionalidade2,
    3: funcionalidade3,
    4: funcionalidade4
}
def escolha(x): #Recebo o número da funcionalidade indicada
    funcao = opcoes[x] #A variável "funcao" irá receber o conteúdo correspondente à X no dicionário "opcoes"
    funcao() #Exibe o conteúdo correspondente à X.