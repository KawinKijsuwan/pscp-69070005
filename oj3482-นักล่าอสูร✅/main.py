"""นักล่าอสูร"""
demons = [
    ["Spider Demon", 1],
    ["Swamp Demon", 2],
    ["Arrow Demon", 1],
    ["Hand Demon", 2],
    ["Drum Demon", 3],
    ["Mugen Train", 2],
    ["Upper Moon", 3]
]

queue = demons[:]

kill_count = 0
attack_count = 0

while kill_count < 5:
    demon = queue.pop(0)

    name = demon[0]
    weak_point = demon[1]

    print(name, flush=True)

    killed = False

    for _ in range(2):
        attack = int(input())
        attack_count += 1

        if attack == weak_point:
            print("kill", flush=True)
            kill_count += 1
            killed = True
            break

    if not killed:
        print("back", flush=True)
        queue.append(demon)

print(attack_count)
