suma = 0
total = 0
# Si se inicializara en 0 nunca entraría al ciclo.
precio = -1

while precio != 0:
    precio = int(input())
    suma = suma + n

if suma >= 250 and suma < 500:
    total = suma * 0.95
elif suma >= 500 and suma < 1000:
    total = suma * 0.9
elif suma >= 1000:
    total = suma * 0.85
else:
    total = suma
    
print("El precio total es: " + str(total))
