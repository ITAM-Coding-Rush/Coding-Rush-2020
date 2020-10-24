n = int(input())  # numero de lecturas

shinys = {}
for i in range(n):
    k = int(input())  # numero de pares de pokemones
    for j in range(k):
        pokemon = input()
        cantidad = int(input())
        if pokemon in shinys:
            shinys[pokemon] += cantidad
        else:
            shinys[pokemon] = cantidad

m = int(input())
for i in range(m):
    pokemon = input()
    capturados = int(input())
    proba = float(input())

    if pokemon in shinys:
        prob_recibida = float(shinys[pokemon] / capturados)
        if (prob_recibida < proba):
            print(pokemon+": "+str(prob_recibida))
