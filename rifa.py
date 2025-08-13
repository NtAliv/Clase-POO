import random 

class persona: 
    def __init__(self, nombre):
        self.nombre = nombre 
        self.numero = [random.randint(100,999) for _ in range(5)]
        
"""""
persona1 = persona("Juan esteban")
persona2 = persona("Isaac")
print(" los numeros para", persona1.nombre, "son", persona1.numero)
print(" los numeros para", persona2.nombre, "son", persona2.numero)
"""""


lista_personas = []
print("Bienvenido a la rifa")
while True:

    print("Ingrese la opcion deseada")
    print("1. registrarte")        
    print("2. datos")
    opcion = int(input())


    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        Nombre = persona(nombre)
        lista_personas.append(Nombre)
        print("cuenta creada exitosamente, sus numeros son", Nombre.numero)

        