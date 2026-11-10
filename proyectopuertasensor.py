producto = "Sensor ultrasónico"
precio = 3450.5
cantidad = 3
impuesto = 0.21
subtotal = precio * cantidad
impuesto_total = impuesto * subtotal
total = impuesto_total + subtotal
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio:.2f}")
print(f"Cantidad: {cantidad} unidades")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Impuesto: ${impuesto_total:,.2f}")
print(f"Total final: ${total:,.2f}")