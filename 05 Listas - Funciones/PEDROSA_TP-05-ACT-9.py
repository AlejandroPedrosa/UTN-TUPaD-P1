def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")
