def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("¿Hasta qué posición de Fibonacci querés ver?: "))
for i in range(n + 1):
    print(f"F({i}) = {fibonacci(i)}")
