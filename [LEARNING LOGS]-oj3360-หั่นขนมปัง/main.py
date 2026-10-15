"""ขนมปัง"""
first = input().split()
W = int(first[0])
H = int(first[1])

xs = input().split()
ys = input().split()

widths = []
prev = 0
for x in xs:
    x = int(x)
    widths.append(x - prev)
    prev = x
widths.append(W - prev)

heights = []
prev = 0
for y in ys:
    y = int(y)
    heights.append(y - prev)
    prev = y
heights.append(H - prev)

widths.sort(reverse=True)
heights.sort(reverse=True)

biggest = widths[0] * heights[0]

option1 = widths[0] * heights[1]
option2 = widths[1] * heights[0]
if option1 > option2:
    second = option1
else:
    second = option2

print(biggest, second)
