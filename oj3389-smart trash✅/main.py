"""smart trash"""
n = int(input())
for _ in range(n):
    data = list(map(float, input().split()))
    plastic = data[0]
    can = data[1]
    glass = data[2]
    total = plastic + can + glass
    result = []
    if total > 50:
        result.append("Overloaded")
    if plastic > 20:
        result.append("Check Type Plastic")
    if can > 20:
        result.append("Check Type Can")
    if glass > 20:
        result.append("Check Type Glass")
    print(f"{total:.1f}", end="")
    for x in result:
        print(", " + x, end="")
    print()
