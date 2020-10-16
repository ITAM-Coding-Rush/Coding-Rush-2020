n = int(input())
for i in range(n):
    tweet = input()
    cars = len(tweet)
    cars += sum([1 if c == ' ' else 0 for c in tweet])
    if cars <= 140:
        print("Correcto")
    else:
        print("Incorrecto")
    print(cars)