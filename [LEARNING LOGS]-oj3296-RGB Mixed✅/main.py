"""RGB MIXED"""
r1 , g1 , b1 = map(int, input().split())
r2 , g2 , b2 = map(int, input().split())

r_av = (r1 + r2) // 2
g_av = (g1 + g2) // 2
b_av = (b1 + b2) // 2

print(f"{r_av} {g_av} {b_av}")
