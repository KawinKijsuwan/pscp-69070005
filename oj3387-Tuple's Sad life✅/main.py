"""Tuple's Sad life"""
items = tuple(input().split())
target = input()

position = items.index(target)
count = items.count(target)

for _ in range(count):
    print(" ".join([str(position)] * count))
