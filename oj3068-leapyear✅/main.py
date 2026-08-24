"""leapyear"""
year = int(input())

if year < 1582:
    if not year % 4:
        print("yes")
    else:
        print("no")
else:
    if (not year % 400) or (not year % 4 and year % 100):
        print("yes")
    else:
        print("no")
