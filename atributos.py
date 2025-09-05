"""
class Persona:
    def __init__(self, nombre, cedula, ti):
        self.nombre = nombre
        self.__cedula = cedula 
        self.__ti = ti 

    def obtener_documento(self):
        if self.__cedula is not None: 
            return self.__cedula
        else: 
            return self.__ti

persona1 = Persona("juan", 2222, None)
persona2 = Persona("Carlos", 3333, None)
niño1 = Persona("Luna", None, 43242)

print("El nombre de la primera persona es", persona1.nombre)
print("El nombre de la segunda persona es", persona2.nombre)

print("Documento de ", persona1.nombre, "es ", persona1.obtener_documento())
print("Documento de ", niño1.nombre, "es",  niño1.obtener_documento()) 
"""

#Espacio casa 
class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False

    def encender(self):
        self.estado =  True 
        print(self.nombre, "encendido")
        """ if self.estado is true: 
                self.estado = false
                print("apagado")
            else: 
                self.estado = True
                print("encendido")"""
    def apagar(self):
        self.estado = False
        print(self.nombre, "apagado")

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__dispositivos = []
    
    def agregard(self, dispositivo):
        self.__dispositivos.append(dispositivo)
        print("dispositivo agg")

    def mostrard(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.nombre)

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.__espacio = []

    def agregare(self, nombre):
        self.__espacio.append(Espacio(nombre))
        print("espacio agg")

    def mostrare(self):
        for espacio in self.__espacio:
            print(espacio.nombre)  
        
    def buscare(self, nombre):
        for espacio in self.__espacio:
            if espacio.nombre == nombre:
                return espacio
        return None
        

mi_casa = Casa("calle 123")
mi_casa.agregare("cocina")
mi_casa.agregare("habitacion")
mi_casa.agregare("baño")
television = Dispositivo("TV")
mi_casa.buscare("habitacion").agregard(television)
mi_casa.buscare("habitacion").mostrard()