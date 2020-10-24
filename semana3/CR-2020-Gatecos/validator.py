import sys

with open('data.out', 'r') as handle:
    res_oficial = handle.read()

lines_oficial = res_oficial.split('\n')
while len(lines_oficial) > 0 and lines_oficial[-1] == '':
    lines_oficial.pop()

res_contestant = sys.stdin.read()

lines_contestant = res_contestant.split('\n')
while len(lines_contestant) > 0 and lines_contestant[-1] == '':
    lines_contestant.pop()

lines_contestant.sort()
lines_oficial.sort()
print(1 if lines_oficial == lines_contestant else 0)
