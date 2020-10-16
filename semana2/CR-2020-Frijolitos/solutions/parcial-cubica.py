n = int(input())
k = int(input())

A = [int(input()) for i in range(n)]

ans = 0
for i in range(n):
    for j in range(i, n):
        if sum(A[i:j+1]) < k:
            ans += 1
        else:
            break

print(ans)
