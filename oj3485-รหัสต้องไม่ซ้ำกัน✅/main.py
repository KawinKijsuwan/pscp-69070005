"""รหัสต้องไม่ซ้ำกัน"""
n = int(input())
nums = []
for x in input().split():
    nums.append(int(x))

result = []
for x in nums:
    if nums.count(x) == 1:
        result.append(x)

result.sort()
print(*result)
