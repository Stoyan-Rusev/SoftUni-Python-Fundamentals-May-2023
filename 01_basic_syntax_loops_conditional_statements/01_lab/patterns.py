stars = int(input())
for i in range(1, stars + 1):
    print(i * "*")
for j in range(stars - 1, 0, -1):
    print(j * "*")

number = int(input())
for i in range(number):
    for j in range(0, i + 1):
        print("*", end="")
    print()
for i in range(number - 1, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")
    print()
