"""ชานมไข่มุก"""
def main():
    """main"""
    pearl = input().split()
    tea = input().split()

    pearl_type = pearl[0]
    pearl_weight = float(pearl[1])

    tea_type = tea[0]
    sweet_level = int(tea[1])
    tea_volume = float(tea[2])

    if pearl_type == 'H':
        pearl_cal = 5
    elif pearl_type == 'O':
        pearl_cal = 3
    else:
        pearl_cal = 2

    if tea_type == 'R':
        if sweet_level == 1:
            tea_cal = 12
        elif sweet_level == 2:
            tea_cal = 18
        else:
            tea_cal = 25
    elif tea_type == 'T':
        if sweet_level == 1:
            tea_cal = 15
        elif sweet_level == 2:
            tea_cal = 20
        else:
            tea_cal = 30
    else:
        if sweet_level == 1:
            tea_cal = 10
        elif sweet_level == 2:
            tea_cal = 15
        else:
            tea_cal = 20

    total = pearl_cal * pearl_weight + tea_cal * tea_volume

    if total == int(total):
        print(int(total))
    else:
        print(total)
main()
