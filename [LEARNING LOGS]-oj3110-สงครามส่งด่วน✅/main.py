"""สงครามส่งด่วน"""
def main():
    """main"""
    origin,destination = input().split()
    weight = float(input())
    if origin == "BKK" and destination == "CNX":
        price = 10 + 30 * weight
        print(f"{price:.2f}")
    elif origin == "CNX" and destination == "UBP":
        price = 15 + 40 * weight
        print(f"{price:.2f}")
    elif origin == "UBP" and destination == "BKK":
        price = 20 + 40 * weight
        print(f"{price:.2f}")
    elif origin == "BKK" and destination == "PKT":
        price = 25 + 50 * weight
        print(f"{price:.2f}")
    elif origin == "PKT" and destination == "CNX":
        price = 30 + 60 * weight
        print(f"{price:.2f}")
    elif origin == "UBP" and destination == "PKT":
        price = 40 + 70 * weight
        print(f"{price:.2f}")
    else:
        print("Error")
main()
