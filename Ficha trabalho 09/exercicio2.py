# Passo 1: Criação do dicionário com as respetivas conspirações e o seu valor de importância numa escala de 0 a 10)

Conspiracoes = {
    
    "MK Ultra": 7,
    "Project Blue Book":10,
    "Reptilianos": 9,
    "New World Order": 10,
    "Roswell": 15,
}

print("As minhas Crenças avaliadas de 1 a 10")
print(Conspiracoes)

# Adicionar Nova Conspiração e o seu valor

Conspiracoes["Betelgeuse Supernova"] = 18




# Remover (temporariamente) uma crença upsss...conspiração

"""
del Conspiracoes["MK Ultra"]

"""

# a mais fixe de todas será...

crenca_mais_fixe = max(Conspiracoes, key=Conspiracoes.get)
crenca_value = Conspiracoes[crenca_mais_fixe]


print(f"A minha crença mais fixe e (É VISIVEL A OLHO NÚ) {crenca_mais_fixe} e nesta lista tem o incrivel valor de {crenca_value: .2f}")



print(Conspiracoes)

