"""Difference"""
n = int(input())
A = set()
m = int(input())
B = set()

for _ in range(n):
    set_a = int(input())
    A.add(set_a)
for _ in range(m):
    set_b = int(input())
    B.add(set_b)
print(*sorted(A-B))
