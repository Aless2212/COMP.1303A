def ordenamientoBurbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

a = [2, 8, 5, 3, 9, 4, 1]
ordenamientoBurbuja(a)
print(a)


def ordenamientoInsercion(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

a = [2, 8, 5, 3, 9, 4, 1]
ordenamientoInsercion(a)
print(a)