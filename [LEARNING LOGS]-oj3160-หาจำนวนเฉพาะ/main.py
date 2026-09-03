"""หาจำนวนเฉพาะ"""
nums = input().split()
start = int(nums[0])
end = int(nums[1])

primes = []
count = 0

for num in range(start, end + 1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, num):
        if not num % i:
            is_prime = False
    if is_prime:
        primes.append(num)
        count = count + 1

result = ""
for i, p in enumerate(primes):
    if not i:
        result = str(p)
    else:
        result = result + " " + str(p)

if count > 0:
    print(result)
print("Total primes: " + str(count))
