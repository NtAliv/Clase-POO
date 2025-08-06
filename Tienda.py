class Tienda:
    def _init_(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def vender(self, cantidad_vendida):
        if cantidad_vendida <= cantidad:
            self.cantidad -= cantidad_vendida
        else:
            print("no tenemos suficiente material")
print("Bienvenido a nuestra tienda")
lista_tienda = []

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
        print("Ingrese la cantidad del producto: ")
        cantidad = int(input())
        print("Ingrese el precio: ")
        precio  = float(input())

        tienda  = Tienda(nombre, cantidad, precio)
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
        print("ingrese el material a comprar")
        merca = input()
        if tienda.nombre.lower() == merca.lower():
            cantidad = int(input("ingrese cuanta cantidad quiere: "))
            tienda.vender(cantidad)
        else:
            ("no se encontro el producto")
        break
    else:
        print("opcion no valida")