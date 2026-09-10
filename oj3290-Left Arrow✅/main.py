"""Left Arrow"""
k = int(input())
n = int(input())
for i in range(n):
    space = abs(i - n // 2)
    print(" " * space + "*" * k)
