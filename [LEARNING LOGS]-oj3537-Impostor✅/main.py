"""Among Us"""
def main():
    """main"""
    alive = {}
    dead = {}

    while True:
        line = input().strip()
        if line == "Start":
            break
        line = line.strip("{}")
        parts = line.split(":")
        name = parts[0].strip().strip("\"'")
        role = parts[1].strip().strip("\"'")
        alive[name] = role

    while True:
        name = input().strip()
        if name == "End":
            break
        if name in alive:
            dead[name] = alive.pop(name)

    impostors = list(alive.values()).count("Impostor")

    print(impostors, "Impostor Remains")
    print("***Alive***")
    for name in sorted(alive):
        print(name, ":", alive[name])
    print("***Dead***")
    for name in sorted(dead):
        print(name, ":", dead[name])
main()
