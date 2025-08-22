lista = []
for i in range(1, 11):
    if i % 2 == 0:
        lista.append(i)

print (lista)

lista2 = [i*i for i in range(1, 11) if i % 2 == 0]
print(lista2)

lista3 = [i**3 for i in range(1, 11) if i % 2 == 0]#potencia
print(lista3)