"""หาค่าที่มากกว่าของแต่ละคู่"""
def main():
    """main"""
    n = int(input())

    equation = ""
    total = 0
    for i in range(n):
        x = int(input())
        y = int(input())
        if x > y:
            bigger = x
        else:
            bigger = y
        total = total + bigger
        if not i:
            equation = str(bigger)
        else:
            equation = equation + " + " + str(bigger)
    if n == 1:
        print(equation)
    else:
        print(equation + " = " + str(total))

main()
