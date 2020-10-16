import random
import os
import itertools as it
from math import *

baseString = """
{N}
{K}
{arreglo}
""".strip(' \t\n\r')

cases = 20

for i in range(cases):
    caseName = '{}.in'.format(i)

    n = random.randint(50000, 100000)
    if i < 5:
        n = random.randint(1, 100)
    elif i < 10:
        n = random.randint(100, 10000)
    k = random.randint(1, n * random.randint(1, 10000))

    arreglo = []

    for j in range(n):
        inf = int(k / n)
        sup = int(k / random.randint(1, n))
        x = random.randint(inf, sup)
        arreglo += [str(x)]

    case = {
        'N': str(n),
        'K': str(k),
        'arreglo': "\n".join(arreglo)
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
