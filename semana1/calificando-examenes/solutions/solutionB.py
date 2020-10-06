n = int(input())
materia = input()
A = []
for i in range(n):
    A += float(input())

print("El promedio del examen de la materia {} es {}".format(materia, str(sum(A) / n)))
