"""Cyan's password generator"""
def main():
    """main"""
    first_name = str(input())
    last_name = str(input())
    age = str(input())
    if len(first_name) <= 5 and len(last_name) <= 5:
        print(f"{first_name} {age} {last_name}")

main()
