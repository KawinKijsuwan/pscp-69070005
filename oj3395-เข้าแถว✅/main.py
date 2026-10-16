"""เข้าแถว"""
n, l = map(int, input().split())

heights = list(map(int, input().split()))
customers = list(map(int, input().split()))

max_before = [0] * n
highest = 0
for i in range(n):
    max_before[i] = highest

    if heights[i] > highest:
        highest = heights[i]

answers = []

for position in customers:
    i = position - 1

    chair_height = max_before[i] - heights[i] + 1

    if chair_height < 0:
        chair_height = 0

    answers.append(chair_height)

print(*answers, sep="\n")
