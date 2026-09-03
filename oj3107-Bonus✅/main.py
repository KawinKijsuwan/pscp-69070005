"""Bonus"""
position,years,salary = input().split()
years_int = int(years)
salary_int = int(salary)
fix_bonus = 0
percent_rate = 0.0

if position == "M":
    fix_bonus = 1500
    if years_int <= 5:
        percent_rate = 0.06
    elif years_int <= 10:
        percent_rate = 0.08
    else:
        percent_rate = 0.1
if position == "B":
    fix_bonus = 1000
    if years_int <= 5:
        percent_rate = 0.05
    elif years_int <= 10:
        percent_rate = 0.06
    else:
        percent_rate = 0.07
if position == "G":
    fix_bonus = 500
    if years_int <= 5:
        percent_rate = 0.04
    elif years_int <= 10:
        percent_rate = 0.05
    else:
        percent_rate = 0.06

total_bonus = fix_bonus + (salary_int * percent_rate)
print(int(total_bonus))
