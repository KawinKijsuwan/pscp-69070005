"""suvanna"""
a = input().split(".")
b = input().split(".")

h1 = int(a[0])
m1 = int(a[1])
h2 = int(b[0])
m2 = int(b[1])

if h1 < 0 or h1 > 23 or h2 < 0 or h2 > 23:
    print("ERROR")
elif m1 < 0 or m1 > 59 or m2 < 0 or m2 > 59:
    print("ERROR")
else:
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2

    if t2 < t1:
        print("ERROR")
    else:
        t = t2 - t1

        if t <= 15:
            print("FREE")
        elif t <= 60:
            print(25)
        elif t <= 120:
            print(50)
        elif t <= 180:
            print(80)
        elif t <= 240:
            print(110)
        elif t <= 300:
            print(145)
        elif t <= 360:
            print(180)
        elif t <= 1440:
            print(250)
        else:
            print("ERROR")
