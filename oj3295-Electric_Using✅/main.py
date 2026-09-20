"""Electic use"""
n = int(input())

if n <= 10:
    cost = n * 5
elif n <= 50:
    cost = 10 * 5 + (n - 10) * 7
elif n <= 100:
    cost = 10 * 5 + 40 * 7 + (n - 50) * 10
elif n <= 200:
    cost = 10 * 5 + 40 * 7 + 50 * 10 + (n - 100) * 12
else:
    cost = 10 * 5 + 40 * 7 + 50 * 10 + 100 * 12 + (n - 200) * 15

total_thousandths = cost * 1070 + n * 500

tenths = (total_thousandths + 50) // 100

baht = tenths // 10
frac = tenths % 10
print(f"{baht}.{frac}")
