#Actividad 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

texto = input("Ingrese una frase o palabra: ")

ultimo_caracter = texto[-1].lower() if texto else ''

if ultimo_caracter in {'a', 'e', 'i', 'o', 'u'}:
    print(texto + "!")
else:
    print(texto)