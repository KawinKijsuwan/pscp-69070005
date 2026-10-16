"""ไฟส่อง"""
n = int(input())

light = [False] * 360

for _ in range(n):
    a, b = map(int, input().split())
    while a != b:
        light[a] = True
        a = (a + 1) % 360
if False not in light:
    print(360)

else:
    longest = 0
    current = 0
    for i in range(720):
        if light[i % 360]:
            current += 1

            if current > longest:
                longest = current
        else:
            current = 0

    print(longest)
