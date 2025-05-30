import random

def coordenadas_random(n):
    return [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(n)]

def distancia_pitagoras(coord):
    return (coord[0]**2 + coord[1]**2) ** 0.5

def coordenada_alejada(coords):
    if len(coords) == 0:
        return None
    if len(coords) == 1:
        x, y = coords[0]
        if x > 0 and y < 0:
            return coords[0]
        else:
            return None
    else:
        mitad = len(coords) // 2
        izquierda = coordenada_alejada(coords[:mitad])
        derecha = coordenada_alejada(coords[mitad:])

        if izquierda and derecha:
            return izquierda if distancia_pitagoras(izquierda) > distancia_pitagoras(derecha) else derecha
        elif izquierda:
            return izquierda
        else:
            return derecha

# Main
def main():
    try:
        n = int(input("Ingrese la cantidad de pares de coordenadas que desee: "))
        coords = coordenadas_random(n)
        print("Coordenadas generadas aleatoriamente:")
        for co in coords:
            print(co)

        resultado = coordenada_alejada(coords)
        if resultado:
            print(f"\nCoordenada más alejada de (0,0): {resultado}")
            print(f"Distancia al origen: {round((resultado[0]**2 + resultado[1]**2) ** 0.5, 2)}")
        else:
            print("\nNo se encontró ninguna coordenada con (0,0)")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()