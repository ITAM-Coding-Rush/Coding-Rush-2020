lc = {}
c=5
for i in range(c):
        nombre = input()
        lc[nombre]=0
n = int(input())
for i in range(n):
        nom = input()
        lc[nom] = lc[nom] + 1
fav = input()
print(lc[fav])