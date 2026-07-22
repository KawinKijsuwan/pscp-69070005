"""moneyexchange"""
def main():
    """moneyexchange"""
    money = int(input())
    coin_10 = money//10
    money = money % 10
    coin_5 = money // 5
    money = money % 5
    coin_2 = money // 2
    money = money % 2
    coin_1 = money
    print(f"10 = {coin_10}")
    print(f"5 = {coin_5}")
    print(f"2 = {coin_2}")
    print(f"1 = {coin_1}")
main()
