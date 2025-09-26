class Empleado: 
    def __init__(self, nombre, documento, edad):
        self.__nombre = nombre
        self.__documento = documento 
        self.__edad = edad 

    def mostrar_datos(self):
        return {"Nombre": self.__nombre, "Documento": self.__documento, "Edad": self.__edad}
        
        """
        def set_nombre(self, nombre):
            self.__nombre = nombre 
        
        """

class Desarrollador(Empleado):
    def __init__(self, nombre, documento, edad, tipo):
        super().__init__(nombre, documento, edad)
        self.__tipo = tipo
    
    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Tipo"] = self.__tipo 
        return datos 

class Gerente(Empleado):
    def __init__(self, nombre, documento, edad, area):
        super().__init__(nombre, documento, edad)
        self.__area = area 
        self.__empleadosAcargo = []
    
    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Tipo"] = self.__area 
        return datos 
    
    def mostrar_personas_a_cargo(self):
        for persona in self.__empleadosAcargo:
            print(persona.mostrar_datos())
    
    def asignar_empleado(self, empleado):
        self.__empleadosAcargo.append(empleado)
    

empleado1 = Empleado("Juan", 34243, 23)

empleado2 = Desarrollador("Luis", 1111, 35, "Backend")


empleado3 = Gerente("Cargo", 43241, 35, "ADMIN")

empleado3.asignar_empleado(empleado2)
empleado3.asignar_empleado(empleado1)
empleado3.mostrar_personas_a_cargo()
print(empleado3.mostrar_datos())