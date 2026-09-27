"""ใส่กล่อง"""
W, L, M, N = map(int, input().split())

min_wasted = W * L

for A in range(M, N + 1):
    first_part = (W // A) * A * L

    rem_W = W % A
    second_part = rem_W * (L // A) * A

    used_area = first_part + second_part

    wasted = (W * L) - used_area

    if wasted < min_wasted:
        min_wasted = wasted

print(min_wasted)
