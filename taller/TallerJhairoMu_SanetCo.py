from abc import ABC, abstractmethod
from dataclasses import dataclass

class Empresa: 
    def __init__(self, nombre, nombre_archivo):
        self.nombre = nombre 
        self.lista_vehiculos = []
        self.nombre_archivo = nombre_archivo

    
    def añadir_vehiculos(self, transporte):
        self.lista_vehiculos.append(transporte)

    def guardar_en_archivo(self):
        try:
            with open(self.nombre_archivo, "w") as f:
                for vehiculo in self.lista_vehiculos:
                    impuesto = vehiculo.calcular_impuesto()
                    f.write(f"{vehiculo.placa}, {vehiculo.marca}, {vehiculo.valor}, {vehiculo.tipo}, {impuesto}\n")
            print("Vehículos guardados exitosamente.")
        except Exception as e:
            print("Hubo un error al guardar los vehículos:", e)
    
    def cargar_vehiculos(self):
        self.lista_vehiculos=[]
        try:
            with open(self.nombre_archivo, "r") as f:
                print("\n Cargando datos:")
                print("Placa | Marca | Valor | Tipo | Impuesto")
                print("----------------------------------")
                for linea in f:
                    placa, marca, valor, tipo ,impuesto = linea.strip().split(",")
                    print(f"{placa} | {marca} | {valor} | {tipo} | {impuesto}")
                    valor = float(valor)
                    if tipo == "Particular":
                        vehiculos = Particular(placa, marca, valor, tipo)
                    elif tipo == "Camion":
                        vehiculos = Camion(placa, marca, valor, tipo)
                    elif tipo == "Moto":
                        vehiculos = Moto(placa, marca, valor, tipo)
                    else:
                        print(" no se encontro el tipo")
                        continue
                    self.lista_vehiculos.append(vehiculos)
        except Exception:
            print(f"No se encontró el archivo {self.nombre_archivo}")

@dataclass
class Transporte(ABC):
    placa: str 
    marca: str 
    valor: float 
    tipo: str


    @abstractmethod
    def calcular_impuesto(self) -> float: 
        ...
    
class Particular(Transporte):
    
    def calcular_impuesto(self):
        return self.valor * 0.10



class Camion(Transporte): 

    def calcular_impuesto(self):
        return self.valor * 0.15


class Moto(Transporte): 

    def calcular_impuesto(self):
        return self.valor * 0.05
    

empresa = Empresa("Transportes S.A.", "flota.txt")

auto = Particular("ABC123", "Toyota", 10000, "Particular")
camion = Camion("XYZ789", "Volvo", 25000, "Camion")
moto = Moto("MNO456", "Yamaha", 5000, "Moto")

empresa.añadir_vehiculos(auto)
empresa.añadir_vehiculos(camion)
empresa.añadir_vehiculos(moto)

empresa.guardar_en_archivo()
empresa.cargar_vehiculos()
