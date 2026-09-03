"""วิเคราะห์ยอดขายร้านกาแฟ"""
def main():
    """main"""
    num = int(input())
    sales = []
    for _ in range(num):
        sales.append(int(input()))
    print(sum(sales))
    print(max(sales))
    print(min(sales))
    print(f"{sum(sales) / num:.1f}")
main()
