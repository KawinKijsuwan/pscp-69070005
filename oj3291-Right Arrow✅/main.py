"""Right Arrow"""
k = int(input())
n = int(input())
middle = n // 2
for i in range(n):
    space = middle - abs(middle-i)
    print(" " * space + "*" * k)
