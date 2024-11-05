#Desarrolle un programa que solicite ingrese tres voltajes distintos 
#e indique si el promedio de los voltajes ingresados es menor a 115 visualice `"VOLTAJE CORRECTO"`,
#caso contrario sea mayor a 115 y menor a 220 visualice `"ALTO VOLTAJE"`,
#y si es mayor a 220 visualice `"PELIGRO"`.

firstVoltage = float(input("Cuál es el primer voltage?: "))
secondVoltage = float(input("Cuál es el segundo voltage?: "))
thirdVoltage = float(input("Cuál es el tercer voltage?: "))

average = (firstVoltage + secondVoltage + thirdVoltage)/3

if average <= 115:
    print("VOLTAJE CORRECTO")
elif average > 115 and average < 220:
    print("ALTO VOLTAJE")
elif average >= 220:
    print("PELIGRO")