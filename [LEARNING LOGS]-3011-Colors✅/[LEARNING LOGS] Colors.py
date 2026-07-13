"""Colors"""
def main():
    """main"""
    first_color = input()
    second_color = input()
    if (first_color == "Red" and second_color == "Yellow" 
        or first_color == "Yellow" and second_color == "Red"
        ):
        print("Orange")
    elif (first_color == "Red" and second_color == "Blue" 
        or first_color == "Blue" and second_color == "Red"
        ):
        print("Violet")
    elif (first_color == "Yellow" and second_color == "Blue" 
          or first_color == "Blue" and second_color == "Yellow"
          ):
        print("Green")
    elif (first_color == second_color and first_color in ["Red", "Yellow", "Blue"]):
        print(first_color)
    else:
        print("Error")
main()
