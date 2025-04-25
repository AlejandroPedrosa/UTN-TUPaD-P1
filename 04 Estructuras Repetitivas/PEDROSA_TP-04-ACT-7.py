#Actividad 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

n = int(input("Ingrese un número entero positivo: "))
suma = 0
if n < 0:
    print("Error! debes ingresar un numero positivo.")
else:
    for i in range(n + 1):
        suma += i
    print("La suma es:", suma)
