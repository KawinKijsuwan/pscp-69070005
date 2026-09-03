"""ของขวัญ"""
line = input().split()
n = int(line[0])
k = int(line[1])
t = int(line[2])

pos = 1
count = 1

if pos == t:
    print(count)
else:
    while True:
        pos = pos + k
        if pos > n:
            pos = pos - n
        count = count + 1
        if pos == 1:
            count = count - 1
            break
        if pos == t:
            break
    print(count)
