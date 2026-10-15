"""บุพเพสันนิวาส"""
name1 = input().strip().lower()
name2 = input().strip().lower()

if len(name1) < len(name2):
    name1 += name1[0] * (len(name2) - len(name1))
elif len(name2) < len(name1):
    name2 += name2[0] * (len(name1) - len(name2))

result = ""

for char1, char2 in zip(name1, name2):
    if char1 in "love" or char2 in "love":
        result += "w"
    else:
        result += "$"

COUNT_W = result.count("w")
longest = 0
current = 0

for char in result:
    if char == "w":
        current += 1
        longest = max(longest, current)
    else:
        current = 0

if COUNT_W % 2 == 1:
    result += str(longest)
elif "ww" not in result:
    result += "#"

print(result)
