#Desarrolle el código fuente de un programa que permita calcular el área de un triángulo equilátero,
#adicional visualizar `"DATOS NO VÁLIDOS"`,si el área es mayor a 1000.
#La fórmula para calcular el área `A` de un triángulo equilátero de lado `a` es: A = (R3/4)*(a**2)

side = float(input("Cuánto miden un lado del tríangulo?: "))

if side < 1000:
    area = ((3 ** 0.5 / 4) * (side ** 2))
    print(f"El valor del área es: {area}.")
else:
    print("DATOS NO VÁLIDOS")