"""
class Registro: 
    def __init__(self, tipo, cantidad, valor_unitario):
        self.tipo = tipo
        self.cantidad = cantidad 
        self.valor_unitario = valor_unitario
        

class Factura:
    def __init__(self, codigo):
        self.codigo = codigo
        self.registros = []
        self.total = 0 
   
    def agregar_registro(self, tipo, cantidad, valor_unitario):
        nuevo_registro = Registro(tipo, cantidad, valor_unitario)
        self.registros.append(nuevo_registro)
        self.total += (cantidad * valor_unitario)

mi_factura = Factura(12345)
mi_factura.agregar_registro("gaseosa", 2, 1000)
mi_factura.agregar_registro("Arepas", 4, 2200)

print("El total es: ", mi_factura.total)
        """
class Registro: 
    def __init__(self, tipo, cantidad, valor_unitario):
        self.tipo = tipo
        self.cantidad = cantidad 
        self.valor_unitario = valor_unitario
        

class Factura:
    def __init__(self, codigo):
        self.codigo = codigo
        self.registros = []
        self.total = 0 
   
    def agregar_registro(self, registro):
        self.registros.append(registro)
        self.total += (registro.cantidad * registro.valor_unitario)
    
mi_factura = Factura(12345)
registro1 = Registro("gaseosa", 5, 2500)
registro2 = Registro("Arepas", 3, 2500)
mi_factura.agregar_registro(registro1)
mi_factura.agregar_registro(registro2)

print("El total es: ", mi_factura.total)