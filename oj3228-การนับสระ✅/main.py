"""การนับสระ"""
TEXT = str(input())
count_vowels = 0
for _ in TEXT:
    if _ in ["a","e","i","o","u"]:
        count_vowels += 1
print(count_vowels)
