class Estudiante: 
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

class Profesor:
    def __init__(self, nombre, edad, xp):
        self.nombre = nombre
        self.edad = edad
        self.xp = xp

class GrupoAsignatura:
    def __init__(self, nombre, horario, codigo, profesor):
        self.nombre = nombre
        self.horario = horario 
        self.codigo = codigo
        self.profesor = profesor 
        self.estudiante = []

    def Agregar_estudiante(self, estudiante):
        self.estudiante.append(estudiante)
        print("Estudiante agg exitosamente")

    def promedio(self):
        acomulador = 0 
        for estudiante in self.estudiante:
            acomulador += estudiante.nota
        
        promedio = acomulador/len(self.estudiante)
        return promedio
    
    def nomEst(self):
        for estudiantes in self.estudiante:
            print(estudiantes.nombre)

    
profesor = Profesor("Juan ESteban", 35, 5) 
poo = GrupoAsignatura("POO", "M-V 10-12", 62, profesor)
print(poo.profesor.nombre)

estudiante1 = Estudiante("Esteban Diaz", 18, 5)
estudiante2 = Estudiante("Esteban Diaz", 18, 3)
estudiante3 = Estudiante("Esteban Diaz", 18, 2)

poo.Agregar_estudiante(estudiante1)
poo.Agregar_estudiante(estudiante2)
poo.Agregar_estudiante(estudiante3)

print(poo.promedio())

poo.nomEst()
