"""MissingNumber"""
n = int(input())
full_set = set(range(1, n + 1))
given_set = set()

while True:
    num = int(input())
    if not num:
        break
    given_set.add(num)
missing_numbers = sorted(full_set - given_set)
print("\n".join(map(str, missing_numbers)))
