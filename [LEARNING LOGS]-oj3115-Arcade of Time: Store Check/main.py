"""arcade"""
a = [0] * 1441

x = input().split()
num = int(x[0])
check = int(x[1])

for i in range(num):
    x = input().split()

    start = int(x[0])
    stop = int(x[1])

    for j in range(start, stop):
        a[j] = a[j] + 1

x = input().split()

for i in range(check):
    time = int(x[i])
    print(a[time], end=" ")
