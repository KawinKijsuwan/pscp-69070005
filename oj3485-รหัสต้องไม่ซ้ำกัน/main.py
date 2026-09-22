"""รหัสต้องไม่ซ้ำกัน"""
n = int(input())
result = []
for i in range(n):
    numlist = input().split()
    if numlist != numlist:
        numlist.append(result)
print(result)
