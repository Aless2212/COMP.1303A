class Perro:
    def __init__(self, nombre = " ", color = " ", edad = 0):
        self._nombre = nombre
        self._color = color
        self._edad = edad
        
p = Perro()
p._nombre = "Box"
print(p._nombre)
q = Perro("Matias", "Caramelo", 4)
print(q._nombre)