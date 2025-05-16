import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0

equipo1 = Equipo("Joaquin")
equipo2 = Equipo("Chino")

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido(NuPartido):
    setGanados1 = 0
    setGanados2 = 0
    puntosTotales1 = 0
    puntosTotales2 = 0
    puntosExtras1 = 0
    puntosExtras2 = 0
    n_Set = 1
    while setGanados1 < 3 and setGanados2 < 3:
        puntos1 = Puntos()
        puntos2 = Puntos()
        puntosTotales1 += puntos1
        puntosTotales2 += puntos2
        if puntos1 >= 25 or puntos2 >= 25:
            if puntos1 > puntos2:
                print(f"{n_Set}er set ganó el equipo {equipo1.nombre} con {puntos1} puntos")
                setGanados1 += 1
            else:
                print(f"{n_Set}er set ganó el equipo {equipo2.nombre} con {puntos2} puntos")
                setGanados2 += 1
        else:
            while True:
                extra1 = PuntosExtras()
                extra2 = PuntosExtras()
                puntos1 += extra1
                puntos2 += extra2
                puntosExtras1 += extra1
                puntosExtras2 += extra2
                if puntos1 > puntos2 and puntos1 > 25:
                    print(f"{n_Set}er set ganó el equipo {equipo1.nombre} con {puntos1} puntos (teniendo {extra1} puntos extra)")
                    setGanados1 += 1
                    break
                elif puntos2 > puntos1 and puntos2 > 25:
                    print(f"{n_Set}er set ganó el equipo {equipo2.nombre} con {puntos2} puntos (teniendo {extra2} puntos extra)")
                    setGanados2 += 1
                    break
        n_Set += 1
    if setGanados1 == 3:
        equipo1.partidosGanados += 1
        equipo2.partidosPerdidos += 1
        print(f"\n{equipo1.nombre} gana el partido {NuPartido} con un total de {puntosTotales1 + puntosExtras1} puntos (teniendo {puntosExtras1} puntos extra)\n")
    else:
        equipo2.partidosGanados += 1
        equipo1.partidosPerdidos += 1
        print(f"\n{equipo2.nombre} gana el partido {NuPartido} con un total de {puntosTotales2 + puntosExtras2} puntos (teniendo {puntosExtras2} puntos extra)\n")

def ResultadoTorneo():
    print("RESULTADOS:")
    print(f"{equipo1.nombre}: {equipo1.partidosGanados} ganados, {equipo1.partidosPerdidos} perdidos")
    print(f"{equipo2.nombre}: {equipo2.partidosGanados} ganados, {equipo2.partidosPerdidos} perdidos")

totalPartidos = int(input("¿Cuántos partidos deben jugar los equipos?: "))
for i in range(totalPartidos):
    print(f"\n--- Partido {i + 1} ---")
    JugarPartido(i + 1)
ResultadoTorneo()