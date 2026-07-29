"""ตรวจสระ"""
def main():
    """main"""
    user_input = str(input())
    vowels = ["a","e","i","o","u"]
    if user_input in vowels:
        print("yes")
    else:
        print("no")
main()
