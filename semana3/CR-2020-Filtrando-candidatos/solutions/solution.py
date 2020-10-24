#leemos n 
#no nos importan realmente todos los campos
#pero aun así hay que leerlos
n = int(input())
for i in range(n):
  input()

#leemos m y guardamos en una lista los campos importantes
m = int(input())
importantes = [""]*m
for i in range(m):
  importantes[i] = input()

#contador representa nuestra respuesta
contador = 0
#leemos el total d aplicantes, y por cada uno
#vemos cuantos campos importantes llenó
s = int(input())
for i in range(s):
  importantesLlenados = 0
  camposLlenados = int(input())

  for j in range(camposLlenados):
    campo = input()
    if( campo in importantes):
      importantesLlenados = importantesLlenados + 1
  #si llenó todos los importantes, sí es candidato
  if(importantesLlenados == m):
    contador = contador + 1

#imprimimos la respuesta
print(contador)