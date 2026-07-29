"""roman"""
def main():
    """roman"""
    user_numinput = int(input())
    if user_numinput == 1:
        print("I")
    elif user_numinput == 2:
        print("II")
    elif user_numinput == 3:
        print("III")
    elif user_numinput == 4:
        print("IV")
    elif user_numinput == 5:
        print("V")
    elif user_numinput == 6:
        print("VI")
    elif user_numinput == 7:
        print("VII")
    elif user_numinput == 8:
        print("VIII")
    elif user_numinput == 9:
        print("IX")
    elif user_numinput < 0:
        print("Error : Please input positive number")
    else:
        print("Error : Out of range")
main()
