"""Coke"""


def main():
    """main"""
    price = int(input())
    caps_needed = int(input())
    exchange_price = int(input())
    bottles_wanted = int(input())

    total_cost = 0
    bottles_have = 0
    caps = 0

    while bottles_have < bottles_wanted:
        if caps_needed > 0 and caps >= caps_needed:
            caps -= caps_needed
            total_cost += exchange_price
        else:
            total_cost += price
        bottles_have += 1
        caps += 1

    print(total_cost)


main()
