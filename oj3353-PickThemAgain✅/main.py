"""PickThemAgain"""
n = input().split()
count = 0
for _ in n[::-1]:
    if not int(_) % 3 or not int(_) % 5:
        print(int(_))
        count += 1
if not count:
    print("Nope")
