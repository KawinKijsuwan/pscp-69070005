"""สหกร"""
def main():
    """main"""
    samacik = input()
    item_count = int(input())
    total_price = 0
    for _ in range(item_count):
        item_price = float(input())
        total_price += item_price
    if samacik == "Y":
        discount = 0.05
    elif samacik == "N" and total_price >= 500:
        discount = 0.03
    else:
        discount = 0
    discount_price = total_price * (1 - discount)

    print(f"{discount_price + 0.000001:.2f}")

main()
