proyecto = input("Nombre del proyecto: ")
componente1 = input("Nombre del componente 1: ")
precio1 = float(input("Ponga el precio del producto 1: "))
cantidad1 = int(input("Ponga la cantidad: "))
componente2 = input("Nombre del componente 2: ")
precio2 = float(input("Ponga el precio del producto 2: "))
cantidad2 = int(input("Ponga la cantidad: "))
integrantes = int(input("Integrantes de grupo: "))
subtotal1 = precio1 * cantidad1
subtotal2 = precio2 * cantidad2
total = subtotal1 + subtotal2
aporte = total / integrantes
print(f"PRESUPUESTO: {proyecto}")
print(f"{componente1}: ${subtotal1:,.2f}")
print(f"{componente2}: ${subtotal2:,.2f}")
print(f"TOTAL: ${total:,.2f}")
print(f"Aporte por integrante: ${aporte:,.2f}")