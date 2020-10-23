# Cuántos amigos a encuestar
numAmigos = int(input())
# Declaración del diccionario de juegos
juegos = {}
# Declaración del diccionario contador
contador = {}
# For que considera cuántos amigos encuestará
for i in range(numAmigos):
  # Lectura de juego y calificación
  juego = input()
  calificacion = float(input())
  # Acumulación de calificaciones para cada juego.
  if not juego in juegos:
    juegos[juego] = calificacion
    contador[juego] = 1
  else:
    juegos[juego] += calificacion
    contador[juego] += 1

promedios = {}
for i in juegos:
  promedio = juegos.get(i)/contador.get(i)
  promedios[i] = promedio

for j in promedios:
  if promedios.get(j) > 8.0:
    print(j)
