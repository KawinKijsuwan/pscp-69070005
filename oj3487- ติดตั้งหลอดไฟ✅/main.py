"""ติดตั้งหลอดไฟ"""
n = int(input())

poles = []

for _ in range(n):
    poles.append(int(input()))

poles.sort()

total = 0
current_height = 0

for height in poles:
    current_height += height
    total += current_height * 2

print(total)
