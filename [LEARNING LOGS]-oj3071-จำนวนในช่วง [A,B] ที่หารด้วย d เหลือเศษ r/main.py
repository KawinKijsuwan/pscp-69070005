"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
def main():
    """main"""
    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())
    count = 0
    for _ in range(A,B + 1):
        if _ % d == r:
            count += 1
    print(count)
main()
