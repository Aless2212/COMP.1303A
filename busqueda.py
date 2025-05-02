def ordseleccion(arr):
    for mano in range(len(arr)-1):
        posmin = mano
        for ojo in range(mano + 1, len(arr)):
            if arr[ojo] < arr[posmin]:
                posmin = ojo
        arr[mano], arr[posmin] = arr[posmin], arr[mano]
            
a = [2, 8, 5, 3, 9, 4, 1]
ordseleccion(a)
print(a)



for i: to 