import random 

class Cuenta:
    def __init__(self, nombre_titular):
        self.nombre_titular = nombre_titular
        self.numero_cuenta = random.randint(10000, 999999)
        self.saldo = 0
    
    def depositar(self, cantidad): 
        self.saldo = self.saldo + cantidad
        return self.saldo
    
    def retirar(self, cantidad):
        if self.saldo > cantidad:
            self.saldo -= cantidad
            return self.saldo 
        else:
            print("No hay dinero para ese retiro")
            return -1
        
    def consultar(self):
        return self.saldo 
    
#Programa principal

lista_cuentas = []

print("Bienvenido al banco")
while True:
    print("Ingrese la opcion deseada")
    print("1. Crear cuenta")        
    print("2. depositar ")
    print("3. Retirar")
    print("4. Consultar saldo")
    print("0. salir")

    opcion = int(input())

    if opcion == 1:
        nombre = input("Ingrese el nombre del titular: ")
        nueva_cuenta = Cuenta(nombre)
        lista_cuentas.append(nueva_cuenta)
        print("cuenta creada exitosamente, su numero de cuenta es", nueva_cuenta.numero_cuenta)
    
    elif opcion == 2:
        numero_cuenta = int(input("ingrese el numero de cuenta: "))
        for cuenta in lista_cuentas:
            existe = False 
            if cuenta.numero_cuenta == numero_cuenta:
                existe = True
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                nuevo_saldo = cuenta.depositar(cantidad)
                print("El nuevo saldo es", nuevo_saldo)
            if existe == False:
                print("no se encontro la cuenta")

    elif opcion == 3:
        numero_cuenta = int(input("ingrese el numero de cuenta: "))
        existe = False 
        for cuenta in lista_cuentas:
            existe = True 
            cantidad  = float(input("Ingrese la cantidad a retirar: "))
            nuevo_saldo = cuenta.retirar(cantidad)

            if nuevo_saldo >= 0:
                print("retiro exitoso. su nuevo saldo es: ", nuevo_saldo)
        
        if existe == False: 
            print("cuenta no existente")
    
    elif opcion == 4:
        numero_cuenta = int(input("ingrese el numero de cuenta: "))
        existe = False 
        for cuenta in lista_cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                existe = True
                print("su saldo es", cuenta.consultar())
            
        if existe == False:
            print("cuenta no existe")
        
    elif opcion == 0:
        print("hasta luego")
    
    else: 
        ("opcion no valida")

            
