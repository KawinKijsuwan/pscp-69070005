"""ไข้หวัดกระต่ายสายพันธุ์ใหม่"""
rows, cols = map(int, input().split())
rabbit_row, rabbit_col = map(int, input().split())
n = int(input())
risk = []
for _ in range(rows):
    risk.append([0] * cols)

for _ in range(n):
    infected_row, infected_col = map(int, input().split())

    for i in range(infected_row - 2, infected_row + 3):
        for j in range(infected_col - 2, infected_col + 3):
            if 0 <= i < rows and 0 <= j < cols:
                distance = max(abs(i - infected_row), abs(j - infected_col))

                if not distance:
                    risk[i][j] = max(risk[i][j], 100)
                elif distance == 1:
                    risk[i][j] = max(risk[i][j], 60)
                elif distance == 2:
                    risk[i][j] = max(risk[i][j], 20)

safe_area = 0

for i in range(rows):
    for j in range(cols):
        if not risk[i][j]:
            safe_area += 1

print(safe_area)
print(str(risk[rabbit_row][rabbit_col]) + "%")
