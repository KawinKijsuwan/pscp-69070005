"""หาร10"""
def main():
    """หาร10"""
    user_input = int(input())
    divison = (user_input // 10) * 10
    while divison >= 0:
        print(divison, end=" ")
        divison = divison - 10
main()
