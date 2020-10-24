import random

n = int(input())

capturados = {}
for i in range(n):
    k = int(input())
    for j in range(k):
        gateco = input()
        cuantos = int(input())
        if gateco in capturados:
            capturados[gateco] += cuantos
        else:
            capturados[gateco] = cuantos

m = int(input())
res = []
for i in range(m):
    gateco = input()
    tot = int(input())
    prob = float(input())
    if gateco in capturados:
        prob_real = capturados[gateco] / tot
        # NO CHECA NADA, SOLO OBTIENE PROBABILIDAD
        res += ["{}: {}".format(gateco, prob_real)]

random.shuffle(res)
print("\n".join(res))
