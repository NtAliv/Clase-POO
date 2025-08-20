class Tienda:
    def __init__(self, nombre, precio, cantidad, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
    
    def vender(self, cantidad_vendida):
        if cantidad_vendida <= cantidad:
            self.cantidad -= cantidad_vendida
            print("producto vendido con exito")
        else:
            print("no tenemos suficiente material")


lista_tienda = []

print("Bienvenido a nuestra tienda")

while True:

    print("seleccione la opcion deseada")
    print("1. agregar mercancia")
    print("2. Mostrar informacion de la mercancia")
    print("3. Mercar")
    print("0. Salir")
    opcion = int(input())

    if opcion == 1:

        print("Ingrese el nombre del producto: ")
        nombre = input()
        print("Ingrese el precio: ")
        precio  = float(input())
        print("Ingrese la cantidad del producto: ")
        cantidad = int(input())
        codigo = int(input("ingrese el codigo: "))

        tienda  = Tienda(nombre, precio, cantidad, codigo)
        lista_tienda.append(tienda)
        print("mercancia entregada correctamente")
    
    elif opcion == 2:
        numero_producto = len(lista_tienda)
        print("El numero de productos es ", numero_producto)
        for estudiante in lista_tienda:
            print("--------Productos--------")
            print("Nombre - Precio - Cantidad")
            print(tienda.nombre, "-", tienda.precio, "-", tienda.cantidad)
    elif opcion == 3:
        codigo_producto = int(input("ingrese el codigo del producto que quiere vender"))
        
        existe = False
        for producto in lista_tienda:
            if tienda.codigo == codigo_producto:
                cantidad_venta = int(input("cuanto desea vender: "))
                tienda.vender(cantidad_venta)
                existe = True
                break
        

        if existe == False:
            print("producto no existente..")
        

    elif opcion == 0:
        print("hasta luego")
        break

    else:
        print("opcion no valida")