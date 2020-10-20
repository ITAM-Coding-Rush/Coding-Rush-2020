linea = input()
spares = 0
strikes = 0
for c in linea:
	if c == '/':
		spares = spares + 1
	elif c == 'X':
		strikes = strikes + 1
if strikes >= spares:
  print("Gatica ha mejorado :D")
else:
  print("Gatica debe seguir practicando T.T")
