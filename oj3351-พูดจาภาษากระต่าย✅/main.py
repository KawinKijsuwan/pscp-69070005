"""พูดจาภาษากระต่าย"""
def main():
    """main"""
    word = input().strip().upper()
    n = len(word)

    only_it = True
    for ch in word:
        if ch not in "IT":
            only_it = False

    if only_it:
        print("unknown", n)
        return

    bad = -1
    for i in range(n):
        ch = word[i]
        if ch == "A":
            if i == 0 or word[i - 1] not in "RA":
                bad = i
                break
        elif ch == "R":
            if i == n - 1 or word[i + 1] != "A":
                bad = i
                break
        elif ch == "B":
            if i == n - 1 or word[i + 1] not in "IT":
                bad = i
                break
        elif ch not in "IT":
            bad = i
            break

    if bad != -1:
        print("no", bad)
        return

    longest = 0
    run = 0
    for ch in word:
        if ch == "A":
            run += 1
            if run > longest:
                longest = run
        else:
            run = 0
    print("yes", longest)
main()
