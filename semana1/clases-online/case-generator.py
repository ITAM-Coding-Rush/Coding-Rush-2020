import random
import os
import itertools as it
from math import *

baseString = """
{N}
{arreglo}
""".strip(' \t\n\r')

cases = 24

for i in range(cases):
    caseName = '{}.in'.format(i)

    horas = i
    arreglo = []
    s = 0
    while s < horas:
        x = random.randint(1, random.randint(1, min(24, horas - s)))
        arreglo += [str(x)]
        s += x
    

    case = {
        'N': len(arreglo),
        'arreglo': "\n".join(arreglo)
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
