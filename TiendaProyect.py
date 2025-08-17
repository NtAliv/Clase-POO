class Tienda:
    def __init__(self, nombre, precio, codigo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
    
    def vender(self, presupuesto_usuario):
        if presupuesto_usuario > precio:
            presupuesto_usuario -= self.precio
            print("producto vendido con exito")
            print("te devolvemos ", f"{presupuesto_usuario:.0f}", "$ pesos")
        else:
            print("no tienes suficiente dinero")


lista_tienda = []

print("Bienvenido a nuestra tienda")

while True:

    print("\nseleccione la opcion deseada")
    print("1. agregar mercancia")
    print("2. Mostrar informacion de la mercancia")
    print("3. Mercar")
    print("0. Salir\n")
    opcion = int(input())

    if opcion == 1:

        print("Ingrese el nombre del producto: ")
        nombre = input()
        print("Ingrese el precio: ")
        precio  = float(input())
        codigo = int(input("ingrese el codigo: "))
        tienda  = Tienda(nombre, precio, codigo)
        lista_tienda.append(tienda)
        print("mercancia entregada correctamente")
    
    elif opcion == 2:
        numero_producto = len(lista_tienda)
        print("\nEl numero de productos es ", numero_producto)
        for estudiante in lista_tienda:
            print("--------Productos--------")
            print("Nombre - Precio - Codigo")
            print(tienda.nombre, "-", f"{tienda.precio:.0f}", "$", tienda.codigo)
    elif opcion == 3:
        codigo_producto = int(input("ingrese el codigo del producto que quieres comprar: "))
        
        existe = False
        for producto in lista_tienda:
            if tienda.codigo == codigo_producto:
                presupuesto_usuario = int(input("cuanto dinero traes: "))
                tienda.vender(presupuesto_usuario)
                existe = True
                break

        if existe == False:
            print("producto no existente..")

    elif opcion == 0:
        print("hasta luego")
        break

    else:
        print("opcion no valida")

