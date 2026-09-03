"""เดินเล่นในงานเทศกาล"""
def main():
    """main"""
    walk = input()
    x = 0
    y = 0
    for _ in walk:
        if _ == "N":
            y = y + 1
        elif _ == "S":
            y = y - 1
        elif _ == "E":
            x = x + 1
        elif _ == "W":
            x = x -1
    d = abs(x) + abs(y)
    print(x,y,d)
main()
