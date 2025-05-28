# TP 5 - Listas - UTN a Distancia

# Actividad 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

# Actividad 2: Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo
cosas_que_me_gustan = ["programar", "leer", "jugar al fútbol", "viajar", "escuchar música"]
print(cosas_que_me_gustan[-2])

# Actividad 3: Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print(lista_vacia)

# Actividad 4: Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# Actividad 5: Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
# Este programa crea una lista de números, elimina el número más grande (en este caso 22) y después imprime la lista resultante.

# Actividad 6: Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros
saltos_cinco = list(range(10, 31, 5))
print(saltos_cinco[:2])

# Actividad 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]
print(autos)

# Actividad 8: Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# Actividad 9: Trabajar con la lista “compras” cuyos elementos representan productos de diferentes clientes
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"
# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")
# d) Imprimir la lista resultante
print(compras)

# Actividad 10: Elaborar una lista anidada llamada “lista_anidada” con los elementos dados
lista_anidada = [15,True,[25.5, 57.9, 30.6],False]
print(lista_anidada)
