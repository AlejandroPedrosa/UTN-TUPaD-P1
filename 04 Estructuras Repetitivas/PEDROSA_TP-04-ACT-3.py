#Actividad 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

menor = min(a, b)
mayor = max(a, b)
suma = 0

for i in range(menor + 1, mayor):
    suma += i

print("La suma es:", suma)
