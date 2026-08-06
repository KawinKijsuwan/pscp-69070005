"""ticket prices"""
def main():
    """main"""
    age = int(input())
    char = str(input())
    if age < 18 or char in ("s","S"):
        print(20)
    else:
        print(50)
main()
