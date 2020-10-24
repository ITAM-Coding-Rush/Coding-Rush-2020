#entero que representa cuantos renglones vas a leer
n = int(input())

#cadena vacia para concatenar el nuevo mensaje
s = ""

for i in range(n):
  #lee el mensaje del profesor
  m = input()
  if (m[0] == '0'):
    for c in range(1, len(m)):
      s = s + m[c]
  else:
    for c in range(len(m)-1, 0, -1):
      s = s + m[c]

print(s)
