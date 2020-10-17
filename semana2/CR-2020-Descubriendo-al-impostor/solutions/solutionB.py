n = int(input())

arr = [input() for i in range(n)]
impostor = [1 if "hm" in st else 0 for st in arr]

if sum(impostor) == 0:
    print("Javiercillo es el impostor")
elif sum(impostor) > 1:
    print("Skip")
else:
    idx = impostor.index(max(impostor))
    print("El jugador {} es el impostor".format(idx+1))
