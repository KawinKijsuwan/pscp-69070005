"""เลขคู่คี่"""
def main():
    """main"""
    even = 0
    odd = 0
    for _ in range(3):
        num = int(input())
        if not num % 2:
            even += 1
        else:
            odd += 1
    print(even)
    print(odd)
main()
