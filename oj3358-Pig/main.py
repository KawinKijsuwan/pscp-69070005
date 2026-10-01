"""pig"""
n = int(input())

weights = list(map(int, input().split()))
max_weights = []

for i in range(n):
    w1 = weights[i * 2]
    w2 = weights[i * 2 + 1]
    max_weights.append(max(w1, w2))

if n == 1:
    print(max_weights[0])
else:
    EQUATION = " + ".join(map(str, max_weights))
    total_sum = sum(max_weights)
    print(f"{EQUATION} = {total_sum}")
