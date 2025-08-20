inventario = {}

print("Bienvenido")
while True:
    print("escoge la opcion deseada")
    print("1. Agregar productos")
    print("2. Vender")
    print("3. mostrar inventario")
    print("0. salir")
    opcion = int(input())

    if opcion == 1:
        nuevo_producto = input("Nombre del producto: ")
        cantidad = int(input("cantidad: "))
        if nuevo_producto in inventario:
            inventario[nuevo_producto] += cantidad
        else:   
            inventario[nuevo_producto] = cantidad
            print("se agrego correctamente")
            print(inventario)
    
    elif opcion == 2:
        producto = input("ingrese el nombre del producto: ")
        if producto in inventario:
            print("Si hay ", producto,"nos queda", inventario[producto])
            compra = int(input("ingrese cuanto quiere comprar: "))
            if inventario[producto] >= compra:
                inventario[producto] -= compra
                print("compra exitosa")
                print(inventario)
            else: 
                print("no hay cantidad suficiente")
        else:
            print("producto no existente")
        
    elif opcion == 3: 
        print(inventario)

    elif opcion == 0:
        print("hasta luego")
        break
    else:
        print("opcion no valida")