while True:

    print("Que desea Covertir")

    print("---------------------------------")

    print("1. Conversor de farenheit a celcius")
    print("2. Conversor de dólares a euros")
    print("3. Salida")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            farenheiht = float(input("Introduce el valor en farenheiht que desee: "))
            celcius = (farenheiht - 32) * 5 / 9
            print(celcius)
        case "2":
            dolares = float(input("Introduce la cantidad de dólares: "))
            euros = dolares * 0.92
            print(euros)
        case "3":
            break
        case _:
            print("Opción no válida")