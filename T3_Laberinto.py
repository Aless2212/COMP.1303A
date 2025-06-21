lab = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1]
]

n = len(lab)
res = [[0 for _ in range(n)] for _ in range(n)]
camino = []
min_puntos = 23
camino_encontrado = False
puntos_finales = 0
movs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # arriba, derecha, abajo, izquierda

def es_valido(x, y):
    return 0 <= x < n and 0 <= y < n and lab[x][y] != 0 and res[x][y] == 0

def puntos_extra(valor):
    return valor if valor in (3, 4) else 0

def encontrar_camino(x, y, puntos):
    global camino_encontrado, puntos_finales
    if camino_encontrado:
        return

    if not es_valido(x, y):
        return

    res[x][y] = 1
    camino.append((x, y))
    puntos += puntos_extra(lab[x][y])

    if (x, y) == (0, 0):  # Llegamos a F
        if puntos >= min_puntos:
            camino_encontrado = True
            puntos_finales = puntos
        else:
            res[x][y] = 0
            camino.pop()
        return

    for dx, dy in movs:
        encontrar_camino(x + dx, y + dy, puntos)
        if camino_encontrado:
            return

    res[x][y] = 0
    camino.pop()

def imprime_laberinto(matriz, titulo=""):
    if titulo:
        print(titulo)
    for i in range(n):
        for j in range(n):
            if (i, j) == (8, 0):
                print("I", end=" ")
            elif (i, j) == (0, 0):
                print("F", end=" ")
            else:
                print(matriz[i][j], end=" ")
        print()
    print()

# Ejecutar búsqueda
encontrar_camino(8, 0, 0)

imprime_laberinto(lab, "Laberinto original (I = Inicio, F = Fin):")

if camino_encontrado:
    print(f"Camino válido encontrado con {puntos_finales} puntos:\n")
    imprime_laberinto(res)
else:
    print("No hay salida válida con ≥23 puntos.")