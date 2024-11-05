#Desarrolle el código fuente de un programa que permita ingresar y leer el valor correspondiente a una distancia en metros
#y la visualice expresadas en km.
#Para convertir `metros` a `kilómetros`, puedes usar la siguiente fórmula: km=m/1000

distance = float(input("Cuál es la distancia?: (En metros)"))

distanceKM = distance/1000

print(f"""La distancia en kilometros es: {distanceKM}""")