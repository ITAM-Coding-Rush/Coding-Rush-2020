import random
import os
import itertools as it
from math import *

baseString = """
{N}
{materia}
{arreglo}
""".strip(' \t\n\r')

cases = 20

materias = ["Bases de Datos", "Ing. en Software", "Sistemas de Comercio",
            "Ideas I", "Ideas II", "Calculo I", "ADSI", "Algoritmos y programas"]

for i in range(cases):
    caseName = '{}.in'.format(i)

    N = random.randint(1, 100000)
    materia = random.choice(materias)
    low = random.randint(0, random.randint(0, 10))
    arreglo = [str(round(low + random.random() * (10-low), 2)) for _ in range(N)]

    case = {
        'N': str(N),
        "materia": materia,
        'arreglo': "\n".join(arreglo)
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
