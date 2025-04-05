votos_c1 = 0
votos_c2 = 0
votos_c3 = 0
votos_c4 = 0
total_votos = 0

print("Ingrese los votos (1-4), termine con 0:")

while True:
        try:
            voto = int(input("Voto: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if voto == 0:
            break
        elif voto == 1:
            votos_c1 += 1
            total_votos += 1
        elif voto == 2:
            votos_c2 += 1
            total_votos += 1
        elif voto == 3:
            votos_c3 += 1
            total_votos += 1
        elif voto == 4:
            votos_c4 += 1
            total_votos += 1
        else:
            print("Voto inválido. Solo se aceptan valores del 1 al 4.")


p1 = (votos_c1 / total_votos) * 100
p2 = (votos_c2 / total_votos) * 100
p3 = (votos_c3 / total_votos) * 100
p4 = (votos_c4 / total_votos) * 100

print("\nResultados:")
print(f"Candidato 1: {votos_c1} votos - {p1:.2f}%")
print(f"Candidato 2: {votos_c2} votos - {p2:.2f}%")
print(f"Candidato 3: {votos_c3} votos - {p3:.2f}%")
print(f"Candidato 4: {votos_c4} votos - {p4:.2f}%")