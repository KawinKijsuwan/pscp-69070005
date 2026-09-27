"""pickthem"""
import json
num = json.loads(input())
even = []
for i in num:
    if not i % 2:
        even.append(i)
if even:
    for x in even:
        print(x)
else:
    print('Nope')
