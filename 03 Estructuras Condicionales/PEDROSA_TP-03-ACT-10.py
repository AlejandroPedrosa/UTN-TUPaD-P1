#Actividad 10: Estaciones del año según fecha y hemisferio

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion = "Otoño" if hemisferio == "N" else "Primavera"
else:
    estacion = "Fecha inválida"

print(f"Estación actual: {estacion}")