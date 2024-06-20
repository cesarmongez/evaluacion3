import funciones as fn
pedidos = []
while True:
    try:
        print("*********MENU PaquExpress**********")
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        opcionMenu = int(input("Seleccione una opción: "))

        if opcionMenu == 1:
            fn.registrar_pedido(pedidos)
        elif opcionMenu == 2:
            fn.listar_todos_los_pedidos(pedidos)
        elif opcionMenu == 3:
            fn.imprimir_hoja_ruta(pedidos)
        elif opcionMenu == 4:
            print("Saliendo del programa.\n")
        else:
            print("Ingrese una opción valida. \n")
        print()

        
    except ValueError:
        print("Ingrese solo numeros. \n")


