# Usamos float por si la nota tiene decimales (ej. 6.5)
nota = float(input("Ponga la nota de su examen, por favor (0-10): "))

# Primero validamos que la nota sea real (entre 0 y 10)
if nota < 0 or nota > 10:
    print("Error: La nota debe estar entre 0 y 10.")
    
# Si es válida, empezamos a clasificar de menor a mayor
elif nota < 5:
    print("Suspenso")
    
elif nota < 7:  # Entra aquí si es mayor o igual a 5 Y menor que 7
    print("Aprobado")
    
elif nota < 9:  # Entra aquí si es mayor o igual a 7 Y menor que 9
    print("Notable")
    
else:           # Entra aquí para cualquier nota entre 9 y 10
    print("Sobresaliente")
