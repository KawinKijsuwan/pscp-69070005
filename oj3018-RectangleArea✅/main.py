"""RectangleArea"""
a = input().split()
x1 = int(a[0])
y1 = int(a[1])
w1 = int(a[2])
h1 = int(a[3])
b = input().split()
x2 = int(b[0])
y2 = int(b[1])
w2 = int(b[2])
h2 = int(b[3])
left = max(x1, x2)
right = min(x1 + w1, x2 + w2)
bottom = max(y1, y2)
top = min(y1 + h1, y2 + h2)
if left < right and bottom < top:
    print((right - left) * (top - bottom))
else:
    print("no overlapping")
