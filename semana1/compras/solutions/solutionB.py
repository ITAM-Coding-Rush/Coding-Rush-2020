total = 0

precio = -1
while precio != 0:
    precio = int(input())
    total += precio

ans = total
if total >= 1000:
    ans -= total * 0.15
elif total >= 500:
    ans -= total * 0.1
elif total >= 250:
    ans -= total * 0.05

print("El precio total es: {}".format(round(ans, 2)))