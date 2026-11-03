stock_nombre = ["ratón", "teclado", "usb", "HD_Externo"]
stock_cantidad = [10, 8, 20, 7]
stock_precioNeto = [2, 6, 3, 10]
stock_PVP = [5, 12, 10, 25]

print("----------------x---------------")

while True:

    print("Elija una opción")

    print("----------------x---------------")

    print("1. Buscar")
    print("2. Ventas")
    print("3. Stock")
    print("4. Salir")

    print("----------------x---------------")

    menu = input("Elija la opción, por favor (1 - 4): ")
    match menu:
        case "1":
            print("Que producto desea buscar")
            break
        case "2":
            print("Nuestras ventas")
            break
        case "3":
            while True:
                print("El stock que tenemos disponible")
                print("1. Listar\n2. Añadir\n3. Volver")
                stock = input("Elija una opción por favor: ")
                match stock:
                    case "1":
                        print("Liste el producto que desea")
                    case "2":
                        print("Añada a su carrito los productos")
                    case "3":
                        print("Volver")
                        break
                    case _:
                        print("Opción no válida")
                break
        case "4":
            print("Gracias por usar nuestra aplicación")
            exit()
        case _:
            print("Esa opción no es válida en este momento")