"""นวัตกรรม"""
name = input().strip()

ascii_first = ord(name[0].upper())
ascii_last = ord(name[-1].upper())
length = len(name)

level1 = []
for pos in range(1, 11):
    place_value = pos - 1
    if pos % 2 != 0:
        val = ascii_first + place_value
    else:
        val = ascii_last - place_value
    level1.append(val)

level2 = []
for val in level1:
    r = val % length
    if r > 9:
        r = r % 10
    level2.append(r)

password = level2[2:8]
print(" ".join(str(d) for d in password))
