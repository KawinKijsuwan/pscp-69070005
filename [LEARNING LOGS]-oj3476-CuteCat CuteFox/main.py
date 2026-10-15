"""cutecat"""
n = int(input())

cats = {}
foxes = {}

for _ in range(n):
    data = input().split('"')

    name = data[1]
    code = data[3]

    if code[:3] == "Cat":
        cats[code] = name
    else:
        foxes[code] = name

if "Cat01" not in cats:
    cats["Cat01"] = "Garfield"

if "Fox01" not in foxes:
    foxes["Fox01"] = "Fubuki"

cat_list = list(cats.items())
fox_list = list(foxes.items())

cat_list.sort(key=lambda x: int(x[0][3:]))
fox_list.sort(key=lambda x: int(x[0][3:]))

print("Cat :", len(cats))
print("Fox :", len(foxes))

for code, name in cat_list:
    print(name, ":", code)

for code, name in fox_list:
    print(name, ":", code)
