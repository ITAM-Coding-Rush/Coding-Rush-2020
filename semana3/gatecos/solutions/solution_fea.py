n=int(input()) #numero de lecturas
respuestas=[]

for i in range(n):
    k = int(input())#numero de pares de pokemones
    dict = {}
    for j in range(k):
        pokemon = input()
        cantidad = int(input())
        dict[pokemon]= cantidad
    respuestas.append(dict)

atrapados={}
probabilidades={}

m=int(input())
for i in range(m):
    pokemon = input()
    capturados = int(input())
    proba=float(input())
    atrapados[pokemon]= capturados
    probabilidades[pokemon]=proba

shinys={}
for x in respuestas:
    for p in x.keys():
        if p in shinys:
            shinys[p]+= x[p]
        else:
            shinys[p] = x[p]

for s in shinys.keys():
    prob_recibida=float(shinys[s]/atrapados[s])
    if(prob_recibida<probabilidades[s]):
        print(s,": ",prob_recibida)