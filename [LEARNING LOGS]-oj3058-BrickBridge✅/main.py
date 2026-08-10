"""aitwit"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    goal = int(input())
    big_used = min(b, goal // 5)
    remaining = goal - big_used * 5
    if remaining <= a:
        print(remaining)
    else:
        print(-1)
main()
