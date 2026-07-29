"""pass or fail"""
def main():
    """main"""
    mid_term = int(input())
    final = int(input())
    score = mid_term + final
    print(score)
    if score >= 50:
        print("pass")
    else:
        print("fail")
main()
