"""เช็คผลการสอบ"""
def main():
    """main"""
    exercies = int(input())
    mid_term = int(input())
    final = int(input())
    if exercies < 5:
        print("fail")
    elif mid_term < 20:
        print("fail")
    elif final < 25:
        print("fail")
    else:
        print("pass")
main()
