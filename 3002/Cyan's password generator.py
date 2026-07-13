"""Cyan's password generator"""
def main():
    """main"""
    first_name = str(input())
    last_name = str(input())
    age = str(input())
    if len(first_name) >= 5 and len(last_name) >= 5:
        print((first_name[0:2] +  last_name[-1] + age[-1]))
    else:
        print((first_name[0] + age + last_name[-1]))
main()
