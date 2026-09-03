"""prime number"""
first_last = input().split()
first =  int(first_last[0])
last =  int(first_last[1])
list_num = []
for r in range(first ,last + 1):
    if r <= 1:
        continue
    for i in range(2,r):
        if not r % i :
            break
    else:
        list_num.append(r)
if len(list_num) > 0:
    print(list_num)
print(f"Total primes: {len(list_num)}")
