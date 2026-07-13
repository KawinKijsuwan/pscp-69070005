"""season"""
def main():
    """main"""
    month = int(input())
    day = int(input())
    if month == 1 or 2 or 3:
        print("Winter")
    elif month % 3 ==0 and day > 21:
        print("Spring")
    