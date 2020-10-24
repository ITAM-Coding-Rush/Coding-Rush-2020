n = int(input())

juegos = []
for i in range(n):
    juego = input()
    calif = input()
    if not juego in juegos:
        juegos += [juego]

print("\n".join(juegos))