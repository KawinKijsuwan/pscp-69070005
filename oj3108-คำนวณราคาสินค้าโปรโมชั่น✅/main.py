"""promotion"""
pencil, notebook, color = map(int, input().split())

PENCIL_PRICE = 25
NOTEBOOK_PRICE = 40
COLOR_PRICE = 55
total = pencil * PENCIL_PRICE + notebook * NOTEBOOK_PRICE + color * COLOR_PRICE

if pencil + notebook + color >= 3:
    sale = total - (total * 0.1)
    print(int(sale))
else:
    print(total)
