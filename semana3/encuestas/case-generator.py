import random
import os
import itertools as it
from math import *

baseString = """
{N}
{criticas}
""".strip(' \t\n\r')

cases = 10

juegos = ['juego' + str(i) for i in range(1, 50)]


for i in range(cases):
    caseName = '{}.in'.format(i)

    n = random.randint(1, 10000)
    arr = []
    for i in range(n):
        juego = random.choice(juegos)
        calif = round(6 + round(random.random(), 2) * 4, 2)
        arr += [juego + '\n' + str(calif)]

    case = {
        'N': n,
        'criticas': "\n".join(arr)
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
