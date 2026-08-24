#สลับอักษรหน้าไปหลังเเละให้ตัวเเรกเป็นตัวใหญ่
"""user_input = input()
reverse_text = user_input[::-1]
first_upper = reverse_text[0].upper()
removefirsttext = reverse_text[1::]
print(f"{first_upper}{removefirsttext}")"""

"""Ra = int(input())
Rb = int(input())
Elo = str(input())
Ea = 1 / (1 + 10 ** ((Rb-Ra) / 400))
Eb = 1 / (1 + 10 ** ((Ra-Rb) / 400))
if Elo == "A":
    print(f"{Ea:.2f}")
elif Elo == "B":
    print(f"{Eb:2f}")"""

"""q1 = float(input())
q2 = float(input())
p1 = float(input())
p2 = float(input())
d = ((q1-p1)**2 + (q2-p2)**2)**0.5
print(d)"""

"""char = str(input())
digit = int(input())
if char == "H" and digit == 4567:
    print("safe unlocked")
elif char == "H":
    print("safe locked - change digit")
elif digit == 4567:
    print("safe locked - change char")
else:
    print("safe locked")"""

"""n = int(input())
fac = 1
for _ in range(1,n+1):
    fac *= _
print(fac)"""

"""n = int(input())
for _ in range(1,n+1):
    if not _ % 3 and not _ % 5:
            print("Fizz Buzz")
    elif not _ % 3:
        print("Fizz")
    elif not _ % 5:
        print("Buzz")
    else:
        print(_)"""

"""text = str(input())
sara = 0
bet = 0
for _ in text:
    if _ in ["a","e","i","o","u"]:
        sara += 1
    elif _.isalpha():
        bet += 1
print(sara)
print(bet)"""

"""text = input()
upper = text.upper()[3::]
lower = text.lower()[:3]
print(f"{upper}{lower}")"""

"""text = input()
print(text[::-2].upper())"""

"""money = int(input())
currency = input().upper()
change_currency = input().upper()

if currency == "THB":
    money_change = money
elif currency == "EUR":
    money_change = money * 38
elif currency == "USD":
    money_change = money * 35

if change_currency == "THB":
    print(money_change)
elif change_currency == "EUR":
    print(money_change / 38)
elif change_currency == "USD":
    print(money_change / 35)"""

"""n = int(input())
for i in range(n):
    for j in range(n):
        print("o", end="")
    print()"""

"""year = int(input())
year_thai = year + 543
if year < 0:
    print("Please insert number that is greater or equal zero")
else:
    print(year_thai)"""


"""text = input()
count_o = 0
for i in text:
    if i in "o":
        count_o += 1
print(count_o)"""

"""n = int(input())
fac = 1
for i in range(n):
    fac *= i+1
print(fac)"""


"""weight1,unit1 = input().split()
weight2,unit2 = input().split()
weight1 = float(weight1)
weight2 = float(weight2)

if unit1 == "g":
    new_weight1 = weight1
elif unit1 == "kg":
    new_weight1 = weight1 * 1000
elif unit1 == "lb":
    new_weight1 = weight1 * 453.59

if unit2 == "g":
    new_weight2 = weight2
elif unit2 == "kg":
    new_weight2 = weight2 * 1000
elif unit2 == "lb":
    new_weight2 = weight2 * 453.59

if new_weight1 > new_weight2:
    print("Item 1 is heavier")
elif new_weight1 < new_weight2:
    print("Item 2 is heavier")
else:
    print("Equal")"""


"""speed,unit = input().split()
speed = float(speed)

if unit == "km/h":
    new_speed = speed
elif unit == "mph":
    new_speed = speed * 1.609
elif unit == "m/s":
    new_speed = speed * 3.6
print(f"{new_speed:.2f} km/h")

if new_speed > 90:
    print("Over Speed")
elif new_speed < 90:
    print("Safe")"""


"""p = float(input())
r = float(input())
t = int(input())
com_type = str(input())

if com_type == "YEARLY":
    n = 1
elif com_type == "QUARTERLY":
    n = 4
elif com_type == "MONTHLY":
    n = 12

a = p*(1+(r/(100*n)))**(n*t)
print(f"{a:.2f}")
print(f"{a-p:.2f}")"""


"""q1 = float(input())
q2 = float(input())
p1 = float(input())
p2 = float(input())

d = abs(q1-p1) + abs(q2-p2)
print(d)"""


"""cx = float(input())
cy = float(input())
r = float(input())
x = float(input())
y = float(input())

d = ((x-cx)**2 + (y-cy)**2)**0.5
print(f"{d:.2f}")
if d < r:
    print("Inside")
elif d == r:
    print("On Circle")
else:
    print("Outside")"""

"""stamina = int(input())
while stamina > 0:
    stamina -= 1
    print("running...")
    if stamina == 0:
        print("ตายห่า")"""


n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n += 1
    print()





    
