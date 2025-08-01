class perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self):
        print(f'{self.nombre} esta ladrando')

class persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    

#Vamos a instanciar un objeto desde la clase perro
Dog = perro("doggy", "golden")
print(Dog.nombre)
print(Dog.raza)

Perra = perro("lulu", "criollo")
print(Perra.nombre)
print(Perra.raza)



print("ingrese datos")
nombre = input("ingrese nombre: ")
raza = input("ingrese raza: ")

Perro = perro(nombre, raza)
print("los nombres y raza son")
print(Perro.nombre)
print(Perro.raza)

print("ahora van a ladrar")
Dog.ladrar()


