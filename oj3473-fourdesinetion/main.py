"""four"""
up    = ["  *  ", " *** ", "* * *", "  *  ", "  *  "]
down  = ["  *  ", "  *  ", "* * *", " *** ", "  *  "]
left  = ["  *  ", " *   ", "*****", " *   ", "  *  "]
right = ["  *  ", "   * ", "*****", "   * ", "  *  "]

commands = input().strip().upper()

for row in range(5):
    line = ""
    for c in commands:
        if c == "U":
            line = line + up[row] + " "
        elif c == "D":
            line = line + down[row] + " "
        elif c == "L":
            line = line + left[row] + " "
        elif c == "R":
            line = line + right[row] + " "
    print(line)
