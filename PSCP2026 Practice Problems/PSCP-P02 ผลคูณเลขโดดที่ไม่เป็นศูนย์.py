"""PSCP-P02 ผลคูณเลขโดดที่ไม่เป็นศูนย์"""
num = input()
plus = 1
count = 0
for i in num:
    if i != "0":
        number = int(i)
        plus = number * plus
        count += 1
if count > 0:
    print(plus)
else:
    print(0)
