"""Surprising"""
def main():
    """main"""
    total = float(input())
    max_score = float(input())

    min_possible = max(0, total - 2 * max_score)
    gap = max_score - min_possible

    if gap > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
