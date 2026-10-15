"""Hint"""
def check(op, value, target):
    if op == "==":
        return value == target
    elif op == ">":
        return value > target
    elif op == "<":
        return value < target
    elif op == ">=":
        return value >= target
    elif op == "<=":
        return value <= target
    elif op == "!=":
        return value != target

line1 = input().split()
op_units = line1[0]
target_units = int(line1[1])

line2 = input().split()
op_tens = line2[0]
target_tens = int(line2[1])

line3 = input().split()
op_hundreds = line3[0]
target_hundreds = int(line3[1])

for n in range(1000):
    hundreds = n // 100
    tens = (n // 10) % 10
    units = n % 10

    if check(op_units, units, target_units) and check(op_tens, tens, target_tens) and check(op_hundreds, hundreds, target_hundreds):
        print(f"{n:03d}")
