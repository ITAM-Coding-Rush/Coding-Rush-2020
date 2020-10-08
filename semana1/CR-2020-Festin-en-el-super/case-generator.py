import random
import os
import itertools as it
from math import *

baseString = """
{arreglo}
0
""".strip(' \t\n\r')

cases = 12
prices = [0, 250, 500, 1000, 2000]

for i in range(cases):
    caseName = '{}.in'.format(i+6)

    idx = i // 4
    low, high = prices[idx], prices[idx+1]

    suma = random.randint(low + 1, high - 1)
    if ((i % 3) == 1):
        suma = low
    elif ((i % 3) == 2):
        suma = high-1

    arreglo = []
    s = 0
    while s < suma:
        x = random.randint(1, random.randint(1, min(1000,suma - s)))
        arreglo += [str(x)]
        s += x

    case = {
        'arreglo': "\n".join(arreglo)
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
