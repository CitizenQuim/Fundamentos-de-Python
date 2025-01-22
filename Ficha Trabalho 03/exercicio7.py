ano = int(input("Digite o ano para notar se é bissexto: "))

if ano%400 == 0:
    print(f"{ano} é um ano bissexto.")
elif ano% 4 == 0 and ano %100!=0:
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é bissexto.")