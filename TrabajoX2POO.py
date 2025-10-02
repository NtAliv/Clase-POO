class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre 
        self.__correo = correo 

    def getcorreo(self):
        return self.__correo
    
    def presentarse(self):
        print(f"hola, mi nombre es {self.nombre} y mi correo es {self.getcorreo()}")
    
    def mostrar_datos(self):
        return {"Nombre": self.nombre, "Correo": self.__correo}

class Empleado(Persona): 
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo)
        self.salario = salario 
        
    def calcular_bono(self):
        bono = self.salario * 0.10
        return bono 

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Salario"] = self.salario 
        return datos

class Desarrollador(Empleado):
    def __init__(self, nombre, correo, salario, lenguajePrincipal):
        super().__init__(nombre, correo, salario)
        self.lenguajePrincipal = lenguajePrincipal
        self.tareas_asignadas = 0   

    def calcular_bono(self):  
        if self.tareas_asignadas > 5:
            bono = self.salario * 0.10 + self.salario * 0.01
        else: 
            bono = self.salario * 0.10
        return bono
    
    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Lenguaje Principal"] = self.lenguajePrincipal
        datos["Tareas asignadas"] = self.tareas_asignadas   
        return datos


class Analista(Empleado):
    def __init__(self, nombre, correo, salario, seniority):
        super().__init__(nombre, correo, salario)
        self.seniority = seniority

    def calcular_bono(self):
        if self.seniority == "Senior":
            bono = self.salario * 0.03
        else:
            bono = 0
        return bono
    
    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Seniority"] = self.seniority
        return datos

class Gerente(Empleado):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo, salario)
        self.__empleadosAcargo = []
    
    def getEmpleadosAcargo(self):
        return self.__empleadosAcargo
    
    def mostrar_personas_a_cargo(self):
        for persona in self.__empleadosAcargo:
            print(persona.mostrar_datos())
    
    def asignar_empleado(self, empleado):
        if empleado == self:
            print("No puedes asignarte a ti mismo")
            return
        elif empleado not in self.__empleadosAcargo:
            self.__empleadosAcargo.append(empleado)
        else:
            print("El empleado ya está a cargo del gerente")
    
    def remover_empleado(self, empleado):
        if empleado in self.__empleadosAcargo:
            self.__empleadosAcargo.remove(empleado)
        else:
            print("El empleado no está a cargo del gerente")
    
    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Empleados a cargo"] = len(self.__empleadosAcargo)
        return datos

class Tarea: 
    def __init__(self, id, descripcion, horasEstimadas, asignadoA=None):
        if horasEstimadas <= 0:
            raise ValueError("Las horas estimadas deben ser un valor positivo")
        self.id = id 
        self.descripcion = descripcion 
        self.horasEstimadas = horasEstimadas
        self.asignadoA = asignadoA

class Proyecto:
    def __init__(self, nombre, presupuesto): 
        self.nombre = nombre 
        self.presupuesto = presupuesto 
        self.tareas = []
    
    def agregar_tarea(self, id, descripcion, horasEstimadas, asignadoA=None):
        tarea = Tarea(id, descripcion, horasEstimadas, asignadoA)
        self.tareas.append(tarea)

    def agregar_empleado_a_tarea(self, empleado, tareaID):
        for tarea in self.tareas:
            if tarea.id == tareaID:
                tarea.asignadoA = empleado
                if isinstance(empleado, Desarrollador):
                    empleado.tareas_asignadas += 1
                return
        print("Tarea no encontrada")
    
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.proyectos = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def crear_proyecto(self, nombre, presupuesto):
        proyecto = Proyecto(nombre, presupuesto)
        self.proyectos.append(proyecto)
        return proyecto
    
    def mostrar_proyectos(self):
        for proyecto in self.proyectos:
            print(f"Proyecto: {proyecto.nombre}, Presupuesto: ${proyecto.presupuesto}, tareas: {len(proyecto.tareas)}")
            print("Tareas:")
            for tarea in proyecto.tareas:
                print(f"  ID: {tarea.id}, Descripcion: {tarea.descripcion}, Horas Estimadas: {tarea.horasEstimadas}, Asignado a: {tarea.asignadoA}")



empresa = Empresa("Proyectos POO")
print("Bienvenido a la empresa", empresa.nombre)

while True:

    print("\nSeleccione la opcion deseada")
    print("1. Agregar empleado")
    print("2. Crear proyecto y tareas")
    print("3. Agregar empleados a tarea")
    print("4. Calcular bono de un empleado") 
    print("5. Mostrar empleados de un gerente") 
    print("6. agregar o remover empleados a un gerente")    
    print("0. Salir\n")

    opcion = int(input())

    if opcion == 1: 
        print("que tipo de empleado deseas agregar?")
        print("1. Desarrollador")
        print("2. Analista")
        print("3. Gerente")
        print("4. empleado base")
        tipoEmpleado = int(input())
        nombre = input("Ingrese el nombre del empleado: ")
        correo = input("Ingrese el correo del empleado: ")
        salario = float(input("Ingrese el salario del empleado: "))

        if tipoEmpleado == 1:
            Lprincipal = input("Ingrese el lenguaje principal del desarrollador: ")
            empleado = Desarrollador(nombre, correo, salario, Lprincipal)
            empresa.agregar_empleado(empleado)
        elif tipoEmpleado == 2:
            seniority = input("Ingrese el nivel de seniority (Junior, Semi-Senior, Senior): ")
            empleado = Analista(nombre, correo, salario, seniority)
            empresa.agregar_empleado(empleado)
        elif tipoEmpleado == 3:
            empleado = Gerente(nombre, correo, salario)     
            empresa.agregar_empleado(empleado)
        elif tipoEmpleado == 4:
            empleado = Empleado(nombre, correo, salario)
            empresa.agregar_empleado(empleado)
    
    elif opcion == 2:
        nombreP = input("Ingrese el nombre del proyecto: ")
        presupuesto = float(input("Ingrese el presupuesto del proyecto: "))
        proyecto = empresa.crear_proyecto(nombreP, presupuesto)
        tareaAgregar = int(input("Cuantas tareas deseas agregar al proyecto? "))
        for i in range(tareaAgregar):
            idTarea = int(input("Ingrese el ID de la tarea: "))
            descripcion = input("Ingrese la descripcion de la tarea: ")
            horasEstimadas = int(input("Ingrese las horas estimadas para la tarea: "))
            proyecto.agregar_tarea(idTarea, descripcion, horasEstimadas, None)
   
    elif opcion == 3:
        print("Proyectos disponibles:")
        for i, proyecto in enumerate(empresa.proyectos):
            print(f"{i+1}. {proyecto.nombre}")

        numProyecto = int(input("Seleccione el número del proyecto: ")) - 1

        if 0 <= numProyecto < len(empresa.proyectos):
            proyectoSeleccionado = empresa.proyectos[numProyecto]

            print("Tareas del proyecto:")
            for tarea in proyectoSeleccionado.tareas:
                if tarea.asignadoA:
                    asignado = tarea.asignadoA.nombre
                else:
                    asignado = "Nadie"
                print(f"  ID: {tarea.id}, Descripción: {tarea.descripcion}, Asignado a: {asignado}")

            tareaID = int(input("Ingrese el ID de la tarea a la que desea asignar un empleado: "))

            print("Empleados disponibles:")
            for i, empleado in enumerate(empresa.empleados):
                print(f"{i+1}. {empleado.mostrar_datos()}")

            escoger = int(input("Seleccione el número del empleado que desea asignar a la tarea: ")) - 1

            if 0 <= escoger < len(empresa.empleados):
                empleadoSeleccionado = empresa.empleados[escoger]
                proyectoSeleccionado.agregar_empleado_a_tarea(empleadoSeleccionado, tareaID)
                print(f"Empleado {empleadoSeleccionado.nombre} asignado a la tarea {tareaID} en el proyecto {proyectoSeleccionado.nombre}")
            else:
                print("Empleado inválido")
        else:
            print("Proyecto inválido")
        
    elif opcion == 4:
        print("Todos los empleados:")
        for i, empleado in enumerate(empresa.empleados):
            print(f"{i+1}. {empleado.mostrar_datos()}")
        
        escoger = int(input("Seleccione el número del empleado para calcular su bono: ")) - 1

        if 0 <= escoger < len(empresa.empleados):
            EmpleadoSeleccionado = empresa.empleados[escoger]
            salariototal = EmpleadoSeleccionado.salario + EmpleadoSeleccionado.calcular_bono()
            print(f"El bono de {EmpleadoSeleccionado.nombre} es: ${EmpleadoSeleccionado.calcular_bono()} y su salario era de ${EmpleadoSeleccionado.salario}. Salario total con bono: ${salariototal}")
        

    elif opcion == 5:
        print("Gerentes disponibles:")
        gerentes = [Ngerentes for Ngerentes in empresa.empleados if isinstance(Ngerentes, Gerente)]
        for i, gerente in enumerate(gerentes):
            print(f"{i+1}. {gerente.mostrar_datos()}")

        escoger = int(input("Seleccione el número del gerente para mostrar sus empleados a cargo: ")) - 1

        if 0 <= escoger < len(gerentes):
            GerenteSeleccionado = gerentes[escoger]
            print(f"Empleados a cargo de {GerenteSeleccionado.nombre}:")
            GerenteSeleccionado.mostrar_personas_a_cargo()
        else:
            print("Gerente inválido")

    elif opcion == 6:
        print("Gerentes disponibles:")
        gerentes = [Ngerentes for Ngerentes in empresa.empleados if isinstance(Ngerentes, Gerente)]
        for i, gerente in enumerate(gerentes):
            print(f"{i+1}. {gerente.mostrar_datos()}")

        escoger = int(input("Seleccione el número del gerente para modificar sus empleados a cargo: ")) - 1

        if 0 <= escoger < len(gerentes):
            GerenteSeleccionado = gerentes[escoger]
            print("1. Agregar empleado a gerente")
            print("2. Remover empleados de gerente")
            opcion = int(input("Seleccione la acción: "))

            if opcion == 1:
                print("Empleados disponibles para asignar:")
                empleados_disponibles = [emp for emp in empresa.empleados if emp != GerenteSeleccionado and emp not in GerenteSeleccionado.getEmpleadosAcargo()]
                for i, empleado in enumerate(empleados_disponibles):
                    print(f"{i+1}. {empleado.mostrar_datos()}")

                escoger_emp = int(input("Seleccione el número del empleado para asignar al gerente: ")) - 1

                if 0 <= escoger_emp < len(empleados_disponibles):
                    EmpleadoSeleccionado = empleados_disponibles[escoger_emp]
                    GerenteSeleccionado.asignar_empleado(EmpleadoSeleccionado)
                    print(f"Empleado {EmpleadoSeleccionado.nombre} asignado a {GerenteSeleccionado.nombre}")
                else:
                    print("Empleado inválido")
            elif opcion == 2:
                print("Empleados a cargo del gerente:")
                empleados_a_cargo = GerenteSeleccionado.getEmpleadosAcargo()
                for i, empleado in enumerate(empleados_a_cargo):
                    print(f"{i+1}. {empleado.mostrar_datos()}")

                escoger_emp = int(input("Seleccione el número del empleado para remover del gerente: ")) - 1

                if 0 <= escoger_emp < len(empleados_a_cargo):
                    EmpleadoSeleccionado = empleados_a_cargo[escoger_emp]
                    GerenteSeleccionado.remover_empleado(EmpleadoSeleccionado)
                    print(f"Empleado {EmpleadoSeleccionado.nombre} removido de {GerenteSeleccionado.nombre}")
                else:
                    print("Empleado inválido")
