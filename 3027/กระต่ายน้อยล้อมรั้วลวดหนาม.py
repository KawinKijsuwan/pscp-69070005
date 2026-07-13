"""กราต่ายน้อยลอมร้วลวดหนาม"""
def main():
    """main"""
    text_input = input()
    text_input = text_input.split(" ")
    width = int(text_input[0])
    length = int(text_input[1])
    floor = int(text_input[2])
    price = int(input())
    total_area = 2*(width + length)*floor
    total_price = total_area * price
    print(total_area)
    print(total_price)
main()
