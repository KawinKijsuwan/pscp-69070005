"""SafePassword"""
def main():
    """SafePassword"""
    letter = str(input())
    password = int(input())
    if letter == "H" and password == 4567:
        print("safe unlocked")
    elif letter == "H":
        print("safe locked - change digit")
    elif password == 4567:
        print("safe locked - change char")
    else:
        print("safe locked")
main()
