"""เกมสะสมเเต้ม"""
def main():
    """main"""
    num = int(input())
    score = 0
    for _ in range(num):
        stat = input()
        if stat == "+":
            score += 10
        elif stat == "-":
            score -= 5
    print(score)
main()
