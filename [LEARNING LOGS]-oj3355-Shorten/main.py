"""Shorten"""
numbers = []

while True:
    x = int(input())
    if x == -1:
        break
    numbers.append(x)

result = []
i = 0

while i < len(numbers):
    start = i

    while i + 1 < len(numbers) and numbers[i + 1] == numbers[i] + 1:
        i += 1

    if start == i:
        result.append(str(numbers[start]))
    else:
        result.append(f"{numbers[start]}-{numbers[i]}")

    i += 1

print(", ".join(result))
