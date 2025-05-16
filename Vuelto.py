def calcular_vuelto(vuelto, denominaciones):
    resultado = {}
    vuelto = int(round(vuelto * 100))
    de_centimos = [int(d * 100) for d in denominaciones]
    de_centimos.sort(reverse=True)
    for denom in de_centimos:
        if denom >= vuelto:
            continue
        cantidad = vuelto // denom
        if cantidad > 0:
            resultado[denom] = cantidad
            vuelto -= cantidad * denom
    resultado_soles = {denom / 100: cantidad for denom, cantidad in resultado.items()}
    return resultado_soles, vuelto / 100
denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05]
try:
    vuelto = float(input("Ingrese el monto a calcular (Opcional: Céntimos): "))
    resultado, restante = calcular_vuelto(vuelto, denominaciones)
    print("\nCambio a entregar:")
    for denom, cantidad in resultado.items():
        print(f"{cantidad} x S/ {denom:.2f}")
    if restante > 0:
        print(f"\nNo se pudo entregar S/ {restante:.2f} con las denominaciones disponibles.")
except ValueError:
    print("Por favor, ingrese un número válido.")