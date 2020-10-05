n = int(input())
k = int(input())

A = [int(input()) for i in range(n)]

# Implementar el barrido
j = -1
suma = 0
ans = 0
for i in range(n):
    if j < i:
        j = i
        suma = A[j]

    while j < n-1 and suma < k:
        j += 1
        suma += A[j]

    if suma >= k:
        suma -= A[j]
        j -= 1

    ans += j - i + 1
    suma -= A[i]

print(ans)
