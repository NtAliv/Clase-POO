class Motor:
    def __init__(self, modelo):
        self.modelo = modelo 
        self.estado = False
    
    def encender(self):
        if self.estado is True: 
            self.estado = False
            print("apagado")
        else: 
            self.estado = True
            print("encendido")

class Vehiculo:
    def __init__(self, nombre, placa):
        self.nombre = nombre
        self.placa = str(placa)
        self.motor = None 
        self.servicio = False 
    
    def agregarM(self, modelo):
        if self.motor is None: 
            self.motor = (Motor(modelo))
            print("motor agregado al vehiculo")
        else: 
            print("El vehiculo ya tiene motor")
    
    def servicios(self):
        if self.servicio is True: 
            self.servicio = False
            print("Fuera de servicio")
        else: 
            self.servicio = True
            print("De nuevo en servicio")
    
    def InfoServicio(self):
        if self.servicio is True: 
            return "En servicio"
        
        else:
            return "No esta en servicio"

class Flota:
    def __init__(self, NombreFlota):
        self.NombreFlota = NombreFlota
        self.vehiculos = []

    def agregarV(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print("Vehiculo Agregado Correctamente a la flota")

    def mostrarV(self):
        numero_Vehiculos = len(self.vehiculos)
        print("\nEl numero de vehiculos es ", numero_Vehiculos)
        print("--------Vehiculos--------")
        print("Nombre - Placa - condicion")
        for TotalFlota in self.vehiculos:
            print(TotalFlota.nombre, "-", TotalFlota.placa, "-", TotalFlota.InfoServicio())

    def quitarV(self, placa):
        existe = False
        for remover in self.vehiculos:
            if remover.placa == placa: 
                self.vehiculos.remove(remover)
                print("Vehiculo con placa", placa, "quitado de la flota")
                existe = True 
                break
        if existe == False:     
            print("No se encontró el vehículo con esa placa")

    def BuscarPlaca(self):
        BuscarP = input("ingrese la placa: ")
        existe = False
        for Busqueda in self.vehiculos:
            if Busqueda.placa == BuscarP:
                print("El vehiculo que estas buscando es: ", Busqueda.nombre)
                existe = True
                break
        if existe == False:
            print("Vehiculo no encontrado")


flota = Flota("¡FLota!")

while True:
    print("\n--- Menú ---")
    print("1. Agregar vehículo")
    print("2. Asignar motor a un vehículo")
    print("3. Mostrar vehículos")
    print("4. Quitar vehículo por placa")
    print("5. Buscar vehículo por placa")
    print("6. Cambiar estado de servicio")
    print("7. Activar/desactivar Motor")
    print("0. Salir")

    opcion = int(input())
    
    if opcion == 1:
        Nombre = input("Ingrese el nombre del vehiculo: ")
        placa = input("Ingrese la placa del vehiculo: ")
        VEHICULO = Vehiculo(Nombre, placa)
        flota.agregarV(VEHICULO)
        print("Vehiculo agregado correctamente.")

    elif opcion == 2:
        placa = input("Ingrese la placa del vehículo al que desea agregar motor: ")
        modelo = input("Ingrese el modelo del motor: ")
        existe = False
        for motor in flota.vehiculos:
            if motor.placa == placa:
                motor.agregarM(modelo)
                existe = True
                break
        if existe == False:
            print("No se encontró el vehículo con esa placa")

    elif opcion == 3:
        flota.mostrarV()

    elif opcion == 4:
        placa = input("Ingrese la placa del vehículo: ")
        flota.quitarV(placa)

    elif opcion == 5:
        flota.BuscarPlaca()

    elif opcion == 6:
        placa = input("Ingrese la placa del vehículo al que deseas cambiar el servicio")
        existe = False
        for servicio in flota.vehiculos:
            if servicio.placa == placa:
                servicio.servicios()
                existe = True
                break
        if existe == False:
            print("No se encontró el vehículo con esa placa")
    
    elif opcion == 7: 
        placa = input("Ingrese la placa del vehículo al que desea activar/desactivar motor")
        existe = False
        for Encender in flota.vehiculos:
            if Encender.placa == placa:
                existe = True
                if Encender.motor is not None: 
                    Encender.motor.encender()
                else:
                    print("El vehiculo no tiene motor")
                break
        if existe == False:
            print("No se encontró el vehículo con esa placa")

    elif opcion == 0:
        print("saliendo")
        break 
    
    else: 
        print("Opcion no valida")

    
        