nombres_completo = []

nombre = ["Noelia", "Adrián", "Himar", "Darío"]
apellidos = ["Bermúdez", "Rodríguez", "Delgado", "García"]
nombre_completo=nombre[0]+" "+apellidos[0]

x = 0

while x < 4:
    nombre_completo = nombre[x] +" "+ apellidos[x]
    # nombre[x] = nombre_completo
    nombre[x] = nombre_completo
    nombres_completo.append(nombre_completo)
    x+=1


print(nombres_completo)
print(nombre)