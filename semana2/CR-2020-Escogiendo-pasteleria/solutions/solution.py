n = int(input())
total = 0

for i in range(n):
    lugar = input()
    j = 0
    pastel = False
    while(j < len(lugar) and not pastel):
        if(lugar[int(j):int(j+6)] == 'pastel'):
            pastel = True
        j += 1
    if (pastel):
        total += 1

if(total < 1):
    print('Cocinar')
elif (total < 16):
    print('Elegir personalmente')
else:
    print('Pedir por Rappi')
