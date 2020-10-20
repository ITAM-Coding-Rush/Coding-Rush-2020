import random
import os
import itertools as it
from math import *

baseString = """
{cadena}
""".strip(' \t\n\r')

cases = 20

opciones = ['X', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(cases):
    caseName = '{}.{}.in'.format(i//2, i)

    n = random.randint(1, 100)
    arr = [random.choice(opciones) for i in range(n)]

    chuzas = sum([1 if c == 'X' else 0 for c in arr])
    spares = sum([1 if c == '/' else 0 for c in arr])

    if (chuzas >= spares and i % 2 == 1) or (chuzas < spares and i % 2 == 0):
        arr = [
            'X' if c == '/'
            else '/' if c == 'X'
            else c for c in arr
        ]

    case = {
        'cadena': "".join(arr)
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
