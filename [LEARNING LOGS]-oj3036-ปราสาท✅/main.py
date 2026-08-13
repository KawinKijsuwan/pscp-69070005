"""ปราสาท"""
N = int(input())
r = int(N**0.5)
if r * r < N:
    r += 1
k = N - (r - 1) ** 2
if not k % 2:
    ans = 2 * r - 3
else:
    ans = 2 * r - 2
print(ans)
