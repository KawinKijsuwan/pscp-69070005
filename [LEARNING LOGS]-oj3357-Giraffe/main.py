"""Giraffe"""
n = int(input())
count = 0
height = []
for _ in range(n):
    height.append(int(input()))

for i in range(n):
    left = True
    right = True

    if i > 0 and height[i] < height[i - 1]:
        left = False
    if i < n - 1 and height[i] < height[i + 1]:
        right = False
    if left and right:
        count += 1
print(count)
