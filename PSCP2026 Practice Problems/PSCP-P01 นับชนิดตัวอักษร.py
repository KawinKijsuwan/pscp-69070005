"""PSCP-P01 นับชนิดตัวอักษร"""
text = input()
text_upper = 0
text_lower = 0
num = 0

for char in text:
    if char.isdigit() :
        num += 1
    if char.isupper():
        text_upper += 1
    if char.islower():
        text_lower += 1
print(text_upper,text_lower,num)
