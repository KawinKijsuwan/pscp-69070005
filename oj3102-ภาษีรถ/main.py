"""ภาษีรถ"""
year_cars = int(input())
cc = int(input())
vat = 0

if year_cars <= 1990:
    if cc <= 1500:
        vat = 1250
    elif cc <= 2000:
        vat = 1400
    elif cc > 2000:
        vat = 2000
if year_cars >= 1991:
    if cc <= 1500:
        vat = 1100
    elif cc <= 2000:
        vat = 1300
    elif cc > 2000:
        vat = 1700
if year_cars >= 2000:
    if cc <= 1500:
        vat = 1000
    elif cc <= 2000:
        vat = 1200
    elif cc >=2000:
        vat = 1500
print(vat)
