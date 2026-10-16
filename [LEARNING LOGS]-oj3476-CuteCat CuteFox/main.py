"""Cats and Foxes"""
def main():
    """main"""
    n = int(input())

    pack = {}
    for _ in range(n):
        line = input().strip().strip("{}")
        parts = line.split(":")
        name = parts[0].strip().strip("\"'")
        code = parts[1].strip().strip("\"'")
        pack[name] = code

    if "Cat01" not in pack.values() and "Garfield" not in pack:
        pack["Garfield"] = "Cat01"
    if "Fox01" not in pack.values() and "Fubuki" not in pack:
        pack["Fubuki"] = "Fox01"

    cats = {}
    foxes = {}
    for name, code in pack.items():
        if code.startswith("Cat"):
            cats[int(code[3:])] = name
        else:
            foxes[int(code[3:])] = name

    print("Cat :", len(cats))
    print("Fox :", len(foxes))

    for number in sorted(cats):
        print(f"{cats[number]} : Cat{number:02d}")
    for number in sorted(foxes):
        print(f"{foxes[number]} : Fox{number:02d}")
main()
