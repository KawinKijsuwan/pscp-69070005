"""LastStand"""
"""line = input()
line = line.strip("[]")
items = line.split(",")

for i in items:
    print(i[-1])"""

import json
num = json.loads(input())
for i in num:
    i = str(i)
    print(i[-1])
