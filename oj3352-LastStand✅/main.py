"""LastStand"""
line = input()
line = line.strip("[]")
items = line.split(",")

for i in items:
    print(i[-1])
