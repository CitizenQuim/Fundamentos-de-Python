#Armzenar as datas

datas = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

lista_datas = datas.split(",")

#IMprimir datas de 2022

datas_2022 = [data for data in lista_datas if "2022" in data]
print("Datas de 2022:", datas_2022)

#criar e ordenar a lista

dias = sorted([data[:2] for data in lista_datas])
print("Dias ordenados:", dias)