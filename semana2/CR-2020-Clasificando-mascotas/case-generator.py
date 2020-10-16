import random as r
alfa = "abcdefghijklmnopqrstuvwxyz"
cases=20
for i in range(cases):
    nombre = "./cases/" + str(i)+".in"
    f = open(nombre, "w")
    n = r.randint(10,30)
    f.write(str(n) + "\n")
    for k in range(n):
        x = r.randint(1,10)
        b = ''
        for j in range(x):
            b+= alfa[r.randint(0,len(alfa)-1)]
        f.write(b + "\n")
    f.close()
