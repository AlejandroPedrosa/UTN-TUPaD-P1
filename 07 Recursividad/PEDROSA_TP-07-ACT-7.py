def contar_bloques(n):
    if n == 0:
        return 0
    return n + contar_bloques(n - 1)

niveles = int(input("Bloques en el nivel más bajo: "))
print(f"Total de bloques: {contar_bloques(niveles)}")
