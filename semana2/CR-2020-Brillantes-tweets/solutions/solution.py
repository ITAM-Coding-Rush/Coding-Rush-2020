n = int(input())
con = 0
for i in range(n):
	con = 0
	t = input()
	for j in t:
		if j == ' ':
			con = con + 2
		else:
			con = con + 1
	if con <= 140:
		print("Correcto")
	else:
		print("Incorrecto")
	print(con)
