"""ค่าtaxi"""
distance = int(input())
price = 0

if not distance:
    price = 0
elif distance <= 1:
    price = 35
elif distance <= 10:
    price = 35 + (distance - 1) * 5
else:
    price = 35 + 45 + (distance - 10) * 8

print(price)
