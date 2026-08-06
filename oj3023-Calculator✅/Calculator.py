"""Calculator"""
def main():
    """Calculator"""
    n = int(input())
    press = 0
    for i in range(1,n+1):
        press += len(str(i))+1
    if n == 1:
        print(1)
    else:
        print(press)
main()
