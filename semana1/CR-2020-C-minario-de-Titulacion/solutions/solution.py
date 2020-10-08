c1 = int(input())
c2 = int(input())
c3 = int(input())

res = ""
c = 38 - c1 - c2 -c3

if (c <= 10):
  res = "Pablo será candidato a la mención honorífica si su calificación en Seminario de Titulación es de " + str(c) + "."
else: 
  res = "No hay poder humano que haga que Pablo obtenga su mención honorífica."

print(res)