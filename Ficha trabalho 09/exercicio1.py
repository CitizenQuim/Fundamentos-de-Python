# Passo 1: Criação do dicionário com os pratos e respetivos preços

menu = {
    
    "entremeada": 7,
    "sardinha": 15,
    "Filetes": 8,
    "Prego": 7,
    "Hamburguer": 8
}

# Passo 2: Devover o preço do "prego"
# Os dicionários permitem aceder ao valor de uma chave específica utilizando menu["Prego"].

#vamos lá então aceder ao preço do "prego"

"""preco_prego = menu["Prego"]

print(f"O preço do Prego é {preco_prego} euros.") """

# Explicação:
#  menu["Prego"] devolve o valor associado à chave "Prego".
#  Guardamos esse valor na variável preco_prego e imprimimos o resultado.

# Passo 3: Print Todas as chaves do dicionário

# Podemos usar menu.keys() para obter todas as chaves do dicionário

"""print("Pratos disponíveis no Menu:")
print(menu.keys())"""

# Passo 4: Adicionar "Ovos Rotos" ao menu com o preço de 10 euros

menu["Ovos Rotos"] = 10

# Passo 5: Print de todo o dicionário (para ver alterações)

# Mostrar Dicionário Atualizado

print("Menu Atualizado:")
print(menu)