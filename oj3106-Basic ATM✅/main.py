"""basic atm"""
user_input = int(input())

if user_input < 100 or user_input > 20000 or user_input % 100:
    print("ERROR")
else:
    thousund = user_input // 1000
    user_input = user_input % 1000

    haroi = user_input // 500
    user_input = user_input % 500

    hundred = user_input // 100
    user_input = user_input % 100

    if thousund > 0:
        print(f"1000 = {thousund}")
    if haroi > 0:
        print(f"500 = {haroi}")
    if hundred > 0:
        print(f"100 = {hundred}")
