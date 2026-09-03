"""กระต่ายน้อยกินราเมน"""
size,ramen_type = input().split()
total_price = 0
if size == "S":
    if ramen_type == "R":
        total_price = 60
    elif ramen_type == "T":
        total_price = 80
elif size == "M":
    if ramen_type == "R":
        total_price = 80
    elif ramen_type == "T":
        total_price = 100
elif size == "L":
    if ramen_type == "R":
        total_price = 100
    elif ramen_type == "T":
        total_price = 120

topping, num_top = (input() + " 0").split()[:2]
if topping == "P":
    total_price += 15 * int(num_top)
elif topping == "E":
    total_price += 10 * int(num_top)

print(total_price)
