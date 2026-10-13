"""แคล"""
total_cal = 0
while True:
    order = int(input())
    if order == 5:
        break
    if order == 1:
        total_cal += 100
    elif order == 2:
        total_cal += 120
    elif order == 3:
        total_cal += 200
    elif order == 4:
        total_cal += 60
print("Bye Bye")
print(f"Total Calories: {total_cal}")
