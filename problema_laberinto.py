lab = [
    [1,1,1,0,0,0,0,0,0],
    [0,0,1,0,1,1,1,1,0],
    [1,1,1,0,1,0,0,1,0],
    [1,0,0,0,1,0,0,1,0],
    [1,1,1,1,1,0,0,1,0],
    [0,0,0,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,1,0],
]

res = [[0 for _ in range(9)] for _ in range(9)]

def imprime(mat):
    for f in mat:
        for c in f:
            print(f"{c},", end="")
        print()
    print()

def valida(fil, col):
    if 0 <= fil < len(lab) and 0 <= col < len(lab[0]):
        if lab[fil][col] == 1 and res[fil][col] == 0:
            return True
    return False

def labbas(lab, res, fil, col):
    if (fil, col) == (9, 9):
        if valida(fil, col):
            res[fil][col] = 1
            imprime(res)
            return True
        else:
            return False
    if valida(fil, col):
        res[fil][col] = 1
        imprime(res)
       
        if labbas(lab, res, fil, col+1):  
            return True
        elif labbas(lab, res, fil, col-1): 
            return True
        elif labbas(lab, res, fil+1, col): 
            return True
        elif labbas(lab, res, fil-1, col):  
            return True
        res[fil][col] = 0  
    return False

inicio_fila = 0
inicio_columna = 0

if labbas(lab, res, inicio_fila, inicio_columna):
    print("¡Saliste del laberinto!")
else:
    print("No hay salida desde esa posición.")
