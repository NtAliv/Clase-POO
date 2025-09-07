class Tienda:
    def __init__(self, nombre, precio, codigo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
    
    def vender(self, presupuesto_usuario):
        if presupuesto_usuario >= self.precio:
            presupuesto_usuario -= self.precio
            print("Producto vendido con exito")
            print("Te devolvemos ", f"{presupuesto_usuario:.0f}", "$ pesos")
            return presupuesto_usuario
        else:
            print("No tienes suficiente dinero")
            return presupuesto_usuario


lista_tienda = []

print("Bienvenido a nuestra tienda")

while True:

    print("\nSeleccione la opcion deseada")
    print("1. Agregar mercancia")
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
        for producto in lista_tienda:
            print("--------Productos--------")
            print("Nombre - Precio - Codigo")
            print(producto.nombre, "-", f"{producto.precio:.0f}", "$", producto.codigo)
    elif opcion == 3:
        nuevo_dinero = int(input("ingrese su presupuesto: "))

        respuesta = "si"
        while respuesta.lower() == "si":
            codigo_producto = int(input("ingrese el codigo del producto que quieres comprar: "))
            existe = False
            for venta in lista_tienda:
                if venta.codigo == codigo_producto:
                    nuevo_dinero = venta.vender(nuevo_dinero)                
                    existe = True
            if existe == False:
                print("producto no encontrado")
            
            if nuevo_dinero > 0:
                respuesta = input("Quieres seguir comprando? (si/no): ")

    elif opcion == 0:
        print("hasta luego")
        break

    else:
        print("opcion no valida")

