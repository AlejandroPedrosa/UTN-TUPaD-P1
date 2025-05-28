def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
def verificar_positivo(num):
    return num if num > 0 else verificar_positivo(int(input("Ingresa un número entero positivo: ")))

# Programa principal
numero = verificar_positivo(int(input("Número: ")))
digito = int(input("Dígito a contar (0-9): "))
print(f"Aparece {contar_digito(numero, digito)} veces")
