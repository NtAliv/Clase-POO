#crear lista
lista = ["1", "dos", "tres"]
longitud = len(lista)
print("la longitud es de ", longitud)
print(lista[2]) # se escoge el elemento
print(lista[-1]) # este es un tip para estar en el ultimo elemento de la lista de una manera mas rabida 
print(lista[1:]) # ignora la primer posicion 
print(lista[:2]) # ignora 3ser posicion
print(lista[:]) # toma todo

# Crear lista con ceros
lista_cero = [0] * 10 
print(lista_cero)

#lista con 10 numeros aleatorios 
import random 
Listaram = []

for i in range(0,10):  
    Listaram.append(random.randint(1,100))     
print(Listaram)

# forma corta
listram2 = [random.randint(1,1000) for _ in range(10)]
print("forma corta", listram2)

#remover 
lista_remover = [_ for _ in range (9)] # toma valores del 0 al 9
print (lista_remover)

# cambia el valor
lista_remover[2]  = 1
lista_remover[5] = 1
print(lista_remover)

"""
# elimina un elemento
lista_remover.remove(3)
print(lista_remover)

#Eliminar por posición 
del lista_remover[2]
print(lista_remover)
"""
# cambiar primero por ultima
lista_remover.reverse()
print(lista_remover)

# tomar elementos y eliminarlos
lista_remover = [elemento for elemento in lista_remover if elemento != 1]
print(lista_remover)

# ordenar lista
lista_remover.sort()
print(lista_remover)

# ordenarla de mayor a menor 
lista_remover.sort(reverse=True)
print(lista_remover)