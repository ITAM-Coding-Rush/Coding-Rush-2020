#leemos n y en un diccionario 
#decimos si el campo nos importa o no
#inicialmente ninguno nos importa
n = int(input())
meImporta = {}
for i in range(n):
  campo = input()
  meImporta[campo] = 0

#leemos m y actualizamos el valor de los que nos importan
m = int(input())
for i in range(m):
  campo = input()
  meImporta[campo] = 1

#contador representa nuestra respuesta
contador = 0
#leemos el total d aplicantes, y por cada uno
#vemos cuantos campos importantes llenó
s = int(input())
for i in range(s):
  camposImportantes = 0
  camposLlenados = int(input())

  for j in range(camposLlenados):
    campo = input()
    if(meImporta[campo] == 1):
      camposImportantes = camposImportantes + 1
  #si llenó todos los importantes, sí es candidato
  if(camposImportantes == m):
    contador = contador + 1

#imprimimos la respuesta
print(contador)