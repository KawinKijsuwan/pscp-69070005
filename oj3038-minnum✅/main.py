"""minnum"""
def main():
    """minxnum"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    min_num = num1
    if num2 < min_num:
        min_num = num2
    if num3 < min_num:
        min_num = num3
    print(min_num)
main()
