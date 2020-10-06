nHoras = int(input())

mHoras = 0
for i in range(nHoras):
    mHoras += int(input())

if mHoras >= 20:
    print('Sacaras 10')
elif mHoras >= 15:
    print('Sacaras 9')
elif mHoras >= 12:
    print('Sacaras 8')
elif mHoras >= 10:
    print('Sacaras 7')
elif mHoras >= 8:
    print('Sacaras 6')
else:
    print('Reprobaras')
