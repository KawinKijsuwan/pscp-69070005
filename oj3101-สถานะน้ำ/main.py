"""สถานะน้ำ"""
def main():
    """main"""  
    temp = float(input())
    unit = input().strip().upper()
    if unit == 'F':
        celsius = (temp - 32) * 5 / 9
    else:
        celsius = temp
    if celsius <= 0:
        print("solid")
    elif celsius >= 100:
        print("gas")
    else:
        print("liquid")
main()
