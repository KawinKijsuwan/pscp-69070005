"""หาระยะทางระหว่างจุด 3D"""
def main():
    """distrance3d"""
    text_1 = input()
    text_1 = text_1.split(" ")
    x1 = int(text_1[0])
    y1 = int(text_1[1])
    z1 = int(text_1[2])
    text_2 = input()
    text_2 = text_2.split(" ")
    x2 = int(text_2[0])
    y2 = int(text_2[1])
    z2 = int(text_2[2])
    d = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
    print(f"{d:.2f}")
main()
