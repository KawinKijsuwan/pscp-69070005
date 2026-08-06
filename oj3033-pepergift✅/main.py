"""gift"""
def main():
    """main"""
    num_input = input()
    num_input = num_input.split(" ")
    r = float(num_input[0])
    height = float(num_input[1])
    glue_area = float(num_input[2])
    width = height + 2 * r
    length = 2 * 3.14 * r + glue_area
    print(f"{width:.2f} {length:.2f}")
main()
