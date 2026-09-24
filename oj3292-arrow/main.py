"""Arrow"""
directions = input()
n = int(input())

for x in range(len(directions)):
    d = directions[x]

    for i in range(n):
        stars = n - i
        if d == "R":
            spaces = i * 2
        else:
            spaces = n - 1 - i
        print(" " * spaces + "*" * stars)

    for i in range(n - 2, -1, -1):
        stars = n - i
        if d == "R":
            spaces = i * 2
        else:
            spaces = n - 1 - i
        print(" " * spaces + "*" * stars)

    if x < len(directions) - 1:
        print()
