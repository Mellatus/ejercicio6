nombre = ["Noelia", "Adrián", "Himar", "Darío"]
apellidos = ["Bermúdez", "Rodríguez", "Delgado", "García"]
nombre_completo=nombre[0]+" "+apellidos[0]
nombre[2] = "Héctor Barrera"
x = 0
while x < 4:
    nombre_completo = nombre[x] +" "+ apellidos[x]
    nombre[x] = nombre_completo
    x+=1
print(nombre)