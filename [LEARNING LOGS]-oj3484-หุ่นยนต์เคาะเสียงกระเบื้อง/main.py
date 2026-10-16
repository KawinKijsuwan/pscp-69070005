"""หุ่นยนต์"""
n, p = input().split()
n = int(n)
p = float(p)

tiles = []

for _ in range(n):
    row = list(map(int, input().split()))
    tiles.append(row)

total_bad_tiles = 0
total_bad_points = 0

column_bad_tiles = [0] * n
column_bad_points = [0] * n

for i in range(n):
    row_bad_tiles = 0
    row_bad_points = 0

    for j in range(n):
        if tiles[i][j] > 0:
            row_bad_tiles += 1
            column_bad_tiles[j] += 1

        row_bad_points += tiles[i][j]
        column_bad_points[j] += tiles[i][j]

    total_bad_tiles += row_bad_tiles
    total_bad_points += row_bad_points

    print(*tiles[i], row_bad_tiles, row_bad_points)

print(*column_bad_tiles)

print(*column_bad_points)

fine = total_bad_points * p
print(total_bad_tiles, total_bad_points, f"{fine:.2f}")
