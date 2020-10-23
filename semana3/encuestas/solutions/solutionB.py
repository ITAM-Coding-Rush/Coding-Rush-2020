n = int(input())
suma = {}
count = {}

for i in range(n):
    juego = input()
    calif = float(input())
    if not juego in suma:
        suma[juego] = 0
        count[juego] = 0
    suma[juego] += calif
    count[juego] += 1

res = []

for juego in suma:
    if suma[juego] / count[juego] >= 8.0:
        res += [juego]

res.sort()
print("\n".join(res))