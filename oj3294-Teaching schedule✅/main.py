"""Teaching schedule"""
N = int(input())
A = int(input())

total_minutes = N * A
hours = total_minutes // 60
minutes = total_minutes % 60

if not hours and not minutes:
    print("No teaching")
elif not hours:
    print(f"{minutes} minute")
elif not minutes:
    print(f"{hours} hours")
else:
    print(f"{hours} hours {minutes} minute")
