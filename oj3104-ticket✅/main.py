"""ticket"""
def main():
    """main"""
    user_input = input()
    user_input = user_input.split(" ")
    age = int(user_input[0])
    days = str(user_input[1])
    if age < 5:
        price = 0
    elif age <= 18:
        price = 100
    else:
        price = 150
    if days == "Wed":
        price = price / 2
    print(int(price))
main()
