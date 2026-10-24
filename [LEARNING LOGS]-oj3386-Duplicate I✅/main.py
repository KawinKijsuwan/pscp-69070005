"""Duplicate"""
m = int(input())
n = int(input())
count = 0
list_m = []
list_n = []

for _ in range(m):
    students_m = input()
    list_m.append(int(students_m))

for _ in range(n):
    students_n = input()
    list_n.append(int(students_n))

list_m.sort(reverse=True)

for x in list_m:
    if x in list_n:
        print(x)
        count += 1

if not count:
    print("Nope")
