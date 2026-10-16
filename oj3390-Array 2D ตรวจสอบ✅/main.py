"""Array 2D ตรวจสอบ"""
matrix = []

for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

wrong_row = -1
wrong_col = -1

for i in range(5):
    if sum(matrix[i]) % 2:
        wrong_row = i

for j in range(5):
    col_sum = 0

    for i in range(5):
        col_sum += matrix[i][j]

    if col_sum % 2:
        wrong_col = j

print(wrong_row, wrong_col)
