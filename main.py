#Desarrolle el código fuente de un programa que permita ingresar cinco voltajes,
#obtener su promedio
#y visualizar `"ALTO VOLTAJE"`, si su promedio es mayor a 220,
#caso contrario sea menor mostrar `"VOLTAJE CORRECTO"`.

firstVoltage = int(input("Cuál es el primer voltaje?: "))
secondVoltage = int(input("Cuál es el segundo voltaje?: "))
thirdVoltage = int(input("Cuál es el tercer voltaje?: "))
fourthVoltage = int(input("Cuál es el cuarto voltaje?: "))
fifthVoltaje = int(input("Cuál es el quinto voltaje?: "))

average = (firstVoltage + secondVoltage + thirdVoltage + fourthVoltage + fifthVoltaje)/5

if average > 220:
    print("ALTO VOLAJE")
else:
    print("VOLTAJE CORRECTO")