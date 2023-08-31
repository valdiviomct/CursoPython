minha_lista = ["abacaxi", "melacia", "acabate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.89, True]
minha_lista4 = []

for item in minha_lista:
    print(item)
tamanho = len(minha_lista)
print(tamanho)
print(minha_lista)
print(minha_lista[1])

minha_lista.append("limao")
print(minha_lista)

if 3 in minha_lista2:
    print("3 esta na lista?")

del minha_lista[2:]
print(minha_lista)
minha_lista4.append(57)
print(minha_lista4)