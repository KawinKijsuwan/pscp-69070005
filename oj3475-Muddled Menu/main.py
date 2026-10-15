"""Muddled Menu"""
menu = []

while True:
    try:
        text = input().strip()
    except EOFError:
        break

    if text == "DONE":
        break

    if text == "CLOSED":
        menu.clear()
        break

    if text == "SOMETHING'S WRONG":
        menu.clear()
        continue

    if text.startswith("Can't do: "):
        name = text[len("Can't do: "):]
        while name in menu:
            menu.remove(name)
        continue

    if not text:
        continue

    name, course = text.rsplit(" #", 1)

    if course == "N":
        menu.append(name)
    else:
        menu.insert(int(course) - 1, name)

print("Full Course:", menu, "Reversed:", menu[::-1])
