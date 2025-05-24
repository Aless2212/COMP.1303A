def mergesort(a):
    if len(a) == 1:
        return a
    
    medio = len(a) // 2
    arrayOne = a[:medio] # Slice izquierdo
    arrayTwo = a[medio:] # Slice derecho
    arrayOne = mergesort(arrayOne)
    arrayTwo = mergesort(arrayTwo)

    return merge(arrayOne, arrayTwo)

def merge(a, b):
    c = [] #Array Salida
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    
    while len(a) > 0:
        c.append(a[0])
        a.pop(0)
        
    while len(b) > 0:
        c.append(b[0])
        b.pop(0)
        
    return c

# Main
lista = [2, 5, 4, 9, 12, 15, 20, 8]
en_orden = mergesort(lista)
print("Lista Original:", lista)
print("Lista Ordenada:", en_orden)