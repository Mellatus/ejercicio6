# Solicitamos los dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Solicitamos la operación
operacion = input("Introduce la operación a realizar (+, -, *, /): ")

# Utilizamos 'match' para evaluar la operación elegida
match operacion:
    case "+":
        resultado = num1 + num2
        print(f"El resultado de {num1} + {num2} es: {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"El resultado de {num1} - {num2} es: {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"El resultado de {num1} * {num2} es: {resultado}")
    case "/":
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    case _:
        # El caso '_' actúa como un "comodín" si no coincide con los anteriores
        print("Error: La operación introducida no es válida.")