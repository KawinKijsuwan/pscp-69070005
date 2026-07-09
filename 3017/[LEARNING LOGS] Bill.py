"""Bills"""
def main():
    """main"""
    food_price = int(input())
    service_charge = 0.1 * food_price
    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000
    vat = 0.07 * (food_price + service_charge)
    total_price = food_price + vat + service_charge
    print(f"{total_price:.2f}")
main()
