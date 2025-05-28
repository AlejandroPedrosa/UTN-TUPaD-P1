def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Palabra: ").lower()
print(f"Es palíndromo la palabra: {palabra}" if es_palindromo(palabra) else f"No es palíndromo la palabra {palabra}")
