"""สะสมเหรียญเวทย์มนตร์"""
n = int(input())
fire = 0
water = 0
earth = 0
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] >= a[3]:
        fire = fire + a[0]
    else:
        fire = fire + a[3]
    if a[1] >= a[4]:
            water = water + a[1]
    else:
        water = water + a[4]
    if a[2] >= a[5]:
            earth = earth + a[2]
    else:
        earth = earth + a[5]
total = fire + water + earth
print("Total:", total)
print("Fire:", fire)
print("Water:", water)
print("Earth:", earth)
if fire > water + earth:
    print("Bonus: YES")
else:
    print("Bonus: NO")
