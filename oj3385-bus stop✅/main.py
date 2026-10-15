"""busstop"""
p = int(input())
n = int(input())

bus_stop = {}

for _ in range(n):
    data = list(map(int, input().split()))

    stop_number = data[0]
    people = data[1:]

    bus_stop[stop_number] = people

inside_bus = []
answer = 0

for stop in range(1, n + 1):
    still_inside = []

    for destination in inside_bus:
        if destination == stop:
            answer += 1
        else:
            still_inside.append(destination)

    inside_bus = still_inside

    for destination in bus_stop[stop]:
        if destination > stop and len(inside_bus) < p:
            inside_bus.append(destination)

print(answer)
