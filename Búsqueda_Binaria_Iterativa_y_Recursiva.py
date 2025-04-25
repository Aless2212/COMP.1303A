def busqueda_binaria_iterativa(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # No se encontró el número, se elije una posición antes que el 0.

def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return 

    medio = (izquierda + derecha) // 2

    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)

#-------------------------------------------------------
#-------------------------------------------------------

# Programa principal
print("Bienvenido al programa de búsqueda binaria.")

# Lista fija dentro del código
lista = [3, 8, 12, 15, 20, 25, 30, 33, 40, 50]
print("Lista ordenada:", lista)

# Pedir al usuario el número a buscar
try:
    objetivo = int(input("Escribe el número que deseas buscar: "))

    # Búsqueda binaria iterativa
    resultado_iter = busqueda_binaria_iterativa(lista, objetivo)

    if resultado_iter != -1:
        print("Resultado (iterativo): El número se encuentra en la posición", resultado_iter)
    else:
        print("Resultado (iterativo): El número no está en la lista.")

    # Búsqueda binaria recursiva
    resultado_rec = busqueda_binaria_recursiva(lista, objetivo, 0, len(lista) - 1)

    if resultado_rec != -1:
        print("Resultado (recursivo): El número se encuentra en la posición", resultado_rec)
    else:
        print("Resultado (recursivo): El número no está en la lista.")

except ValueError:
    print("Por favor, ingresa un número válido.")
    
def busquedaIterativa(lista, n):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == n:
            return medio
        elif lista[medio] < n:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  

def busquedaRecursiva(lista, n, izquierda, derecha):
    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    if lista[medio] == n:
        return medio
    elif lista[medio] < n:
        return busquedaRecursiva(lista,n, medio + 1, derecha)
    else:
        return busquedaRecursiva(lista, n, izquierda, medio - 1)

print("Búsqueda Binarias")
lista = [3, 8, 12, 15, 20, 25, 30, 33, 40, 50]
print("Lista:", lista)

try:
    n = int(input("Escribe el número que deseas buscar: "))
    resul_Iter = busquedaIterativa(lista, n)
    if resul_Iter != -1:
        print("Iterativa - El numero se encuentra en la posición", resul_Iter)
    else:
        print("Iterativo - El numero no está en la lista")
        
    resul_Rec = busquedaRecursiva(lista, n, 0, len(lista) - 1)
    if resul_Rec != -1:
        print("Recursivo - El número se encuentra en la posición", resul_Rec)
    else:
        print("Recusrsivo - El número no está en la lista")

except ValueError:
    print("Error 404")