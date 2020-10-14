import random as r
alfa = "abcdefghijklmnopqrstuvwxyz"
cases=20
for i in range(cases):
    nombre = "./cases/" + str(i)+".in"
    f = open(nombre, "w")
    if i < 15:
        n = r.randint(10,30)
    else:
        n = r.randint(60,100)
    f.write(str(n) + "\n")
    for k in range(n):
        if i < 15:
            x = r.randint(1,10)
        else:
            x = r.randint(20000,100000)
        b = ''
        for j in range(x):
            b+= alfa[r.randint(0,len(alfa)-1)]
        f.write(b + "\n")
    f.close()
