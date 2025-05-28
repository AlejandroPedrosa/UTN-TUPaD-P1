def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "No se puede dividir por 0")

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
