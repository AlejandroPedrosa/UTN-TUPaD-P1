def sumar_digitos(numero):
    if numero // 10 == 0:
        return numero
    else:
        return numero % 10 + sumar_digitos(numero // 10)

def verificar_positivo(numero):
    return numero if numero > 0 else verificar_positivo(int(input("Ingresa un número entero positivo: ")))

numero = int(input("Ingresa un número: "))
numero_verificado = verificar_positivo(numero)
print(f"- La suma de los dígitos de {numero_verificado} es {sumar_digitos(numero_verificado)}")