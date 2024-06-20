SECTORES = ["centro", "norte", "sur"]
def registrar_pedido(pedidos):
    print("REGISTRO DE PEDIDO")
    #VALIDACIONES DATOS PEDIDO
    while True:
        nombre = input("Ingrese el nombre y apellido del cliente: ")

        if nombre == "":
            print("El nombre no puede estar vacio.\n")
        else:
            break

    while True:
        direccion = input("Ingrese la direccion del cliente: ")

        if direccion == "":
            print("La direccion no puede estar vacia.\n")
        else:
            break
    while True:
        sector = input("Seleccione el sector (Centro, Norte o Sur): ").lower()

        if sector in SECTORES:
            break
        else:
            print("Por favor, seleccione uno de los sectores. \n")

    cantPequenio = 0
    cantMediano = 0
    cantGrande = 0
    while True:
        try:
            print("*********MENU Detalle pedido**********")
            print("1. Pedido pequeño.")
            print("2. Pedido mediano.")
            print("3. Pedido grande")
            print("4. Salir del menu Detalle pedido")
            opcionPedido= int(input("Seleccione una opción: "))

            if opcionPedido == 1 or opcionPedido ==2 or opcionPedido ==3:
                while True:
                    cantidad = int(input("Ingrese la cantidad: "))
                    if cantidad <=0:
                        print("La cantidad debe ser mayor que 0.\n")
                    else:
                        break

            if opcionPedido == 1:
                cantPequenio = cantPequenio + cantidad

            elif opcionPedido == 2:
                cantMediano = cantMediano + cantidad

            elif opcionPedido == 3:
                cantGrande = cantGrande + cantidad

            elif opcionPedido == 4:
                print("Saliendo del menu pedido .\n")
                break
            else:
                print("Ingrese una opción valida. \n")
            print()
        except ValueError:
            print("Por favor, ingrese solo numeros. \n")

    pedido ={
        "Cliente": nombre,
        "Direccion": direccion,
        "Sector": sector,
        "Pequeño":  cantPequenio,
        "Mediano": cantMediano,
        "Grande": cantGrande
    }

    pedidos.append(pedido)

    print("Pedido añadido.\n")
   
def listar_todos_los_pedidos(pedidos):
    print("LISTA DE PEDIDOS")
    for pedido in pedidos:
        print("Cliente: ", pedido["Cliente"])
        print("Dirección: ",pedido["Direccion"])
        print("Sector: ",pedido["Sector"])       
        print("Paquetes: ", "Pequeño - ", pedido["Pequeño"], ", Mediano - ",pedido["Mediano"], ", Grande - ", pedido["Grande"])
        print("")

def imprimir_hoja_ruta(pedidos):
    print("IMPRIMIR PEDIDOS")
    while True:
        sectorAImprimir = input("Seleccione el sector (Centro, Norte o Sur): ").lower()

        if sectorAImprimir in SECTORES:
            pedidosAImprimir = []

            for pedido in pedidos:
                if pedido["Sector"] == sectorAImprimir:
                    pedidosAImprimir.append(pedido)
            break
        else:
            print("Por favor, seleccione uno de los sectores. \n")
    
    with open("hoja_de_ruta.txt", "w") as archivo:
        for pedido in pedidosAImprimir:
            archivo.write(f"Cliente:  {pedido["Cliente"]} \n")
            archivo.write(f"Direccion: {pedido["Direccion"]} \n")
            archivo.write(f"Sector: {pedido["Sector"]}, \n")       
            archivo.write(f"Paquetes: Pequeño -  {pedido["Pequeño"]},  Mediano - {pedido["Mediano"]}, Grande - {pedido["Grande"]}\n\n")

    


    


    
