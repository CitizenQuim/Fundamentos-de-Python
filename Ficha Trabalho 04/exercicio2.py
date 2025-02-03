#Dicionário com os estados civis

estados_civis = {
    "S": "Solteiro",
    "C": "Casado",
    "V": "Viúvo"
}

#Pedir uma letra ao utilizador

letra = input("Introduza uma letra (S, C ou V): ").strip().upper()

#Procurar no dicionário e mostrar o resultado

print(estados_civis.get(letra, "Letra inválida! Use apenas S, C ou V."))