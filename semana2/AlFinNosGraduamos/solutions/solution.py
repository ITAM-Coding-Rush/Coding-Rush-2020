#Lectura de calificaciones
calificaciones = input()

numMaterias = len(calificaciones)
minMaterias = numMaterias*0.8

contador=0
for calif in calificaciones:
  if calif=='A':
    contador+=1

if contador >=minMaterias:
  print("G")
else:
  print("F")