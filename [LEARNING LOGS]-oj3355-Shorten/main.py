"""shorten"""
nums = []
while True:
    x = int(input())
    if x == -1:
        break
    nums.append(x)

parts = []
start = nums[0]
prev = nums[0]

for i in range(1, len(nums)):
    if nums[i] == prev + 1:
        prev = nums[i]
    else:
        if start == prev:
            parts.append(str(start))
        else:
            parts.append(str(start) + "-" + str(prev))
        start = nums[i]
        prev = nums[i]

if start == prev:
    parts.append(str(start))
else:
    parts.append(str(start) + "-" + str(prev))

print(", ".join(parts))
