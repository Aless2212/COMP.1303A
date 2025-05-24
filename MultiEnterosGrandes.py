def contar_digitos(n):
    return len(str(abs(n)))
def multi_directa(a, b):
    return a * b
def multi_recursiva(a, b):
    if a == 0 or b == 0:
        return 0
    n = max(contar_digitos(a), contar_digitos(b))
    if n <= 1:
        return multi_directa(a, b)
    n = n // 2
    base = 10 ** n
    
    a_izq = a // base
    a_der = a % base
    b_izq = b // base
    b_der = b % base
    
    parte1 = multi_recursiva(a_izq, b_izq)
    parte2 = multi_recursiva(a_izq, b_der)
    parte3 = multi_recursiva(a_der, b_izq)  
    parte4 = multi_recursiva(a_der, b_der)
    resultado = (parte1 * (10 ** (2 * n))) + ((parte2 + parte3) * base) + parte4
    return resultado

try:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    resultado = multi_recursiva(num1, num2)
    print("Resultado:", resultado)
    
except ValueError:
    print("Por favor, ingresa números enteros válidos.")