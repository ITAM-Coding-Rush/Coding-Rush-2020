canciones = [input() for _ in range(5)]
n = int(input())
arr = [input() for _ in range(n)]
best = input()
print(sum([1 if cancion == best else 0 for cancion in arr]))
