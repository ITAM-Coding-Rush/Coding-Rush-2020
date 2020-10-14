import random
import os
import itertools as it
from math import *

baseString = """
{N}
{tweets}
""".strip(' \t\n\r')

nouns = ("  Puppy", "Car", "Rabbit ", "Girl        ", "Monkey")
verbs = ("runs", "hits  ", "jumps", "drives", "barfs  ")
adv = ("crazily .", "dutifully.", "foolishly.", "merrily.", "  occasionally. . .")
adj = ("adorable - ", "clueless,   ", "dirty;  ", "odd:", "  stupid")
l = [nouns, verbs, adj, adv]

cases = 10

for i in range(cases):
    caseName = '{}.in'.format(i)

    n = random.randint(1, 100)
    tweets = [' '.join([random.choice(i) for t in range(
        random.randint(1, 6)) for i in l]) for j in range(n)]

    case = {
        'N': str(n),
        'tweets': "\n".join(tweets)
    }

    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
