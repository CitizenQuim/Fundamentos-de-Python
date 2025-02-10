#criação lista vazia para armazenar os elementos

lista = []

#1- Adicionar elemento no início

def adicionar_inicio(elemento):
    lista.insert(0, elemento) # Insere o elemento na posição 0 (início)
    print(f"{elemento} foi adicionado no início da lista.")
    
#2- Adicionar um elemento no fim

def adicionar_fim(elemento):
    lista.append(elemento) # Adiciona o elemento no final da lista
    print(f"{elemento} foi adicionado no fim da lista.")
    

#3- Remover um elemento específico

def remover_elemento(elemento):
    if elemento in lista:
        lista.remove(elemento) # Remove o elemento da lista
    else:
        print(f"{elemento} não está na lista.")
        
#4- Obter tamanho da lista

def tamanho_lista():
    print(f"A çista tem {len(lista)} elementos.") # len() retorna o tamanho da lista
    

#5- Imprimir os elementos da lista

def imprimir_lista():
    if lista:
        print("Elementos da lista:", lista)
    else:
        print("A lista está vazia.")
        
#6- Esvaziar a lista

def esvaziar_lista():
    lista.clear()  # Remove todos os elementos da lista
    print("A lista foi esvaziada."