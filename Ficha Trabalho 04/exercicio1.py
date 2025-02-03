#Dicionário com meses

meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

# Pedir um número ao utilizador
numero = int(input("Introduza um número de 1 a 12: "))

#Procurar no dicionário e mostrar o resultado

print(meses.get(numero, "Número Inválido! Introduza um número entre 1 e 12."))
