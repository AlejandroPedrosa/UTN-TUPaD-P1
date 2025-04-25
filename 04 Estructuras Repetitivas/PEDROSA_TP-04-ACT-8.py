#Actividad 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio)

pares = impares = positivos = negativos = 0
for _ in range(100): 
    n = int(input("Ingrese un número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")