#Actividad 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

total_suma = 0
cantidad_numeros = 100

for _ in range(cantidad_numeros):
    total_suma += int(input("Ingrese un número: "))

media = total_suma / cantidad_numeros
print("La media es:", media)