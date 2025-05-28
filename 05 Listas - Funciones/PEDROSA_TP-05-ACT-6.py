def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresá la cantidad de segundos: "))
print(f"Horas: {segundos_a_horas(segundos):.2f}")
