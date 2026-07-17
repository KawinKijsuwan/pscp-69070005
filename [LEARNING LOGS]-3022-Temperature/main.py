"""Temperature"""
def main():
    """Temperature"""
    tem = int(input())
    unit = input()
    change_unit = input()
    if unit == "C" and change_unit == "F":
        print(unit*9/5+32)
main()
