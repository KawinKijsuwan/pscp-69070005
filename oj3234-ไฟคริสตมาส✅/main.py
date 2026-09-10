"""ไฟคริสตมาส"""
colour,count = input().split()
answer = []

if colour == "R":
    rgb = ["Red", "Green", "Blue"]
elif colour == "G":
    rgb = ["Green", "Blue", "Red"]
else:
    rgb = ["Blue", "Red", "Green"]

for i in range(int(count)):
    answer.append(rgb[i%3])

print(" ".join(answer))
    