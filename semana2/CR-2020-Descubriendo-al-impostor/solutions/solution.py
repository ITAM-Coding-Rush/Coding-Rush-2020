n = int(input())

impostores = 0
PrimerSospechoso = 0

for i in range(n):
  frase = input()
  for j in range(len(frase)):
    if frase[int(j):int(j+2)] == 'hm':
      impostores += 1
      if PrimerSospechoso == 0:
        PrimerSospechoso = i + 1

if impostores == 0:
  print("Javiercito es el impostor")
elif impostores == 1:
  print("El jugador " + str(PrimerSospechoso) + " es el impostor")
else:
  print("Skip")
