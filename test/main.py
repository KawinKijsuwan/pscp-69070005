"""chrismas"""
color, amount = input().split()
amount = int(amount)
order = []

for _ in range(amount):
    if color == "R":
        order.append("Red")
        color = "G"
    elif color == "G":
        order.append("Green")
        color = "B"
    elif color == "B":
        order.append("Blue")
        color = "R"


print(" ".join(order))
