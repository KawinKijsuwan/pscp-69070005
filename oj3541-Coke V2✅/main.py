"""Cokev2"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if not b:
    print(d * a)
elif not d:
    print(0)
else:
    discount = (d - 1) // b
    notdiscount = d - discount
    print(notdiscount * a + discount * c)
