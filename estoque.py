estoque = {
    'Banana' : 24.30,
    'Martelo' : 50.50,
    'Foice' : 50.50,
    'Celular' : 10.00
}

#
def estoque():
  produtos = ["Banana", "Martelo", "Foice", "Celular"] #crio uma LISTA com as PALAVRAS-CHAVE do dicionário.
  for i in range(len(produtos)): #Cria-se um loop do mesmo tamanho da lista devido ao len(produtos)
      produto = produtos[i] #Considerando o primeiro LOOP, a variavel produto se torna produto[0], ou seja produto = "Banana"
      valor = estoque[produto]#Aqui chamamos o diconário estoque que tem como índice a palavra-chave 'Banana', Passando o seu significado, que no caso é o seu próprio valor.
      print(f"{produto} - R${valor}")#Aqui temos a parte visual de toda essa lista.
      #o LOOP se repete até chegar no último índice da lista produtos.

NF = []

#STR é o nome do item
#INT é a quantidade
#FLOAT é o dinheiro
# dinheiro = 0.00

def saldo(valor):
    dinheiro = valor
    return dinheiro
    
def comprar(str, int, float):
    escolha = estoque[str]
    quantidade = int
    dinheiro = float
    escolha = escolha * quantidade
    if dinheiro < escolha:
        return print(f"Saldo Insuficiente.\nSeu saldo atual: {dinheiro}")
    else:
        x = dinheiro-escolha
        # print(f"{dinheiro} AAAAAAAAAAAAAAAAAAAAAAA")
        compra = f"{quantidade} x {str}"
        NF.append(compra)
        print(f"Compra Concluída\nVocê Comprou {compra}")
        print (NF)
        return saldo(x)