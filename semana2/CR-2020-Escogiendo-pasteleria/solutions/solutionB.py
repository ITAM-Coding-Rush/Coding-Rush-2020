n = int(input())
lugares = [input() for i in range(n)]
arr = [1 if 'pastel' in lugar else 0 for lugar in lugares]

p = sum(arr)
if p > 15:
    print('Pedir por Rappi')
elif p > 0:
    print('Elegir personalmente')
else:
    print('Cocinar')
