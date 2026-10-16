"แซงรอบ"
n, k = map(int, input().split())

times = []

for _ in range(n):
    times.append(int(input()))

fastest = min(times)
survivors = 0

for time in times:
    if (k - 1) * time < k * fastest:
        survivors += 1

print(survivors)
