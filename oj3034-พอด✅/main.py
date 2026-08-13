"""พอด"""
n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
count = [0] * (k + 1)
for i in range(n):
    row = int(input())
    count[row] += 1
trips = count[1]
for i in range(2, k + 1):
    if count[i] < trips:
        trips = count[i]
taken = trips * k
remaining = n - taken
print(remaining)
