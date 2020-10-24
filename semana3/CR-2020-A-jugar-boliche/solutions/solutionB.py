linea = input()
spares = sum([1 if c == '/' else 0 for c in linea])
chuzas = sum([1 if c == 'X' else 0 for c in linea])
if chuzas >= spares:
    print("Gatica ha mejorado :D")
else:
    print("Gatica debe seguir practicando T.T")
