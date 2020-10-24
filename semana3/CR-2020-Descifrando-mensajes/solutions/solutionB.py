n = int(input())
res = ""
for i in range(n):
    mensaje = input()
    if mensaje[0] == '1':
        res += mensaje[len(mensaje):0:-1]
    else:
        res += mensaje[1:]
print(res)
