"""register"""
colors = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Grey", "White"]
mul_colors = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Gold", "Silver"]
mul_values = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 0.1, 0.01]
tol_colors = ["Brown", "Red", "Green", "Blue", "Purple", "Grey", "Gold", "Silver"]
tol_values = [0.01, 0.02, 0.005, 0.0025, 0.001, 0.0005, 0.05, 0.10]
num1 = ""
num2 = ""
base_number = 0
c1 = input()
c2 = input()
c3 = input()
c4 = input()
if c1 not in colors or c2 not in colors or c3 not in mul_colors or c4 not in tol_colors:
    print("Error")
else:
    num1 = str(colors.index(c1))
    num2 = str(colors.index(c2))
    base_number = int(num1 + num2)

    mul = mul_values[mul_colors.index(c3)]
    ohm = base_number * mul

    tol = tol_values[tol_colors.index(c4)]
    min_val = ohm - (ohm * tol)
    max_val = ohm + (ohm * tol)

    print(f"{min_val:.4f}")
    print(f"{max_val:.4f}")
