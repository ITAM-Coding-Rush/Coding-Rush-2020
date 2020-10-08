n = int(input())

H = []
for i in range(n):
    H += [int(input())]

suma = sum(H)
ans = "Sacaras {}"
if suma < 8:
    ans = "Reprobaras"
elif suma < 10:
    ans = ans.format(6)
elif suma < 12:
    ans = ans.format(7)
elif suma < 15:
    ans = ans.format(8)
elif suma < 20:
    ans = ans.format(9)
else:
    ans = ans.format(10)

print(ans)