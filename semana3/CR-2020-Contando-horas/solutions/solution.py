semana = {'Lunes': 0, 'Martes': 0, 'Miercoles': 0,
          'Jueves': 0, 'Viernes': 0, 'Sabado': 0, 'Domingo': 0}
n = int(input())
totalH = 0
for i in range(n):
  dia = input()
  escuela = int(input())
  semana[dia] += escuela
  divagar = int(input())
  totalH += escuela - divagar
semAnt = int(input())
if(totalH > semAnt):
  print('Sigue así, intenta mejorar tu marca de esta semana: ' + str(totalH))
elif totalH == semAnt:
  print('No has mejorado, pero tampoco empeorado. Esfuérzate un poco más')
else:
  faltante = semAnt - totalH
  print('Te quedaste atras por: ' + str(faltante))
  for i in range(3):
    dia = input()
    print('El día ' + dia + ' invertiste un total de: ' +
          str(semana[dia]) + ' horas')
