"""สามเหลี่ยม"""
n = int(input())
for i in range(n):
    for j in range(i+1):
        if j == 0 or i == n-1 or i == j:
            print("0", end="")
        else:
            print("1", end="")
    print()
