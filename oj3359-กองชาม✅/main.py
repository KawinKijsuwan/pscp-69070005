"""กองชาม"""
n = int(input())

sizes = []
for _ in range(n):
    sizes.append(int(input()))

most = 0
for s in set(sizes):
    if sizes.count(s) > most:
        most = sizes.count(s)

print(most)
