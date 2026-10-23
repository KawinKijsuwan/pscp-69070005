"""Calculator V2"""
def main():
    """main"""
    n = int(input())

    digits = 0
    low = 1
    length = 1
    while low <= n:
        high = min(n, low * 10 - 1)
        digits += (high - low + 1) * length
        low *= 10
        length += 1

    press = digits + max(n, 0)

    if n == 1:
        print(1)
    else:
        print(press)


main()
