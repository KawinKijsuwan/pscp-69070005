"""EuclideanDistance2D"""
def main():
    """main"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    distance = (((p1-q1)**2 + (p2-q2)**2))**0.5
    print(distance)
main()
