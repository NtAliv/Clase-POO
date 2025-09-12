"""class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

    def orinar(self):
        print(f"{self.nombre} está orinando ")

class Perro(Animal):
    def __init__(self, nombre, color_pelota):
        super().__init__(nombre)
        self.color_pelota = color_pelota
    def hacer_sonido(self):
        print(f"{self.nombre} hace guau guau")
    def pasear(self):
        print(f"{self.nombre} está paseando")


class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace miau miau")

animal1 = Perro("Mia", "Rojo")
animal1.hacer_sonido()
animal1.pasear()
animal1.orinar()

animal2 = Gato("vela")
animal2.hacer_sonido()
animal2.orinar()

print(isinstance(animal2, Perro))#valida si el objeto es un objeto de la clase perro F/V
print(isinstance(animal1, Perro))#valida si el objeto es un objeto de la clase Animal F/V
print(issubclass(Perro, Gato)) #Valida si el primero es sub clase del segundo F/V
print(issubclass(Gato, Animal))
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
    
    def años(self):
        print(f"{self.nombre} tiene {self.edad} años ")

class Estudiante(Persona):
    def __init__(self, nombre, edad, estudia):
        super().__init__(nombre, edad)
        self.estudia = estudia 

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.estudia}")

persona1 = Estudiante("esteban", 18, "Ing Sistemas")
persona1.estudiar()
persona1.años()
persona2 = Persona("luis", 32)
persona2.años()