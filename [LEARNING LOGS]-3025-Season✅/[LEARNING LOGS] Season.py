"""season"""
def main():
    """main"""
    month = int(input())
    day = int(input())
    winter_month = (1,2,3)
    spring_month = (4,5,6)
    summer_month = (7,8,9)
    fall_month = (10,11,12)
    if day < 21:
        if month in winter_month:
            print("winter")
        elif month in spring_month:
            print("spring")
        elif month in summer_month:
            print("summer")
        elif month in fall_month:
            print("fall")
    else:
        if day >= 21:
            if month == 3:
                print("spring")
            elif month in (1,2):
                print("winter")
            elif month == 6:
                print("summer")
            elif month in (4,5):
                print("spring")
            elif month == 9:
                print("fall")
            elif month in (7,8):
                print("summer")
            elif month == 12:
                print("winter")
            elif month in (10,11):
                print("fall")
main()
