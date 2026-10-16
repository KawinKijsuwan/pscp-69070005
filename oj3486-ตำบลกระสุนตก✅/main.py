"""ตำบลกระสุนตก"""
n = int(input())

shots = []

for _ in range(n):
    x, y, d = map(int, input().split())
    shots.append((x, y, d))

x0, y0, d0 = shots[0]
candidates = []
for dx in range(-d0, d0 + 1):
    remain = d0 * d0 - dx * dx

    if remain < 0:
        continue

    dy = int(remain ** 0.5)
    while (dy + 1) * (dy + 1) <= remain:
        dy += 1

    while dy * dy > remain:
        dy -= 1

    if dy * dy == remain:
        candidates.append((x0 + dx, y0 + dy))

        if dy:
            candidates.append((x0 + dx, y0 - dy))
for tx, ty in candidates:
    correct = True

    for x, y, d in shots:
        distance_squared = (tx - x) * (tx - x) + (ty - y) * (ty - y)

        if distance_squared != d * d:
            correct = False
            break

    if correct:
        print(tx, ty)
        break
