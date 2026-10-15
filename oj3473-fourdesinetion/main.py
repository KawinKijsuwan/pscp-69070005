"""four"""
arrow = {
    "U": ["  *  ", " * ", "* * ", "  ", "  *  "],
    "D": ["  *  ", "  *  ", "* * ", " ", "  *  "],
    "L": ["  *  ", " *   ", "**", "   ", "  *  "],
    "R": ["  *  ", "   * ", "*", "   * ", "  *  "],
}

code = input().strip()

for row in range(5):
    line = "".join(arrow[ch][row] + " " for ch in code)
    print(line)
