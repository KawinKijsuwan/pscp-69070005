"""กบน้อยกระโดด"""
x,y = map(int,input().split())
total = 0
count = 0

while total < y and x > 0:
    total += x
    count += 1
    x -= 2

if total >= y:
    print(count)
else:
    print(-1)
