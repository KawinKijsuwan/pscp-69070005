"""Easy Histogram"""
text = input()

LETTERS = "abcdefghijklmnopqrstuvwxyz"

for lower in LETTERS:
    upper = lower.upper()

    count_lower = text.count(lower)
    if count_lower > 0:
        print(lower, "=", count_lower)

    count_upper = text.count(upper)
    if count_upper > 0:
        print(upper, "=", count_upper)
