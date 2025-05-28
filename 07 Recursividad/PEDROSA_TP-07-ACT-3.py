def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia_recursiva(base, exponente - 1)

base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"{base}^{exponente} = {potencia_recursiva(base, exponente)}")
