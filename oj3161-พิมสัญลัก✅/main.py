"""yeye"""
def main():
    """main"""
    num = int(input())
    for _ in range(1,num+1):
        if not _ % 5:
            print("X", end="")
        else:
            print("*", end="")
main()
