"""pass or not"""
def main():
    """main"""
    num = int(input())
    total_score = 0
    status = "PASS"
    for _ in range(num):
        score = int(input())
        total_score += score
        if score < 50:
            status = "FAIL"
    average = total_score / num
    if average < 60:
        status = "FAIL"
    print(f"{average:.1f}")
    print(status)
main()
