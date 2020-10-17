n = int(input())
lugares = [input() for i in range(n)]
arr = [1 if 'pastel' else 0 in lugar for lugar in lugares]

p = sum(arr)
if p > 15:
    print('Pedir por Rappi')
elif p > 0:
    print('Elegir personalmente')
else:
    print('Cocinar')
