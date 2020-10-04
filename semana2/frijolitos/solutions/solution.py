n = int(input())
k = int(input())

A = [int(input()) for i in range(n)]

# Implementar el barrido
i = -1
suma = 0
ans = 0
for j in range(n):
    suma += A[j]
    while suma >= k and i < j:
        i += 1
        suma -= A[i]
    ans += j - i

print(ans)
