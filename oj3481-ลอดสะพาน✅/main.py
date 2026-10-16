"""ลอดสะพาน"""
l, n = map(int, input().split())

events = [0] * (l + 1)

for _ in range(n):
    a, b = map(int, input().split())
    events[a] += 1
    events[b] -= 1

current_bridges = 0
maximum_bridges = 0

for position in range(l + 1):
    current_bridges += events[position]

    if current_bridges > maximum_bridges:
        maximum_bridges = current_bridges

print(maximum_bridges)
