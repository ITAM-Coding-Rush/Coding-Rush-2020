n = int(input())
for i in range(n):
    tweet = input()
    cars = len(tweet)
    if cars <= 140:
        print("Correcto")
    else:
        print("Incorrecto")
    print(cars)
