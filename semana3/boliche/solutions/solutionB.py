linea = input()
if sum([1 if c == 'X' else 0 for c in linea]) >= sum([1 if c == '/' else 0 for c in linea]):
    print("Gatica ha mejorado :D")
else:
    print("Gatica debe seguir practicando T.T")
