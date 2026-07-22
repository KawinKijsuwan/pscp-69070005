"""กราต่ายน้อยจ่ายตลัด"""
def main():
    """main"""
    carrot = 10
    cabbage = 25
    tomato = 3
    text_input = input()
    text_input = text_input.split(" ")
    carrot_amount = int(text_input[0])
    cabbage_amount = int(text_input[1])
    tomato_amount = int(text_input[2])
    total = (carrot * carrot_amount) + (cabbage * cabbage_amount) + (tomato * tomato_amount)
    print(total)
main()
