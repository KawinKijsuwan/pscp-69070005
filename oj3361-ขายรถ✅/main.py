"""ขายรถ"""
num = int(input())
P = []
V = []
count = 0
for i in range(num):
    p, v = map(int, input().split())
    P.append(p)
    V.append(v)

for i in range(num):
    for j in range(i + 1, num):
        if V[j] > V[i]:
            count += 1
            break
print(count)
