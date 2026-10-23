"""Filter"""
def main():
    """main"""
    line = input().strip().strip("{}")
    limit = float(input())

    scores = {}
    for item in line.split(","):
        if item.strip() == "":
            continue
        parts = item.split(":")
        student = parts[0].strip().strip("\"'")
        scores[student] = float(parts[1].strip().strip("\"'"))

    found = False
    for student in sorted(scores):
        if scores[student] >= limit:
            print(f"{student}\t{scores[student]:.2f}")
            found = True

    if not found:
        print("Nope")
main()
