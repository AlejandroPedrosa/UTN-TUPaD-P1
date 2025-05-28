def decimal_a_binario_recursivo(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario_recursivo(num // 2) + str(num % 2)
    
num = int(input("Ingresa un numero decimal para convertirlo a binario: "))
print(f"El numero {num} en binario es: {decimal_a_binario_recursivo(num)}")