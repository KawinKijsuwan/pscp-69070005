"""GCD_v2"""
a = int(input())
b = int(input())

while b:
    remainder = a % b
    a = b
    b = remainder

print(a)
