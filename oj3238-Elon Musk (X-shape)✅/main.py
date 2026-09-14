"""Elon Musk (X-shape)"""
x, k = input().split()
x = int(x)

middle = x // 2

for row in range(x):
    line = ""

    for col in range(x):
        if row == col or row + col == x - 1:
            if k == "#":
                line += "#"
            else:
                line += chr(ord(k) + abs(row - middle))
        else:
            line += "-"

    print(line)
