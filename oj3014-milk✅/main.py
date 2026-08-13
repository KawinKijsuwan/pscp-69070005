"""Milk"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
bottles = d // a
total = bottles
caps = bottles
if b > 0 and c > 0:
    while caps >= b:
        exchange = caps // b
        gained = exchange * c
        total += gained
        caps = caps % b + gained

print(total)
