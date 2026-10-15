"""Bus Seat"""
def main():
    """main"""
    seats = int(input())
    rows = int(input())
    mine = int(input())

    for pos in range(seats, 0, -1):
        line = ""
        for row in range(rows):
            number = row * seats + pos
            if number == mine:
                text = "XX"
            else:
                text = f"{number:02d}"
            if row > 0:
                line = line + " "
            line = line + text
        print(line)

        if (seats - pos) % 2 == 1 and pos != 1:
            print()
main()
