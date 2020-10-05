n = int(input())
k = int(input())

A = [int(input()) for i in range(n)]

ans = 0
for i in range(n):
    suma = 0
    for j in range(i, n):
        suma += A[j]
        if suma < k:
            ans += 1
        else:
            break

print(ans)
