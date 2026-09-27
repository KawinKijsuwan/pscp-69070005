"""ตั๋วหนัง"""
def main():
    """main"""
    seats = int(input())

    while seats > 0:
        line = input()

        if line.strip() == "":
            break

        age, num = map(int, line.split())

        if age < 15:
            print(-1)
        elif num > seats:
            print(-2)
        else:
            if age <= 22:
                price_per_ticket = 150 * 80 // 100
            elif age >= 60:
                price_per_ticket = 150 * 50 // 100
            else:
                price_per_ticket = 150

            total_price = price_per_ticket * num
            seats = seats - num

            print(total_price, seats)

main()
