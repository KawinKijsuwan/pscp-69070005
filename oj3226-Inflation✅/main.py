"""Inflation"""
n = float(input())
k = int(input())

satang = round(n * 100)

for _ in range(k):
    satang = satang * 10381 // 10000

baht = satang // 100
cents = satang % 100
print(f"{baht}.{cents:02d}")
