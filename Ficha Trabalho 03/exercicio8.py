lado1 = int(input("Valor lado 1:\t"))
lado2 = int(input("Valor lado 2:\t"))
lado3 = int(input("Valor lado 3:\t"))

if lado1 == lado2 and lado1 == lado3:
    print("Triângulo equilátero.")  
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósceles.")
else:
    print("Triângulo escaleno.")