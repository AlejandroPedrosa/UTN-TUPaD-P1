#Actividad 6: Sesgo de distribución
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Media: {media:.2f}, Mediana: {mediana}, Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar el sesgo con claridad")