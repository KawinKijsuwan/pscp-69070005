"""Pro"""
def main():
    """main"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    groups = z // x
    remainder = z % x
    people_to_pay = groups * y + remainder
    print(people_to_pay * a)
main()
