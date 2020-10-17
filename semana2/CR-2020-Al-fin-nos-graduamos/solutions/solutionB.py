s = input()
arr = [1 if c == 'A' else 0 for c in s]
if sum(arr) >= 0.8*len(arr):
    print("G")
else:
    print("F")
