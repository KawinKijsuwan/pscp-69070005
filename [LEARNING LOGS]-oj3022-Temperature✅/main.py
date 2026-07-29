"""Temperature"""
def main():
    """Temperature"""
    temp = float(input())
    degree = str(input())
    change_degree = str(input())
    if degree == "C":
        cel = temp
    elif degree == "K":
        cel = temp - 273.15
    elif degree == "F":
        cel = (temp - 32)*5/9
    elif degree == "R":
        cel = temp * 5/9 - 273.15
    if change_degree == "C":
        print(f"{cel:.2f}")
    elif change_degree == "K":
        print(f"{cel+273.15:.2f}")
    elif change_degree == "F":
        print(f"{cel*9/5+32:.2f}")
    elif change_degree == "R":
        print(f"{(cel+273.15)*9/5:.2f}")
main()
