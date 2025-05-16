class Objeto:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso
        self.valor_por_peso = valor / peso

    def __repr__(self):
        return f"(Valor: {self.valor}, Peso: {self.peso}, V/P: {self.valor_por_peso:.2f})"

def mochila_fraccionaria_voraz(objetos, capacidad):
    objetos_ordenados = sorted(objetos, key=lambda o: o.valor_por_peso, reverse=True)

    print("\nObjetos ordenados por valor/peso:")
    for o in objetos_ordenados:
        print(o)

    valor_total = 0.0
    for obj in objetos_ordenados:
        if capacidad == 0:
            break
        if obj.peso <= capacidad:
            capacidad -= obj.peso
            valor_total += obj.valor
            print(f"Se toma TODO el objeto: {obj}")
        else:
            fraccion = capacidad / obj.peso
            valor_total += obj.valor * fraccion
            print(f"Se toma {fraccion:.2f} del objeto: {obj}")
            capacidad = 0

    print(f"\n Valor total en la mochila: {valor_total:.2f}")
    return valor_total

objetos = []
n = int(input("¿Cuántos objetos quieres ingresar? "))

for i in range(n):
    print(f"\nObjeto {i+1}:")
    valor = float(input("  Valor: "))
    peso = float(input("  Peso: "))
    objetos.append(Objeto(valor, peso))

capacidad_mochila = float(input("\n¿Cuál es la capacidad de la mochila? "))

mochila_fraccionaria_voraz(objetos, capacidad_mochila)