n = int(input())
arr = [0, 0, 0, 0, 0, 0]

for e in range(0, n):
    nom = input()
    tamaño = len(nom)
    cont = 0
    val = 0
    for i in nom:
        if i == "a" or i == 'y':
            cont = cont + 1
    if cont > 0:
        val = 2
    else:
        val = 1
    if tamaño > 5:
        val = val + 2
    arr[val-1] = arr[val-1] + 1

print("Tiene "+str(arr[0])+" perros macho")
print("Tiene "+str(arr[1])+" perros hembra")
print("Tiene "+str(arr[2])+" gatos macho")
print("Tiene "+str(arr[3])+" gatos hembra")
