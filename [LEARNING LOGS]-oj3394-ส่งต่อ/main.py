"""ส่งต่อ"""
n, s = map(int, input().split())

next_student = [0] + [int(input()) for _ in range(n)]

visited = [False] * (n + 1)
current = s
count = 0

while current and not visited[current]:
    visited[current] = True
    count += 1
    current = next_student[current]

print(count)
