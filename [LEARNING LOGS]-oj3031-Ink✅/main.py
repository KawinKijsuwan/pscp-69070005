"""ink"""
data = input().split()
S = int(data[0])
N = int(data[1])
for _ in range(N):
    pos = input().split()
    x = int(pos[0])
    y = int(pos[1])
    area = 3.1416 * (x * x + y * y)
    time = area / S
    ans = int(time)
    if time > ans:
        ans += 1
    print(ans)
