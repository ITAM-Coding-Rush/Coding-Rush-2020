n = int(input())
W=X=Y=Z=0
for i in range(n):
    mascota = input()
    if len(mascota) <= 5:
        if 'a' in mascota or 'y' in mascota:
            X += 1
        else:
            W += 1
    else:
        if 'a' in mascota or 'y' in mascota:
            Z += 1
        else:
            Y += 1

print("Tiene "+str(W)+" perros macho")
print("Tiene "+str(X)+" perros hembra")
print("Tiene "+str(Y)+" gatos macho")
print("Tiene "+str(Z)+" gatos hembra")
