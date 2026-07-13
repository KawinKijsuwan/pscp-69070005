"""สลับหมายเลข"""
def main():
    """main"""
    num = int(input())
    operator = input()
    reverse_num = int(str(num)[::-1])
    if operator == "+":
        print(f"{num} {operator} {reverse_num} = {int(num) + int(reverse_num)}")
    elif operator == "*":
        print(f"{num} {operator} {reverse_num} = {int(num) * int(reverse_num)}")
main()
