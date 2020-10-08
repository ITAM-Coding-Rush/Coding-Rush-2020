n = int(input())
mat = input()
suma = 0

for i in range(n):
    calif = float(input())
    suma += calif
prom = suma/n
print("El promedio del examen de la materia "+mat+" es "+str(prom))
