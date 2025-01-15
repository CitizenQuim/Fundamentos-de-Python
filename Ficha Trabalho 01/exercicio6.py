
def converter_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

if __name__ == "__main__":
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))
    print(f"O total em segundos é {converter_para_segundos(horas, minutos, segundos)} segundos.")
    
    