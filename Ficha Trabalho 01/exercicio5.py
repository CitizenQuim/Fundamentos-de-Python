a = int(input("Introduza o primeiro cateto do triângulo retângulo\n->"))

b = int(input("Introduza o segundo cateto do triângulo retângulo\n->"))

c = (a**2 + b**2)**0.5 

print("O valor da hipotenusa do triângulo retângulo com catetos {} e {} é igual a: {:.2f}".format(a, b, c))





# Solicitando os valores dos catetos

import math

cateto_a = float(input("Digite o valor do cateto A: "))
cateto_b = float(input("Digite o valor do cateto B: "))

# Calculando a hipotenusa
hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)


# Mostrando o resultado
print("O valor da hipotenusa é: ", hipotenusa)  