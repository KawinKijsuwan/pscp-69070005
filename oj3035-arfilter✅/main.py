"""Arfilter"""
def main():
    """main"""
    user_input = input().split(" ")
    r = int(user_input[0])
    x = int(user_input[1])
    y = int(user_input[2])
    d_squared = x**2 + y**2
    r_squared = r**2
    if d_squared < r_squared:
        print("IN")
    elif d_squared == r_squared:
        print("ON")
    else:
        print("OUT")
main()
