class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cuenta = []

    def agregar_cuenta(self, cuenta):
        self.cuenta.append(cuenta)

class Cuenta:
    def __init__(self, numero, oficina):
        self.numero = numero 
        self.oficina = oficina
        self.saldo = 0
    
    def depositar(self, cantidad):
        self.saldo += cantidad 
        
#crear una instancio(objeto) de la clase persona
persona1 = Persona("Juan", 35)
print("el nombre de la persona es", persona1.nombre)
print(f"la edad de la persona es {persona1.edad}")

#crear una instancio(objeto) de la clase Cuenta
cuenta1 = Cuenta("324234234", "Oficina 1")
print(f"el numero de la cuenta es {cuenta1.numero}")
print(f"la oficina de la cuenta es {cuenta1.oficina}")

#Asociar la cuenta a la persona
persona1.agregar_cuenta(cuenta1)
print(f"la cuenta de {persona1.nombre} es {persona1.cuenta[0].numero} y su oficina es {persona1.cuenta[0].oficina}")


cuenta2 = Cuenta("3242342", "oficina2")

persona1.agregar_cuenta(cuenta2)

persona1.cuenta[0].depositar(1000)

print(persona1.cuenta[0].saldo)

persona1.cuenta[0].depositar(500)
print(persona1.cuenta[0].saldo)
print(persona1.cuenta[1].saldo)