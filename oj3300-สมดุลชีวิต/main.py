"""life go on"""
n = int(input())
days = 0
day_18 = 0

for _ in range(n):
    work_hours = int(input())
    if work_hours > 18:
        day_18 += 1
    else:
        days += 1
if days >= day_18 - 1:
    print(n)
else:
    print(n + (day_18 - 1 - days))
